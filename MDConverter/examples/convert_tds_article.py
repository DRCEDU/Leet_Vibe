#!/usr/bin/env python3
"""
Example usage script for converting the TDS article to markdown.
"""

import os
import sys
from pathlib import Path

# Add the current directory to path so we can import our converter
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from html_to_markdown_converter import WebpageToMarkdownConverter
except ImportError:
    print("❌ Could not import converter. Make sure html_to_markdown_converter.py is in the same directory.")
    sys.exit(1)

def convert_tds_article():
    """Convert the TDS Topic Modeling article to markdown."""
    
    # Define paths
    html_file = "/mnt/c/Users/cjdua/Downloads/Topic Model Labelling with LLMs _ Towards Data Science.html"
    output_file = current_dir / "output" / "TDS_Topic_Model_Labelling_with_LLMs.md"
    
    # Ensure output directory exists
    output_file.parent.mkdir(exist_ok=True)
    
    # Check if input file exists
    if not Path(html_file).exists():
        print(f"❌ HTML file not found: {html_file}")
        print("Please check the file path and try again.")
        return False
    
    try:
        print("🔄 Converting TDS article to markdown...")
        
        # Create converter
        converter = WebpageToMarkdownConverter(html_file, str(output_file))
        
        # Perform conversion
        markdown_content = converter.convert()
        
        print(f"✅ Successfully converted to: {output_file}")
        print(f"📄 Generated {len(markdown_content):,} characters of markdown content")
        
        # Print some stats
        if converter.processed_images:
            print(f"📸 Processed {len(converter.processed_images)} images")
        
        if converter.assets_folder:
            print(f"📁 Assets folder: {converter.assets_folder}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return False

def main():
    """Main function."""
    print("TDS Article to Markdown Converter")
    print("=" * 40)
    
    success = convert_tds_article()
    
    if success:
        print("\n🎉 Conversion completed successfully!")
        print("\nNext steps:")
        print("1. Review the generated markdown file")
        print("2. Check the images/ folder for processed images")
        print("3. Edit the markdown as needed")
    else:
        print("\n💥 Conversion failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
