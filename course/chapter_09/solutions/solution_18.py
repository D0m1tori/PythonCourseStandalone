a= input()
b = a.split()
print("Результат: ",end="")
for i in range(len(b)):
    if(1 == len(b[i])):
        print(b[i][0],end = " ")
    elif(1 == len(b[i]) and i == len(b)-1):
        print(b[i][0])
    elif(1 != len(b[i]) and i == len(b)-1):
        print(b[i][0]+ b[i][len(b[i])-1])
    else:
        print(b[i][0]+ b[i][len(b[i])-1],end = " ")