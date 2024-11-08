myDict = {}
lst =[]
a = input()
n = int(input())
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)):
    myDict[a[i]] = n - a[i]
for i,j in myDict.items():
    if(j in myDict.keys()):
        lst.append(i)
        lst.append(j)
        break
lst = tuple(lst)
print(lst)


