import argparse
import os
import sys
from pdf2image import convert_from_path
import tempfile
import platform
from pathlib import Path
import easygui
from datetime import datetime
import time

def convert_to_jpeg(pdf_to_jpeg_path):
    try:
        output = str(os.path.dirname(pdf_to_jpeg_path))
        tempdir = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
        pages = convert_from_path(pdf_to_jpeg_path, output_folder=tempdir, fmt="jpeg")
        print("Processing...Please Wait...")
        for index, page in enumerate(pages):
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
            page.save(f"Converted-PDF-page{dt_string}.jpeg", "JPEG")
        easygui.msgbox("PDF file converted Successfully \nAll Images available in main folder \n\n\n\n--PDF TO Image TOOL--\n--POWERED BY PYTHON--\n-- Created By WAEL SAHLI--\n Last update was 09-13-2023", title="Done")    
    except Exception as e:
        easygui.msgbox(f"Sorry An Error Occured !\n{str(e)}", title="Error")

def main():
    parser = argparse.ArgumentParser(description='List the content')
    parser.add_argument('PDFtoJPEG_path',metavar='PDFtoJPEG_path',type=str,help='PDFtoJPEG_path')
    args = parser.parse_args()
    pdf_to_jpeg_path = args.PDFtoJPEG_path
    convert_to_jpeg(pdf_to_jpeg_path)

if __name__ == "__main__":
    main()

