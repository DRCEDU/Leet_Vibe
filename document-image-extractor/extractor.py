#!/usr/bin/env python3
"""
Main Document Extractor
Unified interface for extracting images from PDF and Word documents.
"""

import os
import sys
from typing import List, Optional, Tuple, Union, Dict
from .utils import FileUtils, ZipUtils, LoggingUtils, DependencyChecker
from .pdf_extractor import PDFImageExtractor
from .word_extractor import WordImageExtractor


class DocumentExtractor:
    """
    Unified document image extractor for PDF and Word documents.
    
    This class provides a single interface for extracting images from
    both PDF (.pdf) and Word (.docx) documents.
    """
    
    def __init__(self, min_image_size: int = 10, create_zip: bool = True):
        """
        Initialize the document extractor.
        
        Args:
            min_image_size: Minimum image dimension for PDF extraction (filters decorative images)
            create_zip: Whether to create ZIP archives with extracted content
        """
        self.min_image_size = min_image_size
        self.create_zip = create_zip
        self.pdf_extractor = PDFImageExtractor(min_image_size=min_image_size)
        self.word_extractor = WordImageExtractor()
    
    def extract_images(self, document_path: str, output_dir: Optional[str] = None) -> Tuple[List[str], Optional[str]]:
        """
        Extract all images from a document (PDF or Word) and save them as separate files.
        
        Args:
            document_path: Path to the document file
            output_dir: Directory to save extracted images (optional)
        
        Returns:
            Tuple of (list of extracted image filenames, zip file path if created)
        """
        # Validate input
        if not FileUtils.validate_file_exists(document_path):
            raise FileNotFoundError(f"Document not found: {document_path}")
        
        if not FileUtils.is_supported_document(document_path):
            ext = FileUtils.get_file_extension(document_path)
            raise ValueError(f"Unsupported file type: {ext}. Supported types: .pdf, .docx")
        
        # Check dependencies
        file_ext = FileUtils.get_file_extension(document_path)
        if file_ext == '.pdf' and not DependencyChecker.check_dependencies():
            raise ImportError("Missing dependencies for PDF processing")
        
        # Determine document type and set output directory
        if file_ext == '.pdf':
            doc_type = 'PDF'
            if output_dir is None:
                output_dir = os.path.join(os.path.dirname(document_path), "extracted_pdf_images")
            extractor = self.pdf_extractor
        else:  # .docx
            doc_type = 'Word Document'
            if output_dir is None:
                output_dir = os.path.join(os.path.dirname(document_path), "extracted_word_images")
            extractor = self.word_extractor
        
        # Extract images
        extracted_images = extractor.extract_images(document_path, output_dir)
        
        # Create ZIP archive if requested
        zip_path = None
        if self.create_zip and extracted_images:
            zip_path = ZipUtils.create_archive(document_path, extracted_images, doc_type)
        
        return extracted_images, zip_path
    
    def extract_from_multiple_documents(self, document_paths: List[str], 
                                      base_output_dir: Optional[str] = None) -> Dict[str, Tuple[List[str], Optional[str]]]:
        """
        Extract images from multiple documents.
        
        Args:
            document_paths: List of document file paths
            base_output_dir: Base directory for all extractions (optional)
        
        Returns:
            Dictionary mapping document paths to extraction results
        """
        results = {}
        
        for doc_path in document_paths:
            try:
                # Create individual output directory for each document
                if base_output_dir:
                    doc_name = os.path.splitext(os.path.basename(doc_path))[0]
                    file_ext = FileUtils.get_file_extension(doc_path)
                    doc_type = 'pdf' if file_ext == '.pdf' else 'word'
                    output_dir = os.path.join(base_output_dir, f"{doc_name}_{doc_type}_images")
                else:
                    output_dir = None
                
                extracted_images, zip_path = self.extract_images(doc_path, output_dir)
                results[doc_path] = (extracted_images, zip_path)
                
            except Exception as e:
                print(f"Error processing {doc_path}: {str(e)}")
                results[doc_path] = ([], None)
        
        return results
    
    def get_document_info(self, document_path: str) -> dict:
        """
        Get information about a document without extracting images.
        
        Args:
            document_path: Path to the document
            
        Returns:
            Dictionary with document information
        """
        if not FileUtils.validate_file_exists(document_path):
            raise FileNotFoundError(f"Document not found: {document_path}")
        
        file_ext = FileUtils.get_file_extension(document_path)
        
        if file_ext == '.pdf':
            return self.pdf_extractor.get_pdf_info(document_path)
        elif file_ext == '.docx':
            return self.word_extractor.get_docx_info(document_path)
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")
    
    def count_images(self, document_path: str) -> Union[int, Tuple[int, dict]]:
        """
        Count images in a document without extracting them.
        
        Args:
            document_path: Path to the document
            
        Returns:
            For PDF: Tuple of (total_images, page_breakdown)
            For Word: Number of images
        """
        if not FileUtils.validate_file_exists(document_path):
            raise FileNotFoundError(f"Document not found: {document_path}")
        
        file_ext = FileUtils.get_file_extension(document_path)
        
        if file_ext == '.pdf':
            return self.pdf_extractor.count_images_in_pdf(document_path)
        elif file_ext == '.docx':
            return self.word_extractor.count_images_in_docx(document_path)
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")
    
    def find_documents_in_directory(self, directory: str) -> List[str]:
        """
        Find all supported documents in a directory.
        
        Args:
            directory: Directory to search
            
        Returns:
            List of document file paths
        """
        return FileUtils.find_documents_in_directory(directory)
    
    def interactive_document_selection(self, search_directories: Optional[List[str]] = None) -> Optional[str]:
        """
        Interactive document selection from available documents.
        
        Args:
            search_directories: Directories to search (defaults to current dir and Downloads)
            
        Returns:
            Selected document path or None if cancelled
        """
        if search_directories is None:
            search_directories = [
                os.getcwd(),
                "/mnt/c/Users/cjdua/Downloads"
            ]
        
        # Find documents in all search directories
        all_documents = []
        for directory in search_directories:
            if os.path.exists(directory):
                docs = self.find_documents_in_directory(directory)
                all_documents.extend(docs)
        
        if not all_documents:
            print("No supported documents found!")
            print(f"Searched in:")
            for directory in search_directories:
                if os.path.exists(directory):
                    print(f"  - {directory}")
            print("\nSupported formats: .pdf, .docx")
            return None
        
        if len(all_documents) == 1:
            doc_path = all_documents[0]
            file_ext = FileUtils.get_file_extension(doc_path)
            doc_type = 'PDF' if file_ext == '.pdf' else 'Word Document'
            print(f"Found {doc_type}: {os.path.basename(doc_path)}")
            return doc_path
        
        # Multiple documents found - show selection menu
        print("Multiple documents found:")
        for i, doc in enumerate(all_documents, 1):
            file_ext = FileUtils.get_file_extension(doc)
            doc_type = 'PDF' if file_ext == '.pdf' else 'Word Document'
            print(f"  {i}. {os.path.basename(doc)} ({doc_type})")
        
        try:
            choice = input(f"\nSelect document (1-{len(all_documents)}, or 'q' to quit): ")
            if choice.lower() == 'q':
                return None
            return all_documents[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return None
    
    @staticmethod
    def print_usage():
        """Print usage information."""
        print("""
Document Image Extractor
========================

Usage:
    python -m document_image_extractor [document_path]
    
Arguments:
    document_path    Path to PDF or Word document (optional)
                    If not provided, will search current directory and Downloads
    
Supported formats:
    - PDF files (.pdf)
    - Word documents (.docx)
    
Examples:
    python -m document_image_extractor document.pdf
    python -m document_image_extractor report.docx
    python -m document_image_extractor  # Interactive selection
        """)


def main():
    """Command-line interface for the document extractor."""
    # Check if help is requested
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        DocumentExtractor.print_usage()
        return
    
    # Initialize extractor
    extractor = DocumentExtractor()
    
    # Get document path
    if len(sys.argv) > 1:
        document_path = sys.argv[1]
        
        if not FileUtils.validate_file_exists(document_path):
            print(f"Error: Document not found at {document_path}")
            return
    else:
        # Interactive selection
        document_path = extractor.interactive_document_selection()
        if not document_path:
            return
    
    try:
        # Extract images
        print(f"\nStarting extraction from: {os.path.basename(document_path)}")
        extracted_images, zip_path = extractor.extract_images(document_path)
        
        if extracted_images:
            output_dir = os.path.dirname(extracted_images[0])
            print(f"\n✅ SUCCESS!")
            print(f"Images saved to: {output_dir}")
            if zip_path:
                print(f"Zip archive created: {os.path.basename(zip_path)}")
                print(f"Full zip path: {zip_path}")
        else:
            print("\n❌ No images were extracted from the document.")
            
    except Exception as e:
        print(f"\n❌ Error processing document: {str(e)}")


if __name__ == "__main__":
    main()
