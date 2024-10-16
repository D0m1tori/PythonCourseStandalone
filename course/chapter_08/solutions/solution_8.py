lst = []
a = input()
count = 0
while(a != ""):
    count +=1
    lst.append(a)
    if(count%2 == 0):
        a = input()
    else:
        a = int(input())
pagesCount = lst[1::2]
print(f"Самая толстая книга: (\'{lst[lst.index(max(pagesCount))-1]}\', {max(pagesCount)})")
print(f"Суммарное число страниц: {sum(lst[1::2])}")
