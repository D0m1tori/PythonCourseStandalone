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
    if(a in lst1):
        lst1.remove(a)
    else:
        print("такой игрушки нет")
    if(a != ""):
        a = input()
print(lst1)