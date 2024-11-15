myDict = {}
lst =[]
a = input()
while(a != ""):
    lst.append(a)
    a = input()
for i in range(len(lst)):
    lst[i] = lst[i].split()
    dataOfPet = lst[i][0]+", "+lst[i][1]
    nameOfOwner = lst[i][2] + " " + lst[i][3]
    if (nameOfOwner not in myDict.keys()):
        myDict[nameOfOwner] = []
    myDict[nameOfOwner].append(dataOfPet)
for i in myDict.keys():
    print(f"{i}: ",end="")
    for j in range(len(myDict[i])):
        if(j != (len(myDict[i]) -1)):
            print(myDict[i][j],end="; ")
        else:
            print(myDict[i][j],end="")
    print()



