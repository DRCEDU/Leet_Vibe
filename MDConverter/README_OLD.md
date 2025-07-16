# MDConverter - HTML to Markdown Converter

A comprehensive Python toolkit for converting HTML webpage packages into clean, well-formatted Markdown files.

## 📁 Folder Contents

```text
MDConverter/
├── README.md                                    # This file
├── html_to_markdown_converter.py               # Main converter script
├── requirements_html_converter.txt             # Python dependencies
├── setup_converter.sh                          # Automated setup script
├── convert_tds_article.py                      # Example: TDS article converter
├── demo_converter.py                           # Test and demonstration script
├── TEST_RESULTS.md                             # Test results and validation
├── converter_env/                              # Virtual environment (created after setup)
├── images/                                     # Processed images (created after conversion)
└── output/                                     # Generated markdown files
    ├── Abstract_Classes_TDS_Article.md
    ├── Dynamic_Inventory_Optimization_TDS.md
    └── [other_converted_files].md
```

## 🚀 Quick Start

### 1. Setup (First Time Only)

```bash
cd MDConverter
./setup_converter.sh
```

This will:

- Create a virtual environment (`converter_env/`)
- Install all required Python packages
- Display usage instructions

### 2. Basic Usage

```bash
# Activate virtual environment
source converter_env/bin/activate

# Convert any HTML webpage package (outputs to output/ folder by default)
python3 html_to_markdown_converter.py "path/to/webpage.html"

# Convert with custom output file
python3 html_to_markdown_converter.py "input.html" "custom_name.md"

# Convert with specific output location
python3 html_to_markdown_converter.py "input.html" "output/my_article.md"

# Verbose mode for debugging
python3 html_to_markdown_converter.py "input.html" --verbose
```

### 3. Example Conversions

```bash
# Using the TDS article example
python3 convert_tds_article.py

# Running the demo
python3 demo_converter.py

# Help and options
python3 html_to_markdown_converter.py --help
```

## ✨ Features

- **Smart Content Extraction**: Automatically identifies and extracts main article content
- **Image Processing**: Copies images from assets folders and updates markdown references
- **Metadata Preservation**: Extracts title, author, description, and other metadata
- **Code Block Support**: Maintains syntax highlighting information from HTML
- **Clean Formatting**: Produces well-structured markdown with proper spacing
- **Content Filtering**: Removes ads, navigation, headers, footers, and other non-content elements
- **Flexible Input**: Works with complete webpage packages (HTML + assets folder)

## 📊 Output Structure

After conversion, you'll get:

```text
MDConverter/
├── output/
│   └── your_article.md          # Clean markdown file with YAML frontmatter
└── images/                      # Folder containing all processed images
    ├── image1.png
    ├── image2.jpg
    └── ...
```

## 🛠 Advanced Usage

### Command Line Options

- `--verbose` or `-v`: Enable detailed output
- `--help` or `-h`: Show all available options

### Programmatic Usage

```python
from html_to_markdown_converter import WebpageToMarkdownConverter

converter = WebpageToMarkdownConverter("input.html", "output.md")
markdown_content = converter.convert()
```

## 📋 Supported Input Types

- Complete webpage packages (HTML file + assets folder)
- Articles from Medium, Towards Data Science, and similar platforms
- Blog posts and technical documentation
- Any HTML content with associated media files

## 🔧 Dependencies

All dependencies are listed in `requirements_html_converter.txt`:

- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests (if needed)
- `markdownify` - HTML to Markdown conversion
- `lxml` - XML/HTML processing
- `html5lib` - HTML5 parsing

## 💡 Tips

1. **File Paths**: Use absolute paths or ensure you're in the correct directory
2. **Virtual Environment**: Always activate the virtual environment before running scripts
3. **Large Files**: The converter handles large HTML files efficiently
4. **Encoding**: Supports both UTF-8 and Latin-1 file encodings
5. **Debugging**: Use `--verbose` flag to troubleshoot conversion issues

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'bs4'"**
   - Solution: Activate virtual environment with `source converter_env/bin/activate`

2. **"File not found"**
   - Solution: Check file path and use absolute paths when possible

3. **"Permission denied"**
   - Solution: Ensure you have read access to input files and write access to output directory

4. **"Empty output"**
   - Solution: Check if the HTML file contains the expected content structure

### Getting Help

- Run with `--verbose` flag for detailed processing information
- Check the original `README_html_converter.md` for comprehensive documentation
- Review the example scripts (`convert_tds_article.py`, `demo_converter.py`)

## 📈 Performance

- **Processing Speed**: Handles typical blog articles (5-50KB HTML) in seconds
- **Memory Usage**: Efficient processing of large HTML files
- **Image Handling**: Automatically copies and optimizes image references
- **Output Quality**: Produces clean, readable markdown suitable for documentation

## 🎯 Use Cases

- Converting saved web articles for offline reading
- Creating markdown documentation from HTML content
- Archiving blog posts and tutorials
- Preparing content for static site generators
- Building personal knowledge bases from web content

---

**Note**: This toolkit is part of the Leet_Vibe repository and is designed for educational and personal use in converting web content to markdown format.
