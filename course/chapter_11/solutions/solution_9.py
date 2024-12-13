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
    a[i][0][0][0][0][0] = a[i][0][0][0][0][0].lower()
    if(a[i][0][0][0][0][0] in myDict.keys()):
        myDict[a[i][0][0][0][0][0]] +=1
    elif(a[i][0][0][0][0][0]):
        myDict[a[i][0][0][0][0][0]] = 1
b = ""
for i in range(len(a)-1):
    b = a[i][0][0][0][0][0] + " "+a[i+1][0][0][0][0][0]
    b = b.lower()
    if(b in biGramDict.keys()):
        biGramDict[b] +=1
    elif(b):
        biGramDict[b] = 1
for i in range(len(a)-2):
    b = a[i][0][0][0][0][0] + " "+a[i+1][0][0][0][0][0]+" "+a[i+2][0][0][0][0][0]
    b=b.lower()
    if(b in triGramDict.keys()):
        triGramDict[b] +=1
    elif(b):
        triGramDict[b] = 1
count = 0
print("Слова: ", end="")
for i in myDict.keys():
    
    if(count != len(myDict)-1):
        print(f"{i}: {myDict[i]}, ", end="")
    else:
        print(f"{i}: {myDict[i]}")
    count +=1
count =0
#print()
print("Биграммы: ", end="")
for i in biGramDict.keys():
    
    if(count != len(biGramDict)-1):
        print(f"{i}: {biGramDict[i]}, ", end="")
    else:
        print(f"{i}: {biGramDict[i]}")
    count +=1
count =0
#print()
print("Триграммы: ", end="")
for i in triGramDict.keys():
    if(count != len(triGramDict)-1):
        print(f"{i}: {triGramDict[i]}, ", end="")
    else:
        print(f"{i}: {triGramDict[i]}")
    count+=1