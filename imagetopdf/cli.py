"""
PDF to JPEG Converter - Command-line utility for converting PDF files to JPEG images.
"""

import fitz  # PyMuPDF
import argparse
import os
from datetime import datetime
from typing import Optional

from imagetopdf.constants import (
    APP_NAME, APP_VERSION, APP_AUTHOR, JPEG_OUTPUT_PREFIX, JPEG_OUTPUT_SUFFIX,
    SUCCESS_PDF_TO_JPEG, TITLE_DONE
)
from imagetopdf.logger import default_logger
from imagetopdf.utils import (
    validate_file_path, create_output_directory, get_pdf_timestamp,
    log_file_operation
)


def convert_to_jpeg(pdf_path: str) -> None:
    """
    Convert a PDF file to JPEG images using PyMuPDF.
    
    Args:
        pdf_path: Path to the PDF file
    """
    logger = default_logger
    
    # Validate input file
    is_valid, error_msg = validate_file_path(pdf_path)
    if not is_valid:
        logger.error(f"Invalid PDF file: {pdf_path} - {error_msg}")
        print(f"Error: {error_msg}")
        return
    
    try:
        logger.info(f"Starting PDF to JPEG conversion: {pdf_path}")
        doc = fitz.open(pdf_path)
        print("Processing... Please Wait...")
        
        output_dir = create_output_directory()
        
        for page_index in range(len(doc)):
            page = doc.load_page(page_index)
            pix = page.get_pixmap()
            
            timestamp = get_pdf_timestamp()
            output_filename = f"{JPEG_OUTPUT_PREFIX}{page_index + 1}_{timestamp}{JPEG_OUTPUT_SUFFIX}"
            output_path = os.path.join(output_dir, output_filename)
            
            pix.save(output_path)
            print(f"Saved: {output_path}")
            log_file_operation(logger, "Page converted to JPEG", output_path, True)
        
        doc.close()
        
        message = f"{SUCCESS_PDF_TO_JPEG}\n\n{APP_NAME} v{APP_VERSION}\nCreated by {APP_AUTHOR}\nLast update: {datetime.now().strftime('%Y-%m-%d')}"
        print(f"\n{message}")
        
    except Exception as e:
        error_msg = f"Error occurred: {str(e)}"
        logger.error(error_msg)
        print(f"Error: {error_msg}")


def main():
    """Main entry point for the CLI tool."""
    parser = argparse.ArgumentParser(
        description=f'{APP_NAME} v{APP_VERSION} - Convert PDF files to JPEG images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  pdf-to-jpeg document.pdf
  pdf-to-jpeg /path/to/document.pdf

{APP_NAME} v{APP_VERSION} - {APP_AUTHOR}
        """
    )
    
    parser.add_argument(
        'pdf_path',
        metavar='PDF_PATH',
        type=str,
        help='Path to the PDF file to convert'
    )
    
    args = parser.parse_args()
    convert_to_jpeg(args.pdf_path)


if __name__ == "__main__":
    main()
