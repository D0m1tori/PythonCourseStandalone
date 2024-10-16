a = int(input())
count = 0
while(a <=0):
    a = int(input())
for i in range(a):
    if(a%(i+1) == 0):
        print(i+1)
