# PARE India AI Assistant - Quick Start

A customer support and lead generation assistant built with OpenAI Agents SDK.

## Setup

1. Make sure you have Python 3.7+ installed
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_key_here
   ```

## Running the Assistant

### Streamlit UI (Recommended)
Run the Streamlit app with the included script:
```
./run_streamlit.sh
```

Or manually:
```
streamlit run streamlit_app.py
```

The app will open in your browser automatically.

### Command Line Interface
For testing in the terminal:
```
python cli.py
```

## Example Interactions

Try asking the assistant:

1. "Tell me about PARE India"
2. "What products do you offer for walls?"
3. "Tell me about PARE Soffit"
4. "How much do your products cost?"
5. "I'd like to request a callback"

## OpenAI Agents SDK

This assistant is built with the OpenAI Agents SDK, which provides:
- More conversational and natural interactions
- Tool-based approach for specific business functions
- Improved context handling throughout conversations
- Seamless transitions between different conversation topics

The agent is configured to handle:
- Company information requests
- Product inquiries for different categories
- Lead information capture
- Price quote requests
- Support and callback requests