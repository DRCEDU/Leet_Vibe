"""
MDConverter MCP Server
Provides tools for converting HTML webpage packages to Markdown via Model Context Protocol.
"""

import asyncio
import os
import sys
import json
import logging
import tempfile
import shutil
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path
import re
from urllib.parse import urlparse

from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
from pydantic import AnyUrl
import mcp.server.stdio

# HTML processing imports
try:
    from bs4 import BeautifulSoup, Tag, NavigableString
    import requests
    from markdownify import markdownify as md
except ImportError as e:
    print(f"Missing required dependency: {e}")
    print("Please install required packages:")
    print("pip install beautifulsoup4 requests markdownify lxml html5lib")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mdconverter-mcp-server")

# Create server instance
server = Server("mdconverter-mcp")


class MDConverterConfig:
    """Configuration for the MD converter."""
    
    def __init__(self, **kwargs):
        self.output_dir = kwargs.get('output_dir', 'output')
        self.images_dir = kwargs.get('images_dir', 'images')
        self.preserve_images = kwargs.get('preserve_images', True)
        self.clean_html = kwargs.get('clean_html', True)
        self.add_metadata = kwargs.get('add_metadata', True)
        self.log_level = kwargs.get('log_level', 'INFO')
        self.max_file_size = kwargs.get('max_file_size', 50 * 1024 * 1024)  # 50MB


