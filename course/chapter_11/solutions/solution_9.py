myDict = {}
biGramDict = {}
triGramDict = {}
lst =[]
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = a[i].split(".")
    a[i][0] = a[i][0].split(",")
    a[i][0][0] = a[i][0][0].split("!")
    a[i][0][0][0] = a[i][0][0][0].split("?")
    a[i][0][0][0][0] = a[i][0][0][0][0].split(":")
for i in range(len(a)):
    if(a[i][0][0][0][0][0] in myDict.keys()):
        myDict[a[i][0][0][0][0][0]] +=1
    else:
        myDict[a[i][0][0][0][0][0]] = 1
b = ""
for i in range(len(a)-1):
    b = a[i][0][0][0][0][0] + " "+a[i+1][0][0][0][0][0]
    if(b in biGramDict.keys()):
        biGramDict[b] +=1
    else:
        biGramDict[b] = 1
for i in range(len(a)-2):
    b = a[i][0][0][0][0][0] + " "+a[i+1][0][0][0][0][0]+" "+a[i+2][0][0][0][0][0]
    if(b in triGramDict.keys()):
        triGramDict[b] +=1
    else:
        triGramDict[b] = 1
count = 0
print("Слова: ", end="")
for i in myDict.keys():
    
    if(count != len(myDict)):
        print(f"{i}: {myDict[i]}, ", end="")
    else:
        print(f"{i}: {myDict[i]}")
    count +=1
print(len(myDict), count)
count =0
print()
print("Биграммы: ", end="")
for i in biGramDict.keys():
    
    if(count != len(biGramDict)):
        print(f"{i}: {biGramDict[i]}, ", end="")
    else:
        print(f"{i}: {myDict[i]}")
    count +=1
count =0
print()
print("Триграммы: ", end="")
for i in triGramDict.keys():
    if(count != len(triGramDict)):
        print(f"{i}: {triGramDict[i]}, ", end="")
    else:
        print(f"{i}: {triGramDict[i]}")