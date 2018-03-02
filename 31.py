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

###########plant to farms - pf #############

raw_plants=[]
for i in open_file("plant-farm-link"):
    raw_plants.append(i[0])

plants = list(set(raw_plants))

p_len = len(plants)
begin =0
pf={}
while begin < p_len:
    pname = plants[begin]
    for line in open_file("plant-farm-link"):
        if plants[begin] in line:
            if line[0] in pf:
                pf[line[0]].append(line[2])
            else:
                pf[line[0]] = [line[2]]
    begin +=1

########### For making the avgerage - number of farm has been offer - countf #############
p_farms = []
for k,v in pf.items():
    p_farms.extend(v)

countf={}
for f in p_farms:
    if f in countf:
        countf[f] = countf.get(f)+1
    else:
        countf[f] =1

#for k, v in countf.items(): #not enough values to unpack -> use .items()
#    print(k,v)

###################farm to species - fs ################

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

flens =len(farms)
start=0
fs= dict()
while start < flens:
    fname = farms[start]
    start += 1
    d={}
    for line in open_file("clean"):
        if fname in line:
            if line[1] in d:
                d[line[1]] = d[line[1]]+line[2]
            else:
                d[line[1]] = line[2]

        fs[fname] = d
####################avgerage#################
for key , values in fs.items():
    for k,v in values.items():
        for k in countf:
            print(k,v/countf[k])
