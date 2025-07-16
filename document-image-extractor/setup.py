#!/usr/bin/env python3
"""
Setup script for Document Image Extractor package.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="document-image-extractor",
    version="1.0.0",
    author="CJ Duan",
    author_email="",
    description="Extract images from PDF and Word documents with advanced features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DRCEDU/Leet_Vibe",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'extract-document-images=document_image_extractor.__main__:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="pdf word document image extraction docx",
    project_urls={
        "Bug Reports": "https://github.com/DRCEDU/Leet_Vibe/issues",
        "Source": "https://github.com/DRCEDU/Leet_Vibe",
    },
)
