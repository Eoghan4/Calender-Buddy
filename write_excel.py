# This should allow a colleague's name and email to be added to the database (excel)
import xlrd, xlsxwriter
import xlsxwriter.worksheet

def add_colleague(name,email,path):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    print(rows)

    write_book = xlsxwriter.Workbook(path)
    write_sheet = write_book.add_worksheet()

    write_sheet.write("A"+str(rows),name)
    write_sheet.write("B"+str(rows),email)
    print("Added")
    
write_book = xlsxwriter.Workbook("usres.xls")
write_sheet = write_book.add_worksheet()
add_colleague("Eoghan", "emg@gmail.com","usres.xls")