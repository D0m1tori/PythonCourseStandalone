a= input()
b = a.split()
for i in range(len(b)):
    if(b[i].isalpha()):
        b[i] =b[i].title()
b = " ".join(b)
print("Результат: "+b)