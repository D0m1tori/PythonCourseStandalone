a = int(input())
count = False
for i in range(2,a):
    if(a%i == 0):
        count = True
        break
if(count):
    print(a, end="")
    print(" - не простое")
else:
    print(a, end="")
    print(" - простое")