import sys
import PyPDF2

wtr = sys.argv[1]
inputs = sys.argv[2:]
print(inputs,wtr)

def combine(input_lst):
    merger = PyPDF2.PdfFileMerger()
    for pdf in input_lst:
        print(pdf)
        merger.append(pdf)
    merger.write("combine.pdf")

def add_watermark(wtr):
    reader = PyPDF2.PdfFileReader(open("combine.pdf",'rb'))
    watermark = PyPDF2.PdfFileReader(open(wtr,'rb'))
    writer = PyPDF2.PdfFileWriter()
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        page.mergePage(watermark.getPage(0))
        writer.addPage(page)
    with open("Watermark.pdf",'wb') as new_file:
        writer.write(new_file)
    

combine(inputs)
add_watermark(wtr)

