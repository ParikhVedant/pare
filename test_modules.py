"""
PARE India AI Assistant
Simple test script for module functionality.
"""

from src.modules.company_info import handle_company_query
from src.modules.product_info import handle_product_query
from src.modules.lead_capture import handle_lead_capture
from src.modules.support import get_pricing_info, handle_support_request

def run_test():
    """Run basic tests on all modules."""
    print("\n=== Testing Modules ===")
    
    # Test company info
    print("\nCompany Info:")
    result = handle_company_query()
    print(f"Response: {result['message']}")
    
    # Test product info
    print("\nProduct Info (Wall):")
    result = handle_product_query(category="wall")
    print(f"Response: {result['message']}")
    print(f"Brochure: {result['brochure']}")
    
    # Test lead capture
    print("\nLead Capture:")
    lead_data = {"name": None, "phone": None, "email": None, "location": None, 
                "requirement_type": None, "city": None, "quantity": None, "company_name": None}
    result = handle_lead_capture(lead_data)
    print(f"First Prompt: {result['message']}")
    
    # Update with test data and check next field
    lead_data["name"] = "Test User"
    result = handle_lead_capture(lead_data)
    print(f"Next Field: {result['next_field']}")
    
    # Test pricing info
    print("\nPricing Info:")
    result = get_pricing_info()
    print(f"Response: {result['message']}")
    
    # Test support request
    print("\nSupport Request (Callback):")
    result = handle_support_request("callback")
    print(f"Response: {result['message']}")
    
    print("\n=== All Tests Complete ===")

if __name__ == "__main__":
    run_test()