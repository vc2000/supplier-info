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
    d={}
    start += 1
    #print(name)
    for line in data:
        if fname in line:
            fs.setdefault(fname,[]).append(line[1])
            fs.setdefault(fname,[]).append(line[2])

#print a nice dictionaries
for k,v in fs.items():
    print(k,v)
