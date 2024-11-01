firstSrt = input()
lst = []
#for i in range(len(fisrtSrt)):
#    lst.append(firstSrt)
a = set(firstSrt)
a = list(a)
a.sort()
print("Уникальные символы: ",end="")
for i in range(len(a)):
    if(a[i] != " " and i != len(a)-1):
        print(a[i],end=" ")
    if(a[i] != " " and i == len(a)-1):
        print(a[i],end="\n")
    if(a[i] == " " and i == len(a)-1):
        print("\n")


