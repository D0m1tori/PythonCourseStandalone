myDict = {}
lst =[]
a = input()
while(a != ""):
    lst.append(a)
    a = input()
for i in range(len(lst)):
    lst[i] = lst[i].split(": ")
    if(lst[i][0] in myDict.keys()):
        myDict[lst[i][0]]+= (", "+ lst[i][1])
    else:
        myDict[lst[i][0]] = lst[i][1]
for i in myDict.keys():
    print(f"{i}: {myDict[i]}")



