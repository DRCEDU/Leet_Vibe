#!/usr/bin/env python3
"""
Test the updated MCP server with ZIP functionality
"""

import asyncio
import sys
import os
sys.path.append('/mnt/b/Users/cjdua/Github/Leet_Vibe/document-image-extractor-mcp/src')

from document_image_extractor_mcp.server import DocumentExtractor

async def main():
    print("🔧 Testing Updated MCP Server with ZIP functionality...")
    print("=" * 60)
    
    # Test document path
    doc_path = '/mnt/c/Users/cjdua/Downloads/102915_Luca_Nicolas_Scheibler_Week_6_3987509_1511473422.docx'
    
    if not os.path.exists(doc_path):
        print(f"❌ Document not found: {doc_path}")
        return
    
    try:
        # Create extractor with ZIP enabled
        extractor = DocumentExtractor(create_zip=True)
        
        # Extract images
        extracted_images, output_dir, zip_path = extractor.extract_images(doc_path)
        
        print(f"✅ Successfully extracted {len(extracted_images)} images")
        print(f"📁 Output directory: {output_dir}")
        print(f"📦 ZIP file: {zip_path}")
        
        if zip_path and os.path.exists(zip_path):
            zip_size = os.path.getsize(zip_path)
            print(f"📏 ZIP file size: {zip_size:,} bytes ({zip_size/1024/1024:.2f} MB)")
            print("✅ ZIP file created successfully!")
        else:
            print("❌ ZIP file not created")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
