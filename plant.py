import xlrd
workbook = xlrd.open_workbook("plant-farm-link.xlsx")
sheet = workbook.sheet_by_index(0)

raw_data =[]
for rowx in range(sheet.nrows):
    cols = sheet.row_values(rowx)
    raw_data.append(cols)

del raw_data[0]

count=0
for i in raw_data:
    if i[2] == '':
        del raw_data[count]
    count +=1

for i in raw_data:
    print(i)
