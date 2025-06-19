# Wikipedia Research Assistant

A powerful MCP (Model Context Protocol) server that transforms Wikipedia into an intelligent research companion for curious minds—students, journalists, researchers, and professionals who need quick, structured access to Wikipedia's vast knowledge base.

**Following the Educative MCP Fundamentals Course Implementation**

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
- **Smart Error Handling**: Handles disambiguation, missing pages, and search failures gracefully
- **Direct Access**: Immediate links to full articles for further research
- **MCP Integration**: Built using the Model Context Protocol with FastMCP for seamless AI assistant integration

## 🏗️ Architecture

This project implements the server component of a knowledge assistant system using:
- **Python**: Core server implementation
- **FastMCP**: Simplified MCP server framework from the official MCP SDK
- **Wikipedia API**: Direct access to Wikipedia's content via the `wikipedia` Python package
- **Intelligent Processing**: Content extraction and error handling

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

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

## 🔧 Usage

### Running the MCP Server

```bash
# Start the MCP server (stdio transport)
python src/wikipedia_assistant/server.py
```

Or use the example runner:
```bash
python examples/run_server.py
```

### Testing the Tool Functionality

```bash
# Run the demonstration script
python examples/test_tool.py
```

### Available Tool

#### `fetch_wikipedia_info(query: str) -> dict`

Searches Wikipedia for a topic and returns structured information.

**Parameters:**
- `query`: Natural language query about any topic

**Returns:**
- Success: `{"title": str, "summary": str, "url": str}`
- No results: `{"error": "No results found for your query."}`
- Disambiguation: `{"error": "Ambiguous topic. Try one of these: ..."}`
- Page error: `{"error": "No Wikipedia page could be loaded for this query."}`

**Example Usage:**
```python
from src.wikipedia_assistant.server import fetch_wikipedia_info

# Successful query
result = fetch_wikipedia_info("Python programming language")
print(f"Title: {result['title']}")
print(f"Summary: {result['summary'][:100]}...")
print(f"URL: {result['url']}")

# Handle errors
result = fetch_wikipedia_info("nonexistent topic")
if "error" in result:
    print(f"Error: {result['error']}")
```

## 🧪 Testing & Analysis

### Core Testing
```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_wikipedia_tool.py -v

# Run with coverage
pytest --cov=src
```

### MCP Analysis & Demonstrations

This repository includes comprehensive analysis tools to understand how MCP works:

```bash
# Validate MCP configuration and setup
python test_mcp_config.py

# See what metadata your MCP server exposes to AI agents
python demonstrate_mcp_metadata.py

# Analyze how LLM hyperparameters affect tool selection
python llm_hyperparameters_impact.py

# Test tool functionality with various queries
python examples/test_tool.py
```

### Understanding MCP Intelligence

**Key Insights Demonstrated:**
- How AI agents automatically discover and select tools
- Why semantic matching works better than keyword matching
- How LLM quality and hyperparameters affect tool selection
- Best practices for designing MCP-compatible tools

**📚 Comprehensive Documentation:**
- `MCP_TOOL_SELECTION_EXPLAINED.md` - Deep dive into how VS Code selected your tool
- `MCP_INTEGRATION_GUIDE.md` - Complete setup guide for VS Code and Cursor
- `QUICK_MCP_REFERENCE.md` - Copy-paste configurations
- `DOCUMENTATION_INDEX.md` - Navigation guide for all documentation

## 📁 Project Structure

```
wikipedia-research-assistant/
├── src/
│   └── wikipedia_assistant/
│       ├── __init__.py
│       ├── server.py              # Main MCP server (Educative course implementation)
│       ├── models.py              # Data models
│       ├── summarizer.py          # Content summarization
│       └── wikipedia_client.py    # Wikipedia API client
├── tests/
│   ├── test_setup.py              # Setup verification tests
│   ├── test_wikipedia_tool.py     # Wikipedia tool tests
│   ├── test_integration.py        # Integration tests
│   └── ...
├── examples/
│   ├── run_server.py              # Server runner example
│   └── test_tool.py               # Tool demonstration
├── docs/                          # Additional documentation
├── mcp-config-vscode.json         # VS Code MCP configuration
├── mcp-config-cursor.json         # Cursor MCP configuration
├── test_mcp_config.py             # MCP configuration validator
├── demonstrate_mcp_metadata.py    # MCP metadata analysis
├── llm_hyperparameters_impact.py  # Hyperparameter impact analysis
├── MCP_TOOL_SELECTION_EXPLAINED.md # Deep dive into tool selection
├── MCP_INTEGRATION_GUIDE.md       # Complete integration guide
├── QUICK_MCP_REFERENCE.md         # Quick reference configurations
├── DOCUMENTATION_INDEX.md         # Documentation navigation
├── IMPLEMENTATION_SUMMARY.md      # What we built summary
├── requirements.txt               # Dependencies
├── setup.py                       # Package configuration
├── README.md                      # This file
└── SETUP_GUIDE.md                # Detailed setup instructions
```

## 🔍 How It Works

### Basic Flow
1. **Query Processing**: Natural language questions are passed directly to Wikipedia's search API
2. **Content Retrieval**: The system fetches the best-matching Wikipedia article
3. **Structured Response**: Results are formatted with title, summary, and source link
4. **Error Handling**: Gracefully handles disambiguation, missing pages, and search failures
5. **MCP Integration**: All functionality is exposed through the Model Context Protocol using FastMCP

### 🧠 Intelligent Tool Selection (MCP Magic)

