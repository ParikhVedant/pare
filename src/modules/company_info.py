"""
Company Information Module
Handles queries about PARE company.
"""

# Company information template
COMPANY_INFO = """
PARÉ is a leading manufacturer of innovative decorative surfaces for walls, ceilings, and facades. 
We serve both residential and commercial projects across India.
"""

def get_company_info() -> str:
    """Return company information."""
    return COMPANY_INFO.strip()

def handle_company_query() -> dict:
    """Handle a query about the company."""
    response = f"{get_company_info()}\n\nPlease share details about your current requirement?"
    
    # Return response and set next module to lead capture
    return {
        "message": response,
        "next_module": "lead_capture",
        "brochure": None
    } 