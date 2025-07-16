# HTML to Markdown Converter

A comprehensive Python script that converts complete webpage packages (HTML file + assets folder) into clean, well-formatted Markdown files.

## Features

- **Complete Package Processing**: Handles HTML files along with their associated assets folders
- **Image Processing**: Automatically copies and references images in the markdown output
- **Metadata Extraction**: Extracts and preserves article metadata (title, author, description, etc.)
- **Clean Formatting**: Produces well-structured markdown with proper headings, lists, and code blocks
- **Code Block Preservation**: Maintains syntax highlighting information from HTML
- **Content Filtering**: Removes ads, navigation, and other non-content elements
- **Flexible Output**: Supports custom output file paths

## Installation

1. Install required dependencies:
```bash
pip install -r requirements_html_converter.txt
```

Or install manually:
```bash
pip install beautifulsoup4 requests markdownify lxml html5lib
```

## Usage

### Basic Usage
```bash
python html_to_markdown_converter.py "Topic Model Labelling with LLMs _ Towards Data Science.html"
```

### Specify Output File
```bash
python html_to_markdown_converter.py "webpage.html" "output.md"
```

### Verbose Mode
```bash
python html_to_markdown_converter.py "webpage.html" --verbose
```

### Full Path Example
```bash
python html_to_markdown_converter.py "/path/to/webpage.html" "/path/to/output.md"
```

## Example for Your TDS Article

To convert the "Topic Model Labelling with LLMs" article:

```bash
# Navigate to the directory containing the script
cd /mnt/b/Users/cjdua/Github/Leet_Vibe

# Run the converter (adjust path as needed)
python html_to_markdown_converter.py "/mnt/c/Users/cjdua/Downloads/Topic Model Labelling with LLMs _ Towards Data Science.html"
```

This will create:
- `Topic Model Labelling with LLMs _ Towards Data Science.md` - The markdown file
- `images/` folder - Containing all processed images

## Output Structure

The generated markdown file includes:

1. **YAML Frontmatter**: Metadata like title, author, description
2. **Article Information Section**: Publication details
3. **Main Content**: Clean, formatted article content with:
   - Proper headings hierarchy
   - Preserved code blocks with syntax highlighting
   - Images with proper paths
   - Tables, lists, and quotes
   - Links and formatting

## Features in Detail

### Image Handling
- Copies images from the assets folder to a local `images/` directory
- Updates image references in the markdown
- Preserves alt text and handles different image formats
- Skips base64 encoded images (data URIs)

### Content Cleaning
- Removes advertisements, navigation, headers, footers
- Filters out social sharing widgets and cookie banners
- Preserves main article content
- Maintains proper formatting and structure

### Code Block Processing
- Detects and preserves syntax highlighting information
- Converts HTML `<pre><code>` blocks to markdown code fences
- Maintains proper indentation and formatting

## Supported Input Formats

- HTML files saved from browsers (complete webpage packages)
- Articles from Medium, Towards Data Science, and similar platforms
- Blog posts and technical documentation
- Any HTML content with associated assets

## Troubleshooting

### Common Issues

1. **File not found**: Ensure the HTML file path is correct
2. **Missing dependencies**: Install required packages using pip
3. **Encoding issues**: The script handles both UTF-8 and Latin-1 encodings
4. **Permission errors**: Make sure you have write permissions in the output directory

### Verbose Mode
Use `--verbose` flag to see detailed processing information and debug any issues.

## Advanced Usage

The script can be imported as a module:

```python
from html_to_markdown_converter import WebpageToMarkdownConverter

converter = WebpageToMarkdownConverter("input.html", "output.md")
markdown_content = converter.convert()
```

## File Structure After Conversion

```
your_directory/
├── html_to_markdown_converter.py
├── requirements_html_converter.txt
├── Topic Model Labelling with LLMs _ Towards Data Science.md
└── images/
    ├── image1.png
    ├── image2.jpg
    └── ...
```
