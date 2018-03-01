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

###############################################

count=0
fsdata = []
for i in open_file("clean"):
    if i[2]> 0:
        fsdata.append(i)
    count +=1

raw_farms = [] # store all the plant names
raw_species=[]
for i in fsdata:
    raw_farms.append(i[0])
    raw_species.append(i[1])

farms = list(set(raw_farms)) # remove duplicates
species = list(set(raw_species))

################################################


raw_plants=[]
for i in open_file("plant-farm-link"):
    raw_plants.append(i[0])

plants = list(set(raw_plants))

p_len = len(plants)
begin =0
big_dic={}
while begin < p_len:
    pname= plants[begin]
    
    if pname in big_dic:
        big_dic[pname] = big_dic[pname]+plants[1]
    else:
        big_dic[pname] = plants[1]

    lens =len(farms)
    start=0
    fs= dict()
    while start < lens:
        fname = farms[start]
        start += 1
        d={}

        if
        begin += 1
        for line in fsdata:
            if fname in line:
                if line[1] in d:
                    d[line[1]] = d[line[1]]+line[2]
                else:
                    d[line[1]] = line[2]

            fs[fname] = d
print(big_dic)
