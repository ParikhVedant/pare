import os
import json
from typing import Dict, List, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

# Import modules
from src.modules.company_info import handle_company_query
from src.modules.product_info import handle_product_query
from src.modules.lead_capture import handle_lead_capture, send_lead_to_crm
from src.modules.support import get_pricing_info, handle_support_request, close_conversation

# Load environment variables
load_dotenv()

# Set OpenAI API key
from agents import set_default_openai_key
set_default_openai_key(os.getenv("OPENAI_API_KEY"))

class PareAgent:
    def __init__(self):
        # Initialize lead data
        self.lead_data = {
            "name": None,
            "phone": None,
            "email": None,
            "location": None,
            "requirement_type": None,
            "city": None,
            "quantity": None,
            "company_name": None
        }
        
        # Create OpenAI agent
        self.agent = Agent(
            name="pare_assistant",
            instructions="""
            You are a helpful assistant for PARE India, a leading manufacturer of decorative surfaces for walls, ceilings, and facades.
            
            Follow these guidelines:
            1. When customers ask about the company, provide information and ask about their requirements.
            2. When customers ask about products, explain the options based on their interests (walls, ceilings, facades).
            3. Capture lead information (location, requirement_type, quantity) in a conversational way.
            4. Provide pricing information when asked.
            5. Offer support options (callbacks, site visits) when appropriate.
            6. Once customer has narrowed down the requirement, capture the lead information and set a callback and close the conversation.
            7. Always be professional, helpful and enthusiastic.
            8. Answer in language of the customer. 
            9. Keep history of the conversation in the conversation_history variable.
            
            Remember to use the appropriate tools based on the customer's query.
            """,
            tools=[
                function_tool(self.tool_company_info),
                function_tool(self.tool_product_info),
                function_tool(self.tool_lead_capture),
                function_tool(self.tool_pricing_info),
                function_tool(self.tool_support_request),
                function_tool(self.tool_send_brochure)
            ],
            model="gpt-4o"
        )
        
        # Variables to keep track of the latest tool outputs
        self.last_brochure = None
        self.last_message = None
    
    # Tool definitions
    def tool_company_info(self) -> Dict:
        """Provide information about PARE India company."""
        result = handle_company_query()
        # Store message for response processing
        self.last_message = result["message"]
        
        return {
            "message": result["message"],
            "next_action": "lead_capture"
        }
    
    def tool_product_info(self, product_category: Optional[str] = None, specific_product: Optional[str] = None) -> Dict:
        """
        Provide information about PARE products.
        
        Args:
            product_category: Category of interest (wall, ceiling, facade, unsure, all, none)
            specific_product: Specific product of interest
        """
        result = handle_product_query(category=product_category, specific_product=specific_product)
        # Store message and brochure for response processing
        self.last_message = result["message"]
        self.last_brochure = result.get("brochure")
        
        return {
            "message": result["message"],
            "brochure": result.get("brochure"),
            "next_action": result.get("next_module", "lead_capture")
        }
    
    def tool_lead_capture(self, field: str, value: Optional[str] = None) -> Dict:
        """
        Capture customer lead information.
        
        Args:
            field: Lead data field to capture (name, phone, email, etc.)
            value: Value provided by the customer
        """
        result = handle_lead_capture(self.lead_data, field=field, value=value)
        # Store message for response processing
        self.last_message = result["message"]
        
        # Check if lead capture is complete
        if result.get("is_complete", False):
            send_lead_to_crm(self.lead_data)
        
        return {
            "message": result["message"],
            "next_field": result.get("next_field"),
            "is_complete": result.get("is_complete", False),
            "next_action": result.get("next_module", "lead_capture")
        }
    
    def tool_pricing_info(self) -> Dict:
        """Provide pricing information for PARE products."""
        result = get_pricing_info()
        # Store message for response processing
        self.last_message = result["message"]
        
        return {
            "message": result["message"],
            "next_action": "lead_capture"
        }
    
    def tool_support_request(self, request_type: str) -> Dict:
        """
        Handle customer support or callback requests.
        
        Args:
            request_type: Type of support request (callback, whatsapp, site_visit)
        """
        result = handle_support_request(request_type)
        
        response = {
            "message": result["message"],
            "next_action": result.get("next_module", "support")
        }
        
        if result.get("next_module") == "closing":
            response["message"] += "\n\n" + close_conversation()
        
        # Store message for response processing
        self.last_message = response["message"]
        
        return response
    
    def tool_send_brochure(self, brochure_type: str) -> Dict:
        """
        Send product brochure to customer.
        
        Args:
            brochure_type: Type of brochure to send (easy+, innov+, dura+, company)
        """
        # Store brochure for response processing
        self.last_brochure = brochure_type
        self.last_message = f"Here's our {brochure_type} brochure for your reference."
        
        return {
            "message": self.last_message,
            "brochure": brochure_type
        }
    
    def process_message(self, user_message: str) -> Dict[str, Any]:
        """Process user message using the OpenAI Agent and return a response."""
        # Reset stored values
        self.last_brochure = None
        self.last_message = None
        
        # Send message to agent
        result = Runner.run_sync(self.agent, user_message)
        
        # Build response using final output and stored values from tool calls
        response = {
            "response": result.final_output,
            "brochure": self.last_brochure
        }
        
        # If a tool was used and provided a message, use that instead of the model's response
        if self.last_message:
            response["response"] = self.last_message
            
        return response 