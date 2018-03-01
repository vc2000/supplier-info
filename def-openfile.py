import xlrd

def open_file(file):
    workbook = xlrd.open_workbook(str(file)+".xlsx")
    sheet = workbook.sheet_by_index(0)

    raw_data =[]
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        raw_data.append(cols)
    del raw_data[0]

    return raw_data

def main():
    open_file(clean)
