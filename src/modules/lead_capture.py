"""
Lead Capture Module
Handles lead information collection.
"""

from typing import Dict, Optional

# Lead fields to capture
LEAD_FIELDS = [
    {
        "name": "location",
        "prompt": "Which location and city are you from?"
    },
    {
        "name": "requirement_type",
        "prompt": "What type of requirement do you have? (Residential / Commercial)"
    },
    {
        "name": "quantity",
        "prompt": "What quantity (in sq.ft.) are you looking for our panels?"
    }
]

def get_next_field_to_capture(lead_data: Dict[str, Optional[str]]) -> Optional[Dict]:
    """
    Determine the next field to capture from the customer.
    """
    for field_info in LEAD_FIELDS:
        field_name = field_info["name"]
        if lead_data.get(field_name) is None:
            return field_info
    return None

def update_lead_data(lead_data: Dict[str, Optional[str]], field: str, value: str) -> Dict[str, Optional[str]]:
    """
    Update the lead data with a new field value.
    """
    if field in lead_data:
        lead_data[field] = value
    return lead_data

def handle_lead_capture(lead_data: Dict[str, Optional[str]], field: str = None, value: str = None) -> Dict:
    """
    Handle lead capture process.
    """
    # If a field and value are provided, update the lead data
    if field and value:
        lead_data = update_lead_data(lead_data, field, value)
    
    # Get the next field to capture
    next_field = get_next_field_to_capture(lead_data)
    
    # If we have more fields to capture, continue the lead capture process
    if next_field:
        return {
            "message": next_field["prompt"],
            "next_field": next_field["name"],
            "next_module": "lead_capture",
            "is_complete": False
        }
    
    # If we have captured all fields, mark lead capture as complete
    return {
        "message": "Thank you for sharing your details. This will help us offer the best recommendations and support for your project.",
        "next_field": None,
        "next_module": "support",
        "is_complete": True
    }

def send_lead_to_crm(lead_data: Dict[str, Optional[str]]) -> bool:
    """
    Send lead data to CRM system.
    This is a placeholder for actual CRM integration.
    """
    # In a real implementation, this would send the data to a CRM API
    print("Sending lead data to CRM:", lead_data)
    
    # For demo purposes, always return success
    return True 