"""
PARE India AI Assistant - Streamlit Interface
Using OpenAI Agents SDK
"""

import os
import streamlit as st
from src.agent import PareAgent

# Set page configuration
st.set_page_config(
    page_title="PARE India AI Assistant",
    page_icon="💬",
    layout="centered"
)

# st.markdown("""
# <style>
# [data-testid='stSidebar'] {display: none;}
# </style>
# """, unsafe_allow_html=True)

# Initialize agent
@st.cache_resource
def get_agent():
    return PareAgent()

# App title and description
st.title("PARE India AI Assistant")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Welcome to PARE India. I'm your virtual assistant. How can I help you today?"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
        # If there's a brochure to show
        if message.get("brochure"):
            brochure_type = message["brochure"]
            st.info(f"📄 Sending {brochure_type} brochure")
            
            # Display brochure information
            if brochure_type == "easy+":
                st.caption("Wall panels brochure")
            elif brochure_type == "innov+":
                st.caption("Ceiling panels brochure")
            elif brochure_type == "dura+":
                st.caption("Facade panels brochure")
            elif brochure_type == "company":
                st.caption("Company brochure")

# Chat input
user_input = st.chat_input("Type your message here...")

# Handle agent initialization errors
try:
    agent = get_agent()
    agent_initialized = True
except Exception as e:
    st.error(f"Error initializing AI assistant: {str(e)}")
    st.warning("Please make sure you have a valid OPENAI_API_KEY in your .env file")
    agent_initialized = False

# When user inputs a message and agent is initialized
if user_input and agent_initialized:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Show assistant is thinking
    with st.chat_message("assistant"):
        thinking_placeholder = st.empty()
        thinking_placeholder.text("Thinking...")
        
        try:
            # Get response from agent
            response = agent.process_message(user_input)
            
            # Update assistant message
            thinking_placeholder.write(response["response"])
            
            # Show brochure notification if applicable
            if response.get("brochure"):
                brochure_type = response["brochure"]
                st.info(f"📄 Sending {brochure_type} brochure")
                
                # Display brochure information
                if brochure_type == "easy+":
                    st.caption("Wall panels brochure")
                elif brochure_type == "innov+":
                    st.caption("Ceiling panels brochure")
                elif brochure_type == "dura+":
                    st.caption("Facade panels brochure")
                elif brochure_type == "company":
                    st.caption("Company brochure")
            
            # Add assistant response to chat history
            st.session_state.messages.append({
                "role": "assistant",
                "content": response["response"],
                "brochure": response.get("brochure")
            })
            
        except Exception as e:
            thinking_placeholder.error(f"Error: {str(e)}")
            st.error("Please make sure your OpenAI API key is valid and has access to the required models.")

# # Sidebar with information
# with st.sidebar:
#     st.title("About PARE India")
#     st.markdown("""
#     PARÉ is a leading manufacturer of innovative decorative surfaces for walls, 
#     ceilings, and facades. We serve both residential and commercial projects across India.
#     """)
    
#     st.subheader("Product Categories")
#     st.markdown("""
#     - **Walls**: Linea, Pyramid, Arch
#     - **Ceilings**: Soffit, Duo, Louver
#     - **Facades**: Norma, Stretta
#     """)
    
#     st.subheader("Pricing")
#     st.markdown("Our pricing starts from ₹195 - ₹350 per sq.ft., depending on the product and finish.")
    
#     # About the technology
#     st.subheader("Technology")
#     st.markdown("Built with OpenAI Agents SDK for more natural conversations.")
    
#     # Add a reset button to clear the conversation
#     if st.button("Reset Conversation"):
#         st.session_state.messages = [
#             {"role": "assistant", "content": "Hello! Welcome to PARE India. I'm your virtual assistant. How can I help you today?"}
#         ]
#         st.rerun() 