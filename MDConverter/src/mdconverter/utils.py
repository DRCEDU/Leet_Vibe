"""
Utility functions for MDConverter
"""

import os
import sys
import logging
from pathlib import Path
from typing import Optional, List, Tuple
import re
from urllib.parse import urlparse


def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """
    Setup logging configuration for MDConverter
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger('mdconverter')
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def validate_html_file(file_path: str) -> Tuple[bool, str]:
    """
    Validate if the provided file is a valid HTML file
    
    Args:
        file_path: Path to the HTML file
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        file_path = Path(file_path)
        
        # Check if file exists
        if not file_path.exists():
            return False, f"File does not exist: {file_path}"
        
        # Check if it's a file (not directory)
        if not file_path.is_file():
            return False, f"Path is not a file: {file_path}"
        
        # Check file extension
        if file_path.suffix.lower() not in ['.html', '.htm']:
            return False, f"File is not an HTML file: {file_path.suffix}"
        
        # Check file size (basic validation)
        file_size = file_path.stat().st_size
        if file_size == 0:
            return False, "File is empty"
        
        # Check if file is readable
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(100)  # Read first 100 chars
                if not content.strip():
                    return False, "File appears to be empty or unreadable"
        except UnicodeDecodeError:
            # Try with different encoding
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read(100)
            except Exception as e:
                return False, f"Cannot read file: {e}"
        except Exception as e:
            return False, f"Cannot read file: {e}"
        
        return True, "Valid HTML file"
        
    except Exception as e:
        return False, f"Validation error: {e}"


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to be safe for filesystem
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Remove multiple underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    
    # Remove leading/trailing spaces and dots
    sanitized = sanitized.strip(' .')
    
    # Ensure it's not empty
    if not sanitized:
        sanitized = "converted_file"
    
    # Ensure it's not too long (255 is typical filesystem limit)
    if len(sanitized) > 200:
        name, ext = os.path.splitext(sanitized)
        sanitized = name[:200-len(ext)] + ext
    
    return sanitized


def ensure_directory(directory: str) -> Path:
    """
    Ensure directory exists, create if it doesn't
    
    Args:
        directory: Directory path
        
    Returns:
        Path object for the directory
    """
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def get_file_size_mb(file_path: str) -> float:
    """
    Get file size in megabytes
    
    Args:
        file_path: Path to the file
        
    Returns:
        File size in MB
    """
    try:
        size_bytes = Path(file_path).stat().st_size
        return size_bytes / (1024 * 1024)
    except Exception:
        return 0.0


def extract_domain_from_url(url: str) -> str:
    """
    Extract domain from URL
    
    Args:
        url: URL string
        
    Returns:
        Domain name
    """
    try:
        parsed = urlparse(url)
        return parsed.netloc or "unknown"
    except Exception:
        return "unknown"


def clean_text(text: str) -> str:
    """
    Clean and normalize text content
    
    Args:
        text: Raw text content
        
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Remove control characters
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    
    return text


def get_supported_formats() -> List[str]:
    """
    Get list of supported input formats
    
    Returns:
        List of supported file extensions
    """
    return ['.html', '.htm']


def get_output_formats() -> List[str]:
    """
    Get list of supported output formats
    
    Returns:
        List of supported output file extensions
    """
    return ['.md', '.markdown']


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def is_valid_url(url: str) -> bool:
    """
    Check if string is a valid URL
    
    Args:
        url: URL string to validate
        
    Returns:
        True if valid URL, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False
