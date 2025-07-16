# Document Image Extractor

A comprehensive Python package for extracting images from PDF and Word documents with advanced features including automatic document detection, ZIP archiving, and image comparison utilities.

## Features

- **Universal Document Support**: Extract images from both PDF (.pdf) and Word (.docx) documents
- **Automatic Document Detection**: Automatically detects document type and uses appropriate extraction method
- **Smart Image Filtering**: Filters out tiny decorative images from PDFs (configurable threshold)
- **ZIP Archive Creation**: Automatically creates ZIP archives with original document and extracted images
- **Image Format Detection**: Detects image formats using file signatures (magic numbers)
- **Interactive CLI**: Command-line interface with interactive document selection
- **Batch Processing**: Process multiple documents at once
- **Image Comparison**: Compare extracted images from different sources
- **Detailed Logging**: Comprehensive extraction reports and summaries

## Installation

### Prerequisites

Make sure you have Python 3.7+ installed.

### Install Dependencies

```bash
# Navigate to the package directory
cd document-image-extractor

# Install required dependencies
pip install -r requirements.txt
```

### Required Dependencies

- **PyMuPDF (fitz)**: For PDF processing
- **Pillow (PIL)**: For image processing and format detection

## Usage

### Command Line Interface

#### Basic Usage

```bash
# Extract images from a specific document
python -m document_image_extractor document.pdf
python -m document_image_extractor report.docx

# Interactive mode - automatically finds and lets you select documents
python -m document_image_extractor

# Show help
python -m document_image_extractor --help
```

#### Examples

```bash
# Process a PDF file
python -m document_image_extractor /path/to/document.pdf

# Process a Word document
python -m document_image_extractor /path/to/report.docx

# Interactive selection (searches current directory and Downloads)
python -m document_image_extractor
```

### Python API

#### Basic Usage

```python
from document_image_extractor import DocumentExtractor

# Initialize extractor
extractor = DocumentExtractor()

# Extract images from a document
images, zip_path = extractor.extract_images("document.pdf")

print(f"Extracted {len(images)} images")
if zip_path:
    print(f"Archive created: {zip_path}")
```

#### Advanced Usage

```python
from document_image_extractor import DocumentExtractor, ImageComparison

# Initialize with custom settings
extractor = DocumentExtractor(
    min_image_size=20,  # Minimum 20x20 pixels for PDF images
    create_zip=True     # Create ZIP archives
)

# Extract from multiple documents
documents = ["doc1.pdf", "doc2.docx", "doc3.pdf"]
results = extractor.extract_from_multiple_documents(documents)

# Get document information without extracting
info = extractor.get_document_info("document.pdf")
print(f"Document has {info['page_count']} pages")

# Count images without extracting
total_images, page_breakdown = extractor.count_images("document.pdf")
print(f"Total images: {total_images}")

# Compare extractions
comparison = ImageComparison()
comparison.compare_extraction_directories("pdf_images/", "word_images/")
```

#### Individual Extractors

```python
from document_image_extractor import PDFImageExtractor, WordImageExtractor

# PDF-specific extraction
pdf_extractor = PDFImageExtractor(min_image_size=15)
pdf_images = pdf_extractor.extract_images("document.pdf")

# Word-specific extraction  
word_extractor = WordImageExtractor()
word_images = word_extractor.extract_images("document.docx")

# Get detailed document information
pdf_info = pdf_extractor.get_pdf_info("document.pdf")
word_info = word_extractor.get_docx_info("document.docx")
```

## Package Structure

```
document-image-extractor/
├── __init__.py              # Package initialization and exports
├── __main__.py              # Command-line entry point
├── extractor.py             # Main DocumentExtractor class
├── pdf_extractor.py         # PDF-specific extraction logic
├── word_extractor.py        # Word document extraction logic
├── comparison.py            # Image comparison utilities
├── utils.py                 # Utility functions and helpers
├── requirements.txt         # Package dependencies
└── README.md               # This file
```

## Output Structure

### Extracted Files

When you extract images from a document, the package creates:

```
extracted_[document_type]_images/
├── document_image01.jpg
├── document_image02.png
├── document_image03.jpg
└── ...
```

### ZIP Archive

If ZIP creation is enabled (default), you'll also get:

```
document_extracted_content_YYYYMMDD_HHMMSS.zip
├── original_document/
│   └── document.pdf (or .docx)
├── extracted_images/
│   ├── document_image01.jpg
│   ├── document_image02.png
│   └── ...
└── EXTRACTION_SUMMARY.txt
```

