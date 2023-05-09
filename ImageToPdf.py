#Created By Wael SAHLI
#9/16/2021

from PySide6.QtWidgets import QFileDialog,QWidget, QLabel,QPushButton,QApplication,QMainWindow,QHBoxLayout,QVBoxLayout,QMessageBox
import sys,os,subprocess
from PIL import	 Image
from PyPDF2 import PdfFileMerger, PdfFileReader
from PySide6.QtGui import QPixmap,QFont
from PySide6 import QtCore
from datetime import datetime
import time

CREATE_NO_WINDOW = 0x08000000

class JpegToPdf(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("ImageToPdf")
		#self.setMinimumHeight(800)
		#self.setMinimumWidth(400)
		#self.showFullScreen()
		#self.showMaximized()
		self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint)
		self.qv_box=QVBoxLayout()
		self.qh_box = QHBoxLayout()
		self.w = QWidget()
		self.w.setLayout(self.qv_box)
		self.setCentralWidget(self.w)
		self.setObjectName("myWidget")
		self.setStyleSheet("#myWidget {background-color:#002633;}") 
		self.show()

		#Buttons ......
		self.button_1=QPushButton("Image1")
		self.button_1.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_1.clicked.connect(lambda :self.button_clicked(self.button_1))
		self.button_2 = QPushButton("Image2")
		self.button_2.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_2.clicked.connect(lambda: self.button_clicked(self.button_2))
		self.button_3 = QPushButton("Image3")
		self.button_3.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_3.clicked.connect(lambda: self.button_clicked(self.button_3))
		self.button_4 = QPushButton("Image4")
		self.button_4.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_4.clicked.connect(lambda: self.button_clicked(self.button_4))
		self.button_5 = QPushButton("Image5")
		self.button_5.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_5.clicked.connect(lambda: self.button_clicked(self.button_5))
		self.button_6 = QPushButton("Image6")
		self.button_6.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_6.clicked.connect(lambda: self.button_clicked(self.button_6))
		self.button_7 = QPushButton("Image7")
		self.button_7.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_7.clicked.connect(lambda: self.button_clicked(self.button_7))
		self.button_8 = QPushButton("Image8")
		self.button_8.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_8.clicked.connect(lambda: self.button_clicked(self.button_8))
		self.button_9 = QPushButton("Image9")
		self.button_9.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_9.clicked.connect(lambda: self.button_clicked(self.button_9))
		self.button_10 = QPushButton("Image10")
		self.button_10.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_10.clicked.connect(lambda: self.button_clicked(self.button_10))
		self.button_11 = QPushButton("Image11")
		self.button_11.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_11.clicked.connect(lambda: self.button_clicked(self.button_11))
		self.button_12 = QPushButton("Image12")
		self.button_12.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_12.clicked.connect(lambda: self.button_clicked(self.button_12))
		self.button_start = QPushButton("Convert To PDF")
		self.button_start.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_open_dir=QPushButton("Clear All Selection")
		self.button_open_dir.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_open_dir.clicked.connect(lambda:self.clear())
		self.button_pdf_ToImage=QPushButton("Convert PDF To JPEG")
		self.button_pdf_ToImage.setFont(QFont('Times', 10, weight=QFont.Bold))
		self.button_pdf_ToImage.clicked.connect(lambda: self.button_PDF_To_JPEG_clicked(self.button_pdf_ToImage))
		
		#Btn colors
		self.button_1.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_2.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_3.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_4.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_5.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_6.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_7.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_8.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_9.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_10.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_11.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_12.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		
		#Labels.......
		self.button_1_label=QLabel()
		self.button_2_label = QLabel()
		self.button_3_label = QLabel()
		self.button_4_label = QLabel()
		self.button_5_label = QLabel()
		self.button_6_label = QLabel()
		self.button_7_label = QLabel()
		self.button_8_label = QLabel()
		self.button_9_label = QLabel()
		self.button_10_label = QLabel()
		self.button_11_label = QLabel()
		self.button_12_label = QLabel()
		
		self.button_start_label = QLabel()		
		self.button_start.clicked.connect(self.start)
		self.qv_box.addWidget(self.button_1)
		self.qv_box.addWidget(self.button_1_label)
		self.qv_box.addWidget(self.button_2)
		self.qv_box.addWidget(self.button_2_label)
		self.qv_box.addWidget(self.button_3)
		self.qv_box.addWidget(self.button_3_label)	
		self.qv_box.addWidget(self.button_4)
		self.qv_box.addWidget(self.button_4_label)		
		self.qv_box.addWidget(self.button_5)
		self.qv_box.addWidget(self.button_5_label)		
		self.qv_box.addWidget(self.button_6)
		self.qv_box.addWidget(self.button_6_label)	
		self.qv_box.addWidget(self.button_7)
		self.qv_box.addWidget(self.button_7_label)		
		self.qv_box.addWidget(self.button_8)
		self.qv_box.addWidget(self.button_8_label)		
		self.qv_box.addWidget(self.button_9)
		self.qv_box.addWidget(self.button_9_label)		
		self.qv_box.addWidget(self.button_10)
		self.qv_box.addWidget(self.button_10_label)		
		self.qv_box.addWidget(self.button_11)
		self.qv_box.addWidget(self.button_11_label)		
		self.qv_box.addWidget(self.button_12)
		self.qv_box.addWidget(self.button_12_label)
		self.qv_box.addWidget(self.button_start)
		self.qv_box.addWidget(self.button_start_label)
		self.button_start.setEnabled(False)
		self.qh_box.addWidget(self.button_open_dir)
		self.button_open_dir.setEnabled(False)
		self.qh_box.addWidget(self.button_pdf_ToImage)
		self.qv_box.addLayout(self.qh_box)
		
		#label color
		self.button_1_label.setStyleSheet('color: white;')
		self.button_2_label.setStyleSheet('color: white;')
		self.button_3_label.setStyleSheet('color: white;')
		self.button_4_label.setStyleSheet('color: white;')
		self.button_5_label.setStyleSheet('color: white;')
		self.button_6_label.setStyleSheet('color: white;')
		self.button_7_label.setStyleSheet('color: white;')
		self.button_8_label.setStyleSheet('color: white;')
		self.button_9_label.setStyleSheet('color: white;')
		self.button_10_label.setStyleSheet('color: white;')
		self.button_11_label.setStyleSheet('color: white;')
		self.button_12_label.setStyleSheet('color: white;')
		
	def button_PDF_To_JPEG_clicked(self,c):
		self.PDFtoJPEG_path = QFileDialog.getOpenFileName(self, 'Open file', 
		 '',"PDF files (*.pdf)") 
		if c.text()=="Convert PDF To JPEG":
			self.PDFtoJPEG_path=self.PDFtoJPEG_path[0]
			try:
				subprocess.Popen('Python_Lib.exe'+' '+'"'+self.PDFtoJPEG_path+'"', creationflags=CREATE_NO_WINDOW)
				#os.system('Python_Lib.py'+' '+'"'+self.PDFtoJPEG_path+'"')
				self.button_pdf_ToImage.setEnabled(False)
				self.button_open_dir.setEnabled(True)
			except Exception as e:
				self.error(str(e))
	
	def SetMode(self):
		self.button_open_dir.setEnabled(True)
		self.button_start.setEnabled(True)
		self.button_pdf_ToImage.setEnabled(False)

	def button_clicked(self,b):
		self.image_path = QFileDialog.getOpenFileName(self, 'Open file', 
		 '',"Image files (*.jpeg *.jpg *.png)") 
		
		if b.text()=="Image1":
			self.image_1_path=self.image_path[0]
			if self.image_1_path != '':
				self.button_1_label.setText("Selected Image is : "+os.path.basename(self.image_1_path))
				self.button_1.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()

		elif b.text()=="Image2":
			self.image_2_path=self.image_path[0]
			if self.image_2_path != '':
				self.button_2_label.setText("Selected Image is : " + os.path.basename(self.image_2_path))
				self.button_2.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()

		elif b.text()=="Image3":
			self.image_3_path=self.image_path[0]
			if self.image_3_path != '':
				self.button_3_label.setText("Selected Image is : " + os.path.basename(self.image_3_path))
				self.button_3.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image4":
			self.image_4_path=self.image_path[0]
			if self.image_4_path != '':
				self.button_4_label.setText("Selected Image is : " + os.path.basename(self.image_4_path))
				self.button_4.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image5":
			self.image_5_path=self.image_path[0]
			if self.image_5_path != '':
				self.button_5_label.setText("Selected Image is : " + os.path.basename(self.image_5_path))
				self.button_5.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image6":
			self.image_6_path=self.image_path[0]
			if self.image_6_path != '':
				self.button_6_label.setText("Selected Image is : " + os.path.basename(self.image_6_path))
				self.button_6.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image7":
			self.image_7_path=self.image_path[0]
			if self.image_7_path != '':
				self.button_7_label.setText("Selected Image is : " + os.path.basename(self.image_7_path))
				self.button_7.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image8":
			self.image_8_path=self.image_path[0]
			if self.image_8_path != '':
				self.button_8_label.setText("Selected Image is : " + os.path.basename(self.image_8_path))
				self.button_8.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image9":
			self.image_9_path=self.image_path[0]
			if self.image_9_path != '':
				self.button_9_label.setText("Selected Image is : " + os.path.basename(self.image_9_path))
				self.button_9.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image10":
			self.image_10_path=self.image_path[0]
			if self.image_10_path != '':
				self.button_10_label.setText("Selected Image is : " + os.path.basename(self.image_10_path))
				self.button_10.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image11":
			self.image_11_path=self.image_path[0]
			if self.image_11_path != '':
				self.button_11_label.setText("Selected Image is : " + os.path.basename(self.image_11_path))
				self.button_11.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
			
		elif b.text()=="Image12":
			self.image_12_path=self.image_path[0]
			if self.image_12_path != '':
				self.button_12_label.setText("Selected Image is : " + os.path.basename(self.image_12_path))	
				self.button_12.setStyleSheet('QPushButton {background-color: #B2D17C; color: black;}')
				self.SetMode()
	
	def start(self):
		if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.image_1_path == self.image_2_path:
			self.doNotAllow()	
		elif self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.image_2_path == self.image_3_path:
			self.doNotAllow()
		elif self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.image_3_path == self.image_4_path:
			self.doNotAllow()
		elif self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.image_4_path == self.image_5_path:
			self.doNotAllow()
		elif self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.image_5_path == self.image_6_path:
			self.doNotAllow()
		elif self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.image_6_path == self.image_7_path:
			self.doNotAllow()
		elif self.button_7_label.text() != '' and self.button_8_label.text() != '' and self.image_7_path == self.image_9_path:
			self.doNotAllow()
		elif self.button_8_label.text() != '' and self.button_9_label.text() != '' and self.image_8_path == self.image_9_path:
			self.doNotAllow()
		elif self.button_9_label.text() != '' and self.button_10_label.text() != '' and self.image_9_path == self.image_10_path:
			self.doNotAllow()	
		elif self.button_10_label.text() != '' and self.button_11_label.text() != '' and self.image_10_path == self.image_11_path:
			self.doNotAllow()
		elif self.button_11_label.text() != '' and self.button_12_label.text() != '' and self.image_11_path == self.image_12_path:
			self.doNotAllow()	
		else:
			self.startCon()

	def startCon(self):
		if self.button_1_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_1_path)
			if file_extension =='.jpeg':
				#self.image_1_path = self.image_1_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_1_path, self.image_1_path[:-4]+'.jpeg')
					self.image_1_path = self.image_1_path[:-4]+'.jpeg'
				except:
					pass
		
		if self.button_2_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_2_path)
			if file_extension =='.jpeg':
				#self.image_2_path = self.image_2_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_2_path, self.image_2_path[:-4]+'.jpeg')
					self.image_2_path = self.image_2_path[:-4]+'.jpeg'
				except:
					pass	
		
		if self.button_3_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_3_path)
			if file_extension =='.jpeg':
				#self.image_3_path = self.image_3_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_3_path, self.image_3_path[:-4]+'.jpeg')
					self.image_3_path = self.image_3_path[:-4]+'.jpeg'
				except:
					pass	
		
		if self.button_4_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_4_path)
			if file_extension =='.jpeg':
				#self.image_4_path = self.image_4_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_4_path, self.image_4_path[:-4]+'.jpeg')
					self.image_4_path = self.image_4_path[:-4]+'.jpeg'
				except:
					pass	
		
		if self.button_5_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_5_path)
			if file_extension =='.jpeg':
				#self.image_5_path = self.image_5_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_5_path, self.image_5_path[:-4]+'.jpeg')
					self.image_5_path = self.image_5_path[:-4]+'.jpeg'
				except:
					pass	
		
		if self.button_6_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_6_path)
			if file_extension =='.jpeg':
				#self.image_6_path = self.image_6_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_6_path, self.image_6_path[:-4]+'.jpeg')
					self.image_6_path = self.image_6_path[:-4]+'.jpeg'
				except:
					pass
					
		if self.button_7_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_7_path)
			if file_extension =='.jpeg':
				#self.image_7_path = self.image_7_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_7_path, self.image_7_path[:-4]+'.jpeg')
					self.image_7_path = self.image_7_path[:-4]+'.jpeg'
				except:
					pass	
		
		if self.button_8_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_8_path)
			if file_extension =='.jpeg':
				#self.image_8_path = self.image_8_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_8_path, self.image_8_path[:-4]+'.jpeg')
					self.image_8_path = self.image_8_path[:-4]+'.jpeg'
				except:
					pass	
		
		if self.button_9_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_9_path)
			if file_extension =='.jpeg':
				#self.image_9_path = self.image_9_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_9_path, self.image_9_path[:-4]+'.jpeg')
					self.image_9_path = self.image_9_path[:-4]+'.jpeg'
				except:
					pass
		
		if self.button_10_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_10_path)
			if file_extension =='.jpeg':
				#self.image_10_path = self.image_10_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_10_path, self.image_10_path[:-4]+'.jpeg')
					self.image_10_path = self.image_10_path[:-4]+'.jpeg'
				except:
					pass
					
		if self.button_11_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_11_path)
			if file_extension =='.jpeg':
				#self.image_11_path = self.image_11_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_11_path, self.image_11_path[:-4]+'.jpeg')
					self.image_11_path = self.image_11_path[:-4]+'.jpeg'
				except:
					pass
					
		if self.button_12_label.text() != '':
			file_name, file_extension = os.path.splitext(self.image_12_path)
			if file_extension =='.jpeg':
				#self.image_12_path = self.image_12_path[:-4]+'.jpeg'
				pass
			else:
				try:
					os.rename(self.image_12_path, self.image_12_path[:-4]+'.jpeg')
					self.image_12_path = self.image_12_path[:-4]+'.jpeg'
				except:
					pass
		
			
		self.run()		
			
	def run(self):
		try:
			merger = PdfFileMerger()
			now = datetime.now()
			dt_string = now.strftime("%d-%m-%Y_%H-%M-%S-%f")
			
			#1 image selected
			if self.button_1_label.text() != '' and self.button_2_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),os.path.basename(self.image_1_path))[:-4] + "pdf"
				im1.save(self.pdf_1_path)
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str("Merged pdf of "+str(os.path.basename(self.pdf_1_path))[:-4]+".pdf"))
				merger.write(self.pdf_path)	
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass
			
			#2 images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#3 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
					
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass	
				
			#4 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))		
					
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+".pdf")
				merger.write(self.pdf_path)	
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass
			
			#5 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
					
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+".pdf")
				merger.write(self.pdf_path)															
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass
					
			#6 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#7 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.button_8_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				image7 = Image.open(self.image_7_path)
				im7 = image7.convert('RGB')
				self.pdf_7_path = os.path.join(os.path.dirname(self.image_7_path),
										   str(os.path.basename(self.image_7_path))[:-4] + "pdf")
				im7.save(self.pdf_7_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				with open(self.pdf_7_path,'rb') as pdf7:
					merger.append(PdfFileReader(pdf7))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+" "+str(os.path.basename(self.pdf_7_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#8 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.button_8_label.text() != '' and self.button_9_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				image7 = Image.open(self.image_7_path)
				im7 = image7.convert('RGB')
				self.pdf_7_path = os.path.join(os.path.dirname(self.image_7_path),
										   str(os.path.basename(self.image_7_path))[:-4] + "pdf")
				im7.save(self.pdf_7_path)
				
				image8 = Image.open(self.image_8_path)
				im8 = image8.convert('RGB')
				self.pdf_8_path = os.path.join(os.path.dirname(self.image_8_path),
										   str(os.path.basename(self.image_8_path))[:-4] + "pdf")
				im8.save(self.pdf_8_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				with open(self.pdf_7_path,'rb') as pdf7:
					merger.append(PdfFileReader(pdf7))
				
				with open(self.pdf_8_path,'rb') as pdf8:
					merger.append(PdfFileReader(pdf8))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+" "+str(os.path.basename(self.pdf_7_path))[:-4]+" "+str(os.path.basename(self.pdf_8_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#9 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.button_8_label.text() != '' and self.button_9_label.text() != '' and self.button_10_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				image7 = Image.open(self.image_7_path)
				im7 = image7.convert('RGB')
				self.pdf_7_path = os.path.join(os.path.dirname(self.image_7_path),
										   str(os.path.basename(self.image_7_path))[:-4] + "pdf")
				im7.save(self.pdf_7_path)
				
				image8 = Image.open(self.image_8_path)
				im8 = image8.convert('RGB')
				self.pdf_8_path = os.path.join(os.path.dirname(self.image_8_path),
										   str(os.path.basename(self.image_8_path))[:-4] + "pdf")
				im8.save(self.pdf_8_path)
				
				image9 = Image.open(self.image_9_path)
				im9 = image9.convert('RGB')
				self.pdf_9_path = os.path.join(os.path.dirname(self.image_9_path),
										   str(os.path.basename(self.image_9_path))[:-4] + "pdf")
				im9.save(self.pdf_9_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				with open(self.pdf_7_path,'rb') as pdf7:
					merger.append(PdfFileReader(pdf7))
				
				with open(self.pdf_8_path,'rb') as pdf8:
					merger.append(PdfFileReader(pdf8))
				
				with open(self.pdf_9_path,'rb') as pdf9:
					merger.append(PdfFileReader(pdf9))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+" "+str(os.path.basename(self.pdf_7_path))[:-4]+" "+str(os.path.basename(self.pdf_8_path))[:-4]+" "+str(os.path.basename(self.pdf_9_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#10 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.button_8_label.text() != '' and self.button_9_label.text() != '' and self.button_10_label.text() != '' and self.button_11_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				image7 = Image.open(self.image_7_path)
				im7 = image7.convert('RGB')
				self.pdf_7_path = os.path.join(os.path.dirname(self.image_7_path),
										   str(os.path.basename(self.image_7_path))[:-4] + "pdf")
				im7.save(self.pdf_7_path)
				
				image8 = Image.open(self.image_8_path)
				im8 = image8.convert('RGB')
				self.pdf_8_path = os.path.join(os.path.dirname(self.image_8_path),
										   str(os.path.basename(self.image_8_path))[:-4] + "pdf")
				im8.save(self.pdf_8_path)
				
				image9 = Image.open(self.image_9_path)
				im9 = image9.convert('RGB')
				self.pdf_9_path = os.path.join(os.path.dirname(self.image_9_path),
										   str(os.path.basename(self.image_9_path))[:-4] + "pdf")
				im9.save(self.pdf_9_path)
				
				image10 = Image.open(self.image_10_path)
				im10 = image10.convert('RGB')
				self.pdf_10_path = os.path.join(os.path.dirname(self.image_10_path),
										   str(os.path.basename(self.image_10_path))[:-4] + "pdf")
				im10.save(self.pdf_10_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				with open(self.pdf_7_path,'rb') as pdf7:
					merger.append(PdfFileReader(pdf7))
				
				with open(self.pdf_8_path,'rb') as pdf8:
					merger.append(PdfFileReader(pdf8))
				
				with open(self.pdf_9_path,'rb') as pdf9:
					merger.append(PdfFileReader(pdf9))
				
				with open(self.pdf_10_path,'rb') as pdf10:
					merger.append(PdfFileReader(pdf10))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+" "+str(os.path.basename(self.pdf_7_path))[:-4]+" "+str(os.path.basename(self.pdf_8_path))[:-4]+" "+str(os.path.basename(self.pdf_9_path))[:-4]+" "+str(os.path.basename(self.pdf_10_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#11 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.button_8_label.text() != '' and self.button_9_label.text() != '' and self.button_10_label.text() != '' and self.button_11_label.text() != '' and self.button_12_label.text() == '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				image7 = Image.open(self.image_7_path)
				im7 = image7.convert('RGB')
				self.pdf_7_path = os.path.join(os.path.dirname(self.image_7_path),
										   str(os.path.basename(self.image_7_path))[:-4] + "pdf")
				im7.save(self.pdf_7_path)
				
				image8 = Image.open(self.image_8_path)
				im8 = image8.convert('RGB')
				self.pdf_8_path = os.path.join(os.path.dirname(self.image_8_path),
										   str(os.path.basename(self.image_8_path))[:-4] + "pdf")
				im8.save(self.pdf_8_path)
				
				image9 = Image.open(self.image_9_path)
				im9 = image9.convert('RGB')
				self.pdf_9_path = os.path.join(os.path.dirname(self.image_9_path),
										   str(os.path.basename(self.image_9_path))[:-4] + "pdf")
				im9.save(self.pdf_9_path)
				
				image10 = Image.open(self.image_10_path)
				im10 = image10.convert('RGB')
				self.pdf_10_path = os.path.join(os.path.dirname(self.image_10_path),
										   str(os.path.basename(self.image_10_path))[:-4] + "pdf")
				im10.save(self.pdf_10_path)
				
				image11 = Image.open(self.image_11_path)
				im11 = image11.convert('RGB')
				self.pdf_11_path = os.path.join(os.path.dirname(self.image_11_path),
										   str(os.path.basename(self.image_11_path))[:-4] + "pdf")
				im11.save(self.pdf_11_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				with open(self.pdf_7_path,'rb') as pdf7:
					merger.append(PdfFileReader(pdf7))
				
				with open(self.pdf_8_path,'rb') as pdf8:
					merger.append(PdfFileReader(pdf8))
				
				with open(self.pdf_9_path,'rb') as pdf9:
					merger.append(PdfFileReader(pdf9))
				
				with open(self.pdf_10_path,'rb') as pdf10:
					merger.append(PdfFileReader(pdf10))
				
				with open(self.pdf_11_path,'rb') as pdf11:
					merger.append(PdfFileReader(pdf11))
				
				self.pdf_path=os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+" "+str(os.path.basename(self.pdf_7_path))[:-4]+" "+str(os.path.basename(self.pdf_8_path))[:-4]+" "+str(os.path.basename(self.pdf_9_path))[:-4]+" "+str(os.path.basename(self.pdf_10_path))[:-4]+" "+str(os.path.basename(self.pdf_11_path))[:-4]+".pdf")
				merger.write(self.pdf_path)														
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass

			#12 Images selected
			if self.button_1_label.text() != '' and self.button_2_label.text() != '' and self.button_3_label.text() != '' and self.button_4_label.text() != '' and self.button_5_label.text() != '' and self.button_6_label.text() != '' and self.button_7_label.text() != '' and self.button_8_label.text() != '' and self.button_9_label.text() != '' and self.button_10_label.text() != '' and self.button_11_label.text() != '' and self.button_12_label.text() != '':
				image1 = Image.open(self.image_1_path)
				im1 = image1.convert('RGB')
				self.pdf_1_path = os.path.join(os.path.dirname(self.image_1_path),
										   str(os.path.basename(self.image_1_path))[:-4] + "pdf")
				im1.save(self.pdf_1_path)
				
				image2 = Image.open(self.image_2_path)
				im2 = image2.convert('RGB')
				self.pdf_2_path = os.path.join(os.path.dirname(self.image_2_path),
										   str(os.path.basename(self.image_2_path))[:-4] + "pdf")
				im2.save(self.pdf_2_path)
				
				image3 = Image.open(self.image_3_path)
				im3 = image3.convert('RGB')
				self.pdf_3_path = os.path.join(os.path.dirname(self.image_3_path),
										   str(os.path.basename(self.image_3_path))[:-4] + "pdf")
				im3.save(self.pdf_3_path)
				
				image4 = Image.open(self.image_4_path)
				im4 = image4.convert('RGB')
				self.pdf_4_path = os.path.join(os.path.dirname(self.image_4_path),
										   str(os.path.basename(self.image_4_path))[:-4] + "pdf")
				im4.save(self.pdf_4_path)
				
				image5 = Image.open(self.image_5_path)
				im5 = image5.convert('RGB')
				self.pdf_5_path = os.path.join(os.path.dirname(self.image_5_path),
										   str(os.path.basename(self.image_5_path))[:-4] + "pdf")
				im5.save(self.pdf_5_path)
				
				image6 = Image.open(self.image_6_path)
				im6 = image6.convert('RGB')
				self.pdf_6_path = os.path.join(os.path.dirname(self.image_6_path),
										   str(os.path.basename(self.image_6_path))[:-4] + "pdf")
				im6.save(self.pdf_6_path)
				
				image7 = Image.open(self.image_7_path)
				im7 = image7.convert('RGB')
				self.pdf_7_path = os.path.join(os.path.dirname(self.image_7_path),
										   str(os.path.basename(self.image_7_path))[:-4] + "pdf")
				im7.save(self.pdf_7_path)
				
				image8 = Image.open(self.image_8_path)
				im8 = image8.convert('RGB')
				self.pdf_8_path = os.path.join(os.path.dirname(self.image_8_path),
										   str(os.path.basename(self.image_8_path))[:-4] + "pdf")
				im8.save(self.pdf_8_path)
				
				image9 = Image.open(self.image_9_path)
				im9 = image9.convert('RGB')
				self.pdf_9_path = os.path.join(os.path.dirname(self.image_9_path),
										   str(os.path.basename(self.image_9_path))[:-4] + "pdf")
				im9.save(self.pdf_9_path)
				
				image10 = Image.open(self.image_10_path)
				im10 = image10.convert('RGB')
				self.pdf_10_path = os.path.join(os.path.dirname(self.image_10_path),
										   str(os.path.basename(self.image_10_path))[:-4] + "pdf")
				im10.save(self.pdf_10_path)
				
				image11 = Image.open(self.image_11_path)
				im11 = image11.convert('RGB')
				self.pdf_11_path = os.path.join(os.path.dirname(self.image_11_path),
										   str(os.path.basename(self.image_11_path))[:-4] + "pdf")
				im11.save(self.pdf_11_path)
				
				image12 = Image.open(self.image_12_path)
				im12 = image12.convert('RGB')
				self.pdf_12_path = os.path.join(os.path.dirname(self.image_12_path),
										   str(os.path.basename(self.image_12_path))[:-4] + "pdf")
				im12.save(self.pdf_12_path)
				
				with open(self.pdf_1_path,'rb') as pdf1:
					merger.append(PdfFileReader(pdf1))
					
				with open(self.pdf_2_path,'rb') as pdf2:
					merger.append(PdfFileReader(pdf2))
					
				with open(self.pdf_3_path,'rb') as pdf3:
					merger.append(PdfFileReader(pdf3))	
				
				with open(self.pdf_4_path,'rb') as pdf4:
					merger.append(PdfFileReader(pdf4))	
				
				with open(self.pdf_5_path,'rb') as pdf5:
					merger.append(PdfFileReader(pdf5))
				
				with open(self.pdf_6_path,'rb') as pdf6:
					merger.append(PdfFileReader(pdf6))
				
				with open(self.pdf_7_path,'rb') as pdf7:
					merger.append(PdfFileReader(pdf7))
				
				with open(self.pdf_8_path,'rb') as pdf8:
					merger.append(PdfFileReader(pdf8))
				
				with open(self.pdf_9_path,'rb') as pdf9:
					merger.append(PdfFileReader(pdf9))
				
				with open(self.pdf_10_path,'rb') as pdf10:
					merger.append(PdfFileReader(pdf10))
				
				with open(self.pdf_11_path,'rb') as pdf11:
					merger.append(PdfFileReader(pdf11))
				
				with open(self.pdf_12_path,'rb') as pdf12:
					merger.append(PdfFileReader(pdf12))
				
				self.pdf_path = os.path.join(os.path.dirname(self.pdf_1_path),str(os.path.basename(self.pdf_1_path))[:-4]+" "+str(os.path.basename(self.pdf_2_path))[:-4]+" "+str(os.path.basename(self.pdf_3_path))[:-4]+" "+str(os.path.basename(self.pdf_4_path))[:-4]+" "+str(os.path.basename(self.pdf_5_path))[:-4]+" "+str(os.path.basename(self.pdf_6_path))[:-4]+" "+str(os.path.basename(self.pdf_7_path))[:-4]+" "+str(os.path.basename(self.pdf_8_path))[:-4]+" "+str(os.path.basename(self.pdf_9_path))[:-4]+" "+str(os.path.basename(self.pdf_10_path))[:-4]+" "+str(os.path.basename(self.pdf_11_path))[:-4]+" "+str(os.path.basename(self.pdf_12_path))[:-4]+".pdf")
				merger.write(self.pdf_path)
				NewName = ("Merged PDF"+dt_string+".pdf")
				try:
					os.rename(self.pdf_path, NewName)
				except:
					pass	
				
		except Exception as e:
			self.error(str(e))
			pass
		
		merger.close()
		self.wael()
		
		try:
			os.remove(self.pdf_1_path)
			os.remove(self.pdf_2_path)
			os.remove(self.pdf_3_path)
			os.remove(self.pdf_4_path)
			os.remove(self.pdf_5_path)
			os.remove(self.pdf_6_path)
			os.remove(self.pdf_7_path)
			os.remove(self.pdf_8_path)
			os.remove(self.pdf_9_path)
			os.remove(self.pdf_10_path)
			os.remove(self.pdf_11_path)
			os.remove(self.pdf_12_path)
		except:
			pass
		
		self.button_open_dir.setEnabled(True)
		self.button_pdf_ToImage.setEnabled(True)
		
	def wael(self):
		error_message = QMessageBox()
		error_message.setFixedWidth(400)
		error_message.setWindowTitle("Done!")
		error_message.setText("PDF file converted Successfully \nPDF File available in main folder \n\n\n\n--Image To PDF Tool--\n--Powered By Python--\n--Created By Wael SAHLI--\n 2021")
		error_message.exec()
		
	def error(self,e):
		error_message = QMessageBox()
		error_message.setFixedWidth(400)
		error_message.setWindowTitle("Error!")
		error_message.setText(e)
		error_message.exec()	
	
	def doNotAllow(self):
		self.clear()
		error_message = QMessageBox()
		error_message.setFixedWidth(400)
		error_message.setWindowTitle("Error!")
		error_message.setText("This Action is not supported! Please select different files.")
		error_message.exec()	
	
	def clear(self):	
		self.button_1_label.setText("")
		self.button_2_label.setText("")
		self.button_3_label.setText("")
		self.button_4_label.setText("")
		self.button_5_label.setText("")
		self.button_6_label.setText("")
		self.button_7_label.setText("")
		self.button_8_label.setText("")
		self.button_9_label.setText("")
		self.button_10_label.setText("")
		self.button_11_label.setText("")
		self.button_12_label.setText("")
		self.button_12_label.setText("")
		self.button_start.setEnabled(False)
		self.button_open_dir.setEnabled(False)
		self.button_pdf_ToImage.setEnabled(True)
		#Btn colors
		self.button_1.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_2.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_3.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_4.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_5.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_6.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_7.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_8.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_9.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_10.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_11.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		self.button_12.setStyleSheet('QPushButton {background-color: #007399; color: white;}')
		
myApp= QApplication(sys.argv)
jpeg_to_pdf=JpegToPdf()
sys.exit(myApp.exec())