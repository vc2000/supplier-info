import xlrd

def open_file(file):
    workbook = xlrd.open_workbook(file+".xlsx")
    sheet = workbook.sheet_by_index(0)

    raw_data =[]
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        raw_data.append(cols)
    del raw_data[0]

    return raw_data

###########plant ship to endorser #############

raw_plants =[]
for i in open_file("Shipped Data"):
    raw_plants.append(i[0])

plants = list(set(raw_plants))

p_len = len(plants)
begin =0
pe={}
while begin < p_len:
    pname = plants[begin]
    for line in open_file("Shipped Data"):
        if plants[begin] in line:
            if line[0] in pe:
                pe[line[0]].append(line[4])
            else:
                pe[line[0]] = [line[4]]
    begin +=1

###########number of species ship to endorser #############

for k,v in pe.items():
    print(k,v)
