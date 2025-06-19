#!/usr/bin/env python3
"""
Demonstration script showing what metadata MCP servers expose to clients.
This explains how VS Code agent decides which tools to call.
"""

import inspect
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from wikipedia_assistant.server import fetch_wikipedia_info, mcp

def demonstrate_mcp_metadata():
    """Show what metadata MCP clients receive about our tools."""
    
    print("🔍 MCP Tool Discovery: What VS Code Agent Sees")
    print("=" * 60)
    
    print("\n📋 1. SERVER INFORMATION")
    print("-" * 30)
    print(f"Server Name: 'WikipediaSearch'")
    print(f"Server Type: FastMCP")
    print(f"Transport: stdio (standard input/output)")
    
    print("\n📋 2. TOOL METADATA EXPOSED TO CLIENT")
    print("-" * 30)
    
    # Tool name (from function name)
    print(f"Tool Name: '{fetch_wikipedia_info.__name__}'")
    
    # Tool description (from docstring)
    print(f"Tool Description: '{fetch_wikipedia_info.__doc__.strip()}'")
    
    # Function signature (parameter types and return type)
    sig = inspect.signature(fetch_wikipedia_info)
    print(f"Function Signature: {fetch_wikipedia_info.__name__}{sig}")
    
    # Parameter details
    print("\nParameter Details:")
    for param_name, param in sig.parameters.items():
        print(f"  - {param_name}: {param.annotation.__name__ if param.annotation != inspect.Parameter.empty else 'Any'}")
    
    # Return type
    return_annotation = sig.return_annotation
    return_type = return_annotation.__name__ if return_annotation != inspect.Parameter.empty else 'Any'
    print(f"Return Type: {return_type}")
    
    print("\n📋 3. WHAT THE AI AGENT ANALYZES")
    print("-" * 30)
    
    analysis_factors = [
        ("Tool Name", "fetch_wikipedia_info", "Contains 'wikipedia' - suggests Wikipedia functionality"),
        ("Description", "Search Wikipedia for a topic and return title, summary, and URL", "Clearly indicates Wikipedia search capability"),
        ("Parameter", "query: str", "Expects a search query string"),
        ("Return Type", "dict", "Returns structured data (dictionary)"),
        ("Server Name", "WikipediaSearch", "Reinforces Wikipedia focus")
    ]
    
    for factor, value, meaning in analysis_factors:
        print(f"  {factor}: '{value}'")
        print(f"    → {meaning}")
        print()

def analyze_prompt_matching():
    """Explain how the prompt 'Tell me about artificial intelligence' matches our tool."""
    
    print("\n🧠 PROMPT ANALYSIS: 'Tell me about artificial intelligence'")
    print("=" * 60)
    
    print("\n📝 1. PROMPT BREAKDOWN")
    print("-" * 30)
    prompt_elements = [
        ("Intent", "Tell me about", "Information seeking/research request"),
        ("Subject", "artificial intelligence", "Specific topic to research"),
        ("Expectation", "Implicit", "User wants comprehensive information")
    ]
    
    for element, content, analysis in prompt_elements:
        print(f"  {element}: '{content}'")
        print(f"    → {analysis}")
        print()
    
    print("📊 2. TOOL MATCHING LOGIC")
    print("-" * 30)
    
    matching_factors = [
        ("✅ Topic Research", "User wants information about a specific topic", "Matches Wikipedia search purpose"),
        ("✅ Comprehensive Info", "User expects detailed information", "Wikipedia provides comprehensive articles"),
        ("✅ Reliable Source", "Information request implies need for reliability", "Wikipedia is a trusted information source"),
        ("✅ Structured Response", "AI needs structured data to format response", "Tool returns title, summary, URL"),
        ("✅ Query Format", "'artificial intelligence' is a searchable term", "Matches expected query parameter")
    ]
    
    for match, reason, conclusion in matching_factors:
        print(f"  {match}")
        print(f"    Reason: {reason}")
        print(f"    Match: {conclusion}")
        print()

def show_mcp_communication_flow():
    """Show the complete MCP communication flow."""
    
    print("\n🔄 MCP COMMUNICATION FLOW")
    print("=" * 60)
    
    steps = [
        ("1. Tool Discovery", "VS Code → MCP Server", "Request: 'What tools do you have?'"),
        ("", "MCP Server → VS Code", "Response: Tool metadata (name, description, parameters)"),
        ("2. Prompt Analysis", "VS Code AI Agent", "Analyzes user prompt: 'Tell me about artificial intelligence'"),
        ("3. Tool Selection", "VS Code AI Agent", "Matches prompt intent with available tool capabilities"),
        ("4. Tool Execution", "VS Code → MCP Server", "Call: fetch_wikipedia_info('artificial intelligence')"),
        ("", "MCP Server → Wikipedia", "HTTP request to Wikipedia API"),
        ("", "Wikipedia → MCP Server", "Returns article data"),
        ("", "MCP Server → VS Code", "Returns: {title, summary, url}"),
        ("5. Response Generation", "VS Code AI Agent", "Formats structured data into natural language response")
    ]
    
    for step, direction, description in steps:
        if step:
            print(f"\n{step}")
            print("-" * 20)
        print(f"  {direction}: {description}")

def demonstrate_decision_factors():
    """Show the key factors that influenced tool selection."""
    
    print("\n🎯 KEY DECISION FACTORS")
    print("=" * 60)
    
    print("\n🔍 Why fetch_wikipedia_info was chosen:")
    print("-" * 40)
    
    decision_factors = [
        ("High Relevance", "Tool name contains 'wikipedia' - directly matches information seeking"),
        ("Clear Purpose", "Description mentions 'Search Wikipedia for a topic'"),
        ("Perfect Match", "Function expects 'query: str' - matches user's topic"),
        ("Structured Output", "Returns dict with title/summary/url - ideal for AI response"),
        ("No Alternatives", "Only one tool available - but it's perfectly suited"),
        ("Topic Suitability", "'Artificial intelligence' is exactly the type of topic Wikipedia covers well")
    ]
    
    for factor, explanation in decision_factors:
        print(f"  ✅ {factor}")
        print(f"     → {explanation}")
        print()

if __name__ == "__main__":
    demonstrate_mcp_metadata()
    analyze_prompt_matching()
    show_mcp_communication_flow()
    demonstrate_decision_factors()
    
    print("\n" + "=" * 60)
    print("🎉 SUMMARY: How VS Code Agent Made Its Decision")
    print("=" * 60)
    print("""
The VS Code agent chose fetch_wikipedia_info because:

1. 📊 METADATA ANALYSIS: Tool metadata clearly indicated Wikipedia search capability
2. 🧠 PROMPT MATCHING: User's request matched the tool's purpose perfectly  
3. 🎯 PARAMETER COMPATIBILITY: Tool expects exactly what user provided (a topic)
4. 📋 OUTPUT SUITABILITY: Tool returns structured data perfect for AI response
5. 🔄 PROTOCOL EFFICIENCY: MCP enabled seamless tool discovery and execution

This is MCP working as designed - intelligent tool selection based on 
comprehensive metadata analysis and semantic matching!
""") 