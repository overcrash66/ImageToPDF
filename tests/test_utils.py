"""
Unit tests for utility functions.
"""

import unittest
import os
import tempfile
from pathlib import Path
from imagetopdf.utils import (
    validate_file_path, get_file_extension, sanitize_filename,
    generate_unique_filename, create_output_directory, get_timestamp,
    get_pdf_timestamp, log_file_operation
)
from imagetopdf.constants import MAX_IMAGE_SIZE, MAX_FILE_SIZE


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_image = Path(self.temp_dir) / "test.jpg"
        self.test_image.write_bytes(b"fake image data")
        
        self.test_pdf = Path(self.temp_dir) / "test.pdf"
        self.test_pdf.write_bytes(b"fake pdf data")
    
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_validate_file_path_valid_image(self):
        """Test validation of valid image file."""
        is_valid, error_msg = validate_file_path(str(self.test_image))
        self.assertTrue(is_valid)
        self.assertIsNone(error_msg)
    
    def test_validate_file_path_valid_pdf(self):
        """Test validation of valid PDF file."""
        is_valid, error_msg = validate_file_path(str(self.test_pdf))
        self.assertTrue(is_valid)
        self.assertIsNone(error_msg)
    
    def test_validate_file_path_nonexistent(self):
        """Test validation of non-existent file."""
        is_valid, error_msg = validate_file_path("/nonexistent/file.pdf")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error_msg)
    
    def test_validate_file_path_invalid_extension(self):
        """Test validation of file with invalid extension."""
        invalid_file = Path(self.temp_dir) / "test.txt"
        invalid_file.write_bytes(b"fake data")
        
        is_valid, error_msg = validate_file_path(str(invalid_file))
        self.assertFalse(is_valid)
        self.assertIsNotNone(error_msg)
    
    def test_validate_file_path_too_large(self):
        """Test validation of file that is too large."""
        large_file = Path(self.temp_dir) / "large.pdf"
        large_file.write_bytes(b"x" * (MAX_FILE_SIZE + 1))
        
        is_valid, error_msg = validate_file_path(str(large_file))
        self.assertFalse(is_valid)
        self.assertIn("too large", error_msg.lower())
    
    def test_get_file_extension(self):
        """Test file extension extraction."""
        self.assertEqual(get_file_extension("test.jpg"), ".jpg")
        self.assertEqual(get_file_extension("test.jpeg"), ".jpeg")
        self.assertEqual(get_file_extension("test.png"), ".png")
        self.assertEqual(get_file_extension("test.pdf"), ".pdf")
    
    def test_sanitize_filename(self):
        """Test filename sanitization."""
        self.assertEqual(sanitize_filename("test file.jpg"), "test_file.jpg")
        # < and > are each replaced with _, so test<file> becomes test_file_
        self.assertEqual(sanitize_filename("test<file>.jpg"), "test_file_.jpg")
        self.assertEqual(sanitize_filename("test|file.jpg"), "test_file.jpg")
        self.assertEqual(sanitize_filename("test/file.jpg"), "test_file.jpg")
    
    def test_generate_unique_filename(self):
        """Test unique filename generation."""
        import uuid
        output_dir = self.temp_dir
        # Use unique base name to avoid conflicts
        base_name = f"test_{uuid.uuid4().hex[:8]}"
        extension = ".pdf"
        
        # First file should be created without counter
        filename1 = generate_unique_filename(base_name, extension, output_dir)
        self.assertIn(base_name, filename1)
        # Create the file so the next call generates a unique name
        Path(filename1).touch()
        self.assertTrue(os.path.exists(filename1))
        
        # Second file should have counter
        filename2 = generate_unique_filename(base_name, extension, output_dir)
        self.assertNotEqual(filename1, filename2)
        self.assertIn(base_name, filename2)
    
    def test_create_output_directory(self):
        """Test output directory creation."""
        output_dir = create_output_directory()
        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(os.path.isdir(output_dir))
    
    def test_get_timestamp(self):
        """Test timestamp generation."""
        timestamp = get_timestamp()
        self.assertIsInstance(timestamp, str)
        self.assertEqual(len(timestamp), 14)  # YYYYMMDDHHMMSS
    
    def test_get_pdf_timestamp(self):
        """Test PDF timestamp generation."""
        timestamp = get_pdf_timestamp()
        self.assertIsInstance(timestamp, str)
        self.assertIn("-", timestamp)  # Contains date separator
        self.assertIn("_", timestamp)  # Contains date/time separator


if __name__ == '__main__':
    unittest.main()