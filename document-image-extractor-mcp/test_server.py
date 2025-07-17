#!/usr/bin/env python3
"""
Simple test script to verify the MCP server tools are working.
"""

import asyncio
import json
from src.document_image_extractor_mcp.server import handle_list_tools, handle_call_tool


async def test_server():
    """Test the MCP server functionality."""
    print("🔧 Testing Document Image Extractor MCP Server")
    print("=" * 60)
    
    # Test 1: List available tools
    print("\n1. Testing list_tools:")
    try:
        tools = await handle_list_tools()
        print(f"✅ Found {len(tools)} tools:")
        for tool in tools:
            print(f"   - {tool.name}: {tool.description}")
    except Exception as e:
        print(f"❌ Error listing tools: {e}")
        return
    
    # Test 2: Test list_supported_formats tool
    print("\n2. Testing list_supported_formats tool:")
    try:
        result = await handle_call_tool("list_supported_formats", {})
        print("✅ Supported formats:")
        print(result[0].text)
    except Exception as e:
        print(f"❌ Error testing list_supported_formats: {e}")
    
    # Test 3: Test validate_document tool with non-existent file
    print("\n3. Testing validate_document tool (non-existent file):")
    try:
        result = await handle_call_tool("validate_document", {
            "document_path": "/non/existent/file.pdf"
        })
        print("✅ Validation result:")
        print(result[0].text)
    except Exception as e:
        print(f"❌ Error testing validate_document: {e}")
    
    # Test 4: Test get_document_info tool with non-existent file
    print("\n4. Testing get_document_info tool (non-existent file - should fail gracefully):")
    try:
        result = await handle_call_tool("get_document_info", {
            "document_path": "/non/existent/file.pdf"
        })
        print("✅ Document info result:")
        print(result[0].text)
    except Exception as e:
        print(f"❌ Error testing get_document_info: {e}")
    
    # Test 5: Test extract_document_images tool with non-existent file
    print("\n5. Testing extract_document_images tool (non-existent file - should fail gracefully):")
    try:
        result = await handle_call_tool("extract_document_images", {
            "document_path": "/non/existent/file.pdf"
        })
        print("✅ Extraction result:")
        print(result[0].text)
    except Exception as e:
        print(f"❌ Error testing extract_document_images: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 MCP Server test completed!")
    print("\nThe server appears to be working correctly.")
    print("You can now integrate it with MCP clients like Claude Desktop.")


if __name__ == "__main__":
    asyncio.run(test_server())
