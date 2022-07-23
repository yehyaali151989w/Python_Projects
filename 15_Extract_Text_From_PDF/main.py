import PyPDF2

pdf = open(r"D:\Python_Prpjects\14_Extract_Text_From_PDF\yehya.pdf", "rb")

reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())

