with open("tr-heaploop.ref", "r") as f:
    dictI = {}
    dictD = {}    
    for line in f:
        line = line.strip()
        temp = line.split(",",1)
        add = temp[0][0:-3]
       
        if temp[1] == 'I':
            if add in dictI.keys():
                dictI[add] = dictI[add] + 1
            else:
                dictI[add] = 1
        else:
            if add in dictD.keys():
                dictD[add] = dictD[add] + 1
            else:
                dictD[add] = 1
f.close()
with open("tr-matmul.ref", "r") as f:
    dictI = {}
    dictD = {}    
    for line in f:
        line = line.strip()
        temp = line.split(",",1)
        add = temp[0][0:-3]
       
        if temp[1] == 'I':
            if add in dictI.keys():
                dictI[add] = dictI[add] + 1
            else:
                dictI[add] = 1
        else:
            if add in dictD.keys():
                dictD[add] = dictD[add] + 1
            else:
                dictD[add] = 1               
f.close()
print("Instructions:\n")
for i in dictI:
    print(i + ":" + str(dictI[i]))
f.close()
print("\n")
print("Data:\n")
for i in dictD:
    print(i + ":" + str(dictD[i]))
f.close()
    
    
         
