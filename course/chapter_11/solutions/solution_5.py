myDict = {}
lst =[]
a = input()
while(a != ""):
    lst.append(a)
    a = input()
for i in range(len(lst)):
    lst[i] = lst[i].split()
    lst[i][0] = lst[i][0][:-1:]
    for j in range(1,len(lst[i])):
        myDict[lst[i][j]] = lst[i][0]
names = list(myDict.keys())
names.sort()
for i in names:
    print(i + "@" + myDict[i])



