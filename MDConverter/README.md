# MDConverter - HTML to Markdown Converter

A comprehensive Python package for converting HTML webpage packages into clean, well-formatted Markdown files.

## 🚀 Features

- **Clean Conversion**: Converts HTML to well-formatted Markdown
- **Image Processing**: Handles and preserves images from webpage packages  
- **Configurable**: Extensive configuration options via files or CLI
- **Package Structure**: Proper Python package with modular design
- **CLI Interface**: Easy-to-use command line interface
- **Logging**: Comprehensive logging and error handling
- **Templates**: Customizable output templates

## 📁 Optimized Project Structure

```text
MDConverter/
├── README.md                           # Main documentation
├── setup.py                           # Package setup script
├── requirements.txt                   # Python dependencies
├── setup_converter.sh                 # Setup script (legacy)
├── html_to_markdown_converter.py      # Legacy script (kept for compatibility)
├── 
├── src/mdconverter/                   # 📦 MAIN PACKAGE
│   ├── __init__.py                    # Package initialization
│   ├── converter.py                   # Core conversion logic
│   ├── config.py                      # Configuration management
│   ├── cli.py                         # Command line interface
│   └── utils.py                       # Utility functions
│
├── tests/                             # 🧪 TESTS
│   ├── __init__.py
│   └── test_mdconverter.py           # Test suite
│
├── examples/                          # 📋 EXAMPLES
│   ├── basic_usage.py                # Basic usage examples
│   ├── convert_tds_article.py        # TDS article converter example
│   └── demo_converter.py             # Demo and testing script
│
├── docs/                              # 📚 DOCUMENTATION  
│   ├── configuration.md              # Configuration guide
│   ├── README_html_converter.md       # Detailed documentation
│   ├── TEST_RESULTS.md               # Test validation results
│   └── ORGANIZATION_SUMMARY.md       # Organization notes
│
├── assets/                            # 🎨 ASSETS
│   ├── images/                       # Processed images (50+ files)
│   │   ├── chris-ried-ieic5Tq8YMk-unsplash-scaled-1.jpg
│   │   ├── Components-of-topic-modelling-pipeline-1-1024x793.png
│   │   └── ... (47+ more image files)
│   └── templates/                    # Output templates
│       └── article_template.md       # Article template
│
└── output/                           # 📋 OUTPUT
    ├── Abstract_Classes_TDS_Article.md
    └── Dynamic_Inventory_Optimization_TDS.md
```

## 🔧 Installation

### Option 1: Development Installation
```bash
cd MDConverter
pip install -e .
```

### Option 2: Direct Installation (from requirements)
```bash
cd MDConverter  
pip install -r requirements.txt
```

### Option 3: Legacy Setup Script
```bash
cd MDConverter
./setup_converter.sh
```

## 📖 Usage

### Command Line Interface

```bash
# Basic usage
mdconverter input.html

# With custom output file
mdconverter input.html -o output.md

# With configuration file
mdconverter input.html --config config.json

# With custom settings
mdconverter input.html --output-dir custom_output --log-level DEBUG
```

### Python API

```python
from mdconverter import HTMLToMarkdownConverter, Config

# Basic conversion
converter = HTMLToMarkdownConverter("input.html")
success = converter.convert()

# With custom configuration
config = Config({
    'output_dir': 'custom_output',
    'add_metadata': True,
    'log_level': 'DEBUG'
})

converter = HTMLToMarkdownConverter(
    "input.html", 
    output_file="custom.md",
    config=config
)
success = converter.convert()
```

### Configuration

Create a `config.json` file:

```json
{
  "output_dir": "output",
  "images_dir": "assets/images",
  "preserve_images": true,
  "clean_html": true,
  "add_metadata": true,
  "log_level": "INFO"
}
```

## 🧪 Testing

```bash
# Run tests with pytest (if installed)
python -m pytest tests/

# Run basic tests manually
python tests/test_mdconverter.py
```

## 📚 Documentation

- [Configuration Guide](docs/configuration.md)
- [Detailed Documentation](docs/README_html_converter.md)
- [Test Results](docs/TEST_RESULTS.md)

## 🔄 Migration from Legacy

The legacy `html_to_markdown_converter.py` script is still available for compatibility, but we recommend using the new package structure:

```bash
# Legacy (still works)
python html_to_markdown_converter.py input.html

# New package (recommended)
mdconverter input.html
```

## ✨ Key Improvements

1. **Modular Design**: Separated concerns into distinct modules
2. **Proper Package Structure**: Following Python packaging best practices
3. **Configuration Management**: Centralized, flexible configuration system
4. **CLI Interface**: Professional command-line interface with argparse
5. **Error Handling**: Comprehensive validation and error reporting
6. **Documentation**: Well-organized documentation and examples
7. **Testing**: Unit tests and validation framework
8. **Asset Organization**: Proper separation of code, docs, examples, and assets

## 🤝 Contributing

1. Follow the established package structure
2. Add tests for new features
3. Update documentation as needed
4. Use the configuration system for new settings
