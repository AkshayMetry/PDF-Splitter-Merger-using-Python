import glob
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2

files = glob.glob("*.pdf")
files.sort() 
file1 = files[0]

x = file1.split(".pdf")
print(type(x))
print(x[0])


# pdf_reader = PdfFileReader(open("sample-pdf-with-images.pdf", "rb"))
# total_page = pdf_reader.getNumPages()
# pdf_writer = PdfFileWriter()
# for page in range(0,1):
#     pdf_writer.addPage(pdf_reader.getPage(page))

# with open("testpdf.pdf", 'wb') as out:
#     pdf_writer.write(out)

import time
from datetime import datetime

s= datetime.now()
timestamp = int(round(s.timestamp()))
print(type(timestamp))