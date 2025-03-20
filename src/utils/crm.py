"""
CRM Integration Utility - Simplified
Handles sending lead data to the CRM system.
"""

import os
import json
from typing import Dict, Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_lead_to_crm(lead_data: Dict[str, Optional[str]]) -> bool:
    """Send lead data to the CRM system."""
    # Get API credentials
    crm_api_url = os.getenv("CRM_API_URL")
    crm_api_key = os.getenv("CRM_API_KEY")
    
    if not crm_api_url or not crm_api_key:
        print("CRM credentials not configured - storing lead data locally")
        # For demo purposes, just print the data
        print(f"LEAD DATA: {json.dumps(lead_data, indent=2)}")
        return True
    
    try:
        # Clean up lead data (remove None values)
        clean_lead_data = {k: v for k, v in lead_data.items() if v is not None}
        
        # Make API request to CRM
        headers = {
            "Authorization": f"Bearer {crm_api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            crm_api_url, 
            headers=headers,
            data=json.dumps(clean_lead_data)
        )
        
        if response.status_code == 200:
            print("Successfully sent lead to CRM")
            return True
        else:
            print(f"Error sending lead to CRM: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

def notify_sales_team(lead_data: Dict[str, Optional[str]], salesperson_id: str = None) -> bool:
    """
    Notify the sales team about a new lead.
    
    Args:
        lead_data: Dictionary containing lead information
        salesperson_id: Optional ID of the specific salesperson to notify
        
    Returns:
        bool: True if successful, False otherwise
    """
    # This is a placeholder for actual notification logic
    # In a real implementation, this might:
    # 1. Send an email to the sales team
    # 2. Send a notification through a mobile app
    # 3. Create a task in a CRM system
    
    print(f"Notifying sales team about lead: {lead_data.get('name', 'Unknown customer')}")
    
    if salesperson_id:
        print(f"Assigned to salesperson ID: {salesperson_id}")
    
    return True 