#!/bin/bash

# PARE India AI Assistant - Streamlit Launcher
# Using OpenAI Agents SDK

# Color codes for better readability
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== PARE India AI Assistant ===${NC}"
echo -e "Powered by OpenAI Agents SDK"
echo ""

# Check if environment file exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}Creating .env file...${NC}"
    echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
    echo -e "${RED}ACTION REQUIRED: Please edit the .env file to add your OpenAI API key.${NC}"
    echo ""
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is not installed.${NC}"
    echo "Please install Python 3 to run this application."
    exit 1
fi

# Install dependencies if needed
echo -e "${GREEN}Installing dependencies...${NC}"
pip install -r requirements.txt

# Start the Streamlit app
echo -e "${GREEN}Starting PARE India AI Assistant...${NC}"
echo -e "The app will open in your browser shortly."
echo ""
streamlit run streamlit_app.py 