# Wikipedia Research Assistant

A powerful MCP (Model Context Protocol) server that transforms Wikipedia into an intelligent research companion for curious minds—students, journalists, researchers, and professionals who need quick, structured access to Wikipedia's vast knowledge base.

## 🎯 Purpose

Instead of opening multiple browser tabs and scanning through walls of dense Wikipedia text, users can now ask natural language questions like:
- "Tell me about Alan Turing"
- "Summarize the topic of carbon cycles"
- "What is quantum computing?"

And receive clean, structured responses containing:
- **Concise Summary**: Key information extracted and summarized
- **Article Title**: The exact Wikipedia article title
- **Direct Link**: URL to the full Wikipedia page for deeper reading

## ✨ Features

- **Natural Language Queries**: Ask questions in plain English
- **Structured Responses**: Get organized information instead of raw article text
- **Smart Summarization**: Extract key points from lengthy Wikipedia articles
- **Direct Access**: Immediate links to full articles for further research
- **MCP Integration**: Built using the Model Context Protocol for seamless AI assistant integration

## 🏗️ Architecture

This project implements the server component of a knowledge assistant system using:
- **Python**: Core server implementation
- **MCP (Model Context Protocol)**: Communication protocol for AI assistants
- **Wikipedia API**: Direct access to Wikipedia's content
- **Intelligent Processing**: Content extraction and summarization capabilities

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection for Wikipedia API access

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shuhaimiao/wikipedia-research-assistant.git
   cd wikipedia-research-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration if needed
   ```

2. **Verify Installation**
   ```bash
   python -m wikipedia_assistant --help
   ```

## 🔧 Usage

### Basic Query
```python
from wikipedia_assistant import WikipediaAssistant

assistant = WikipediaAssistant()
result = assistant.query("Tell me about Alan Turing")

print(f"Title: {result.title}")
print(f"Summary: {result.summary}")
print(f"Link: {result.url}")
```

### MCP Server Mode
```bash
# Start the MCP server
python -m wikipedia_assistant serve --port 8000

# The server will be available for MCP client connections
```

### Example Queries

- **Historical Figures**: "Who was Marie Curie?"
- **Scientific Concepts**: "Explain photosynthesis"
- **Current Events**: "What is climate change?"
- **Technology**: "What is artificial intelligence?"
- **Geography**: "Tell me about the Amazon rainforest"

## 📋 API Reference

### Core Methods

#### `query(question: str) -> WikipediaResult`
Processes a natural language question and returns structured Wikipedia information.

**Parameters:**
- `question`: Natural language query about any topic

**Returns:**
- `WikipediaResult` object with `title`, `summary`, and `url` fields

#### `search(term: str, limit: int = 5) -> List[str]`
Searches Wikipedia for articles matching the given term.

**Parameters:**
- `term`: Search term
- `limit`: Maximum number of results (default: 5)

**Returns:**
- List of article titles

## 🛠️ Development

### Project Structure
```
wikipedia-research-assistant/
├── src/
│   ├── wikipedia_assistant/
│   │   ├── __init__.py
│   │   ├── server.py          # MCP server implementation
│   │   ├── wikipedia_client.py # Wikipedia API client
│   │   ├── summarizer.py      # Content summarization
│   │   └── models.py          # Data models
├── tests/
│   ├── test_server.py
│   ├── test_client.py
│   └── test_integration.py
├── requirements.txt
├── setup.py
└── README.md
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=wikipedia_assistant

# Run specific test file
pytest tests/test_server.py
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔍 How It Works

1. **Query Processing**: Natural language questions are parsed and converted into Wikipedia search terms
2. **Content Retrieval**: The system fetches relevant Wikipedia articles using the Wikipedia API
3. **Smart Summarization**: Key information is extracted and condensed into digestible summaries
4. **Structured Response**: Results are formatted with title, summary, and source link
5. **MCP Integration**: All functionality is exposed through the Model Context Protocol for AI assistant integration

## 🌟 Use Cases

### For Students
- Quick research for assignments and projects
- Understanding complex topics with simplified explanations
- Finding reliable sources with direct Wikipedia links

### For Journalists
- Background research on people, events, and topics
- Fact-checking and source verification
- Rapid information gathering for articles

### For Professionals
- Industry research and competitive analysis
- Technical concept clarification
- Historical context for business decisions

## 📚 Educational Value

This project serves as an excellent example of:
- **MCP Implementation**: Learn how to build Model Context Protocol servers
- **API Integration**: Working with external APIs (Wikipedia)
- **Natural Language Processing**: Basic NLP techniques for query understanding
- **Information Architecture**: Structuring and presenting data effectively

## 🤝 Acknowledgments

- Inspired by [Educative's MCP Fundamentals Course](https://www.educative.io)
- Built with the [Model Context Protocol](https://modelcontextprotocol.io/)
- Powered by [Wikipedia's API](https://www.mediawiki.org/wiki/API:Main_page)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs)
- [Wikipedia API Documentation](https://www.mediawiki.org/wiki/API:Main_page)
- [Project Repository](https://github.com/shuhaimiao/wikipedia-research-assistant)

---

**Ready to transform your research workflow?** Start exploring Wikipedia like never before with intelligent, structured responses to your curious questions! 🚀
