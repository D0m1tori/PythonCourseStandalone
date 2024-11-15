myDict = {}
lst =[]
a = input()
b = False
indx = 0
for i in range(len(a)):
    if a[i] in myDict:
        myDict[a[i]] += 1
    else:
        myDict[a[i]] = 1
for i in range(len(a)):
    if(myDict[a[i]] == 1):
        b = True
        indx = i
        break
if(b):
    print(a[indx])
else:
    print("None")


