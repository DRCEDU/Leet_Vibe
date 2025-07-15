#!/usr/bin/env python3
"""
Quick test and demonstration of the HTML to Markdown converter
"""

import os
import sys
from pathlib import Path

def demonstrate_converter():
    """Demonstrate how the converter works with example paths."""
    
    print("🔄 HTML to Markdown Converter Demo")
    print("=" * 40)
    
    # Common file paths for TDS articles
    possible_paths = [
        "/mnt/c/Users/cjdua/Downloads/Topic Model Labelling with LLMs _ Towards Data Science.html",
        "./Topic Model Labelling with LLMs _ Towards Data Science.html",
        "Topic Model Labelling with LLMs _ Towards Data Science.html"
    ]
    
    print("🔍 Checking for HTML file in common locations...")
    
    html_file = None
    for path in possible_paths:
        if os.path.exists(path):
            html_file = path
            print(f"✅ Found HTML file: {path}")
            break
        else:
            print(f"❌ Not found: {path}")
    
    if not html_file:
        print("\n📝 Manual Usage Instructions:")
        print("1. Activate the virtual environment:")
        print("   source converter_env/bin/activate")
        print("")
        print("2. Run the converter with the correct path:")
        print("   python3 html_to_markdown_converter.py \"YOUR_HTML_FILE_PATH\"")
        print("")
        print("3. Example:")
        print("   python3 html_to_markdown_converter.py \"/full/path/to/Topic Model Labelling with LLMs _ Towards Data Science.html\"")
        print("")
        return False
    
    # Test import
    try:
        from html_to_markdown_converter import WebpageToMarkdownConverter
        print("✅ Converter module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import converter: {e}")
        print("Make sure you're in the virtual environment:")
        print("   source converter_env/bin/activate")
        return False
    
    # Try conversion
    try:
        print(f"\n🔄 Converting: {html_file}")
        
        output_file = "TDS_Topic_Model_Labelling_Demo.md"
        converter = WebpageToMarkdownConverter(html_file, output_file)
        
        markdown_content = converter.convert()
        
        print(f"✅ Conversion successful!")
        print(f"📄 Output file: {output_file}")
        print(f"📊 Content size: {len(markdown_content):,} characters")
        
        # Show first few lines
        lines = markdown_content.split('\n')
        preview_lines = lines[:20]
        
        print(f"\n📖 Preview (first 20 lines):")
        print("-" * 50)
        for i, line in enumerate(preview_lines, 1):
            print(f"{i:2d}: {line}")
        
        if len(lines) > 20:
            print(f"... ({len(lines) - 20} more lines)")
        
        return True
        
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
        return False

if __name__ == "__main__":
    success = demonstrate_converter()
    
    if success:
        print(f"\n🎉 Demo completed successfully!")
    else:
        print(f"\n💡 Demo completed with instructions for manual usage.")
    
    print(f"\n📚 For more information, see README_html_converter.md")
