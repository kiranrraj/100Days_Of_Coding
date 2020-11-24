# Title  : Matrix Multiplications
# Author : Kiran Raj R.
# Date   : 20/11/2020

mat1 = [[2,5,8], [4,3,8], [9,4,7]]
mat2 = [[5,3,9], [8,3,1], [2,2,8]]
result = [[0,0,0,], [0,0,0], [0,0,0]]

def multi(mat_1, mat_2):
    if len(mat_1[0]) != len(mat_2):
        print("Multiplication not possible")
        return
    else:
        for i in range(len(mat_1)):
            for j in range(len(mat_2[0])):
                for k in range(len(mat_2)):
                    result[i][j] += mat_1[i][k] * mat_2[k][j]
    print(result)

multi(mat1, mat2)