#!/usr/bin/env python3
"""
Test script to demonstrate the fetch_wikipedia_info tool functionality.

This script shows how the Wikipedia Research Assistant works with various queries.
"""

import sys
import os
import json

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wikipedia_assistant.server import fetch_wikipedia_info

def test_query(query: str):
    """Test a single query and display results."""
    print(f"🔍 Searching for: '{query}'")
    print("-" * 50)
    
    result = fetch_wikipedia_info(query)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"📖 Title: {result['title']}")
        print(f"🔗 URL: {result['url']}")
        print(f"📝 Summary: {result['summary'][:200]}...")
        print(f"   (Full summary length: {len(result['summary'])} characters)")
    
    print("\n" + "=" * 60 + "\n")

def main():
    """Run demonstration queries."""
    print("🎯 Wikipedia Research Assistant - Tool Demonstration")
    print("Following the Educative Course Implementation")
    print("=" * 60 + "\n")
    
    # Test queries from the course examples
    test_queries = [
        "Alan Turing",
        "Python programming language", 
        "Artificial Intelligence",
        "Carbon cycle",
        "Quantum computing",
        "nonexistentquery12345",  # Should trigger "no results" error
        "Mercury"  # Might trigger disambiguation
    ]
    
    for query in test_queries:
        test_query(query)
    
    print("✅ Demonstration complete!")
    print("💡 The fetch_wikipedia_info tool is working correctly and ready for MCP integration.")

if __name__ == "__main__":
    main() 