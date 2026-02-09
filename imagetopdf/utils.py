"""
Utility functions for file operations and validation.
"""

import os
import logging
from pathlib import Path
from typing import List, Tuple, Optional
from imagetopdf.constants import (
    IMAGE_EXTENSIONS, PDF_EXTENSIONS, MAX_FILE_SIZE, MAX_IMAGE_SIZE,
    ERROR_INVALID_FILE, ERROR_FILE_TOO_LARGE, ERROR_UNKNOWN
)
from imagetopdf.logger import default_logger


def validate_file_path(file_path: str) -> Tuple[bool, Optional[str]]:
    """
    Validate a file path and check if it exists and has a valid extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not file_path:
        return False, "File path cannot be empty"
    
    if not os.path.exists(file_path):
        return False, "File does not exist"
    
    if not os.path.isfile(file_path):
        return False, "Path is not a file"
    
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext in IMAGE_EXTENSIONS:
        file_size = os.path.getsize(file_path)
        if file_size > MAX_IMAGE_SIZE:
            return False, ERROR_FILE_TOO_LARGE.format(max_size=MAX_IMAGE_SIZE)
    elif file_ext in PDF_EXTENSIONS:
        file_size = os.path.getsize(file_path)
        if file_size > MAX_FILE_SIZE:
            return False, ERROR_FILE_TOO_LARGE.format(max_size=MAX_FILE_SIZE)
    else:
        return False, ERROR_INVALID_FILE
    
    return True, None


def get_file_extension(file_path: str) -> str:
    """
    Get the file extension from a file path.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File extension including the dot
    """
    return os.path.splitext(file_path)[1].lower()


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename by removing invalid characters.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove invalid characters (including spaces for cross-platform compatibility)
    invalid_chars = '<>:"/\\|?* '
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    
    return filename


def generate_unique_filename(base_name: str, extension: str, output_dir: str = ".") -> str:
    """
    Generate a unique filename by appending a counter if the file already exists.
    
    Args:
        base_name: Base filename without extension
        extension: File extension including the dot
        output_dir: Output directory path
        
    Returns:
        Unique filename
    """
    output_path = os.path.join(output_dir, base_name + extension)
    
    if not os.path.exists(output_path):
        return output_path
    
    counter = 1
    while True:
        new_name = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(output_dir, new_name)
        if not os.path.exists(new_path):
            return new_path
        counter += 1


def create_output_directory() -> str:
    """
    Create output directory if it doesn't exist.
    
    Returns:
        Path to the output directory
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def get_timestamp(format_str: str = "%Y%m%d%H%M%S") -> str:
    """
    Get current timestamp in specified format.
    
    Args:
        format_str: Timestamp format string
        
    Returns:
        Formatted timestamp
    """
    from datetime import datetime
    return datetime.now().strftime(format_str)


def get_pdf_timestamp(format_str: str = "%d-%m-%Y_%H-%M-%S-%f") -> str:
    """
    Get current timestamp in PDF-specific format.
    
    Args:
        format_str: Timestamp format string
        
    Returns:
        Formatted timestamp
    """
    from datetime import datetime
    return datetime.now().strftime(format_str)


def log_file_operation(logger: logging.Logger, operation: str, file_path: str, success: bool = True):
    """
    Log file operation with context.
    
    Args:
        logger: Logger instance
        operation: Operation description
        file_path: Path to the file
        success: Whether the operation was successful
    """
    status = "SUCCESS" if success else "FAILED"
    logger.info(f"{operation}: {file_path} [{status}]")