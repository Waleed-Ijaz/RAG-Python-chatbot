# RAG Chatbot with Vectara and Claude

A Retrieval-Augmented Generation (RAG) chatbot built with Streamlit that combines Vectara's vector search capabilities with Anthropic's Claude AI for intelligent document-based conversations.

## Features

- **Vector Search**: Utilizes Vectara for efficient document retrieval and semantic search
- **AI-Powered Responses**: Leverages Anthropic's Claude for generating contextual and accurate responses
- **Conversation Memory**: Maintains chat history for context-aware interactions
- **Source Attribution**: Provides source citations for retrieved information
- **Interactive Web Interface**: Built with Streamlit for easy deployment and use

## Architecture

The chatbot follows a RAG (Retrieval-Augmented Generation) architecture:

1. **User Query** → Vectara retrieves relevant documents
2. **Retrieved Context** + **Conversation History** → Claude generates response
3. **Response** includes source citations and maintains conversation context

## Prerequisites

- Python 3.8+
- Vectara account with API credentials
- Anthropic API key for Claude access

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/rag-chatbot-vectara-claude.git
cd rag-chatbot-vectara-claude
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your API credentials:
```env
VECTARA_CUSTOMER_ID=your_customer_id
VECTARA_API_KEY=your_api_key
VECTARA_CORPUS_ID=your_corpus_id
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Usage

### Running the Streamlit App

```bash
streamlit run chatbot_app.py
```

The app will be available at `http://localhost:8501`

### Using the Jupyter Notebook

Launch Jupyter and open the notebook file to explore the chatbot functionality interactively:

```bash
jupyter notebook
```

## Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `VECTARA_CUSTOMER_ID` | Your Vectara customer ID |
| `VECTARA_API_KEY` | Your Vectara API key |
| `VECTARA_CORPUS_ID` | ID of the Vectara corpus to query |
| `ANTHROPIC_API_KEY` | Your Anthropic API key for Claude |

### Vectara Setup

1. Create a Vectara account at [vectara.com](https://vectara.com)
2. Create a corpus and upload your documents
3. Generate API credentials
4. Note your customer ID and corpus ID

### Anthropic Setup

1. Sign up for Anthropic API access
2. Generate an API key
3. Add the key to your environment variables

## Project Structure

```
rag-chatbot-vectara-claude/
├── chatbot_app.py          # Main Streamlit application
├── notebook.ipynb         # Jupyter notebook for exploration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Key Components

### ConversationMemory Class
Manages chat history to provide context for ongoing conversations.

### Vectara Integration
- Queries the Vectara API for relevant document retrieval
- Formats results with source attribution
- Handles API responses and error cases

### Claude Integration
- Uses Anthropic's Claude for response generation
- Combines retrieved context with conversation history
- Generates coherent, contextual responses

## Customization

### Adjusting Retrieval Parameters
Modify the `num_results` parameter in `get_query_json()` to change the number of documents retrieved.

### Claude Model Selection
Update the `model` parameter in `generate_answer()` to use different Claude models.

### Response Length
Adjust the `max_tokens` parameter to control response length.

## Error Handling

The application includes error handling for:
- API connection failures
- Invalid API responses
- Missing environment variables
- Malformed queries

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions or issues:
- Open an issue in this repository
- Check the [Vectara documentation](https://docs.vectara.com/)
- Refer to the [Anthropic API documentation](https://docs.anthropic.com/)

## Acknowledgments

- [Vectara](https://vectara.com) for providing vector search capabilities
- [Anthropic](https://anthropic.com) for the Claude AI model
- [Streamlit](https://streamlit.io) for the web framework