import barcode
from barcode.writer import ImageWriter
A = barcode.get_barcode_class('ean13')
a = A(input('enter the 12 number which has to converted into barcode: '), writer=ImageWriter())#in this format we have to give 12 digits
a.save(input("enter the file name :"))
#we can generate all types of barcode by just changing string in .get_barcode_class('here we have to change') by below list
#'code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca'
#we have to install barcode modlue by giving command:' pip install python-barcode'
