#!/usr/bin/env python3
"""
Word Document Image Extractor
Extracts all images from Word documents (.docx) by parsing the internal ZIP structure.
"""

import os
import zipfile
from typing import List, Optional
from .utils import FileUtils, ImageUtils, LoggingUtils


class WordImageExtractor:
    """Extracts images from Word documents (.docx)."""
    
    def __init__(self):
        """Initialize Word image extractor."""
        pass
    
    def extract_images(self, docx_path: str, output_dir: Optional[str] = None) -> List[str]:
        """
        Extract all images from a Word document (.docx) and save them as separate files.
        
        Args:
            docx_path: Path to the Word document (.docx file)
            output_dir: Directory to save extracted images (optional)
        
        Returns:
            List of extracted image file paths
        """
        # Validate input
        if not FileUtils.validate_file_exists(docx_path):
            raise FileNotFoundError(f"Word document not found: {docx_path}")
        
        if FileUtils.get_file_extension(docx_path) != '.docx':
            raise ValueError("File must be a .docx Word document")
        
        # Set output directory
        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(docx_path), "extracted_word_images")
        
        FileUtils.create_output_directory(output_dir)
        
        LoggingUtils.log_extraction_start(docx_path, "Word Document")
        
        extracted_images = []
        
        try:
            # Open the .docx file as a zip archive
            with zipfile.ZipFile(docx_path, 'r') as docx_zip:
                # List all files in the document
                file_list = docx_zip.namelist()
                
                # Find media files (images are typically in word/media/ folder)
                media_files = [f for f in file_list if f.startswith('word/media/')]
                
                print(f"Found {len(media_files)} media file(s) in document")
                
                if not media_files:
                    print("No images found in the document.")
                    return []
                
                # Extract each media file
                for media_file in media_files:
                    try:
                        extracted_path = self._extract_single_image(
                            docx_zip, media_file, docx_path, output_dir, len(extracted_images)
                        )
                        
                        if extracted_path:
                            extracted_images.append(extracted_path)
                            
                    except Exception as e:
                        print(f"  - Error extracting {media_file}: {str(e)}")
                        continue
        
        except Exception as e:
            raise Exception(f"Error reading Word document: {str(e)}")
        
        LoggingUtils.log_extraction_complete(extracted_images)
        return extracted_images
    
    def _extract_single_image(self, docx_zip: zipfile.ZipFile, media_file: str,
                             docx_path: str, output_dir: str, image_index: int) -> Optional[str]:
        """Extract a single image from Word document."""
        # Get the file data
        file_data = docx_zip.read(media_file)
        
        # Determine file extension
        original_filename = os.path.basename(media_file)
        file_ext = os.path.splitext(original_filename)[1].lower()
        
        # If no extension, try to determine from content using magic numbers
        if not file_ext:
            file_ext = ImageUtils.detect_image_format_from_signature(file_data)
        
        # Create output filename
        base_name = os.path.splitext(os.path.basename(docx_path))[0]
        img_filename = f"{base_name}_image{image_index + 1:02d}{file_ext}"
        img_path = os.path.join(output_dir, img_filename)
        
        # Save the image
        with open(img_path, 'wb') as img_file:
            img_file.write(file_data)
        
        # Get image dimensions and file size for display
        dimensions = ImageUtils.get_image_dimensions(img_path)
        size_info = ImageUtils.format_size_info(dimensions)
        file_size = len(file_data) / 1024  # Size in KB
        
        print(f"  - Extracted: {img_filename}{size_info} [{file_size:.1f} KB]")
        return img_path
    
    def get_docx_info(self, docx_path: str) -> dict:
        """
        Get basic information about a Word document.
        
        Args:
            docx_path: Path to the Word document
            
        Returns:
            Dictionary with document information
        """
        if not FileUtils.validate_file_exists(docx_path):
            raise FileNotFoundError(f"Word document not found: {docx_path}")
        
        try:
            with zipfile.ZipFile(docx_path, 'r') as docx_zip:
                file_list = docx_zip.namelist()
                media_files = [f for f in file_list if f.startswith('word/media/')]
                
                # Try to get document properties
                properties = {}
                try:
                    # Check for core properties
                    if 'docProps/core.xml' in file_list:
                        core_xml = docx_zip.read('docProps/core.xml').decode('utf-8')
                        properties['has_core_properties'] = True
                    else:
                        properties['has_core_properties'] = False
                except:
                    properties['has_core_properties'] = False
                
                info = {
                    'filename': os.path.basename(docx_path),
                    'file_size_kb': FileUtils.get_file_size_kb(docx_path),
                    'total_files_in_archive': len(file_list),
                    'media_files_count': len(media_files),
                    'media_files': [os.path.basename(f) for f in media_files],
                    'properties': properties
                }
                
                return info
                
        except Exception as e:
            raise Exception(f"Error reading Word document: {str(e)}")
    
    def count_images_in_docx(self, docx_path: str) -> int:
        """
        Count total images in a Word document without extracting them.
        
        Args:
            docx_path: Path to the Word document
            
        Returns:
            Number of images found
        """
        if not FileUtils.validate_file_exists(docx_path):
            raise FileNotFoundError(f"Word document not found: {docx_path}")
        
        try:
            with zipfile.ZipFile(docx_path, 'r') as docx_zip:
                file_list = docx_zip.namelist()
                media_files = [f for f in file_list if f.startswith('word/media/')]
                return len(media_files)
                
        except Exception as e:
            raise Exception(f"Error reading Word document: {str(e)}")
    
    def list_media_files(self, docx_path: str) -> List[dict]:
        """
        List all media files in a Word document with their details.
        
        Args:
            docx_path: Path to the Word document
            
        Returns:
            List of dictionaries with media file information
        """
        if not FileUtils.validate_file_exists(docx_path):
            raise FileNotFoundError(f"Word document not found: {docx_path}")
        
        try:
            with zipfile.ZipFile(docx_path, 'r') as docx_zip:
                file_list = docx_zip.namelist()
                media_files = [f for f in file_list if f.startswith('word/media/')]
                
                media_info = []
                for media_file in media_files:
                    file_data = docx_zip.read(media_file)
                    original_filename = os.path.basename(media_file)
                    file_ext = os.path.splitext(original_filename)[1].lower()
                    
                    if not file_ext:
                        file_ext = ImageUtils.detect_image_format_from_signature(file_data)
                    
                    media_info.append({
                        'internal_path': media_file,
                        'filename': original_filename,
                        'extension': file_ext,
                        'size_bytes': len(file_data),
                        'size_kb': len(file_data) / 1024
                    })
                
                return media_info
                
        except Exception as e:
            raise Exception(f"Error reading Word document: {str(e)}")
