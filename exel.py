import xlsxwriter
from functions import stroygid
from functions import profcom

def writer(parametr):
    book = xlsxwriter.Workbook(r'E:\lerning\building\build.xlsx')
    page = book.add_worksheet('products')
    row = 0
    column = 0
    page.set_column('A:A', 30)
    page.set_column('B:B', 30)
    #page.set_column('C:C', 30)
    #page.set_column('D:D', 30)
    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        #page.write(row, column+2, item[2])
        #page.write(row, column+3, item[3])
        row += 1
    book.close()

