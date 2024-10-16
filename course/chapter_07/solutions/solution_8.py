a=  input()
lst1 = []
while(a != ""):
    lst1.append(a)
    a = input()
a=  input()
while(a != ""):
    lst1.append(a)
    a = input()
a=  input()
while(a != ""):
    lst1.remove(a)
    if(a != ""):
        a = input()
print(lst1)