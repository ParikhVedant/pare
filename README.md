# PARE India AI Assistant

An AI-powered customer support, lead generation, and product information assistant for PARE India using OpenAI Agents SDK.

## Features

- Company information sharing
- Product details and recommendations
- Lead capturing
- Pricing information
- Customer support request handling

## Technology

- Built with OpenAI Agents SDK for more conversational interactions
- Streamlit for the user interface
- Python for business logic

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key: `OPENAI_API_KEY=your_key_here`
4. Run the Streamlit app: `./run_streamlit.sh` or `streamlit run streamlit_app.py`

## Project Structure

- `streamlit_app.py`: Main Streamlit application
- `src/`: Source code directory
  - `agent.py`: OpenAI Agents SDK configuration
  - `modules/`: Business logic modules
    - `company_info.py`: Company information module
    - `product_info.py`: Product information module
    - `lead_capture.py`: Lead capturing module
    - `support.py`: Customer support module
  - `utils/`: Utility functions
    - `crm.py`: CRM integration
- `public/`: Static files (brochures, images)

## Testing

- For CLI testing, run: `python cli.py`
- For module testing without API calls: `python test_modules.py`