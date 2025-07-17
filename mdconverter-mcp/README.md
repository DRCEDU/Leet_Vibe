# MDConverter MCP Server

An MCP (Model Context Protocol) server that provides tools for converting HTML webpage packages to clean, well-formatted Markdown files.

## Features

- **HTML to Markdown Conversion**: Convert complete webpage packages to clean Markdown
- **Metadata Extraction**: Extract and preserve article metadata (title, author, description, etc.)
- **Image Processing**: Handle and organize images from webpage packages
- **Content Cleaning**: Remove ads, scripts, navigation, and other unwanted elements
- **Code Block Preservation**: Maintain syntax highlighting in code blocks
- **Configurable Output**: Customize conversion behavior and output formatting

## Installation

1. Clone or download this MCP server
2. Install the package:
   ```bash
   cd mdconverter-mcp
   pip install -e .
   ```

## Usage

### As an MCP Server

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "mdconverter-mcp": {
      "command": "mdconverter-mcp",
      "args": []
    }
  }
}
```

### Available Tools

1. **convert_html_to_markdown**
   - Convert HTML files to Markdown with full processing
   - Handles images, metadata, and content optimization
   - Configurable output options

2. **validate_html_file**
   - Validate HTML files before conversion
   - Check file existence, format, and readability

3. **get_html_metadata**
   - Extract metadata from HTML files without full conversion
   - Useful for previewing content information

4. **list_supported_formats**
   - List supported input and output formats
   - Show available features and capabilities

5. **convert_html_content**
   - Convert HTML content strings directly to Markdown
   - Useful for processing HTML snippets

## Examples

### Basic HTML to Markdown Conversion

```python
# Via MCP tool call
{
  "tool": "convert_html_to_markdown",
  "arguments": {
    "html_file_path": "/path/to/webpage.html",
    "output_dir": "converted_articles",
    "preserve_images": true,
    "add_metadata": true
  }
}
```

### HTML Content Conversion

```python
# Convert HTML string directly
{
  "tool": "convert_html_content",
  "arguments": {
    "html_content": "<h1>Title</h1><p>Content here</p>",
    "clean_html": true
  }
}
```

### Metadata Extraction

```python
# Extract just the metadata
{
  "tool": "get_html_metadata",
  "arguments": {
    "html_file_path": "/path/to/article.html"
  }
}
```

## Configuration Options

The converter supports various configuration options:

- `output_dir`: Directory for output files (default: "output")
- `images_dir`: Directory for processed images (default: "images")
- `preserve_images`: Whether to process and copy images (default: true)
- `clean_html`: Whether to remove unwanted elements (default: true)
- `add_metadata`: Whether to add YAML frontmatter (default: true)

## Input Formats

- **HTML files** (`.html`, `.htm`)
- **Webpage packages** (HTML + associated assets folders)
- **HTML content strings**

## Output Features

- **Clean Markdown**: Well-formatted, readable output
- **YAML Frontmatter**: Structured metadata headers
- **Image Organization**: Copied and organized image files
- **Code Preservation**: Syntax highlighting maintained
- **Content Optimization**: Cleaned and optimized content

## Requirements

- Python 3.12+
- Dependencies: `mcp`, `beautifulsoup4`, `requests`, `markdownify`, `lxml`, `html5lib`

## Error Handling

The server includes comprehensive error handling:
- File validation and existence checks
- Format validation and support verification
- Graceful handling of encoding issues
- Detailed error messages and logging

## Development

To contribute or modify the server:

1. Clone the repository
2. Install in development mode: `pip install -e .`
3. Make your changes
4. Test with an MCP client

## License

This project is part of the Leet_Vibe repository and follows the same licensing terms.
