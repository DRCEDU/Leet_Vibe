# MDConverter MCP Server Setup Guide

This guide walks you through setting up and using the MDConverter MCP server.

## Quick Start

1. **Install the MCP server:**
   ```bash
   cd mdconverter-mcp
   pip install -e .
   ```

2. **Test the installation:**
   ```bash
   mdconverter-mcp --help
   ```

## MCP Client Configuration

### VS Code with MCP Extension

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "mdconverter-mcp": {
      "command": "mdconverter-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

### Claude Desktop

Add to your `claude_desktop_config.json`:

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

## Available Tools

### 1. convert_html_to_markdown
Converts HTML files to Markdown with full processing.

**Parameters:**
- `html_file_path` (required): Path to HTML file
- `output_file` (optional): Custom output file path
- `output_dir` (optional): Output directory (default: "output")
- `images_dir` (optional): Images directory (default: "images")
- `preserve_images` (optional): Process images (default: true)
- `clean_html` (optional): Clean HTML content (default: true)
- `add_metadata` (optional): Add YAML frontmatter (default: true)

**Example:**
```json
{
  "tool": "convert_html_to_markdown",
  "arguments": {
    "html_file_path": "/path/to/article.html",
    "output_dir": "converted_articles",
    "preserve_images": true,
    "add_metadata": true
  }
}
```

### 2. validate_html_file
Validates HTML files before conversion.

**Parameters:**
- `html_file_path` (required): Path to HTML file

**Example:**
```json
{
  "tool": "validate_html_file",
  "arguments": {
    "html_file_path": "/path/to/article.html"
  }
}
```

### 3. get_html_metadata
Extracts metadata from HTML files.

**Parameters:**
- `html_file_path` (required): Path to HTML file

**Example:**
```json
{
  "tool": "get_html_metadata",
  "arguments": {
    "html_file_path": "/path/to/article.html"
  }
}
```

### 4. convert_html_content
Converts HTML content strings to Markdown.

**Parameters:**
- `html_content` (required): HTML content string
- `add_metadata` (optional): Add metadata (default: false)
- `clean_html` (optional): Clean HTML (default: true)

**Example:**
```json
{
  "tool": "convert_html_content",
  "arguments": {
    "html_content": "<h1>Title</h1><p>Content here</p>",
    "clean_html": true
  }
}
```

### 5. list_supported_formats
Lists supported formats and features.

**Parameters:** None

**Example:**
```json
{
  "tool": "list_supported_formats",
  "arguments": {}
}
```

## Common Use Cases

### Converting TDS Articles
```json
{
  "tool": "convert_html_to_markdown",
  "arguments": {
    "html_file_path": "/path/to/TDS_Article.html",
    "output_dir": "tds_articles",
    "preserve_images": true,
    "add_metadata": true
  }
}
```

### Batch Processing
Use the validation tool first, then convert:
```json
{
  "tool": "validate_html_file",
  "arguments": {
    "html_file_path": "/path/to/article.html"
  }
}
```

### Quick HTML Snippet Conversion
```json
{
  "tool": "convert_html_content",
  "arguments": {
    "html_content": "<h2>Quick Note</h2><p>This is a quick HTML snippet.</p>",
    "clean_html": true
  }
}
```

## Output Structure

The MCP server creates organized output:

```
output/
├── article_name.md          # Converted markdown
└── images/                  # Processed images
    ├── image1.jpg
    ├── image2.png
    └── ...
```

## Troubleshooting

### Common Issues

1. **Import errors**: Install dependencies with `pip install -e .`
2. **File not found**: Check file paths and permissions
3. **Empty output**: Verify HTML file is valid and readable
4. **Image processing**: Ensure image assets folder exists

### Debug Mode

Enable debug logging by setting environment variable:
```bash
export MDCONVERTER_LOG_LEVEL=DEBUG
```

## Advanced Configuration

### Custom Output Templates
The server supports customizable output formatting through the configuration system.

### Image Processing Options
- Minimum image size filtering
- Format conversion options
- Quality optimization settings

### Content Cleaning Rules
- Customizable unwanted element selectors
- Configurable content area detection
- Advanced text processing options

## Support

For issues or questions:
1. Check the logs for error messages
2. Verify file permissions and paths
3. Test with simple HTML files first
4. Check MCP client configuration

## Next Steps

1. Test the server with sample HTML files
2. Configure your MCP client
3. Start converting your HTML content to Markdown
4. Explore advanced configuration options
