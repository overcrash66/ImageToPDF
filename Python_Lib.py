import argparse
import os, sys
from pdf2image import convert_from_path
import tempfile
import platform
from pathlib import Path
import easygui
from datetime import datetime
import time

#os.system("mode con cols=40 lines=40")
#os.system('color 02')

def ConvertToJpeg(PDFtoJPEG_path):
	try:
		output= str(os.path.dirname(PDFtoJPEG_path))
		tempdir = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
		pages = convert_from_path(PDFtoJPEG_path, output_folder=tempdir, fmt="jpeg")
		print("Processing...Please Wait...")
		for page in pages:
			now = datetime.now()
			dt_string = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
			#page.save("%s-page%d.jpeg" % (output,pages.index(page)), "JPEG")
			page.save("Converted-PDF-page"+dt_string+".jpeg", "JPEG")
		easygui.msgbox("PDF file converted Successfully \nAll Images available in main folder \n\n\n\n--PDF TO Image TOOL--\n--POWERED BY PYTHON--\n--Created By WAEL SAHLI--\n 2021", title="Done")	
	except Exception as e:
		easygui.msgbox("Sorry An Error Occured !\n"+str(e), title="Error")
		#os.system('pause')
		
my_parser = argparse.ArgumentParser(description='List the content')
my_parser.add_argument('PDFtoJPEG_path',metavar='PDFtoJPEG_path',type=str,help='PDFtoJPEG_path')
args = my_parser.parse_args()
PDFtoJPEG_path = args.PDFtoJPEG_path
ConvertToJpeg(PDFtoJPEG_path) 

