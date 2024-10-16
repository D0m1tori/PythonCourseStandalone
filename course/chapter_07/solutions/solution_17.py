numbers = [int(i) for i in input().split()]
n = int(input())
a = numbers[::n]
a.sort()
print(a)


