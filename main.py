import os
from tkinter import *
import os.path
from tkinter import filedialog
from tkinter.filedialog import askopenfilenames
import tkinter as tk
import re
import fitz
import sys
from PyPDF2 import PdfFileReader
import shutil

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
the_files = []

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path,relative_path)
def select_exam():

    directory = askopenfilenames(initialdir="/",title="Select Exam")
    for files1 in directory:
        the_files.append(files1)
    print(directory)
    print(the_files)
    if len(the_files) > 1:
        the_files.remove(the_files[0])
        the_files[-1] = the_files[0]
        print(f'{the_files}')

def examname():
    global hotname
    hotname = name1.get()
    donelabel = tk.Label(window,text="Name of Exam File was set!",bg='#FFD53D')
    name1.delete(0,'end')
    donelabel.pack()

def videosmerge():
    directorypath = filedialog.askdirectory()
    filepath = os.path.join(directorypath)
    print(f'zeb y {filepath}')
    #with open(f"{filepath}.mp4", "wb") as file:
    #    finale_files = list(file_names)
    #    print(finale_files)
    directory = the_files[0]
    input_file = directory
    output_file = rf"{filepath}\{hotname}.pdf"

    doc = PdfFileReader(open(directory, 'rb'))
    res = doc.getPage(0).mediaBox
    page_res = res[0:6]
    image_y = page_res[3:5]

    # insert extra page shit
    global coverpage
    if var.get() == 1:
        coverpage = resource_path('coveryear9.pdf')
    elif var.get() == 2:
        coverpage = resource_path('coverolevel.pdf')
    elif var.get() == 3:
        coverpage = resource_path('coveraslevel.pdf')
    elif var.get() == 4:
        coverpage = resource_path('covera2level.pdf')

    the_start_file = rf"{filepath}\{hotname}.pdf"
    the_final_file = rf"{filepath}\{hotname}.pdf"
    f = 0
    global thefirstfile
    thefirstfile = the_files[0]
    shutil.copyfile(thefirstfile, rf'{thefirstfile}{14}')
    while f < 2:
        for i in image_y:
            final_y = i
        for i in image_y:
            under_final_y = i
        for i in image_y:
            finale_y = i
        for i in image_y:
            finale_question = i

        final_y = (final_y * 667) / 10000
        final_y_under = (under_final_y * 1973) / 1000
        final_line = (under_final_y * 1698) / 1000
        finale_question_line = (finale_question * 1924) / 1000
        wierd_constant = 611
        pages_list = []
        deleted_pages = []

        print(final_y)

        words = [ "Permission to reproduce items where third-party owned material protected by copyright is included has been sought and cleared where possible. Every reasonable effort has been made by the publisher (UCLES) to trace copyright holders, but if any items requiring clearance have unwittingly been included, the publisher will be pleased to make amends at the earliest possible opportunity. To avoid the issue of disclosure of answer-related information to candidates, all copyright acknowledgements are reproduced online in the Cambridge International Examinations Copyright Acknowledgements Booklet. This is produced for each series of examinations and is freely available to download at www.cie.org.uk after the live examination series. Cambridge International Examinations is part of the Cambridge Assessment Group. Cambridge Assessment is the brand name of University of Cambridge Local Examinations Syndicate (UCLES), which is itself a department of the University of Cambridge.","Permission to reproduce items where third-party owned material protected by copyright is included has been sought and cleared where possible. Every reasonable effort has been made by the publisher (UCLES) to trace copyright holders, but if any items requiring clearance have unwittingly been included, the publisher will be pleased to make amends at the earliest possible opportunity. To avoid the issue of disclosure of answer-related information to candidates, all copyright acknowledgements are reproduced online in the Cambridge Assessment International Education Copyright Acknowledgements Booklet. This is produced for each series of examinations and is freely available to download at www.cambridgeinternational.org after the live examination series. Cambridge Assessment International Education is part of the Cambridge Assessment Group. Cambridge Assessment is the brand name of the University of Cambridge Local Examinations Syndicate (UCLES), which itself is a department of the University of Cambridge.","Permission to reproduce items where third-party owned material protected by copyright is included has been sought and cleared where possible. Every reasonable effort has been made by the publisher (UCLES) to trace copyright holders, but if any items requiring clearance have unwittingly been included, the publisher will be pleased to make amends at the earliest possible opportunity. To avoid the issue of disclosure of answer-related information to candidates, all copyright acknowledgements are reproduced online in the Cambridge Assessment International Education Copyright Acknowledgements Booklet. This is produced for each series of examinations and is freely available to download at www.cambridgeinternational.org after the live examination series. Cambridge Assessment International Education is part of the Cambridge Assessment Group. Cambridge Assessment is the brand name of the University of Cambridge Local Examinations Syndicate (UCLES), which itself is a department of the University of Cambridge."]

        wordtanya = []
        wordblank = 'BLANK	PAGE'
        wordblank2 = 'BLANK PAGE'
        wordtalta = ['[Turn Over','[Turn  Over','[Turn   Over']
        wordmetnaka = ['']
        for numba in range(1,40):
            wordtanya.append(f'Question {str(numba)} is printed on the next page.')
        print(wordtanya)
        a7a = list(range(1,50))

        doc = fitz.open(directory)
        question_rect = fitz.Rect(0, 0, wierd_constant, finale_question_line)
        line = fitz.Rect(0, 0, wierd_constant, final_line)
        rect = fitz.Rect(0, 0, wierd_constant, final_y)
        rect2 = fitz.Rect(0, 0, wierd_constant, final_y_under)

        for page in doc:
            page.insert_image(rect, filename=resource_path('imageedit1.jpg'))
            page.insert_image(rect2, filename=resource_path('imageedit2.jpg'))
            pages_list.append(page)
            for word in words:
                text_instances = page.searchFor(word)

                for rect_coordinates in text_instances:
                    page.addRedactAnnot(rect_coordinates, text_color=(1, 1, 1), fill=(1, 1, 1))
                    page.insert_image(line, filename=resource_path('imageedit1.jpg'))

                page.apply_redactions()

            for kelma in wordtanya:
                text_instances1 = page.searchFor(kelma)

                for rect_coordinates in text_instances1:
                    page.addRedactAnnot(rect_coordinates, text_color=(1, 1, 1), fill=(1, 1, 1))

                page.apply_redactions()

            for kelmaz in wordtalta:
                text_instances2 = page.searchFor(kelmaz)

                for rect_coordinates in text_instances2:
                    page.addRedactAnnot(rect_coordinates, text_color=(1, 1, 1), fill=(1, 1, 1))

                page.apply_redactions()


            #for kelmat in wordquestion:
                #text_instances3 = page.searchFor(kelmat)

                #for rect_coordinates in text_instances3:
                    #page.addRedactAnnot(rect_coordinates, text_color=(1, 1, 1), fill=(1, 1, 1))
                    #page.apply_redactions()
                #for rect_coordinates in text_instances3:
                    #page.insert_image(question_rect, filename=r"D:\coding\imageedit6.jpg")

            text = ''
            text += page.get_text()

            if len(re.findall(wordblank, text)) > 0:
                print(f'count on page {page.number + 1} is: {len(re.findall(wordblank, text))}')
                deleted_pages.append(page.number)

            elif len(re.findall(wordblank2, text)) > 0:
                print(f'count on page {page.number + 1} is: {len(re.findall(wordblank, text))}')
                deleted_pages.append(page.number)
        j = 0
        file_handle = fitz.open(input_file)
        final_pages = []
        for the_page in pages_list:
            j += 1
            final_pages.append(j - 1)
        for deletedpage in deleted_pages:
            final_pages.remove(deletedpage)

        print(final_pages)



        print(final_pages)
        final_pages.remove(final_pages[0])
        file_handle.select(final_pages)
        file_handle.save(output_file, deflate=True)

        doc.saveIncr()
        f += 1

    original_pdf = fitz.open(the_start_file)
    extra_page = fitz.open(coverpage)
    original_pdf.insertPDF(extra_page)
    print(final_pages)
    my_range = []
    print(original_pdf)
    my_list = list(range(final_pages[0],final_pages[-1] + 1))
    print(final_pages)
    print(f'{my_list} a7a')
    if final_pages == my_list and final_pages[0] == 1:
        final_pages.insert(0, 0)
        original_pdf.movePage(final_pages[-1], 0)
        original_pdf.save(the_final_file, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP,deflate=True)
        shutil.move(rf'{thefirstfile}{14}', thefirstfile)
    else:

        final_pages[-1] = final_pages[-1] + 1
        print(final_pages)
        final_pages = list(range(final_pages[0],final_pages[-1]))
        print(final_pages)
        final_pages.insert(0,0)
        final_pages = list(range(final_pages[0], final_pages[-1]))
        original_pdf.movePage(final_pages[-1],0)
        print(final_pages)
        original_pdf.save(the_final_file, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP,deflate=True)

    shutil.move(rf'{thefirstfile}{14}',thefirstfile )
