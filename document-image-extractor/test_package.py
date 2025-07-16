#!/usr/bin/env python3
"""
Test script for Document Image Extractor package.
Run this to verify the package is working correctly.
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the package to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from document_image_extractor import DocumentExtractor
        print("✓ DocumentExtractor imported successfully")
        
        from document_image_extractor import PDFImageExtractor
        print("✓ PDFImageExtractor imported successfully")
        
        from document_image_extractor import WordImageExtractor
        print("✓ WordImageExtractor imported successfully")
        
        from document_image_extractor import ImageComparison
        print("✓ ImageComparison imported successfully")
        
        from document_image_extractor import FileUtils, ZipUtils
        print("✓ Utility classes imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_dependency_check():
    """Test dependency checking."""
    print("\nTesting dependency checking...")
    
    try:
        from document_image_extractor.utils import DependencyChecker
        
        # Check dependencies
        has_deps = DependencyChecker.check_dependencies()
        if has_deps:
            print("✓ All dependencies are available")
        else:
            print("⚠ Some dependencies are missing (see above)")
        
        return True
    except Exception as e:
        print(f"✗ Dependency check failed: {e}")
        return False

def test_file_utils():
    """Test file utility functions."""
    print("\nTesting file utilities...")
    
    try:
        from document_image_extractor.utils import FileUtils
        
        # Test file existence check
        test_result = FileUtils.validate_file_exists(__file__)
        if test_result:
            print("✓ File existence check works")
        else:
            print("✗ File existence check failed")
            return False
        
        # Test extension detection
        ext = FileUtils.get_file_extension("test.pdf")
        if ext == ".pdf":
            print("✓ File extension detection works")
        else:
            print("✗ File extension detection failed")
            return False
        
        # Test supported document check
        is_supported = FileUtils.is_supported_document("test.pdf")
        if is_supported:
            print("✓ Supported document detection works")
        else:
            print("✗ Supported document detection failed")
            return False
        
        return True
    except Exception as e:
        print(f"✗ File utilities test failed: {e}")
        return False

def test_extractor_initialization():
    """Test that extractors can be initialized."""
    print("\nTesting extractor initialization...")
    
    try:
        from document_image_extractor import DocumentExtractor, PDFImageExtractor, WordImageExtractor
        
        # Test main extractor
        extractor = DocumentExtractor()
        print("✓ DocumentExtractor initialized successfully")
        
        # Test PDF extractor
        pdf_extractor = PDFImageExtractor()
        print("✓ PDFImageExtractor initialized successfully")
        
        # Test Word extractor
        word_extractor = WordImageExtractor()
        print("✓ WordImageExtractor initialized successfully")
        
        return True
    except Exception as e:
        print(f"✗ Extractor initialization failed: {e}")
        return False

def test_image_comparison():
    """Test image comparison utilities."""
    print("\nTesting image comparison...")
    
    try:
        from document_image_extractor import ImageComparison
        
        comparison = ImageComparison()
        print("✓ ImageComparison initialized successfully")
        
        return True
    except Exception as e:
        print(f"✗ Image comparison test failed: {e}")
        return False

def test_document_finder():
    """Test document finding functionality."""
    print("\nTesting document finder...")
    
    try:
        from document_image_extractor import DocumentExtractor
        
        extractor = DocumentExtractor()
        
        # Test finding documents in current directory
        current_docs = extractor.find_documents_in_directory(".")
        print(f"✓ Found {len(current_docs)} documents in current directory")
        
        # Test finding documents in Downloads (if it exists)
        downloads_dir = "/mnt/c/Users/cjdua/Downloads"
        if os.path.exists(downloads_dir):
            downloads_docs = extractor.find_documents_in_directory(downloads_dir)
            print(f"✓ Found {len(downloads_docs)} documents in Downloads")
        else:
            print("⚠ Downloads directory not found (this is okay)")
        
        return True
    except Exception as e:
        print(f"✗ Document finder test failed: {e}")
        return False

def run_all_tests():
    """Run all tests."""
    print("Document Image Extractor - Package Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_dependency_check,
        test_file_utils,
        test_extractor_initialization,
        test_image_comparison,
        test_document_finder,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The package is ready to use.")
        return True
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return False

def show_usage_examples():
    """Show usage examples."""
    print("\n" + "=" * 50)
    print("USAGE EXAMPLES")
    print("=" * 50)
    print("""
To use the package:

1. Command Line Interface:
   python -m document_image_extractor                    # Interactive mode
   python -m document_image_extractor document.pdf      # Extract from PDF
   python -m document_image_extractor document.docx     # Extract from Word

2. Python API:
   from document_image_extractor import DocumentExtractor
   
   extractor = DocumentExtractor()
   images, zip_path = extractor.extract_images("document.pdf")
   print(f"Extracted {len(images)} images")

3. Individual Extractors:
   from document_image_extractor import PDFImageExtractor, WordImageExtractor
   
   pdf_extractor = PDFImageExtractor()
   word_extractor = WordImageExtractor()
   
   pdf_images = pdf_extractor.extract_images("document.pdf")
   word_images = word_extractor.extract_images("document.docx")

4. Image Comparison:
   from document_image_extractor import ImageComparison
   
   comparison = ImageComparison()
   comparison.compare_extraction_directories("pdf_images/", "word_images/")
    """)

if __name__ == "__main__":
    success = run_all_tests()
    show_usage_examples()
    
    if success:
        print("\n✅ Package is ready to use!")
        sys.exit(0)
    else:
        print("\n❌ Package has issues that need to be resolved.")
        sys.exit(1)