This project demonstrates how AI assistants (like VS Code's AI agent) automatically and intelligently select the right tool:

**When you ask: "Tell me about artificial intelligence"**

1. **Tool Discovery**: AI agent discovers available tools through MCP metadata
2. **Semantic Analysis**: AI understands your intent (information seeking about a topic)
3. **Smart Matching**: AI matches your intent with tool capabilities
4. **Automatic Selection**: AI chooses `fetch_wikipedia_info` without manual configuration
5. **Structured Response**: AI formats the returned data into natural language

**Key Factors That Make This Work:**
- **Rich Metadata**: Clear tool names and descriptions (`fetch_wikipedia_info`)
- **Type Compatibility**: String query input matches user's topic requests
- **Structured Output**: Dictionary return format perfect for AI processing
- **Semantic Clarity**: "Wikipedia" + "search" + "topic" = crystal clear purpose

### 🎛️ LLM Dependencies & Hyperparameter Impact

The quality of tool selection depends on:

**LLM Capabilities:**
- **Advanced LLMs** (GPT-4, Claude): Perfect semantic analysis and tool selection
- **Basic LLMs**: May need more explicit keyword-rich descriptions

**Hyperparameter Settings:**
- **Temperature (0.4-0.6)**: Balanced consistency and flexibility for tool selection
- **Top-K/Top-P**: Conservative settings ensure reliable tool choices
- **Production vs Development**: Different settings optimize for consistency vs exploration

> 📊 **See It In Action**: Run `python llm_hyperparameters_impact.py` to see how different LLM settings affect tool selection quality and consistency.

## 🌟 Example Queries

### Successful Queries
- "Python programming language" → Returns comprehensive article about Python
- "Artificial Intelligence" → Returns AI overview and applications
- "Carbon cycle" → Returns biogeochemical process information

### Error Handling
- "nonexistentquery12345" → "No results found for your query."
- "Mercury" → "Ambiguous topic. Try one of these: Mercury (planet), Mercury (element)..."

## 🔬 Key Research Insights

This repository goes beyond a simple Wikipedia tool - it provides deep insights into how MCP and AI tool selection works:

### 🧠 MCP Intelligence Discoveries

**1. Automatic Tool Discovery**
- AI agents automatically discover tools through MCP metadata
- No manual configuration or registration required
- Rich metadata (names, descriptions, types) guides intelligent selection

**2. Semantic Matching Over Keywords**
- AI agents use semantic understanding, not just keyword matching
- "Tell me about AI" → Understands information-seeking intent
- Matches user intent with tool capabilities intelligently

**3. LLM Quality Dependencies**
- Tool selection quality depends heavily on underlying LLM capabilities
- Advanced LLMs (GPT-4, Claude) → Perfect semantic analysis
- Basic LLMs → May need more explicit, keyword-rich descriptions

**4. Hyperparameter Impact**
- Temperature, top-k, top-p significantly affect tool selection consistency
- Recommended for MCP: Temperature 0.4, Top-K 30, Top-P 0.85
- Consistency more important than creativity for tool selection

### 🎯 Design Best Practices Demonstrated

**Metadata Excellence:**
- Clear, descriptive function names (`fetch_wikipedia_info`)
- Comprehensive docstrings explaining tool purpose
- Proper type hints for parameter compatibility
- Structured return formats (dict) perfect for AI processing

**Error Handling Strategies:**
- Graceful disambiguation handling
- Clear error messages for missing content
- Fallback behaviors for edge cases

### 🔍 Analysis Tools Created

**Configuration Validation:**
- `test_mcp_config.py` - Validates MCP setup (6 comprehensive tests)
- Ensures proper Python paths, server accessibility, and configuration

**Metadata Analysis:**
- `demonstrate_mcp_metadata.py` - Shows what AI agents see
- Reveals the metadata that drives intelligent tool selection

**Hyperparameter Research:**
- `llm_hyperparameters_impact.py` - Comprehensive analysis
- Shows how LLM settings affect tool selection quality and consistency

## 🛠️ Development

### Running Tests
```bash
pytest tests/ -v
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

## 🤝 Acknowledgments

- **Inspired by**: [Educative's MCP Fundamentals Course](https://www.educative.io)
- **Built with**: [Model Context Protocol](https://modelcontextprotocol.io/) and [FastMCP](https://github.com/modelcontextprotocol/python-sdk)
- **Powered by**: [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) via the `wikipedia` Python package

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs)
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [Wikipedia API Documentation](https://www.mediawiki.org/wiki/API:Main_page)
- [Project Repository](https://github.com/shuhaimiao/wikipedia-research-assistant)

---

## 🎉 **What Makes This Repository Special**

This isn't just a Wikipedia tool - it's a **comprehensive MCP research project** that:

✅ **Implements the Educative Course Solution** - Exact code from MCP Fundamentals Course  
✅ **Demonstrates MCP Intelligence** - Shows how AI agents automatically select tools  
✅ **Provides Deep Analysis** - Reveals the science behind tool selection  
✅ **Includes Research Tools** - Scripts to analyze metadata, hyperparameters, and configuration  
✅ **Offers Complete Documentation** - From setup to advanced MCP concepts  
✅ **Shows Best Practices** - Proven patterns for MCP tool design  

**Ready to explore both Wikipedia AND the intelligence behind MCP?** 🚀

Your Wikipedia Research Assistant demonstrates MCP working exactly as designed - intelligent, automatic tool selection powered by rich metadata and sophisticated AI reasoning. But more importantly, it reveals **how and why** this magic works!

**🔍 Start Exploring:**
1. Set up the tool: `python test_mcp_config.py`
2. See the metadata: `python demonstrate_mcp_metadata.py`  
3. Understand the intelligence: Read `MCP_TOOL_SELECTION_EXPLAINED.md`
4. Analyze hyperparameters: `python llm_hyperparameters_impact.py`

**This repository transforms you from an MCP user into an MCP expert!** 🎓
