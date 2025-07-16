"""
Document Image Extractor Package
================================

A comprehensive package for extracting images from PDF and Word documents.

Features:
- Extract images from PDF files (.pdf)
- Extract images from Word documents (.docx)
- Automatic document type detection
- Zip archive creation with extracted content
- Image comparison utilities
- Command-line interface

Usage:
    from document_image_extractor import DocumentExtractor
    
    extractor = DocumentExtractor()
    images, zip_path = extractor.extract_images("document.pdf")
"""

__version__ = "1.0.0"
__author__ = "CJ Duan"

from .extractor import DocumentExtractor
from .pdf_extractor import PDFImageExtractor
from .word_extractor import WordImageExtractor
from .comparison import ImageComparison
from .utils import FileUtils, ZipUtils

__all__ = [
    'DocumentExtractor',
    'PDFImageExtractor', 
    'WordImageExtractor',
    'ImageComparison',
    'FileUtils',
    'ZipUtils'
]
