# Quick MCP Configuration Reference

## 📋 Ready-to-Copy Configurations

### For VS Code (settings.json)

Add this to your VS Code `settings.json`:

```json
{
  "mcp.servers": {
    "wikipedia-research-assistant": {
      "command": "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/venv/bin/python",
      "args": [
        "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/src/wikipedia_assistant/server.py"
      ],
      "cwd": "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant",
      "env": {
        "PYTHONPATH": "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/src"
      }
    }
  }
}
```

### For Cursor (mcp-servers.json)

Create/edit `~/Library/Application Support/Cursor/mcp-servers.json`:

```json
{
  "mcpServers": {
    "wikipedia-research-assistant": {
      "command": "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/venv/bin/python",
      "args": [
        "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/src/wikipedia_assistant/server.py"
      ],
      "cwd": "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant",
      "env": {
        "PYTHONPATH": "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/src"
      }
    }
  }
}
```

## 🚀 Quick Setup Steps

### VS Code:
1. Install MCP extension
2. Open Settings → Search "MCP"
3. Edit settings.json and add the configuration above
4. Restart VS Code

### Cursor:
1. Create the config file: `~/Library/Application Support/Cursor/mcp-servers.json`
2. Add the configuration above
3. Restart Cursor

## 🧪 Test Command

To verify everything works:

```bash
python test_mcp_config.py
```

## 🎯 Available Tool

Once configured, you can use:

**Tool Name**: `fetch_wikipedia_info`
**Purpose**: Search Wikipedia and get structured information
**Example**: "Tell me about Python programming language"

---

✅ **Configuration Status**: Tested and Ready!
🎉 **All paths verified**: 6/6 tests passed 