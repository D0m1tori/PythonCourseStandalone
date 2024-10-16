lst1 = []
lst2 = []
for i in range(3):
    a = int(input())
    lst1.append(a)
tpl1 = tuple(lst1)
for i in range(3):
    a = int(input())
    lst2.append(a)
tpl2 = tuple(lst2)
if(tpl1 > tpl2):
    print(f"{tpl1} > {tpl2}")
elif(tpl1 == tpl2):
    print(f"{tpl1} = {tpl2}")
else:
    print(f"{tpl1} < {tpl2}")
