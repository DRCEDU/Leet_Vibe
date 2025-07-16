#!/usr/bin/env python3
"""
Command-line interface for the Document Image Extractor package.
"""

import sys
import os

# Add the package directory to the path to allow running as a script
if __name__ == "__main__":
    # Get the directory containing this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Add parent directory to path so we can import the package
    parent_dir = os.path.dirname(current_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from document_image_extractor.extractor import main

if __name__ == "__main__":
    main()
