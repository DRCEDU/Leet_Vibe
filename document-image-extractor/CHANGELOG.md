# Changelog

All notable changes to the Document Image Extractor package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-16

### Added
- Initial release of consolidated Document Image Extractor package
- **DocumentExtractor**: Unified interface for PDF and Word document processing
- **PDFImageExtractor**: Specialized PDF image extraction using PyMuPDF
- **WordImageExtractor**: Specialized Word document image extraction via ZIP parsing
- **ImageComparison**: Utilities for comparing extracted images from different sources
- **Comprehensive Utilities**: File operations, ZIP archiving, logging, and dependency checking
- **Command-Line Interface**: Interactive and direct document processing
- **Automatic Document Discovery**: Searches common directories for supported documents
- **ZIP Archive Creation**: Packages original document and extracted images with detailed summaries
- **Image Format Detection**: Uses file signatures (magic numbers) for accurate format detection
- **Batch Processing**: Extract images from multiple documents at once
- **Smart Filtering**: Configurable minimum image size filtering for PDFs
- **Error Handling**: Comprehensive error handling and user-friendly messages
- **Type Hints**: Full type annotation throughout the codebase
- **Documentation**: Extensive README with usage examples and API documentation

### Features
- Support for PDF (.pdf) and Word (.docx) documents
- Extracts images while preserving original quality and format
- Creates organized output directories with clear naming conventions
- Generates detailed extraction summaries with image dimensions and file sizes
- Interactive document selection when multiple documents are found
- Cross-platform compatibility (Windows, Linux, macOS)
- Modular design for easy extension and customization

### Technical Improvements
- Consolidated 5 separate scripts into a unified, well-structured package
- Eliminated code duplication through shared utility modules
- Improved error handling and user experience
- Added comprehensive logging and progress reporting
- Implemented proper Python package structure with setup.py
- Added requirements management and dependency checking
- Created comprehensive test suite for package validation

### Migration from Individual Scripts
This package consolidates the following original scripts:
- `extract_word_images_universal.py` → Enhanced and integrated into package
- `extract_document_images.py` → Functionality merged into DocumentExtractor
- `extract_pdf_images.py` → Enhanced and moved to PDFImageExtractor
- `extract_word_images.py` → Enhanced and moved to WordImageExtractor  
- `compare_extractions.py` → Enhanced and moved to ImageComparison

### Breaking Changes
- Removed hardcoded file paths present in original scripts
- Changed from standalone scripts to importable package modules
- Updated command-line interface for better usability
