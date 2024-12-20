b = input()
b = b.split()
for i in range(len(b)):
    b[i] = int(b[i])
c = list(map(lambda x: x*x,b))
print(c)