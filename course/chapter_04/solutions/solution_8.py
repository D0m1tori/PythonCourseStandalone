n = int(input())
firstNum = 1
secondNum = 1
print("Числа Фибоначчи:")
for i in range(n):
    print(firstNum)
    swap = secondNum
    secondNum += firstNum
    firstNum = swap
