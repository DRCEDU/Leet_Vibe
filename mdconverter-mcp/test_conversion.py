#!/usr/bin/env python3
"""
Test script for the mdconverter-mcp server functionality
"""

import sys
import os
sys.path.insert(0, 'src')

from mdconverter_mcp.server import HTMLToMarkdownConverter, validate_html_file, MDConverterConfig

def test_conversion():
    """Test the HTML to Markdown conversion with one of the downloaded webpage packages."""
    
    # Path to the TDS article
    html_file = "/mnt/c/Users/cjdua/Downloads/Accuracy Is Dead_ Calibration, Discrimination, and Other Metrics You Actually Need _ Towards Data Science.html"
    
    print("🧪 Testing MDConverter MCP Server")
    print("=" * 50)
    
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
            output_dir="test_output",
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
        return False

if __name__ == "__main__":
    success = test_conversion()
    if success:
        print("\n🎉 All tests passed!")
    else:
        print("\n💥 Tests failed!")
        sys.exit(1)
