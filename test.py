a= {'plant1':{'fish1':200 , 'fish2' : 300}, 'plant2':{'fish1':2,'fish2':3} }


b={'plant1':5}
count =0
while count < len(a['plant1']):
    for a['plant1'][count] in a:
        print(a['plant1'][count]/b['plant1'])
    count +=1
#print(len(a['plant1']))
