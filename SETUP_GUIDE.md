# Wikipedia Research Assistant - Setup Guide

This guide will walk you through setting up the Wikipedia Research Assistant project from scratch. Follow these steps carefully to ensure a proper development environment.

## 📋 Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- pip package manager
- Git (for version control)
- A terminal/command line interface

### Verify Python Installation
```bash
python --version
# or
python3 --version
```

### Verify pip Installation
```bash
pip --version
# or
pip3 --version
```

## 🚀 Step-by-Step Setup

### Step 1: Navigate to Your Project Directory
```bash
# Navigate to where you want to create the project
cd /Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant
```

### Step 2: Create Python Virtual Environment
A virtual environment isolates your project dependencies from your system Python installation.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Alternative if using python3 specifically
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

**Verification:** After activation, your terminal prompt should show `(venv)` at the beginning.

### Step 4: Upgrade pip (Recommended)
```bash
pip install --upgrade pip
```

### Step 5: Install Required Dependencies

Install the core libraries needed for the Wikipedia Research Assistant:

```bash
# Install Wikipedia API wrapper
pip install wikipedia

# Install MCP (Model Context Protocol) SDK
pip install mcp
```

### Step 6: Create Requirements File
Document your dependencies for future reference and deployment:

```bash
# Generate requirements.txt with current packages
pip freeze > requirements.txt
```

### Step 7: Verify Installation
Test that the packages are installed correctly:

```bash
python -c "import wikipedia; print('Wikipedia package installed successfully')"
python -c "import mcp; print('MCP package installed successfully')"
```

## 📁 Project Structure Setup

### Step 8: Create Project Directory Structure
```bash
# Create source directory
mkdir -p src/wikipedia_assistant

# Create tests directory
mkdir tests

# Create other necessary directories
mkdir docs
mkdir examples
```

### Step 9: Create Initial Python Files
```bash
# Create main package files
touch src/wikipedia_assistant/__init__.py
touch src/wikipedia_assistant/server.py
touch src/wikipedia_assistant/wikipedia_client.py
touch src/wikipedia_assistant/summarizer.py
touch src/wikipedia_assistant/models.py

# Create test files
touch tests/__init__.py
touch tests/test_server.py
touch tests/test_client.py
touch tests/test_integration.py

# Create configuration files
touch .env.example
touch setup.py
```

### Step 10: Create Environment Configuration
```bash
# Create .env.example file
cat > .env.example << 'EOF'
# Wikipedia Research Assistant Configuration
DEBUG=True
LOG_LEVEL=INFO
MCP_SERVER_PORT=8000
WIKIPEDIA_LANGUAGE=en
MAX_SUMMARY_LENGTH=500
EOF

# Copy to actual .env file
cp .env.example .env
```

## 🔧 Development Environment Setup

### Step 11: Install Development Dependencies
```bash
# Install testing and development tools
pip install pytest pytest-cov black flake8 mypy

# Update requirements.txt
pip freeze > requirements.txt
```

### Step 12: Create Setup Configuration
```bash
cat > setup.py << 'EOF'
from setuptools import setup, find_packages

setup(
    name="wikipedia-research-assistant",
    version="0.1.0",
    description="A MCP server for intelligent Wikipedia research",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "wikipedia>=1.4.0",
        "mcp>=0.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ]
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "wikipedia-assistant=wikipedia_assistant.server:main",
        ],
    },
)
EOF
```

### Step 13: Install Package in Development Mode
```bash
# Install the package in editable mode
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"
```

## 🧪 Testing the Setup

### Step 14: Create a Simple Test
```bash
cat > tests/test_setup.py << 'EOF'
"""Test basic setup and imports."""
import pytest

def test_wikipedia_import():
    """Test that wikipedia package can be imported."""
    import wikipedia
    assert hasattr(wikipedia, 'search')
    assert hasattr(wikipedia, 'page')

def test_mcp_import():
    """Test that mcp package can be imported."""
    import mcp
    # Basic import test - specific attributes depend on MCP version

def test_python_version():
    """Test that Python version is compatible."""
    import sys
    assert sys.version_info >= (3, 8)
EOF
```

### Step 15: Run Initial Tests
```bash
# Run the setup tests
pytest tests/test_setup.py -v

# Run with coverage
pytest tests/test_setup.py --cov=src --cov-report=term-missing
```

## 📝 Quick Reference Commands

### Virtual Environment Management
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Deactivate virtual environment
deactivate

# Remove virtual environment (if needed)
rm -rf venv              # macOS/Linux
rmdir /s venv            # Windows
```

### Package Management
```bash
# Install new package
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Uninstall package
pip uninstall package_name
```

### Development Commands
```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src

# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

## 🔍 Troubleshooting

### Common Issues and Solutions

1. **Virtual Environment Not Activating**
   - Ensure you're in the correct directory
   - Check the path to the activation script
   - Try using the full path: `/path/to/venv/bin/activate`

2. **Package Installation Fails**
   - Upgrade pip: `pip install --upgrade pip`
   - Use `--user` flag: `pip install --user package_name`
   - Check internet connection

3. **Import Errors**
   - Ensure virtual environment is activated
   - Verify packages are installed: `pip list`
   - Check Python path: `python -c "import sys; print(sys.path)"`

4. **Permission Errors**
   - Use virtual environment instead of system Python
   - Check file permissions: `ls -la`
   - Use `sudo` only if absolutely necessary (not recommended)

## 📚 Next Steps

After completing this setup:

1. **Implement the Wikipedia Client** (`src/wikipedia_assistant/wikipedia_client.py`)
2. **Create the MCP Server** (`src/wikipedia_assistant/server.py`)
3. **Add Summarization Logic** (`src/wikipedia_assistant/summarizer.py`)
4. **Define Data Models** (`src/wikipedia_assistant/models.py`)
5. **Write Comprehensive Tests**
6. **Add Documentation and Examples**

## 🎯 Verification Checklist

- [ ] Python 3.8+ installed and accessible
- [ ] Virtual environment created and activated
- [ ] Required packages (wikipedia, mcp) installed
- [ ] Project structure created
- [ ] Configuration files in place
- [ ] Development tools installed
- [ ] Basic tests passing
- [ ] Package installed in development mode

---

**Congratulations!** 🎉 Your Wikipedia Research Assistant development environment is now ready. You can proceed with implementing the core functionality of your MCP server.

Remember to always activate your virtual environment before working on the project:
```bash
source venv/bin/activate  # macOS/Linux
```

Happy coding! 🚀 