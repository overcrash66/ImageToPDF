"""
Logging configuration for ImageToPDF application.
"""

import logging
import os
from datetime import datetime
from imagetopdf.constants import LOG_LEVEL, LOG_FORMAT, LOG_FILE


def setup_logger(name: str = __name__) -> logging.Logger:
    """
    Set up and configure a logger with file and console handlers.
    
    Args:
        name: Name of the logger
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # Avoid adding multiple handlers if logger already has them
    if logger.handlers:
        return logger
    
    # Create formatters
    file_formatter = logging.Formatter(LOG_FORMAT)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    # File handler
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, LOG_FILE)
    
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# Create a default logger instance
default_logger = setup_logger()