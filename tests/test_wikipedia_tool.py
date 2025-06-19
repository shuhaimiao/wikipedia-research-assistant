"""Test the Wikipedia fetch tool implementation."""
import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wikipedia_assistant.server import fetch_wikipedia_info


def test_fetch_wikipedia_info_success():
    """Test successful Wikipedia query."""
    result = fetch_wikipedia_info("Python programming language")
    
    assert isinstance(result, dict)
    assert "title" in result
    assert "summary" in result
    assert "url" in result
    assert "error" not in result
    
    # Verify the content is reasonable
    assert len(result["title"]) > 0
    assert len(result["summary"]) > 100  # Should have substantial content
    assert result["url"].startswith("https://en.wikipedia.org/wiki/")


def test_fetch_wikipedia_info_no_results():
    """Test query with no results."""
    result = fetch_wikipedia_info("xyznonexistentquery123456")
    
    assert isinstance(result, dict)
    assert "error" in result
    assert "No results found" in result["error"]


def test_fetch_wikipedia_info_ambiguous():
    """Test ambiguous query that triggers disambiguation."""
    # "Mercury" is typically ambiguous (planet, element, etc.)
    result = fetch_wikipedia_info("Mercury")
    
    assert isinstance(result, dict)
    # This might return either a valid result or disambiguation error
    # depending on Wikipedia's current disambiguation handling
    if "error" in result:
        assert "Ambiguous topic" in result["error"] or "Try one of these" in result["error"]
    else:
        # If it returns a result, it should be valid
        assert "title" in result
        assert "summary" in result
        assert "url" in result


def test_fetch_wikipedia_info_basic_functionality():
    """Test basic functionality with a well-known topic."""
    result = fetch_wikipedia_info("Albert Einstein")
    
    assert isinstance(result, dict)
    if "error" not in result:
        assert "title" in result
        assert "summary" in result
        assert "url" in result
        assert "Einstein" in result["title"] 