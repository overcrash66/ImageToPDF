import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QFileDialog, QWidget, QLabel, QPushButton, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QMessageBox)
from PySide6.QtGui import QFont
from PySide6 import QtCore
from PyPDF2 import PdfMerger, PdfReader
from datetime import datetime
from PIL import Image

CREATE_NO_WINDOW = 0x08000000

class JpegToPdf(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ImageToPdf")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setStyleSheet("#myWidget {background-color:#002633;}")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.qv_box = QVBoxLayout(self.central_widget)
        self.qh_box = QHBoxLayout()

        self.buttons = [self.createButton(f"Image {i}") for i in range(1, 13)]
        self.labels = [QLabel() for _ in range(12)]

        for button in self.buttons:
            self.qv_box.addWidget(button)

        for label in self.labels:
            label.setStyleSheet('color: red;')
            self.qv_box.addWidget(label)

        self.button_start = self.createButton("Convert To PDF")
        self.button_start.setEnabled(False)
        self.button_open_dir = self.createButton("Clear All Selection")
        self.button_open_dir.setEnabled(False)
        self.button_pdf_to_image = self.createButton("Convert PDF To JPEG")
        self.button_image_to_pdf = self.createButton("Convert Images To PDF")

        self.qh_box.addWidget(self.button_open_dir)
        self.qh_box.addWidget(self.button_pdf_to_image)
        self.qh_box.addWidget(self.button_image_to_pdf)
        self.qv_box.addLayout(self.qh_box)

        self.pdf_merger = PdfMerger()
        self.image_paths = [""] * 12
        self.pdf_path = ""

        self.button_pdf_to_image.clicked.connect(self.convertPdfToJpeg)
        self.button_open_dir.clicked.connect(self.clearAllSelection)
        self.button_start.clicked.connect(self.convertImagesToPdf)
        self.button_image_to_pdf.clicked.connect(self.convertImagesToPdf)
        
    def createButton(self, text):
        button = QPushButton(text)
        button.setFont(QFont('Times', 10, weight=QFont.Bold))
        button.clicked.connect(self.buttonClicked)
        button.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
        return button

    def buttonClicked(self):
        button = self.sender()
        button_text = button.text()
        
        # Check if the button text can be converted to an integer
        try:
            image_number = int(button_text.split()[-1])
        except ValueError:
            image_number = None

        if image_number is not None:
            image_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Image files (*.jpeg *.jpg *.png)")
            if image_path:
                self.image_paths[image_number - 1] = image_path
                self.labels[image_number - 1].setText(f"Selected Image is: {os.path.basename(image_path)}")
                button.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
                self.updateButtonState()
        else:
            pass

    def updateButtonState(self):
        enabled = any(self.image_paths)
        self.button_start.setEnabled(enabled)
        self.button_open_dir.setEnabled(enabled)
        #self.button_image_to_pdf.setEnabled(enabled)


    def clearAllSelection(self):
        self.image_paths = [""] * 12
        for label in self.labels:
            label.clear()
        for button in self.buttons:
            button.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
        self.updateButtonState()

    def convertPdfToJpeg(self):
        file_dialog = QFileDialog(self, 'Open file', '', "PDF files (*.pdf)")
        pdf_path, _ = file_dialog.getOpenFileName()
        if pdf_path:
            try:
                subprocess.Popen([sys.executable, 'Python_Lib.py', pdf_path], creationflags=CREATE_NO_WINDOW)
            except Exception as e:
                self.error(str(e))

    def convertImagesToPdf(self):
        selected_images = [image_path for image_path in self.image_paths if image_path]
        if selected_images:
            try:
                merger = PdfMerger()
                pdf_paths = []

                for image_path in selected_images:
                    image = Image.open(image_path)
                    image = image.convert('RGB')
                    base_pdf_name = os.path.splitext(os.path.basename(image_path))[0]
                    pdf_path = base_pdf_name + ".pdf"

                    # Check if the PDF file with the same name exists
                    counter = 1
                    while os.path.exists(pdf_path):
                        pdf_path = f"{base_pdf_name}_{counter}.pdf"
                        counter += 1

                    image.save(pdf_path)
                    pdf_paths.append(pdf_path)

                for pdf_path in pdf_paths:
                    merger.append(pdf_path)

                self.pdf_path = os.path.join(
                    os.path.dirname(pdf_paths[0]),
                    f"Merged_PDF_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
                )
                merger.write(self.pdf_path)
                merger.close()

                for pdf_path in pdf_paths:
                    os.remove(pdf_path)

                self.updateButtonState()
                QMessageBox.information(self, "Info", "Images converted to PDF successfully.\nAll Images are available in main folder \n\n\n\n--Image2PDF TOOL--\n--POWERED BY PYTHON--\n-- Created By WAEL SAHLI--\n Last update was 01-23-2026")
            except Exception as e:
                self.error(str(e))
        else:
            QMessageBox.warning(self, "Warning", "Please select at least one image to convert to PDF.")

    def error(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    jpeg_to_pdf = JpegToPdf()
    jpeg_to_pdf.show()
    sys.exit(myApp.exec())
