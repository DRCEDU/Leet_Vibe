#!/usr/bin/env python3
"""
PDF Image Extractor
Extracts all images from PDF files using PyMuPDF (fitz).
"""

import os
from typing import List, Optional, Tuple
from .utils import FileUtils, ImageUtils, LoggingUtils


class PDFImageExtractor:
    """Extracts images from PDF documents."""
    
    def __init__(self, min_image_size: int = 10):
        """
        Initialize PDF image extractor.
        
        Args:
            min_image_size: Minimum image dimension to extract (filters out tiny decorative images)
        """
        self.min_image_size = min_image_size
    
    def extract_images(self, pdf_path: str, output_dir: Optional[str] = None) -> List[str]:
        """
        Extract all images from a PDF file and save them as separate files.
        
        Args:
            pdf_path: Path to the PDF file
            output_dir: Directory to save extracted images (optional)
        
        Returns:
            List of extracted image file paths
        """
        # Validate input
        if not FileUtils.validate_file_exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if FileUtils.get_file_extension(pdf_path) != '.pdf':
            raise ValueError("File must be a PDF document")
        
        # Import PyMuPDF
        try:
            import fitz
        except ImportError:
            raise ImportError("PyMuPDF is required for PDF processing. Install with: pip install PyMuPDF")
        
        # Set output directory
        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(pdf_path), "extracted_pdf_images")
        
        FileUtils.create_output_directory(output_dir)
        
        LoggingUtils.log_extraction_start(pdf_path, "PDF")
        
        # Open the PDF
        pdf_document = fitz.open(pdf_path)
        extracted_images = []
        image_count = 0
        
        print(f"Total pages: {len(pdf_document)}")
        
        try:
            # Iterate through each page
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                
                # Get list of images on this page
                image_list = page.get_images()
                
                print(f"Page {page_num + 1}: Found {len(image_list)} image(s)")
                
                # Extract each image
                for img_index, img in enumerate(image_list):
                    try:
                        extracted_path = self._extract_single_image(
                            pdf_document, img, page_num, img_index, 
                            pdf_path, output_dir, image_count
                        )
                        
                        if extracted_path:
                            extracted_images.append(extracted_path)
                            image_count += 1
                            
                    except Exception as e:
                        print(f"  - Error extracting image {img_index + 1}: {str(e)}")
                        continue
        
        finally:
            # Close the PDF
            pdf_document.close()
        
        LoggingUtils.log_extraction_complete(extracted_images)
        return extracted_images
    
    def _extract_single_image(self, pdf_document, img, page_num: int, img_index: int,
                             pdf_path: str, output_dir: str, image_count: int) -> Optional[str]:
        """Extract a single image from PDF."""
        import fitz
        
        # Get image data
        xref = img[0]  # xref number
        pix = fitz.Pixmap(pdf_document, xref)
        
        try:
            # Skip if image is too small (likely decorative)
            if pix.width < self.min_image_size or pix.height < self.min_image_size:
                print(f"  - Skipping small image ({pix.width}x{pix.height})")
                return None
            
            # Determine file format
            img_format = "png"
            
            # Create filename
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            img_filename = f"{base_name}_page{page_num + 1}_img{img_index + 1}.{img_format}"
            img_path = os.path.join(output_dir, img_filename)
            
            # Save the image based on color space
            if pix.n - pix.alpha == 1:  # Grayscale
                pix.save(img_path)
            elif pix.n - pix.alpha == 3:  # RGB
                pix.save(img_path)
            else:  # CMYK or other
                # Convert to RGB first
                pix_rgb = fitz.Pixmap(fitz.csRGB, pix)
                pix_rgb.save(img_path)
                pix_rgb = None
            
            print(f"  - Extracted: {img_filename} ({pix.width}x{pix.height})")
            return img_path
            
        finally:
            # Clean up
            pix = None
    
    def get_pdf_info(self, pdf_path: str) -> dict:
        """
        Get basic information about a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Dictionary with PDF information
        """
        try:
            import fitz
            
            if not FileUtils.validate_file_exists(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
            pdf_document = fitz.open(pdf_path)
            
            try:
                info = {
                    'filename': os.path.basename(pdf_path),
                    'page_count': len(pdf_document),
                    'file_size_kb': FileUtils.get_file_size_kb(pdf_path),
                    'metadata': pdf_document.metadata
                }
                
                return info
                
            finally:
                pdf_document.close()
                
        except ImportError:
            raise ImportError("PyMuPDF is required for PDF processing. Install with: pip install PyMuPDF")
    
    def count_images_in_pdf(self, pdf_path: str) -> Tuple[int, dict]:
        """
        Count total images in a PDF without extracting them.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Tuple of (total_images, page_breakdown)
        """
        try:
            import fitz
            
            if not FileUtils.validate_file_exists(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
            pdf_document = fitz.open(pdf_path)
            
            try:
                total_images = 0
                page_breakdown = {}
                
                for page_num in range(len(pdf_document)):
                    page = pdf_document[page_num]
                    image_list = page.get_images()
                    
                    # Filter out small images
                    valid_images = 0
                    for img in image_list:
                        xref = img[0]
                        pix = fitz.Pixmap(pdf_document, xref)
                        if pix.width >= self.min_image_size and pix.height >= self.min_image_size:
                            valid_images += 1
                        pix = None
                    
                    page_breakdown[page_num + 1] = valid_images
                    total_images += valid_images
                
                return total_images, page_breakdown
                
            finally:
                pdf_document.close()
                
        except ImportError:
            raise ImportError("PyMuPDF is required for PDF processing. Install with: pip install PyMuPDF")
