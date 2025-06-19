# MCP Integration Guide: VS Code & Cursor

This guide shows you how to integrate your Wikipedia Research Assistant with VS Code and Cursor using the Model Context Protocol (MCP).

## 🎯 Prerequisites

✅ **Completed Setup**: You should have already completed the basic setup from `SETUP_GUIDE.md`
✅ **Working Server**: Your `fetch_wikipedia_info` tool should be working
✅ **Virtual Environment**: Your Python venv should be activated and working

## 🔧 VS Code Integration

### Step 1: Install MCP Extension for VS Code

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "MCP" or "Model Context Protocol"
4. Install the MCP extension (the exact name may vary)

### Step 2: Configure MCP Server

1. **Open VS Code Settings**:
   - Press `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
   - Or go to Code → Preferences → Settings

2. **Find MCP Settings**:
   - Search for "MCP" in the settings search bar
   - Look for "MCP Servers" or similar configuration option

3. **Add Server Configuration**:
   - Click "Edit in settings.json" or find the JSON configuration option
   - Add the following configuration to your `settings.json`:

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

### Step 3: Restart VS Code

1. Close VS Code completely
2. Reopen VS Code
3. The MCP server should now be available

### Step 4: Test the Integration

1. Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
2. Look for MCP-related commands
3. Try using the Wikipedia Research Assistant tool
4. You should be able to ask questions like "Tell me about Python programming"

## 🔧 Cursor Integration

### Step 1: Check for MCP Support

Cursor may have built-in MCP support or require an extension. Check:

1. Open Cursor
2. Go to Extensions or Settings
3. Look for MCP or Model Context Protocol options

### Step 2: Configure MCP Server

**Option A: If Cursor has MCP settings in preferences:**

1. Open Cursor Settings/Preferences
2. Look for "MCP Servers" or "Model Context Protocol"
3. Add the server configuration

**Option B: If Cursor uses a configuration file:**

1. Create or edit the MCP configuration file (location varies by OS):
   - **macOS**: `~/Library/Application Support/Cursor/mcp-servers.json`
   - **Windows**: `%APPDATA%/Cursor/mcp-servers.json`
   - **Linux**: `~/.config/Cursor/mcp-servers.json`

2. Add this configuration:

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

### Step 3: Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. The MCP server should now be available

## 🧪 Testing Your Integration

### Manual Test Commands

You can test your MCP server manually from the terminal:

```bash
# Activate your virtual environment
source venv/bin/activate

# Test the server directly
python src/wikipedia_assistant/server.py
```

### Expected Behavior

When properly integrated, you should be able to:

1. **Ask Natural Questions**: "Tell me about artificial intelligence"
2. **Get Structured Responses**: Title, summary, and Wikipedia URL
3. **Handle Errors Gracefully**: Disambiguation suggestions, no results found
4. **Use in AI Conversations**: The AI assistant can call your tool automatically

## 🔍 Troubleshooting

### Common Issues

**1. "Command not found" or "Python not found"**
- ✅ **Solution**: Check that the Python path is correct
- ✅ **Verify**: Run `which python` in your terminal (with venv activated)

**2. "Module not found" errors**
- ✅ **Solution**: Check the `PYTHONPATH` environment variable
- ✅ **Verify**: The path should point to your `src` directory

**3. "Server not responding"**
- ✅ **Solution**: Test the server manually first
- ✅ **Check**: Run `python examples/test_tool.py` to verify functionality

**4. "Permission denied"**
- ✅ **Solution**: Make sure the Python executable has proper permissions
- ✅ **Fix**: Run `chmod +x venv/bin/python` if needed

### Debug Steps

1. **Test Server Manually**:
   ```bash
   source venv/bin/activate
   python examples/test_tool.py
   ```

2. **Check Paths**:
   ```bash
   ls -la /Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/venv/bin/python
   ls -la /Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant/src/wikipedia_assistant/server.py
   ```

3. **Verify Dependencies**:
   ```bash
   source venv/bin/activate
   python -c "import wikipedia, mcp; print('✅ All dependencies working')"
   ```

## 🎯 Configuration Explained

### Key Configuration Elements

- **`command`**: Path to your Python interpreter (in venv)
- **`args`**: Path to your server script
- **`cwd`**: Working directory for the server
- **`env.PYTHONPATH`**: Ensures Python can find your modules

### Why These Paths Matter

- **Virtual Environment**: Ensures all dependencies are available
- **Working Directory**: Allows relative imports and file access
- **PYTHONPATH**: Lets Python find your custom modules

## 🚀 Next Steps

Once integrated, you can:

1. **Ask Wikipedia Questions**: The AI can automatically use your tool
2. **Build More Tools**: Add more `@mcp.tool()` functions to your server
3. **Share with Others**: Others can use your MCP server configuration

## 📚 Additional Resources

- **MCP Documentation**: Check the official MCP documentation for your editor
- **Server Logs**: Monitor your terminal for server startup messages
- **Tool Testing**: Use `examples/test_tool.py` for development and debugging

---

**🎉 Congratulations!** Your Wikipedia Research Assistant is now integrated with your code editor and ready to help with research tasks! 