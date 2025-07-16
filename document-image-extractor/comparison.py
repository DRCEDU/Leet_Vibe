#!/usr/bin/env python3
"""
Image Comparison Utilities
Compare images extracted from different document formats.
"""

import os
from typing import List, Dict, Optional, Tuple
from .utils import FileUtils, ImageUtils


class ImageComparison:
    """Compare images extracted from different sources."""
    
    def __init__(self):
        """Initialize image comparison utility."""
        pass
    
    def compare_extraction_directories(self, pdf_dir: str, word_dir: str) -> Dict:
        """
        Compare images from PDF and Word extractions.
        
        Args:
            pdf_dir: Directory containing PDF extracted images
            word_dir: Directory containing Word extracted images
            
        Returns:
            Dictionary with comparison results
        """
        if not os.path.exists(pdf_dir):
            raise FileNotFoundError(f"PDF extraction directory not found: {pdf_dir}")
        
        if not os.path.exists(word_dir):
            raise FileNotFoundError(f"Word extraction directory not found: {word_dir}")
        
        # Get image files
        pdf_images = self._get_image_files(pdf_dir)
        word_images = self._get_image_files(word_dir)
        
        print("📊 DOCUMENT IMAGE EXTRACTION COMPARISON")
        print("=" * 60)
        print(f"PDF Images Found: {len(pdf_images)}")
        print(f"Word Images Found: {len(word_images)}")
        print("-" * 60)
        
        # Analyze PDF images
        pdf_analysis = self._analyze_images(pdf_images, pdf_dir, "PDF")
        
        # Analyze Word images
        word_analysis = self._analyze_images(word_images, word_dir, "Word")
        
        # Create comparison summary
        comparison = {
            'pdf_count': len(pdf_images),
            'word_count': len(word_images),
            'pdf_total_size_kb': pdf_analysis['total_size_kb'],
            'word_total_size_kb': word_analysis['total_size_kb'],
            'pdf_analysis': pdf_analysis,
            'word_analysis': word_analysis,
            'summary': self._generate_comparison_summary(pdf_analysis, word_analysis)
        }
        
        self._print_comparison_summary(comparison)
        
        return comparison
    
    def _get_image_files(self, directory: str) -> List[str]:
        """Get all image files from a directory."""
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.img'}
        return [f for f in os.listdir(directory) 
                if os.path.splitext(f.lower())[1] in image_extensions]
    
    def _analyze_images(self, image_files: List[str], directory: str, source_type: str) -> Dict:
        """Analyze a collection of images."""
        print(f"\n📄 {source_type.upper()} EXTRACTED IMAGES:")
        
        total_size_kb = 0
        formats = {}
        dimensions_list = []
        
        for i, img_file in enumerate(sorted(image_files), 1):
            img_path = os.path.join(directory, img_file)
            
            try:
                # Get file info
                size_kb = FileUtils.get_file_size_kb(img_path)
                total_size_kb += size_kb
                
                # Get image dimensions and format
                dimensions = ImageUtils.get_image_dimensions(img_path)
                
                # Determine format from extension
                file_ext = os.path.splitext(img_file.lower())[1]
                formats[file_ext] = formats.get(file_ext, 0) + 1
                
                if dimensions:
                    dimensions_list.append(dimensions)
                    size_info = f" ({dimensions[0]}x{dimensions[1]})"
                    
                    # Try to get format from PIL
                    try:
                        from PIL import Image
                        with Image.open(img_path) as img:
                            format_info = f" | Format: {img.format}"
                    except:
                        format_info = ""
                else:
                    size_info = ""
                    format_info = ""
                
                print(f"{i:2d}. {img_file}")
                print(f"    Size: {size_kb:.1f} KB{size_info}{format_info}")
                
            except Exception as e:
                print(f"{i:2d}. {img_file} - Error: {e}")
        
        # Calculate average dimensions
        avg_dimensions = None
        if dimensions_list:
            avg_width = sum(d[0] for d in dimensions_list) / len(dimensions_list)
            avg_height = sum(d[1] for d in dimensions_list) / len(dimensions_list)
            avg_dimensions = (int(avg_width), int(avg_height))
        
        return {
            'count': len(image_files),
            'total_size_kb': total_size_kb,
            'average_size_kb': total_size_kb / len(image_files) if image_files else 0,
            'formats': formats,
            'dimensions': dimensions_list,
            'average_dimensions': avg_dimensions
        }
    
    def _generate_comparison_summary(self, pdf_analysis: Dict, word_analysis: Dict) -> List[str]:
        """Generate comparison summary points."""
        summary = []
        
        if pdf_analysis['count'] == word_analysis['count']:
            summary.append(f"✓ Both PDF and Word contain {pdf_analysis['count']} images")
        else:
            summary.append(f"⚠ Different image counts: PDF={pdf_analysis['count']}, Word={word_analysis['count']}")
        
        # Compare formats
        pdf_formats = set(pdf_analysis['formats'].keys())
        word_formats = set(word_analysis['formats'].keys())
        
        if pdf_formats == word_formats:
            summary.append(f"✓ Same image formats: {', '.join(pdf_formats)}")
        else:
            summary.append(f"⚠ Different formats - PDF: {', '.join(pdf_formats)}, Word: {', '.join(word_formats)}")
        
        # Compare file sizes
        pdf_total = pdf_analysis['total_size_kb']
        word_total = word_analysis['total_size_kb']
        
        if word_total < pdf_total:
            savings = ((pdf_total - word_total) / pdf_total) * 100
            summary.append(f"✓ Word images are {savings:.1f}% smaller in total size")
        elif pdf_total < word_total:
            increase = ((word_total - pdf_total) / pdf_total) * 100
            summary.append(f"⚠ Word images are {increase:.1f}% larger in total size")
        else:
            summary.append("✓ Similar total file sizes")
        
        # Compare dimensions
        if (pdf_analysis['average_dimensions'] and word_analysis['average_dimensions'] and
            pdf_analysis['average_dimensions'] == word_analysis['average_dimensions']):
            summary.append("✓ Same average image dimensions")
        
        return summary
    
    def _print_comparison_summary(self, comparison: Dict) -> None:
        """Print formatted comparison summary."""
        print(f"\n{'='*60}")
        print("🔍 COMPARISON SUMMARY:")
        
        for point in comparison['summary']:
            print(f"{point}")
        
        print(f"\n📊 STATISTICS:")
        print(f"PDF Total Size: {comparison['pdf_total_size_kb']:.1f} KB")
        print(f"Word Total Size: {comparison['word_total_size_kb']:.1f} KB")
        
        if comparison['pdf_count'] > 0:
            print(f"PDF Average Size: {comparison['pdf_analysis']['average_size_kb']:.1f} KB per image")
        
        if comparison['word_count'] > 0:
            print(f"Word Average Size: {comparison['word_analysis']['average_size_kb']:.1f} KB per image")
    
    def find_similar_images(self, dir1: str, dir2: str, threshold: float = 0.95) -> List[Tuple[str, str, float]]:
        """
        Find similar images between two directories using basic comparison.
        
        Args:
            dir1: First directory to compare
            dir2: Second directory to compare
            threshold: Similarity threshold (0.0 to 1.0)
            
        Returns:
            List of tuples (file1, file2, similarity_score)
        """
        try:
            from PIL import Image
            import hashlib
        except ImportError:
            print("PIL is required for image similarity comparison")
            return []
        
        images1 = self._get_image_files(dir1)
        images2 = self._get_image_files(dir2)
        
        similar_pairs = []
        
        for img1 in images1:
            path1 = os.path.join(dir1, img1)
            
            try:
                # Get basic properties of first image
                with Image.open(path1) as image1:
                    size1 = image1.size
                    
                for img2 in images2:
                    path2 = os.path.join(dir2, img2)
                    
                    try:
                        with Image.open(path2) as image2:
                            size2 = image2.size
                            
                            # Basic similarity check: same dimensions
                            if size1 == size2:
                                # Consider them similar if dimensions match
                                # More sophisticated comparison would require additional libraries
                                similarity = 1.0 if size1 == size2 else 0.0
                                
                                if similarity >= threshold:
                                    similar_pairs.append((img1, img2, similarity))
                    
                    except Exception:
                        continue
            
            except Exception:
                continue
        
        return similar_pairs
    
    def generate_comparison_report(self, pdf_dir: str, word_dir: str, output_file: str) -> None:
        """
        Generate a detailed comparison report and save to file.
        
        Args:
            pdf_dir: Directory containing PDF extracted images
            word_dir: Directory containing Word extracted images
            output_file: Path to save the report
        """
        comparison = self.compare_extraction_directories(pdf_dir, word_dir)
        
        report_content = f"""Document Image Extraction Comparison Report
=============================================

Generated: {FileUtils.get_current_timestamp()}

SUMMARY:
--------
PDF Images: {comparison['pdf_count']}
Word Images: {comparison['word_count']}
PDF Total Size: {comparison['pdf_total_size_kb']:.1f} KB
Word Total Size: {comparison['word_total_size_kb']:.1f} KB

ANALYSIS:
---------
"""
        
        for point in comparison['summary']:
            report_content += f"{point}\n"
        
        report_content += f"""

DETAILED PDF ANALYSIS:
----------------------
Count: {comparison['pdf_analysis']['count']}
Total Size: {comparison['pdf_analysis']['total_size_kb']:.1f} KB
Average Size: {comparison['pdf_analysis']['average_size_kb']:.1f} KB
Formats: {comparison['pdf_analysis']['formats']}

DETAILED WORD ANALYSIS:
-----------------------
Count: {comparison['word_analysis']['count']}
Total Size: {comparison['word_analysis']['total_size_kb']:.1f} KB
Average Size: {comparison['word_analysis']['average_size_kb']:.1f} KB
Formats: {comparison['word_analysis']['formats']}
"""
        
        with open(output_file, 'w') as f:
            f.write(report_content)
        
        print(f"\n📄 Comparison report saved to: {output_file}")
