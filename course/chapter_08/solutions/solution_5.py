matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):
    for j in range(3):
        if(j != 2):
            print(matrix[j][i],end=" ")
        else:
            print(matrix[j][i],end="")
    print()
