myDict = {}
idk = []
a = input()
while(a != ""):
    a = a.split(": ")
    idk.append(a)
    a = input()

for i in idk:
    if i[1] in myDict:
        myDict[i[1]].append(i[0])
    else:
        myDict[i[1]] = [i[0]]
for i,j in myDict.items():
    print(f"Класс {i}: ",end="")
    for k in j:
        if(j.index(k)!= len(j)-1):
            print(k,end=", ")
        else:
            print(k)


