"""
Customer Support Module
Handles customer support requests and callbacks.
"""

# Support message templates
CALLBACK_REQUEST = """
I can have one of our customer support specialists reach out to you for a detailed discussion. 
Would you prefer a call or a WhatsApp message?
"""

SITE_VISIT_REQUEST = """
We'd be happy to arrange a site visit after price confirmation. 
Would you like to proceed with a quotation first, so we can tailor the best solution for your needs?
"""

PRICING_INFO = """
Our pricing starts from ₹195 - ₹350 per sq.ft., depending on the product and finish. 
Would you like a detailed quotation based on your specific requirements?
"""

CLOSING_MESSAGE = """
Thank you for reaching out to PARE India! I'll ensure that our team follows up with the required details. 
Let us know if you need any additional support. Have a great day!
"""

def get_pricing_info() -> dict:
    """Return pricing information."""
    return {
        "message": PRICING_INFO,
        "next_module": "lead_capture"
    }

def handle_support_request(request_type: str) -> dict:
    """Handle customer support requests."""
    message = ""
    next_module = "support"
    
    if request_type == "callback":
        message = CALLBACK_REQUEST
    elif request_type == "whatsapp":
        message = "We'll arrange for a WhatsApp message from our customer support team soon."
        next_module = "closing"
    elif request_type == "site_visit":
        message = SITE_VISIT_REQUEST
    
    return {
        "message": message,
        "next_module": next_module
    }

def close_conversation() -> str:
    """Return closing message for the conversation."""
    return CLOSING_MESSAGE 