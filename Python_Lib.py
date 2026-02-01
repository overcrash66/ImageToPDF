import fitz  # PyMuPDF
import easygui
from datetime import datetime
import os
import argparse

def convert_to_jpeg(pdf_to_jpeg_path: str) -> None:
    """Converts a PDF file to JPEG images using PyMuPDF."""
    try:
        doc = fitz.open(pdf_to_jpeg_path)
        print("Processing... Please Wait...")
        
        for page_index in range(len(doc)):
            page = doc.load_page(page_index)
            pix = page.get_pixmap()
            
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
            output_filename = f"Converted-PDF-page{page_index + 1}_{dt_string}.jpeg"
            
            pix.save(output_filename)
            print(f"Saved: {output_filename}")
            
        doc.close()
        easygui.msgbox("PDF file converted Successfully\nAll Images available in main folder\n\n\n\n--PDF TO Image TOOL--\n--POWERED BY PYTHON--\n-- Created By WAEL SAHLI--\n Last update was 01-23-2026", title="Done")
    except Exception as e:
        print(f"Error occurred: {e}")
        easygui.msgbox(f"Sorry An Error Occured!\n{str(e)}", title="Error")

def main():
    parser = argparse.ArgumentParser(description='List the content')
    parser.add_argument('PDFtoJPEG_path',metavar='PDFtoJPEG_path',type=str,help='PDFtoJPEG_path')
    args = parser.parse_args()
    pdf_to_jpeg_path = args.PDFtoJPEG_path
    convert_to_jpeg(pdf_to_jpeg_path)

if __name__ == "__main__":
    main()

