import PyPDF2
import re
import fitz
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

from PyPDF2 import PdfFileReader

directory = r"D:\coding\test5.pdf"
doclocation = r"D:\coding\test3.pdf"
input_file = directory
output_file = r"D:\coding\rearrange.pdf"
pdf_reader = PdfFileReader(directory,strict=False)

cover = "year9"
coverpagey9 = r'D:\coding\coveryear9.pdf'
doc = PdfFileReader(open(directory, 'rb'))
res = doc.getPage(0).mediaBox
page_res = res[0:6]
image_y= page_res[3:5]

print(image_y)
f = 0
while f < 2:
    for i in image_y:
        final_y = i
    for i in image_y:
        under_final_y = i
    for i in image_y:
        finale_y = i
    for i in image_y:
        finale_question = i

    final_y = (final_y*667)/10000
    final_y_under = (under_final_y*1973)/1000
    final_line = (under_final_y*1698)/1000
    finale_question_line = (finale_question*1924)/1000
    wierd_constant = 611
    pages_list = []
    deleted_pages = []

    print(final_y)



    words = ["Permission to reproduce items where third-party owned material protected by copyright is included has been sought and cleared where possible. Every reasonable effort has been made by the publisher (UCLES) to trace copyright holders, but if any items requiring clearance have unwittingly been included, the publisher will be pleased to make amends at the earliest possible opportunity. To avoid the issue of disclosure of answer-related information to candidates, all copyright acknowledgements are reproduced online in the Cambridge International Examinations Copyright Acknowledgements Booklet. This is produced for each series of examinations and is freely available to download at www.cie.org.uk after the live examination series. Cambridge International Examinations is part of the Cambridge Assessment Group. Cambridge Assessment is the brand name of University of Cambridge Local Examinations Syndicate (UCLES), which is itself a department of the University of Cambridge."]
    wordtanya =["is printed on the next page."]
    wordblank = 'BLANK	PAGE'
    wordblank2 = 'BLANK PAGE'
    doc = fitz.open(directory)
    question_rect = fitz.Rect(0,0,wierd_constant,finale_question_line)
    line = fitz.Rect(0,0,wierd_constant,final_line)
    rect = fitz.Rect(0,0,wierd_constant,final_y)
    rect2 = fitz.Rect(0,0,wierd_constant,final_y_under)

    for page in doc:
        page.insert_image(rect, filename = r"D:\coding\imageedit1.jpg")
        page.insert_image(rect2, filename = r"D:\coding\imageedit2.jpg")
        pages_list.append(page)
        for word in words:
            text_instances = page.searchFor(word)

            for rect_coordinates in text_instances:
                page.addRedactAnnot(rect_coordinates, text_color=(1, 1, 1), fill=(1, 1, 1))
                page.insert_image(line, filename=r"D:\coding\imageedit5.jpg")

            page.apply_redactions()

        for kelma in wordtanya:
            text_instances1 = page.searchFor(kelma)

            for rect_coordinates in text_instances1:
                page.insert_image(question_rect, filename=r"D:\coding\imageedit5.jpg")

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

    file_handle.select(final_pages)
    file_handle.save(output_file,deflate=True)

    doc.saveIncr()
    f += 1


