a = input()
b = a.split()
for i in range(len(b)):
    b[i] = int(b[i])
b = set(b)
b = list(b)
b.reverse()
print(*b)

