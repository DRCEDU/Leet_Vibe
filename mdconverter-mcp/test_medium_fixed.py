#!/usr/bin/env python3
"""
Test script for the second webpage package (Medium article) with proper filename handling
"""

import sys
import os
sys.path.insert(0, 'src')

from mdconverter_mcp.server import HTMLToMarkdownConverter, validate_html_file, MDConverterConfig

def test_medium_conversion():
    """Test the HTML to Markdown conversion with the Medium article."""
    
    # Path to the Medium article (using glob to find the file)
    import glob
    pattern = "/mnt/c/Users/cjdua/Downloads/Capturing The Long-Term Causal Effect*.html"
    files = glob.glob(pattern)
    
    if not files:
        print("❌ Medium article file not found!")
        return False
    
    html_file = files[0]
    print(f"📄 Found file: {html_file}")
    
    print("🧪 Testing MDConverter MCP Server - Medium Article")
    print("=" * 60)
    
    # Test 1: Validate HTML file
    print("\n1. Validating HTML file...")
    is_valid, message = validate_html_file(html_file)
    print(f"   Valid: {is_valid}")
    print(f"   Message: {message}")
    
    if not is_valid:
        print("❌ HTML file validation failed!")
        return False
    
    # Test 2: Convert HTML to Markdown
    print("\n2. Converting HTML to Markdown...")
    try:
        config = MDConverterConfig(
            output_dir="test_output_medium",
            images_dir="images",
            preserve_images=True,
            clean_html=True,
            add_metadata=True
        )
        
        converter = HTMLToMarkdownConverter(html_file, config=config)
        markdown_content, result_info = converter.convert()
        
        print(f"   ✅ Conversion successful!")
        print(f"   Output file: {result_info['output_file']}")
        print(f"   Content length: {result_info['content_length']:,} characters")
        print(f"   Images processed: {result_info['images_processed']}")
        
        # Display metadata
        if result_info['metadata']:
            print(f"   Metadata extracted: {len(result_info['metadata'])} items")
            for key, value in result_info['metadata'].items():
                print(f"     - {key}: {value[:100]}..." if len(value) > 100 else f"     - {key}: {value}")
        
        # Show first few lines of markdown
        print(f"\n   First 500 characters of markdown:")
        print(f"   {'-' * 40}")
        print(f"   {markdown_content[:500]}...")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Conversion failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_medium_conversion()
    if success:
        print("\n🎉 Medium article conversion test passed!")
    else:
        print("\n💥 Medium article conversion test failed!")
        sys.exit(1)
