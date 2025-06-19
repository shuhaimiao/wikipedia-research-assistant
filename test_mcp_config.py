#!/usr/bin/env python3
"""
Test script to verify MCP configuration is correct.
This script validates all the paths and settings used in the MCP configuration files.
"""

import os
import sys
import subprocess
import json

def test_mcp_configuration():
    """Test that all MCP configuration elements are correct."""
    print("🧪 Testing MCP Configuration for Wikipedia Research Assistant")
    print("=" * 60)
    
    # Configuration paths (from the MCP config files)
    project_root = "/Users/smiao/Documents/Workspace/GitHub/shuhaimiao/wikipedia-research-assistant"
    python_path = f"{project_root}/venv/bin/python"
    server_path = f"{project_root}/src/wikipedia_assistant/server.py"
    pythonpath_env = f"{project_root}/src"
    
    tests_passed = 0
    total_tests = 6
    
    # Test 1: Project root exists
    print("1. Testing project root directory...")
    if os.path.exists(project_root):
        print(f"   ✅ Project root exists: {project_root}")
        tests_passed += 1
    else:
        print(f"   ❌ Project root not found: {project_root}")
    
    # Test 2: Python interpreter exists
    print("\n2. Testing Python interpreter...")
    if os.path.exists(python_path):
        print(f"   ✅ Python interpreter exists: {python_path}")
        tests_passed += 1
    else:
        print(f"   ❌ Python interpreter not found: {python_path}")
    
    # Test 3: Server script exists
    print("\n3. Testing server script...")
    if os.path.exists(server_path):
        print(f"   ✅ Server script exists: {server_path}")
        tests_passed += 1
    else:
        print(f"   ❌ Server script not found: {server_path}")
    
    # Test 4: PYTHONPATH directory exists
    print("\n4. Testing PYTHONPATH directory...")
    if os.path.exists(pythonpath_env):
        print(f"   ✅ PYTHONPATH directory exists: {pythonpath_env}")
        tests_passed += 1
    else:
        print(f"   ❌ PYTHONPATH directory not found: {pythonpath_env}")
    
    # Test 5: Python can import required modules
    print("\n5. Testing Python dependencies...")
    try:
        env = os.environ.copy()
        env['PYTHONPATH'] = pythonpath_env
        result = subprocess.run([
            python_path, '-c', 
            'import wikipedia, mcp; from wikipedia_assistant.server import fetch_wikipedia_info; print("All imports successful")'
        ], capture_output=True, text=True, env=env, cwd=project_root)
        
        if result.returncode == 0:
            print("   ✅ All Python dependencies can be imported")
            tests_passed += 1
        else:
            print(f"   ❌ Import error: {result.stderr}")
    except Exception as e:
        print(f"   ❌ Failed to test imports: {e}")
    
    # Test 6: Server function works
    print("\n6. Testing server functionality...")
    try:
        env = os.environ.copy()
        env['PYTHONPATH'] = pythonpath_env
        result = subprocess.run([
            python_path, '-c', 
            'from wikipedia_assistant.server import fetch_wikipedia_info; result = fetch_wikipedia_info("Python programming language"); print("SUCCESS" if "title" in result else "FAILED")'
        ], capture_output=True, text=True, env=env, cwd=project_root)
        
        if result.returncode == 0 and "SUCCESS" in result.stdout:
            print("   ✅ Server function works correctly")
            tests_passed += 1
        else:
            print(f"   ❌ Server function failed: {result.stderr}")
    except Exception as e:
        print(f"   ❌ Failed to test server function: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"🎯 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Your MCP configuration should work perfectly.")
        print("\n📋 Next steps:")
        print("   1. Copy the configuration from mcp-config-vscode.json or mcp-config-cursor.json")
        print("   2. Add it to your editor's MCP settings")
        print("   3. Restart your editor")
        print("   4. Start using your Wikipedia Research Assistant!")
    else:
        print("⚠️  Some tests failed. Please check the errors above before proceeding.")
        print("   Run this script again after fixing the issues.")
    
    return tests_passed == total_tests

def show_config_files():
    """Display the contents of the MCP configuration files."""
    print("\n📄 MCP Configuration Files:")
    print("=" * 40)
    
    config_files = ["mcp-config-vscode.json", "mcp-config-cursor.json"]
    
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"\n📁 {config_file}:")
            print("-" * 30)
            with open(config_file, 'r') as f:
                content = json.load(f)
                print(json.dumps(content, indent=2))
        else:
            print(f"\n❌ {config_file} not found")

if __name__ == "__main__":
    success = test_mcp_configuration()
    show_config_files()
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1) 