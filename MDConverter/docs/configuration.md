# Configuration File for MDConverter

This is an example configuration file for MDConverter. 
You can copy this file and modify the settings as needed.

## JSON Configuration Example

```json
{
  "output_dir": "output",
  "images_dir": "assets/images", 
  "preserve_images": true,
  "clean_html": true,
  "strip_javascript": true,
  "convert_links": true,
  "add_metadata": true,
  "add_toc": false,
  "wrap_width": 80,
  "heading_style": "atx",
  "log_level": "INFO",
  "max_file_size": 52428800,
  "timeout": 30
}
```

## YAML Configuration Example

```yaml
# File paths
output_dir: "output"
images_dir: "assets/images"
templates_dir: "assets/templates"

# Conversion settings  
preserve_images: true
clean_html: true
strip_javascript: true
convert_links: true
markdown_extensions: [".md"]

# Image processing
max_image_size: 5242880  # 5MB
supported_image_formats: [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"]
optimize_images: false

# Output formatting
add_metadata: true
add_toc: false
wrap_width: 80
heading_style: "atx"  # or "setext"

# Logging
log_level: "INFO"
log_file: "conversion.log"

# Performance
max_file_size: 52428800  # 50MB
timeout: 30  # seconds
```

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `output_dir` | string | "output" | Directory for converted files |
| `images_dir` | string | "assets/images" | Directory for processed images |
| `preserve_images` | boolean | true | Whether to process and save images |
| `clean_html` | boolean | true | Whether to clean HTML content |
| `add_metadata` | boolean | true | Whether to add metadata header |
| `log_level` | string | "INFO" | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |
| `max_file_size` | integer | 52428800 | Maximum file size in bytes (50MB) |
| `timeout` | integer | 30 | Request timeout in seconds |