class HTMLToMarkdownConverter:
    """Convert HTML webpage packages to markdown format."""
    
    def __init__(self, html_file_path: str, output_file: Optional[str] = None, config: Optional[MDConverterConfig] = None):
        """Initialize the converter."""
        self.config = config or MDConverterConfig()
        self.html_file_path = Path(html_file_path)
        self.base_dir = self.html_file_path.parent
        self.assets_folder = self._find_assets_folder()
        
        # Set output file
        if output_file:
            self.output_file = Path(output_file)
        else:
            # Check if custom output directory is specified
            if hasattr(config, 'output_dir') and config.output_dir != 'output':
                # Custom output directory specified
                output_dir = self._ensure_directory(config.output_dir)
                filename = self._sanitize_filename(f"{self.html_file_path.stem}.md")
                self.output_file = output_dir / filename
            else:
                # Default: place output in same folder as input HTML file
                filename = self._sanitize_filename(f"{self.html_file_path.stem}.md")
                self.output_file = self.base_dir / filename
        
        # Create images directory - place relative to output file location
        self.images_dir = self._ensure_directory(
            self.output_file.parent / self.config.images_dir
        )
        
        # Track processed images
        self.processed_images: Dict[str, str] = {}
        
    def _find_assets_folder(self) -> Optional[Path]:
        """Find the assets folder associated with the HTML file."""
        patterns = [
            f"{self.html_file_path.stem}_files",
            f"{self.html_file_path.stem}_assets",
            f"{self.html_file_path.name}_files",
        ]
        
        for pattern in patterns:
            assets_path = self.base_dir / pattern
            if assets_path.exists() and assets_path.is_dir():
                return assets_path
        
        return None
    
    def _ensure_directory(self, directory: str) -> Path:
        """Ensure directory exists, create if it doesn't."""
        dir_path = Path(directory)
        dir_path.mkdir(parents=True, exist_ok=True)
        return dir_path
    
    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename to be safe for filesystem."""
        sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
        sanitized = re.sub(r'_+', '_', sanitized)
        sanitized = sanitized.strip(' .')
        
        if not sanitized:
            sanitized = "converted_file"
        
        if len(sanitized) > 200:
            name, ext = os.path.splitext(sanitized)
            sanitized = name[:200-len(ext)] + ext
        
        return sanitized
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text content."""
        if not text:
            return ""
        
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&quot;', '"')
        
        return text
    
    def _process_image(self, img_src: str) -> str:
        """Process image and return markdown-compatible path."""
        if not img_src:
            return ""
        
        if img_src.startswith(('http://', 'https://')):
            return img_src
        
        if img_src.startswith('data:'):
            return ""
        
        img_filename = os.path.basename(img_src)
        
        if self.assets_folder:
            potential_paths = [
                self.assets_folder / img_filename,
                self.assets_folder / img_src.lstrip('./'),
                self.base_dir / img_src.lstrip('./'),
            ]
            
            for img_path in potential_paths:
                if img_path.exists():
                    dest_path = self.images_dir / img_filename
                    if not dest_path.exists():
                        shutil.copy2(img_path, dest_path)
                    
                    return f"images/{img_filename}"
        
        return img_src
    
    def _extract_metadata(self, soup: BeautifulSoup) -> Dict[str, str]:
        """Extract metadata from HTML head."""
        metadata = {}
        
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = self._clean_text(title_tag.get_text())
        
        meta_tags = soup.find_all('meta')
        for meta in meta_tags:
            name = meta.get('name') or meta.get('property')
            content = meta.get('content')
            
            if name and content:
                if name in ['description', 'og:description']:
                    metadata['description'] = content
                elif name in ['author', 'og:author']:
                    metadata['author'] = content
                elif name in ['keywords']:
                    metadata['keywords'] = content
                elif name in ['og:title']:
                    metadata['og_title'] = content
                elif name in ['og:url']:
                    metadata['url'] = content
                elif name in ['article:published_time', 'pubdate']:
                    metadata['published'] = content
        
        return metadata
    
    def _extract_main_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Extract main content from the webpage."""
        unwanted_selectors = [
            'script', 'style', 'nav', 'header', 'footer',
            '.advertisement', '.ad', '.popup', '.modal',
            '.cookie-banner', '.newsletter-signup',
            '[class*="ad-"]', '[id*="ad-"]',
            '.social-share', '.comments-section'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()
        
        main_content_selectors = [
            'main', 'article', '[role="main"]',
            '.post-content', '.article-content', '.entry-content',
            '.content', '.main-content'
        ]
        
        for selector in main_content_selectors:
            main_element = soup.select_one(selector)
            if main_element:
                return main_element
        
        body = soup.find('body')
        return body if body else soup
    
    def _process_code_blocks(self, soup: BeautifulSoup) -> None:
        """Process code blocks and preserve syntax highlighting info."""
        for pre in soup.find_all('pre'):
            code = pre.find('code')
            if code:
                classes = code.get('class', [])
                language = ""
                
                for cls in classes:
                    if cls.startswith('language-'):
                        language = cls.replace('language-', '')
                        break
                    elif cls.startswith('lang-'):
                        language = cls.replace('lang-', '')
                        break
                
                code_content = code.get_text()
                if language:
                    pre.string = f"```{language}\n{code_content}\n```"
                else:
                    pre.string = f"```\n{code_content}\n```"
                
                if code.parent == pre:
                    code.unwrap()
    
    def _fix_markdown_formatting(self, markdown_content: str) -> str:
        """Fix and improve markdown formatting."""
        markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
        markdown_content = re.sub(r'\n(#{1,6}\s)', r'\n\n\1', markdown_content)
        markdown_content = re.sub(r'(#{1,6}.*)\n([^\n#])', r'\1\n\n\2', markdown_content)
        markdown_content = re.sub(r'\n(\*|\+|-|\d+\.)\s', r'\n\n\1 ', markdown_content)
        markdown_content = re.sub(r'\n(>)', r'\n\n\1', markdown_content)
        markdown_content = re.sub(r'[ \t]+', ' ', markdown_content)
        markdown_content = markdown_content.strip()
        
        return markdown_content
    
    def convert(self) -> Tuple[str, Dict[str, Any]]:
        """Convert HTML webpage to markdown."""
        logger.info(f"Converting {self.html_file_path} to markdown...")
        
        # Read HTML file
        try:
            with open(self.html_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except UnicodeDecodeError:
            with open(self.html_file_path, 'r', encoding='latin-1') as f:
                html_content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract metadata
        metadata = self._extract_metadata(soup)
        
        # Process images
        if self.config.preserve_images:
            for img in soup.find_all('img'):
                src = img.get('src', '')
                if src:
                    new_src = self._process_image(src)
                    if new_src:
                        img['src'] = new_src
                        
                    if not img.get('alt'):
                        img['alt'] = "Image"
        
        # Process code blocks
        self._process_code_blocks(soup)
        
        # Extract main content
        main_content = self._extract_main_content(soup)
        
        # Convert to markdown
        markdown_content = md(
            str(main_content),
            heading_style="ATX",
            bullets="-",
            strip=['script', 'style', 'nav', 'header', 'footer']
        )
        
        # Fix markdown formatting
        markdown_content = self._fix_markdown_formatting(markdown_content)
        
        # Create final markdown with metadata
        final_markdown = self._create_final_markdown(metadata, markdown_content)
        
        # Write to file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(final_markdown)
        
        # Return results
        result_info = {
            "input_file": str(self.html_file_path),
            "output_file": str(self.output_file),
            "assets_folder": str(self.assets_folder) if self.assets_folder else None,
            "images_processed": len(self.processed_images),
            "images_directory": str(self.images_dir),
            "metadata": metadata,
            "content_length": len(final_markdown),
            "status": "success"
        }
        
        logger.info(f"Conversion complete! Output saved to: {self.output_file}")
        return final_markdown, result_info
    
    def _create_final_markdown(self, metadata: Dict[str, str], content: str) -> str:
        """Create the final markdown document with metadata header."""
        lines = []
        
        if self.config.add_metadata and metadata:
            lines.append("---")
            for key, value in metadata.items():
                safe_value = value.replace('"', '\\"')
                lines.append(f'{key}: "{safe_value}"')
            lines.append("---")
            lines.append("")
        
        if 'title' in metadata:
            lines.append(f"# {metadata['title']}")
            lines.append("")
        
        if any(key in metadata for key in ['author', 'published', 'url']):
            lines.append("## Article Information")
            lines.append("")
            
            if 'author' in metadata:
                lines.append(f"**Author:** {metadata['author']}")
            if 'published' in metadata:
                lines.append(f"**Published:** {metadata['published']}")
            if 'url' in metadata:
                lines.append(f"**Original URL:** {metadata['url']}")
            
            lines.append("")
            if 'description' in metadata:
                lines.append(f"**Description:** {metadata['description']}")
                lines.append("")
        
        lines.append("---")
        lines.append("")
        lines.append(content)
        
        return "\n".join(lines)


def validate_html_file(file_path: str) -> Tuple[bool, str]:
    """Validate if the provided file is a valid HTML file."""
    try:
        file_path = Path(file_path)
        
        if not file_path.exists():
            return False, f"File does not exist: {file_path}"
        
        if not file_path.is_file():
            return False, f"Path is not a file: {file_path}"
        
        if file_path.suffix.lower() not in ['.html', '.htm']:
            return False, f"File is not an HTML file: {file_path.suffix}"
        
        file_size = file_path.stat().st_size
        if file_size == 0:
            return False, "File is empty"
        
        # Check if file is readable
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(100)
                if not content.strip():
                    return False, "File appears to be empty or unreadable"
        except UnicodeDecodeError:
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


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available HTML to Markdown conversion tools."""
    return [
        types.Tool(
            name="convert_html_to_markdown",
            description="Convert an HTML webpage package to clean, well-formatted Markdown with metadata, image processing, and content optimization",
            inputSchema={
                "type": "object",
                "properties": {
                    "html_file_path": {
                        "type": "string",
                        "description": "Path to the HTML file to convert"
                    },
                    "output_file": {
                        "type": "string",
                        "description": "Optional output markdown file path (defaults to same folder as input HTML file)"
                    },
                    "output_dir": {
                        "type": "string",
                        "description": "Output directory for converted files (default: same folder as input HTML file)"
                    },
                    "images_dir": {
                        "type": "string",
                        "description": "Directory name for processed images (default: 'images' in same folder as input HTML file)"
                    },
                    "preserve_images": {
                        "type": "boolean",
                        "description": "Whether to process and preserve images (default: true)"
                    },
                    "clean_html": {
                        "type": "boolean",
                        "description": "Whether to clean HTML content (remove ads, scripts, etc.) (default: true)"
                    },
                    "add_metadata": {
                        "type": "boolean",
                        "description": "Whether to add YAML frontmatter metadata (default: true)"
                    }
                },
                "required": ["html_file_path"]
            }
        ),
        types.Tool(
            name="validate_html_file",
            description="Validate if an HTML file is suitable for conversion to Markdown",
            inputSchema={
                "type": "object",
                "properties": {
                    "html_file_path": {
                        "type": "string",
                        "description": "Path to the HTML file to validate"
                    }
                },
                "required": ["html_file_path"]
            }
        ),
        types.Tool(
            name="get_html_metadata",
            description="Extract metadata from an HTML file without performing full conversion",
            inputSchema={
                "type": "object",
                "properties": {
                    "html_file_path": {
                        "type": "string",
                        "description": "Path to the HTML file to analyze"
                    }
                },
                "required": ["html_file_path"]
            }
        ),
        types.Tool(
            name="list_supported_formats",
            description="List supported input and output formats for HTML to Markdown conversion",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="convert_html_content",
            description="Convert HTML content string directly to Markdown without file I/O",
            inputSchema={
                "type": "object",
                "properties": {
                    "html_content": {
                        "type": "string",
                        "description": "HTML content string to convert"
                    },
                    "add_metadata": {
                        "type": "boolean",
                        "description": "Whether to add metadata header (default: false for content conversion)"
                    },
                    "clean_html": {
                        "type": "boolean",
                        "description": "Whether to clean HTML content (default: true)"
                    }
                },
                "required": ["html_content"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle HTML to Markdown conversion tool calls."""
    
    if not arguments:
        arguments = {}
    
    if name == "convert_html_to_markdown":
        html_file_path = arguments.get("html_file_path")
        output_file = arguments.get("output_file")
        
        if not html_file_path:
            raise ValueError("html_file_path is required")
        
        try:
            # Validate input file
            is_valid, error_msg = validate_html_file(html_file_path)
            if not is_valid:
                return [types.TextContent(type="text", text=f"Invalid HTML file: {error_msg}")]
            
            # Create configuration
            config = MDConverterConfig(
                output_dir=arguments.get("output_dir", "output"),
                images_dir=arguments.get("images_dir", "images"),
                preserve_images=arguments.get("preserve_images", True),
                clean_html=arguments.get("clean_html", True),
                add_metadata=arguments.get("add_metadata", True)
            )
            
            # Create converter and convert
            converter = HTMLToMarkdownConverter(html_file_path, output_file, config)
            markdown_content, result_info = converter.convert()
            
            # Format response
            response_text = f"✅ Successfully converted HTML to Markdown!\n\n"
            response_text += f"**Input:** {result_info['input_file']}\n"
            response_text += f"**Output:** {result_info['output_file']}\n"
            response_text += f"**Content Length:** {result_info['content_length']:,} characters\n"
            response_text += f"**Images Processed:** {result_info['images_processed']}\n"
            
            if result_info['metadata']:
                response_text += f"\n**Extracted Metadata:**\n"
                for key, value in result_info['metadata'].items():
                    response_text += f"- {key}: {value}\n"
            
            response_text += f"\n**Full Result Details:**\n```json\n{json.dumps(result_info, indent=2)}\n```"
            
            return [types.TextContent(type="text", text=response_text)]
            
        except Exception as e:
            logger.error(f"Error converting HTML to Markdown: {str(e)}")
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]
    
    elif name == "validate_html_file":
        html_file_path = arguments.get("html_file_path")
        
        if not html_file_path:
            raise ValueError("html_file_path is required")
        
        try:
            is_valid, message = validate_html_file(html_file_path)
            
            validation_result = {
                "file_path": html_file_path,
                "is_valid": is_valid,
                "message": message,
                "file_exists": os.path.exists(html_file_path),
                "file_size": os.path.getsize(html_file_path) if os.path.exists(html_file_path) else 0
            }
            
            status_emoji = "✅" if is_valid else "❌"
            response_text = f"{status_emoji} HTML File Validation Result\n\n"
            response_text += f"**File:** {html_file_path}\n"
            response_text += f"**Status:** {'Valid' if is_valid else 'Invalid'}\n"
            response_text += f"**Message:** {message}\n"
            response_text += f"\n**Details:**\n```json\n{json.dumps(validation_result, indent=2)}\n```"
            
            return [types.TextContent(type="text", text=response_text)]
            
        except Exception as e:
            logger.error(f"Error validating HTML file: {str(e)}")
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]
    
    elif name == "get_html_metadata":
        html_file_path = arguments.get("html_file_path")
        
        if not html_file_path:
            raise ValueError("html_file_path is required")
        
        try:
            # Validate file first
            is_valid, error_msg = validate_html_file(html_file_path)
            if not is_valid:
                return [types.TextContent(type="text", text=f"Invalid HTML file: {error_msg}")]
            
            # Create minimal converter just for metadata extraction
            converter = HTMLToMarkdownConverter(html_file_path)
            
            # Read and parse HTML
            with open(html_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            metadata = converter._extract_metadata(soup)
            
            response_text = f"📄 HTML Metadata Extraction\n\n"
            response_text += f"**File:** {html_file_path}\n"
            response_text += f"**Metadata Found:** {len(metadata)} items\n\n"
            
            if metadata:
                response_text += "**Extracted Metadata:**\n"
                for key, value in metadata.items():
                    response_text += f"- **{key}:** {value}\n"
            else:
                response_text += "No metadata found in HTML file.\n"
            
            response_text += f"\n**Raw Metadata:**\n```json\n{json.dumps(metadata, indent=2)}\n```"
            
            return [types.TextContent(type="text", text=response_text)]
            
        except Exception as e:
            logger.error(f"Error extracting HTML metadata: {str(e)}")
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]
    
    elif name == "list_supported_formats":
        formats_info = {
            "input_formats": {
                "supported_extensions": [".html", ".htm"],
                "description": "HTML files and webpage packages",
                "notes": [
                    "Supports both individual HTML files and webpage packages with assets",
                    "Automatically detects and processes associated asset folders (_files, _assets)",
                    "Handles multiple text encodings (UTF-8, Latin-1)"
                ]
            },
            "output_formats": {
                "supported_extensions": [".md", ".markdown"],
                "description": "Markdown files with optional YAML frontmatter",
                "features": [
                    "Clean, well-formatted Markdown output",
                    "YAML frontmatter with extracted metadata",
                    "Preserved code blocks with syntax highlighting",
                    "Organized image processing and referencing",
                    "Cleaned content (removes ads, scripts, navigation)"
                ]
            },
            "processing_features": [
                "Metadata extraction (title, author, description, etc.)",
                "Image processing and organization",
                "Content cleaning and optimization",
                "Code block preservation",
                "Configurable output formatting"
            ]
        }
        
        response_text = "📋 Supported Formats for HTML to Markdown Conversion\n\n"
        response_text += f"```json\n{json.dumps(formats_info, indent=2)}\n```"
        
        return [types.TextContent(type="text", text=response_text)]
    
    elif name == "convert_html_content":
        html_content = arguments.get("html_content")
        
        if not html_content:
            raise ValueError("html_content is required")
        
        try:
            # Create temporary file for processing
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp_file:
                tmp_file.write(html_content)
                tmp_file_path = tmp_file.name
            
            try:
                # Create configuration
                config = MDConverterConfig(
                    add_metadata=arguments.get("add_metadata", False),
                    clean_html=arguments.get("clean_html", True),
                    preserve_images=False  # No image processing for content conversion
                )
                
                # Create converter and convert
                converter = HTMLToMarkdownConverter(tmp_file_path, config=config)
                markdown_content, result_info = converter.convert()
                
                # Read the generated markdown
                with open(result_info['output_file'], 'r', encoding='utf-8') as f:
                    final_markdown = f.read()
                
                response_text = f"✅ Successfully converted HTML content to Markdown!\n\n"
                response_text += f"**Content Length:** {len(final_markdown):,} characters\n"
                response_text += f"**Processing:** Content cleaned and optimized\n\n"
                response_text += f"**Converted Markdown:**\n```markdown\n{final_markdown}\n```"
                
                return [types.TextContent(type="text", text=response_text)]
                
            finally:
                # Clean up temporary files
                os.unlink(tmp_file_path)
                if os.path.exists(result_info['output_file']):
                    os.unlink(result_info['output_file'])
            
        except Exception as e:
            logger.error(f"Error converting HTML content: {str(e)}")
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]
    
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Main entry point for the server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mdconverter-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
