"""
MDConverter - HTML to Markdown Converter Package

A comprehensive Python toolkit for converting HTML webpage packages 
into clean, well-formatted Markdown files.
"""

__version__ = "1.0.0"
__author__ = "DRCEDU"

from .converter import HTMLToMarkdownConverter
from .utils import setup_logging, validate_html_file
from .config import Config

__all__ = [
    "HTMLToMarkdownConverter",
    "setup_logging", 
    "validate_html_file",
    "Config"
]
