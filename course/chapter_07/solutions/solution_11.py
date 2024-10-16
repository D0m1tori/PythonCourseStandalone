a= input()
lst1 = []
while(a != ""):
    lst1.append(a)
    a = input()
if("Палатка" not in lst1):
    print("Вы не взяли палатку!")
print(len(lst1))


