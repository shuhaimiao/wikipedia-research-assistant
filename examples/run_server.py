#!/usr/bin/env python3
"""
Example script to run the Wikipedia Research Assistant MCP Server.

This follows the Educative course implementation using FastMCP.
The server runs with stdio transport, suitable for MCP client connections.
"""

import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wikipedia_assistant.server import mcp

if __name__ == "__main__":
    print("🚀 Starting Wikipedia Research Assistant MCP Server...")
    print("📚 Available tools:")
    print("  - fetch_wikipedia_info: Search Wikipedia and get structured information")
    print("💡 Server running with stdio transport - ready for MCP client connections")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error running server: {e}")
        sys.exit(1) 