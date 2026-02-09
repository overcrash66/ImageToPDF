# ImageToPDF

A lightweight GUI application for converting images to PDF and PDF files to images. Built with PySide6, PyPDF2, and PyMuPDF.

![Screenshot](Screenshot.png)

## Features

- **Image to PDF Conversion**: Convert multiple images (JPEG, PNG) into a single merged PDF document
- **PDF to Image Conversion**: Extract individual pages from PDF files as JPEG images
- **Batch Processing**: Handle multiple images at once
- **Automatic Duplicate Handling**: Prevents overwriting files with automatic naming
- **User-Friendly GUI**: Intuitive interface with visual feedback
- **File Validation**: Validates file types, sizes, and paths before processing
- **Logging System**: Comprehensive logging for debugging and monitoring
- **Output Organization**: All converted files are saved in a dedicated output folder
- **Error Handling**: Robust error handling with user-friendly messages

## Requirements

- Python 3.6 or higher
- PyMuPDF (fitz) - Required for PDF to JPEG conversion

## Installation

```bash
pip install imagetopdf-gui
```

### Or manually:

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install PyMuPDF (Required for CLI tool)

```bash
pip install pymupdf
```

### 3. Run the Application

```bash
python ImageToPdf.py
```

## Usage

### GUI Application (ImageToPdf.py)

1. **Convert Images to PDF**:
   - Click on any "Image 1-12" button to select image files
   - Selected images will be highlighted in green
   - Click "Convert Images To PDF" to merge all selected images into a single PDF
   - Output file will be saved as `Merged_PDF_[timestamp].pdf` in the `output` folder

2. **Convert PDF to JPEG**:
   - Click "Convert PDF To JPEG" button
   - Select a PDF file
   - Each PDF page will be converted to a separate JPEG image
   - Output images will be saved in the `output` folder with naming format: `Converted-PDF-page[number]_[timestamp].jpeg`

3. **Clear Selection**:
   - Click "Clear All Selection" to reset all selected images

### Command Line Tool (Python_Lib.py)

Convert PDF files to JPEG images from the command line:

```bash
python Python_Lib.py /path/to/your/file.pdf
```

This will extract each page as a separate JPEG image in the `output` folder.

## Project Structure

```
ImageToPDF/
├── ImageToPdf.py          # GUI Application
├── Python_Lib.py          # CLI Tool
├── constants.py           # Application constants
├── logger.py              # Logging configuration
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── Screenshot.png         # Application screenshot
└── logs/                  # Log files (auto-created)
    └── image_to_pdf.log
```

## Technology Stack

- **GUI Framework**: PySide6
- **PDF Processing**: PyPDF2, PyMuPDF (fitz)
- **Image Processing**: Pillow (PIL)
- **Logging**: Python logging module
- **CLI**: argparse

## Improvements

This version includes the following improvements over the original:

- **Security**: Added file path validation and sanitization
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Logging**: Full logging system for debugging and monitoring
- **Code Quality**: Type hints, docstrings, and consistent code style
- **Configuration**: Centralized constants file for easy maintenance
- **Output Organization**: Dedicated output folder for all converted files
- **File Size Limits**: Maximum file size validation to prevent memory issues
- **Code Comments**: Detailed comments explaining functionality
- **Type Safety**: Type hints for better code clarity and IDE support
- **Modularity**: Separated concerns into utility modules
- **Documentation**: Improved README with project structure and usage examples

## Notes

- The application has been tested on Windows 10 and Windows 11
- Both GUI ([`ImageToPdf.py`](ImageToPdf.py:1)) and command-line tool ([`Python_Lib.py`](Python_Lib.py:1)) can be used independently
- Converted files are saved in the `output` folder
- Log files are saved in the `logs` folder
- Last updated: 2026-02-08

## License

This project is created by WAEL SAHLI.

## Support

For issues or questions, please refer to the log files in the `logs` directory for detailed error information.
