#!/bin/bash
"""
Setup script for HTML to Markdown Converter
This script sets up the environment and provides usage instructions.
"""

echo "🚀 HTML to Markdown Converter Setup"
echo "===================================="

# Check if we're in the right directory
if [ ! -f "html_to_markdown_converter.py" ]; then
    echo "❌ Error: html_to_markdown_converter.py not found in current directory"
    echo "Please run this script from the MDConverter directory."
    echo "Usage: cd MDConverter && ./setup_converter.sh"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "converter_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv converter_env
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
    echo "✅ Virtual environment created"
fi

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source converter_env/bin/activate

# Install packages
pip install beautifulsoup4 requests markdownify lxml html5lib

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Usage Instructions:"
echo "======================"
echo ""
echo "1. To convert a webpage package to markdown:"
echo "   source converter_env/bin/activate"
echo "   python3 html_to_markdown_converter.py \"path/to/your/webpage.html\""
echo ""
echo "2. To convert with custom output file:"
echo "   source converter_env/bin/activate"
echo "   python3 html_to_markdown_converter.py \"input.html\" \"output.md\""
echo ""
echo "3. To see all options:"
echo "   source converter_env/bin/activate"
echo "   python3 html_to_markdown_converter.py --help"
echo ""
echo "4. To run example scripts:"
echo "   source converter_env/bin/activate"
echo "   python3 demo_converter.py"
echo "   python3 convert_tds_article.py"
echo ""
echo "📁 Files in this folder:"
echo "- converter_env/                      (virtual environment)"
echo "- html_to_markdown_converter.py       (main converter script)"
echo "- requirements_html_converter.txt     (dependencies list)"
echo "- README.md                          (this folder's documentation)"
echo "- README_html_converter.md           (comprehensive documentation)"
echo "- convert_tds_article.py             (TDS article example)"
echo "- demo_converter.py                  (demo script)"
echo ""
echo "💡 Quick Start:"
echo "   source converter_env/bin/activate"
echo "   python3 html_to_markdown_converter.py --help"
