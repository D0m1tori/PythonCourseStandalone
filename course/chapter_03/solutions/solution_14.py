a = input()
count = 0
while(a[0] == "-"):
    a = input()
for i in range(len(a)):
    count += int(a[i])
print(count)