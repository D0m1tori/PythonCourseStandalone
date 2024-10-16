n = int(input())
result = 0
count=0
for i in range(2,n+1):
    for j in range(1,i):
        if(i%j==0):
            count+=1
    if(count<2):
        print(i)
    count=0
        