window = tk.Tk()
window.geometry('500x700')


window.title("Mr Loay Exam Maker")
window.configure(bg='#FFD53D')
tk.Label(window,text="Mr Loay Exam Maker", font="Raleway 15 bold",bg='#FFD53D').pack(pady=10)



select_button = tk.Button(window,font="Helvetica 15 ",text="1.Select Exam", bg='#40B0DF', width = 29,height = 3,relief = "solid",command = lambda: select_exam())
select_button.pack(pady=20)

name_button = tk.Button(window,font="Helvetica 11 ",text = "2.Set Exam Name",bg='#40B0DF',relief = "solid", width = 37,height = 4, command=lambda: examname())
name_button.pack(pady=20)
name1 = Entry(window, width=30, relief="solid",font=('italic',15))
name1.pack()

var = IntVar()

radiobutton1 = Radiobutton(window,text="Year 9",variable = var,value=1, bg='#FFD53D',command=lambda :var.get())
radiobutton2 = Radiobutton(window,text="O Level",variable = var,value=2, bg='#FFD53D',command=lambda :var.get())
radiobutton3 = Radiobutton(window,text="AS Level",variable = var,value=3, bg='#FFD53D',command=lambda :var.get())
radiobutton4 = Radiobutton(window,text="A2 Level",variable = var,value=4,bg='#FFD53D', command=lambda :var.get())
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()
print(var)

merge_button = tk.Button(window,font="Helvetica 15 ",text="3.Create Exam",bg='#40B0DF',relief = "solid", width = 29,height = 3,command=lambda: videosmerge())

merge_button.pack(pady=20)

window.mainloop()



