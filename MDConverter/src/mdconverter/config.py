"""
Configuration module for MDConverter
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional


class Config:
    """Configuration class for MDConverter settings"""
    
    def __init__(self, config_dict: Optional[Dict[str, Any]] = None):
        """Initialize configuration with default values"""
        self.config = config_dict or {}
        self._set_defaults()
    
    def _set_defaults(self):
        """Set default configuration values"""
        defaults = {
            # File paths
            'output_dir': 'output',
            'images_dir': 'assets/images',
            'templates_dir': 'assets/templates',
            
            # Conversion settings
            'preserve_images': True,
            'clean_html': True,
            'strip_javascript': True,
            'convert_links': True,
            'markdown_extensions': ['.md'],
            
            # Image processing
            'max_image_size': 5 * 1024 * 1024,  # 5MB
            'supported_image_formats': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
            'optimize_images': False,
            
            # Output formatting
            'add_metadata': True,
            'add_toc': False,
            'wrap_width': 80,
            'heading_style': 'atx',  # or 'setext'
            
            # Logging
            'log_level': 'INFO',
            'log_file': 'conversion.log',
            
            # Performance
            'max_file_size': 50 * 1024 * 1024,  # 50MB
            'timeout': 30,  # seconds
        }
        
        for key, value in defaults.items():
            if key not in self.config:
                self.config[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
    
    def update(self, config_dict: Dict[str, Any]) -> None:
        """Update configuration with new values"""
        self.config.update(config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Return configuration as dictionary"""
        return self.config.copy()
    
    @classmethod
    def from_file(cls, config_path: str) -> 'Config':
        """Load configuration from file"""
        config_path = Path(config_path)
        
        if not config_path.exists():
            return cls()
        
        try:
            if config_path.suffix.lower() == '.json':
                import json
                with open(config_path, 'r') as f:
                    config_dict = json.load(f)
            elif config_path.suffix.lower() in ['.yaml', '.yml']:
                import yaml
                with open(config_path, 'r') as f:
                    config_dict = yaml.safe_load(f)
            else:
                # Assume it's a Python file
                import importlib.util
                spec = importlib.util.spec_from_file_location("config", config_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                config_dict = {k: v for k, v in module.__dict__.items() 
                             if not k.startswith('_')}
            
            return cls(config_dict)
            
        except Exception as e:
            print(f"Warning: Failed to load config from {config_path}: {e}")
            return cls()
    
    def save_to_file(self, config_path: str) -> None:
        """Save configuration to file"""
        config_path = Path(config_path)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            if config_path.suffix.lower() == '.json':
                import json
                with open(config_path, 'w') as f:
                    json.dump(self.config, f, indent=2)
            elif config_path.suffix.lower() in ['.yaml', '.yml']:
                import yaml
                with open(config_path, 'w') as f:
                    yaml.dump(self.config, f, default_flow_style=False, indent=2)
            else:
                raise ValueError(f"Unsupported config file format: {config_path.suffix}")
                
        except Exception as e:
            print(f"Error: Failed to save config to {config_path}: {e}")


# Default configuration instance
default_config = Config()
