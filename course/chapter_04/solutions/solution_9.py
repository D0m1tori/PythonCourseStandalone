firstNum = int(input())
secondNum = int(input())
n = int(input())
for i in range(n):
    print(firstNum)
    swap = secondNum
    secondNum += firstNum
    firstNum = swap
