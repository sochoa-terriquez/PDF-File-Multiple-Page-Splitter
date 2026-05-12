from PyPDF2 import PdfReader, PdfWriter
pdf_file_path = "/Users/samanthaochoa-terriquez/Documents/Downloads/Final Case Study-OchoaSam (1).pdf"

reader = PdfReader(pdf_file_path)
writer = PdfWriter()


for page_num in range(2, 6):
    writer.add_page(reader.pages[page_num])

with open('NewOutput.pdf', 'wb') as out:
    writer.write(out)

print('PDF file has been split!')

