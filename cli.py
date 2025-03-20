"""
PARE India AI Assistant - CLI Interface
Command-line interface for testing the assistant.
"""

import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the PareAgent
from src.agent import PareAgent

# ASCII art for the CLI
PARE_ASCII = """
██████╗  █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██████╔╝█████╗  
██╔═══╝ ██╔══██║██╔══██╗██╔══╝  
██║     ██║  ██║██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
AI Assistant - Customer Support & Lead Generation
"""

def main():
    """Run the PARE AI Assistant in CLI mode."""
    print(PARE_ASCII)
    print("Welcome to PARE India AI Assistant!")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    try:
        # Initialize the agent
        print("Initializing AI assistant...")
        agent = PareAgent()
        print("AI assistant ready!\n")
        
        # Main conversation loop
        while True:
            # Get user input
            user_message = input("You: ")
            
            # Check for exit command
            if user_message.lower() in ["exit", "quit"]:
                print("\nThank you for using PARE India AI Assistant. Goodbye!")
                break
            
            try:
                # Show thinking indicator
                print("\nThinking", end="")
                for _ in range(3):
                    time.sleep(0.3)
                    print(".", end="", flush=True)
                print("\n")
                
                # Get response from agent
                response = agent.process_message(user_message)
                
                # Print the response
                print(f"Assistant: {response['response']}")
                
                # If a brochure is included, mention it
                if response.get("brochure"):
                    print(f"\n[Sending {response['brochure']} brochure]")
                
                print()  # Empty line for better readability
                
            except Exception as e:
                print(f"\nError during processing: {str(e)}")
                print("Please try again with a different query.")
                
    except Exception as e:
        print(f"\nError initializing AI assistant: {str(e)}")
        print("Please make sure you have a valid OpenAI API key in your .env file.")

if __name__ == "__main__":
    main()