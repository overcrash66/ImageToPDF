"""
ImageToPDF - GUI Application for converting images to PDF and PDFs to images.
Built with PySide6, PyPDF2, and PyMuPDF.
"""

import sys
import os
import subprocess
from typing import List, Optional
from PySide6.QtWidgets import (
    QFileDialog, QWidget, QLabel, QPushButton, QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout, QMessageBox, QProgressBar
)
from PySide6.QtGui import QFont
from PySide6 import QtCore
from PyPDF2 import PdfMerger, PdfReader
from PIL import Image
from datetime import datetime

from imagetopdf.constants import (
    APP_NAME, APP_VERSION, MAX_IMAGE_BUTTONS, BUTTON_TEXT_COLOR,
    BUTTON_SELECTED_COLOR, BUTTON_TEXT_COLOR_SELECTED, WINDOW_MINIMIZE_FLAG,
    PDF_OUTPUT_PREFIX, PDF_OUTPUT_SUFFIX, JPEG_OUTPUT_PREFIX, JPEG_OUTPUT_SUFFIX,
    SUCCESS_IMAGE_TO_PDF, SUCCESS_PDF_TO_JPEG, TITLE_INFO, TITLE_WARNING,
    TITLE_ERROR, TITLE_DONE
)
from imagetopdf.logger import default_logger
from imagetopdf.utils import (
    validate_file_path, get_file_extension, sanitize_filename,
    generate_unique_filename, create_output_directory, get_timestamp,
    log_file_operation
)

CREATE_NO_WINDOW = WINDOW_MINIMIZE_FLAG


