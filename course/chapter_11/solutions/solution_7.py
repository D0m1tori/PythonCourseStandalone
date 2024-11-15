myDict = {}
lst =[]
a = input()
a = a.split()
for i in range(len(a)):
    if(a[i] in myDict.keys()):
        myDict[a[i]]+=1
        a[i] = a[i] + "_" + str(myDict[a[i]])
    else:
        myDict[a[i]] = 0
print(*a)



