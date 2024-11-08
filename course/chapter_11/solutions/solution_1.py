firstSrt = input()
firstSet = firstSrt.split()
myDict = {}
for i in firstSet:
    if i in myDict:
        myDict[i] +=1
    else:
        myDict[i] =1
for i,j in myDict.items():
    print(f"{i}: {j}")

