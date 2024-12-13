import copy
def replace_in_matrix(matrix, old_value, new_value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[j][i] == old_value):
                matrix[j][i] = new_value
    return matrix
