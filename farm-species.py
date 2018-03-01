import xlrd
workbook = xlrd.open_workbook("clean.xlsx")
sheet = workbook.sheet_by_index(0)

raw_data =[]
for rowx in range(sheet.nrows):
    cols = sheet.row_values(rowx)
    raw_data.append(cols)

del raw_data[0] # delete the first row

count=0
data = []
for i in raw_data:
    if i[2]> 0:
        data.append(i)
    count +=1

raw_farms = [] # store all the plant names
raw_species=[]
for i in data:
    raw_farms.append(i[0])
    raw_species.append(i[1])

farms = list(set(raw_farms)) # remove duplicates
species = list(set(raw_species))

"""for i in species:
    if i =="Striped Bass":
        print(i)"""


lens =len(farms)
start=0
fs= dict()
while start < lens:
    fname = farms[start]
    start += 1
    d={}
    for line in data:
        if fname in line:
            if line[1] in d:
                d[line[1]] = d[line[1]]+line[2]
            else:
                d[line[1]] = line[2]

        fs[fname] = d

print(fs)
#for k,v in fs.items():
#    print(k,v)
