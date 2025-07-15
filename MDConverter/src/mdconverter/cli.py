"""
Command Line Interface for MDConverter
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from .converter import HTMLToMarkdownConverter
from .config import Config
from .utils import setup_logging


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(
        description="Convert HTML webpage packages to Markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  mdconverter input.html
  mdconverter input.html -o output.md
  mdconverter input.html --config config.json
  mdconverter input.html --images-dir custom_images
        """
    )
    
    parser.add_argument(
        "html_file",
        help="Path to the HTML file to convert"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output markdown file path (default: auto-generated in output directory)"
    )
    
    parser.add_argument(
        "--config",
        help="Path to configuration file (JSON or YAML)"
    )
    
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory for converted files (default: output)"
    )
    
    parser.add_argument(
        "--images-dir", 
        help="Directory name for processed images (default: images)"
    )
    
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level (default: INFO)"
    )
    
    parser.add_argument(
        "--log-file",
        help="Log file path (default: console only)"
    )
    
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Skip image processing"
    )
    
    parser.add_argument(
        "--no-cleanup",
        action="store_true", 
        help="Don't clean HTML content"
    )
    
    parser.add_argument(
        "--add-metadata",
        action="store_true",
        help="Add metadata header to output"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="MDConverter 1.0.0"
    )
    
    return parser


def main():
    """Main entry point for CLI"""
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        # Load configuration
        if args.config:
            config = Config.from_file(args.config)
        else:
            config = Config()
        
        # Override config with command line arguments
        config_overrides = {}
        
        if args.output_dir:
            config_overrides['output_dir'] = args.output_dir
        if args.images_dir:
            config_overrides['images_dir'] = args.images_dir
        if args.log_level:
            config_overrides['log_level'] = args.log_level
        if args.log_file:
            config_overrides['log_file'] = args.log_file
        if args.no_images:
            config_overrides['preserve_images'] = False
        if args.no_cleanup:
            config_overrides['clean_html'] = False
        if args.add_metadata:
            config_overrides['add_metadata'] = True
            
        config.update(config_overrides)
        
        # Setup logging
        logger = setup_logging(
            config.get('log_level', 'INFO'),
            config.get('log_file')
        )
        
        logger.info(f"Starting conversion of {args.html_file}")
        
        # Create converter and run conversion
        converter = HTMLToMarkdownConverter(
            args.html_file, 
            args.output,
            config
        )
        
        success = converter.convert()
        
        if success:
            logger.info(f"Conversion completed successfully")
            logger.info(f"Output file: {converter.output_file}")
            print(f"✅ Conversion completed: {converter.output_file}")
        else:
            logger.error("Conversion failed")
            print("❌ Conversion failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n❌ Conversion interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
