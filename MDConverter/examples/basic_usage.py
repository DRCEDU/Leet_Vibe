"""
Example: Basic HTML to Markdown conversion
"""

from pathlib import Path
import sys

# Add the source directory to path for importing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mdconverter import HTMLToMarkdownConverter, Config


def basic_conversion_example():
    """Basic example of converting an HTML file to Markdown"""
    
    # Example HTML file path (replace with your actual file)
    html_file = "sample.html"
    
    if not Path(html_file).exists():
        print(f"Please create a sample HTML file: {html_file}")
        return
    
    try:
        # Basic conversion with default settings
        converter = HTMLToMarkdownConverter(html_file)
        success = converter.convert()
        
        if success:
            print(f"✅ Conversion successful!")
            print(f"Output file: {converter.output_file}")
        else:
            print("❌ Conversion failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")


def advanced_conversion_example():
    """Advanced example with custom configuration"""
    
    html_file = "sample.html"
    
    if not Path(html_file).exists():
        print(f"Please create a sample HTML file: {html_file}")
        return
    
    try:
        # Create custom configuration
        config = Config({
            'output_dir': 'custom_output',
            'images_dir': 'custom_images', 
            'add_metadata': True,
            'clean_html': True,
            'log_level': 'DEBUG'
        })
        
        # Convert with custom settings
        converter = HTMLToMarkdownConverter(
            html_file, 
            output_file="custom_output.md",
            config=config
        )
        
        success = converter.convert()
        
        if success:
            print(f"✅ Advanced conversion successful!")
            print(f"Output file: {converter.output_file}")
        else:
            print("❌ Conversion failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("=== Basic Conversion Example ===")
    basic_conversion_example()
    
    print("\n=== Advanced Conversion Example ===")
    advanced_conversion_example()
