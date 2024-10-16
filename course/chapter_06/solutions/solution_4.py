n = int(input())
result = 0
for i in range(n):
    for j in range(n-i):
        print(n-j, end="")
    print()