"""
Tests for MDConverter package
"""

import pytest
import tempfile
from pathlib import Path
import sys

# Add the source directory to path for importing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mdconverter import HTMLToMarkdownConverter, Config
from mdconverter.utils import validate_html_file, sanitize_filename, clean_text


class TestConfig:
    """Test configuration class"""
    
    def test_default_config(self):
        """Test default configuration values"""
        config = Config()
        assert config.get('output_dir') == 'output'
        assert config.get('preserve_images') is True
        assert config.get('log_level') == 'INFO'
    
    def test_custom_config(self):
        """Test custom configuration"""
        custom_config = {'output_dir': 'custom', 'log_level': 'DEBUG'}
        config = Config(custom_config)
        assert config.get('output_dir') == 'custom'
        assert config.get('log_level') == 'DEBUG'
        assert config.get('preserve_images') is True  # Default value
    
    def test_config_update(self):
        """Test configuration update"""
        config = Config()
        config.update({'new_setting': 'value'})
        assert config.get('new_setting') == 'value'


class TestUtils:
    """Test utility functions"""
    
    def test_sanitize_filename(self):
        """Test filename sanitization"""
        assert sanitize_filename("test<>file.md") == "test__file.md"
        assert sanitize_filename("  test  ") == "test"
        assert sanitize_filename("") == "converted_file"
    
    def test_clean_text(self):
        """Test text cleaning"""
        assert clean_text("  test   text  ") == "test text"
        assert clean_text("test&nbsp;text") == "test text"
        assert clean_text("") == ""
    
    def test_validate_html_file_nonexistent(self):
        """Test validation of non-existent file"""
        is_valid, error = validate_html_file("nonexistent.html")
        assert not is_valid
        assert "does not exist" in error
    
    def test_validate_html_file_wrong_extension(self):
        """Test validation of file with wrong extension"""
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
            temp_file = f.name
        
        try:
            is_valid, error = validate_html_file(temp_file)
            assert not is_valid
            assert "not an HTML file" in error
        finally:
            Path(temp_file).unlink()


class TestHTMLToMarkdownConverter:
    """Test HTML to Markdown converter"""
    
    def test_converter_invalid_file(self):
        """Test converter with invalid file"""
        with pytest.raises(ValueError):
            HTMLToMarkdownConverter("nonexistent.html")
    
    def test_converter_with_valid_html(self):
        """Test converter with valid HTML file"""
        # Create a temporary HTML file
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>Test</title></head>
        <body><h1>Test Heading</h1><p>Test paragraph</p></body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix=".html", delete=False) as f:
            f.write(html_content)
            temp_html = f.name
        
        try:
            converter = HTMLToMarkdownConverter(temp_html)
            assert converter.html_file_path.exists()
            assert converter.output_file.suffix == '.md'
        finally:
            Path(temp_html).unlink()
    
    def test_converter_with_config(self):
        """Test converter with custom configuration"""
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>Test</title></head>
        <body><h1>Test</h1></body>
        </html>
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix=".html", delete=False) as f:
            f.write(html_content)
            temp_html = f.name
        
        try:
            config = Config({'log_level': 'DEBUG'})
            converter = HTMLToMarkdownConverter(temp_html, config=config)
            assert converter.config.get('log_level') == 'DEBUG'
        finally:
            Path(temp_html).unlink()


if __name__ == "__main__":
    # Run tests if pytest is available, otherwise run basic tests
    try:
        import pytest
        pytest.main([__file__])
    except ImportError:
        print("Running basic tests (install pytest for full test suite)")
        
        # Run basic tests manually
        test_config = TestConfig()
        test_config.test_default_config()
        test_config.test_custom_config()
        test_config.test_config_update()
        print("✅ Config tests passed")
        
        test_utils = TestUtils()
        test_utils.test_sanitize_filename()
        test_utils.test_clean_text()
        test_utils.test_validate_html_file_nonexistent()
        print("✅ Utils tests passed")
        
        print("✅ All basic tests passed!")