### Extraction Summary

The summary file contains:

```
PDF Image Extraction Summary
============================

Original Document: document.pdf
Document Type: PDF
Extraction Date: 2025-07-16 14:30:22
Total Images Extracted: 5

Extracted Images:
 1. document_image01.jpg (1200x800) [145.2 KB]
 2. document_image02.png (800x600) [89.7 KB]
 3. document_image03.jpg (1024x768) [167.3 KB]
 ...
```

## Features in Detail

### PDF Image Extraction

- Uses PyMuPDF for reliable PDF processing
- Handles different color spaces (RGB, CMYK, Grayscale)
- Automatic conversion to RGB when needed
- Filters out decorative images based on size threshold
- Page-by-page extraction with detailed progress

### Word Document Extraction

- Processes .docx files as ZIP archives
- Extracts from internal `word/media/` folder
- Automatic image format detection using file signatures
- Preserves original image quality and format
- Handles images without file extensions

### Image Format Detection

The package can detect image formats using file signatures (magic numbers):

- **JPEG**: `FF D8 FF E0` or `FF D8 FF E1`
- **PNG**: `89 50 4E 47 0D 0A 1A 0A`
- **GIF**: `GIF87a` or `GIF89a`
- **BMP**: `42 4D`

### Automatic Document Discovery

When no document is specified, the package searches:

1. Current working directory
2. Downloads folder (`/mnt/c/Users/cjdua/Downloads`)
3. Any additional directories you specify

### Comparison Features

```python
from document_image_extractor import ImageComparison

comparison = ImageComparison()

# Compare extraction directories
result = comparison.compare_extraction_directories(
    "extracted_pdf_images/", 
    "extracted_word_images/"
)

# Generate detailed report
comparison.generate_comparison_report(
    "pdf_images/", 
    "word_images/", 
    "comparison_report.txt"
)

# Find similar images
similar = comparison.find_similar_images("dir1/", "dir2/")
```

## Error Handling

The package includes comprehensive error handling:

- **File not found**: Clear error messages with suggestions
- **Unsupported formats**: Lists supported file types
- **Missing dependencies**: Instructions for installation
- **Corrupted files**: Graceful handling with error reporting
- **Permission issues**: Clear error messages

## Configuration Options

### DocumentExtractor Options

```python
extractor = DocumentExtractor(
    min_image_size=10,    # Minimum image size for PDF (pixels)
    create_zip=True       # Create ZIP archives
)
```

### PDF Extractor Options

```python
pdf_extractor = PDFImageExtractor(
    min_image_size=15     # Minimum 15x15 pixels
)
```

## Performance Notes

- **Memory Usage**: Processes images one at a time to minimize memory usage
- **Large PDFs**: Efficiently handles large PDF files with many pages
- **ZIP Compression**: Uses ZIP_DEFLATED for optimal compression
- **Progress Reporting**: Real-time progress updates for long operations

## Troubleshooting

### Common Issues

#### Missing Dependencies

```bash
# Install PyMuPDF
pip install PyMuPDF

# Install Pillow
pip install Pillow
```

#### Permission Errors

Make sure you have read access to source documents and write access to output directories.

#### No Images Found

- **PDF**: Check if the PDF actually contains embedded images
- **Word**: Ensure the document is in .docx format (not .doc)
- **Both**: Verify the document isn't corrupted

#### Import Errors

If you get import errors when running as a module, make sure you're in the parent directory of the package:

```bash
# Correct: Run from the directory containing document-image-extractor/
python -m document_image_extractor

# Not: Don't run from inside the package directory
```

## Contributing

This package consolidates functionality from multiple standalone scripts into a unified, well-structured package. The modular design makes it easy to extend with additional document formats or extraction methods.

### Code Structure

- **Separation of Concerns**: Each module has a specific responsibility
- **Type Hints**: Full type annotation for better code clarity
- **Error Handling**: Comprehensive error handling throughout
- **Documentation**: Detailed docstrings for all public methods
- **Utility Functions**: Reusable utilities in separate module

## License

This project is part of the Leet_Vibe repository. Please refer to the main repository license.

## Version History

- **v1.0.0**: Initial consolidated package release
  - Unified PDF and Word document extraction
  - ZIP archive creation
  - Interactive CLI
  - Image comparison utilities
  - Comprehensive error handling and logging
