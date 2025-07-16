#!/usr/bin/env python3
"""
Utility functions for document image extraction.
"""

import os
import zipfile
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple


class FileUtils:
    """Utility functions for file operations."""
    
    @staticmethod
    def validate_file_exists(file_path: str) -> bool:
        """Check if a file exists."""
        return os.path.exists(file_path)
    
    @staticmethod
    def get_file_extension(file_path: str) -> str:
        """Get file extension in lowercase."""
        return os.path.splitext(file_path)[1].lower()
    
    @staticmethod
    def is_supported_document(file_path: str) -> bool:
        """Check if file is a supported document type."""
        ext = FileUtils.get_file_extension(file_path)
        return ext in ['.pdf', '.docx']
    
    @staticmethod
    def find_documents_in_directory(directory: str) -> List[str]:
        """Find all supported document files in a directory."""
        if not os.path.exists(directory):
            return []
        
        documents = []
        for file in os.listdir(directory):
            if (file.lower().endswith(('.pdf', '.docx')) and 
                not file.startswith('~')):  # Exclude temp files
                documents.append(os.path.join(directory, file))
        return documents
    
    @staticmethod
    def create_output_directory(output_dir: str) -> None:
        """Create output directory if it doesn't exist."""
        os.makedirs(output_dir, exist_ok=True)
    
    @staticmethod
    def get_file_size_kb(file_path: str) -> float:
        """Get file size in KB."""
        return os.path.getsize(file_path) / 1024
    
    @staticmethod
    def get_current_timestamp() -> str:
        """Get current timestamp as formatted string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class ImageUtils:
    """Utility functions for image operations."""
    
    @staticmethod
    def detect_image_format_from_signature(file_data: bytes) -> str:
        """Detect image format from file signature (magic numbers)."""
        if file_data[:4] == b'\xff\xd8\xff\xe0' or file_data[:4] == b'\xff\xd8\xff\xe1':
            return '.jpg'
        elif file_data[:8] == b'\x89PNG\r\n\x1a\n':
            return '.png'
        elif file_data[:6] == b'GIF87a' or file_data[:6] == b'GIF89a':
            return '.gif'
        elif file_data[:2] == b'BM':
            return '.bmp'
        else:
            return '.img'  # Unknown format
    
    @staticmethod
    def get_image_dimensions(image_path: str) -> Optional[Tuple[int, int]]:
        """Get image dimensions using PIL."""
        try:
            from PIL import Image
            with Image.open(image_path) as img:
                return img.size
        except Exception:
            return None
    
    @staticmethod
    def format_size_info(dimensions: Optional[Tuple[int, int]]) -> str:
        """Format image size information for display."""
        if dimensions:
            return f" ({dimensions[0]}x{dimensions[1]})"
        return ""


class ZipUtils:
    """Utility functions for ZIP archive operations."""
    
    @staticmethod
    def create_archive(original_doc_path: str, extracted_images: List[str], 
                      doc_type: str) -> Optional[str]:
        """
        Create a zip file containing the original document and all extracted images.
        
        Args:
            original_doc_path: Path to the original document
            extracted_images: List of paths to extracted image files
            doc_type: Type of document (PDF or Word Document)
        
        Returns:
            Path to the created zip file or None if failed
        """
        if not extracted_images:
            return None
        
        # Create zip filename based on document name and timestamp
        doc_basename = os.path.splitext(os.path.basename(original_doc_path))[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"{doc_basename}_extracted_content_{timestamp}.zip"
        zip_path = os.path.join(os.path.dirname(original_doc_path), zip_filename)
        
        print(f"\nCreating zip archive: {zip_filename}")
        print("-" * 50)
        
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Add the original document
                doc_basename_in_zip = os.path.basename(original_doc_path)
                zipf.write(original_doc_path, f"original_document/{doc_basename_in_zip}")
                print(f"Added to zip: original_document/{doc_basename_in_zip}")
                
                # Add all extracted images
                for img_path in extracted_images:
                    img_basename = os.path.basename(img_path)
                    zipf.write(img_path, f"extracted_images/{img_basename}")
                    print(f"Added to zip: extracted_images/{img_basename}")
                
                # Create and add summary file
                summary_content = ZipUtils._create_summary_content(
                    original_doc_path, extracted_images, doc_type)
                zipf.writestr("EXTRACTION_SUMMARY.txt", summary_content)
                print("Added to zip: EXTRACTION_SUMMARY.txt")
            
            print("-" * 50)
            print(f"Zip archive created successfully: {zip_filename}")
            print(f"Archive size: {FileUtils.get_file_size_kb(zip_path) / 1024:.2f} MB")
            
            return zip_path
            
        except Exception as e:
            print(f"Error creating zip archive: {str(e)}")
            return None
    
    @staticmethod
    def _create_summary_content(doc_path: str, extracted_images: List[str], 
                               doc_type: str) -> str:
        """Create summary content for the zip archive."""
        summary_content = f"""{doc_type} Image Extraction Summary
==========================================

Original Document: {os.path.basename(doc_path)}
Document Type: {doc_type}
Document Path: {doc_path}
Extraction Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Total Images Extracted: {len(extracted_images)}

Extracted Images:
"""
        
        for i, img_path in enumerate(extracted_images, 1):
            img_basename = os.path.basename(img_path)
            file_size = FileUtils.get_file_size_kb(img_path)
            dimensions = ImageUtils.get_image_dimensions(img_path)
            size_info = ImageUtils.format_size_info(dimensions)
            
            summary_content += f"{i:2d}. {img_basename}{size_info} [{file_size:.1f} KB]\n"
        
        return summary_content


class LoggingUtils:
    """Utility functions for logging setup."""
    
    @staticmethod
    def setup_logging(verbose: bool = False) -> None:
        """Setup logging configuration."""
        level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    @staticmethod
    def log_extraction_start(doc_path: str, doc_type: str) -> None:
        """Log the start of extraction process."""
        print(f"Processing {doc_type}: {os.path.basename(doc_path)}")
        print("-" * 50)
    
    @staticmethod
    def log_extraction_complete(extracted_images: List[str]) -> None:
        """Log the completion of extraction process."""
        print("-" * 50)
        print(f"Extraction complete!")
        print(f"Total images extracted: {len(extracted_images)}")
        
        if extracted_images:
            print("\nExtracted images:")
            for img_path in extracted_images:
                print(f"  - {os.path.basename(img_path)}")


class DependencyChecker:
    """Check for required dependencies."""
    
    @staticmethod
    def check_dependencies() -> bool:
        """Check if all required libraries are installed."""
        missing_deps = []
        
        try:
            import fitz
        except ImportError:
            missing_deps.append("PyMuPDF")
        
        try:
            import PIL
        except ImportError:
            missing_deps.append("Pillow")
        
        if missing_deps:
            print("Missing dependencies:")
            for dep in missing_deps:
                print(f"  - {dep}")
            print("\nInstall with: pip install " + " ".join(missing_deps))
            return False
        
        return True
