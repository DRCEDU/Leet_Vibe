#!/bin/bash
# Installation script for Document Image Extractor package

set -e  # Exit on any error

echo "Document Image Extractor - Installation Script"
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.7+ and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✓ Found Python $python_version"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    echo "Please install pip3 and try again."
    exit 1
fi

echo "✓ Found pip3"

# Install dependencies
echo ""
echo "Installing dependencies..."
echo "------------------------"

pip3 install PyMuPDF>=1.23.0
echo "✓ Installed PyMuPDF (PDF processing)"

pip3 install Pillow>=9.0.0
echo "✓ Installed Pillow (image processing)"

echo ""
echo "Installation completed successfully!"
echo ""
echo "Usage:"
echo "------"
echo "# Navigate to the package directory"
echo "cd document-image-extractor"
echo ""
echo "# Run the package"
echo "python3 -m document_image_extractor                  # Interactive mode"
echo "python3 -m document_image_extractor document.pdf     # Process specific file"
echo ""
echo "# Test the installation"
echo "python3 test_package.py"
echo ""
echo "# For Python API usage, see README.md"
echo ""
echo "🎉 Ready to extract images from documents!"
