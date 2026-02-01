# ImageToPDF

A lightweight GUI application for converting images to PDF and PDF files to images. Built with PySide6, PyPDF2, and PyMuPDF.

![Screenshot](Screenshot.png)

## Features

- **Image to PDF Conversion**: Convert multiple images (JPEG, PNG) into a single merged PDF document
- **PDF to Image Conversion**: Extract individual pages from PDF files as JPEG images
- **Batch Processing**: Handle multiple images at once
- **Automatic Duplicate Handling**: Prevents overwriting files with automatic naming
- **User-Friendly GUI**: Intuitive interface with visual feedback

## Requirements

- Python 3.6 or higher

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python ImageToPdf.py
```

## Usage

### GUI Application (ImageToPdf.py)

1. **Convert Images to PDF**:
   - Click on any "Image 1-12" button to select image files
   - Selected images will be highlighted in green
   - Click "Convert Images To PDF" to merge all selected images into a single PDF
   - Output file will be saved as `Merged_PDF_[timestamp].pdf` in the current directory

2. **Convert PDF to JPEG**:
   - Click "Convert PDF To JPEG" button
   - Select a PDF file
   - Each PDF page will be converted to a separate JPEG image
   - Output images will be saved in the current directory with naming format: `Converted-PDF-page[number]_[timestamp].jpeg`

3. **Clear Selection**:
   - Click "Clear All Selection" to reset all selected images

### Command Line Tool (Python_Lib.py)

Convert PDF files to JPEG images from the command line:

```bash
python Python_Lib.py /path/to/your/file.pdf
```

This will extract each page as a separate JPEG image in the current directory.

## Technology Stack

- **GUI Framework**: PySide6
- **PDF Processing**: PyPDF2, PyMuPDF (fitz)
- **Image Processing**: Pillow (PIL)
- **UI Utilities**: easygui

## Notes

- The application has been tested on Windows 10 and Windows 11
- Both GUI (`ImageToPdf.py`) and command-line tool (`Python_Lib.py`) can be used independently
- Converted files are saved in the application's working directory
- Last updated: 01-31-2026
