n = int(input())
#round(n/2)-abs(round(n/2)-j)
for i in range(n):
    for j in range(n):
        a = min(i,j,n-i-1,n-j-1)
        if(j != n-1):
            print(a+1,end=" ")
        else:
            print(a+1,end="")
        
    print()


        