class ImageToPdfConverter(QMainWindow):
    """
    Main GUI application for ImageToPDF conversion.
    """
    
    def __init__(self):
        super().__init__()
        self.logger = default_logger
        self.initUI()
    
    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setStyleSheet("#myWidget {background-color:#002633;}")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.qv_box = QVBoxLayout(self.central_widget)
        self.qh_box = QHBoxLayout()
        
        # Create image selection buttons and labels
        self.buttons = [self.create_button(f"Image {i}") for i in range(1, MAX_IMAGE_BUTTONS + 1)]
        self.labels = [QLabel() for _ in range(MAX_IMAGE_BUTTONS)]
        
        for button in self.buttons:
            self.qv_box.addWidget(button)
        
        for label in self.labels:
            label.setStyleSheet('color: red;')
            self.qv_box.addWidget(label)
        
        # Create action buttons with specific handlers
        self.button_clear = self.create_button("Clear All Selection", self.clear_all_selection)
        self.button_clear.setEnabled(False)
        self.button_pdf_to_image = self.create_button("Convert PDF To JPEG", self.convert_pdf_to_jpeg)
        self.button_image_to_pdf = self.create_button("Convert Images To PDF", self.convert_images_to_pdf)
        
        self.qh_box.addWidget(self.button_clear)
        self.qh_box.addWidget(self.button_pdf_to_image)
        self.qh_box.addWidget(self.button_image_to_pdf)
        self.qv_box.addLayout(self.qh_box)

        # Initialize state
        self.image_paths: List[str] = [""] * MAX_IMAGE_BUTTONS
        self.pdf_path: Optional[str] = None

        self.logger.info("Application initialized successfully")
    
    def create_button(self, text: str, handler=None) -> QPushButton:
        """
        Create a styled button.

        Args:
            text: Button text
            handler: Optional click handler function

        Returns:
            Configured QPushButton
        """
        button = QPushButton(text)
        button.setFont(QFont('Times', 10, weight=QFont.Bold))
        # Only connect handler if provided (explicit connection in initUI handles the rest)
        if handler:
            button.clicked.connect(handler)
        else:
            button.clicked.connect(self.button_clicked)
        button.setStyleSheet(f'QPushButton {{background-color: {BUTTON_TEXT_COLOR}; color: white;}}')
        return button
    
    def button_clicked(self):
        """Handle button click events."""
        button = self.sender()
        button_text = button.text()
        
        try:
            image_number = int(button_text.split()[-1])
        except (ValueError, IndexError):
            self.logger.warning(f"Invalid button text: {button_text}")
            return
        
        if 1 <= image_number <= MAX_IMAGE_BUTTONS:
            self.select_image(image_number)
        else:
            self.logger.warning(f"Image number out of range: {image_number}")
    
    def select_image(self, image_number: int):
        """
        Select an image file for conversion.
        
        Args:
            image_number: Image button number (1-12)
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open file', '', "Image files (*.jpeg *.jpg *.png)"
        )
        
        if file_path:
            is_valid, error_msg = validate_file_path(file_path)
            
            if not is_valid:
                self.logger.error(f"Invalid file selected: {file_path} - {error_msg}")
                QMessageBox.warning(self, TITLE_WARNING, error_msg)
                return
            
            self.image_paths[image_number - 1] = file_path
            filename = os.path.basename(file_path)
            self.labels[image_number - 1].setText(f"Selected Image is: {filename}")
            self.buttons[image_number - 1].setStyleSheet(
                f'QPushButton {{background-color: {BUTTON_SELECTED_COLOR}; color: {BUTTON_TEXT_COLOR_SELECTED};}}'
            )
            self.logger.info(f"Image {image_number} selected: {file_path}")
            self.update_button_state()
    
    def update_button_state(self):
        """Update button enable states based on selected images."""
        has_selection = any(self.image_paths)
        self.button_clear.setEnabled(has_selection)
        self.logger.debug(f"Button state updated: has_selection={has_selection}")
    
    def clear_all_selection(self):
        """Clear all selected images."""
        self.image_paths = [""] * MAX_IMAGE_BUTTONS
        for label in self.labels:
            label.clear()
        for button in self.buttons:
            button.setStyleSheet(f'QPushButton {{background-color: {BUTTON_TEXT_COLOR}; color: white;}}')
        self.update_button_state()
        self.logger.info("All selections cleared")
    
    def convert_pdf_to_jpeg(self):
        """Convert PDF file to JPEG images."""
        file_dialog = QFileDialog(self, 'Open file', '', "PDF files (*.pdf)")
        pdf_path, _ = file_dialog.getOpenFileName()
        
        if pdf_path:
            is_valid, error_msg = validate_file_path(pdf_path)
            
            if not is_valid:
                self.logger.error(f"Invalid PDF file: {pdf_path} - {error_msg}")
                QMessageBox.warning(self, TITLE_WARNING, error_msg)
                return
            
            try:
                self.logger.info(f"Starting PDF to JPEG conversion: {pdf_path}")
                subprocess.Popen([sys.executable, '-m', 'imagetopdf.cli', pdf_path], creationflags=CREATE_NO_WINDOW)
                QMessageBox.information(self, TITLE_INFO, SUCCESS_PDF_TO_JPEG)
            except Exception as e:
                error_msg = f"Failed to convert PDF: {str(e)}"
                self.logger.error(error_msg)
                QMessageBox.critical(self, TITLE_ERROR, error_msg)
    
    def convert_images_to_pdf(self):
        """Convert selected images to a single PDF file."""
        selected_images = [path for path in self.image_paths if path]
        
        if not selected_images:
            self.logger.warning("No images selected for conversion")
            QMessageBox.warning(self, TITLE_WARNING, "Please select at least one image to convert to PDF.")
            return
        
        try:
            self.logger.info(f"Starting image to PDF conversion: {len(selected_images)} images")
            output_dir = create_output_directory()
            
            # Convert each image to PDF
            pdf_paths = []
            for image_path in selected_images:
                try:
                    image = Image.open(image_path)
                    image = image.convert('RGB')
                    base_name = sanitize_filename(os.path.splitext(os.path.basename(image_path))[0])
                    pdf_path = generate_unique_filename(base_name, PDF_OUTPUT_SUFFIX, output_dir)
                    
                    image.save(pdf_path)
                    pdf_paths.append(pdf_path)
                    log_file_operation(self.logger, "Image saved as PDF", pdf_path, True)
                    
                except Exception as e:
                    error_msg = f"Failed to convert image {image_path}: {str(e)}"
                    self.logger.error(error_msg)
                    QMessageBox.critical(self, TITLE_ERROR, error_msg)
                    return
            
            # Merge all PDFs
            try:
                merger = PdfMerger()
                for pdf_path in pdf_paths:
                    merger.append(pdf_path)
                
                timestamp = get_timestamp()
                self.pdf_path = os.path.join(
                    output_dir,
                    f"{PDF_OUTPUT_PREFIX}{timestamp}{PDF_OUTPUT_SUFFIX}"
                )
                merger.write(self.pdf_path)
                merger.close()
                log_file_operation(self.logger, "PDF merged", self.pdf_path, True)
                
                # Clean up temporary PDFs
                for pdf_path in pdf_paths:
                    try:
                        os.remove(pdf_path)
                        log_file_operation(self.logger, "Temporary PDF removed", pdf_path, True)
                    except Exception as e:
                        self.logger.warning(f"Failed to remove temporary PDF {pdf_path}: {str(e)}")
                
                self.update_button_state()
                QMessageBox.information(self, TITLE_INFO, SUCCESS_IMAGE_TO_PDF)
                self.logger.info(f"Successfully created merged PDF: {self.pdf_path}")
                
            except Exception as e:
                error_msg = f"Failed to merge PDFs: {str(e)}"
                self.logger.error(error_msg)
                QMessageBox.critical(self, TITLE_ERROR, error_msg)
                return
                
        except Exception as e:
            error_msg = f"Unexpected error during conversion: {str(e)}"
            self.logger.error(error_msg)
            QMessageBox.critical(self, TITLE_ERROR, error_msg)
    
    def error(self, message: str):
        """
        Display error message.
        
        Args:
            message: Error message to display
        """
        QMessageBox.critical(self, TITLE_ERROR, message)


def main():
    """Main entry point for the GUI application."""
    try:
        myApp = QApplication(sys.argv)
        converter = ImageToPdfConverter()
        converter.show()
        sys.exit(myApp.exec())
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
