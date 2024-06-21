import xlrd

path = 'roster.xls'

def get_row(path,name):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    i = 0
    while(sheet.cell_value(i,0) != name) and (i < sheet.nrows):
        i+=1

    return i



def get_times(path, row):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    start_times=[]
    end_times=[]
    dates=[]

    for i in range(1,sheet.ncols):
        if(sheet.cell_value(row,i) != '  '):
            if i % 2 == 0:
                end_times.append(sheet.cell_value(row,i))
            else:
                start_times.append(sheet.cell_value(row,i))
                dates.append(sheet.cell_value(0,i))

    for i in range(0,len(dates)):
        dates[i]=dates[i][4]+dates[i][5]+dates[i][7]+dates[i][8]
    

    
    print(dates)
    print(start_times)
    print(end_times)

    return(dates,start_times,end_times)