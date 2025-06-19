"""Test basic setup and imports."""
import pytest
import sys


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
    assert sys.version_info >= (3, 8)


def test_wikipedia_basic_functionality():
    """Test basic Wikipedia functionality."""
    import wikipedia
    
    # Test search functionality
    results = wikipedia.search("Python programming", results=3)
    assert isinstance(results, list)
    assert len(results) > 0
    
    # Test that we can get a page summary
    try:
        summary = wikipedia.summary("Python (programming language)", sentences=2)
        assert isinstance(summary, str)
        assert len(summary) > 0
    except wikipedia.exceptions.DisambiguationError:
        # This is fine - just means the topic has multiple meanings
        pass
    except wikipedia.exceptions.PageError:
        # This is also fine - just means the page doesn't exist
        pass 