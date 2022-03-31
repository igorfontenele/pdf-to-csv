import pdfplumber
import csv

f = open("filename.csv", "w", newline='')

writer = csv.writer(f)

writer.writerow(["type here your csv's headers separated to commas"])

list_pages = ["type here the pages of your pdf you want to iterate separated to commas"];

pdf = pdfplumber.open("pass path of your pdf file")

for i in list_pages:
    page = pdf.pages[1].extract_text()[i]
    writer.writerow(page)
    count =+ 1 

#created at fonseca brasil advogados
