import glob
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
from datetime import datetime

path = "C:\\Users\\aksha\\Desktop\\suven\\Project 2\\Spilt Pdfs"  

#--------------------PDF selection------------------------------
def select_pdf():
    files = glob.glob("*.pdf")
    files.sort()    
  
    print("No of PDFs:", len(files))
    print("----------------------------------") 
    for index,file in enumerate(files):
       print("{}.{}".format(index,file))
      
    
    print("----------------------------------")
    while True:
        try:
            _pdf = int(input("Select the pdf:"))
            if _pdf >= 0 and  _pdf < len(files):
                select_pdf = files[_pdf]
                print("Selected PDF:",select_pdf)   
                break
            else:
                print("Enter Valid Number")
                
        except ValueError:
            print("Type Positive Integer")
            
    return select_pdf


#-------------------Split---------------------------------------------
#pdf page no start form 0
#user input are decrementing by 1 to match the page no
def split_pdf():
    selected_pdf = select_pdf()
    # print(type(selected_pdf))
    x = selected_pdf.split(".pdf")
    y = x[0]

    pdf_reader = PdfFileReader(open(selected_pdf, "rb"))
    total_page = pdf_reader.getNumPages()

    if total_page == 1:
        print("PDF contain only 1")
    else:
        if selected_pdf:
            start = 0
            end = 0
            while True:
                try:
                    print("Number of Pages in PDF:",total_page)
                    page_number_start = int(input("Enter the Start Page:"))
                    page_number_end = int(input("Enter the End Page:"))
                
                
                    if page_number_start == 1 and page_number_end == total_page:
                        print("You are Spliting Whole Pdf")
                    elif page_number_start == total_page and page_number_end == 1:
                        print("Enter a valid number")
                    elif page_number_start <= start or page_number_end > total_page:
                        print("Enter a valid number")
                    elif page_number_start > total_page or page_number_end <= end:
                        print("Enter a valid number")
                    elif page_number_start == start and page_number_end == end:
                        print("Enter a valid number")
                    elif page_number_start == page_number_end:
                        start = page_number_start - 1
                        end = page_number_end 
                        print("Spliting PDF page no:{}".format(page_number_start))
                        break
                    else:
                        start = page_number_start - 1
                        end = page_number_end
                        print("Spliting Pdf from page no {} to {}".format(page_number_start,page_number_end))
                        # print(start, end)
                        break
                except ValueError:
                    print("Enter Positive Integer")

        pdf_writer = PdfFileWriter()
        for page in range(start,end):
            pdf_writer.addPage(pdf_reader.getPage(page))                
        
        if not os.path.exists(path):
            os.mkdir(path)
        

        output_filename = "{}_split_{} to {}.pdf".format(y,page_number_start,page_number_end)
        with open(os.path.join(path,output_filename), "wb") as file:
            pdf_writer.write(file)
   
#--------------------Merge-------------------------------------------
def merge_pdf():
    os.chdir(path)
    merge_list = []
   
    merge_pdf_1 = select_pdf()
    merge_list.append(merge_pdf_1)
    merge_pdf_2 = select_pdf()
    merge_list.append(merge_pdf_2)
    # index_list = select_pdf()
    more_pdf = ''
    while more_pdf != '2':
        print("1.Yes")
        print("2.No")
        more_pdf = input("Do you want to merge more pdf:")
        if more_pdf == "1":
            merge_more_pdf = select_pdf()
            merge_list.append(merge_more_pdf)
        elif more_pdf == '2':
            print("Thank You")
            break
        else:
            print("Prit Valid Option")

    
    currt_time= datetime.now()
    timestamp = int(round(currt_time.timestamp()))
    # print(select_pdf_1,select_pdf_2)
    merge_path = "C:\\Users\\aksha\\Desktop\\suven\\Project 2\\Merge Pdfs"
    mergeFile = PyPDF2.PdfFileMerger()
    for allpdf in merge_list:
        mergeFile.append(PyPDF2.PdfFileReader(allpdf, 'rb'))
    merge_filename = "Combined Pdf {}.pdf".format(timestamp)
    # mergeFile.write(merge_filename)
    if not os.path.exists(merge_path):
        os.mkdir(merge_path)
    
    # mergeFile.write("Combined Pdf {}".format(presentime))
    
    # with open(os.path.join(merge_path,merge_filename),"wb") as file_:
    # os.chdir(merge_path)
    
    with open(os.path.join(merge_path,merge_filename), "wb") as file:
        mergeFile.write(file)
   
    
   
#-----------------------Menu -----------------------------------
select_option = ''
while select_option != '3':
    print("1.Split PDF")
    print("2.Merge PDF")
    print("3.Exit")
    select_option = input("What Operation do want to Perform: ")

    if select_option == "1":
        split_pdf()
        input_ = ''
        while input_ != 'No':
            print("1.Yes")
            print("2.No")
            input_ = input("Do you want to split more PDFs: ")
            if input_ == '1':
                split_pdf()
            elif input_ == '2':
                print('Thank You')
                break
            else:
                print("Enter a valid option")
    elif select_option == "2":
        merge_pdf()
    elif select_option == "3":
        exit
    else:
        print("Enter a valid option")




