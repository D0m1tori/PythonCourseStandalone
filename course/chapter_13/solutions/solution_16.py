b = input()
b = b.split()
for i in range(len(b)):
    b[i] = int(b[i])
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
c = list(map(lambda x,y: x**y,b,a))
print(c)