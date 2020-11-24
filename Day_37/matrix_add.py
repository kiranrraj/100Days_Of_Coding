# Title  : Matrix Addition 
# Author : Kiran Raj R.
# Date   : 20/11/2020

mat_1 = [[2,5,8], [4,3,8], [9,4,7]]
mat_2 = [[5,3,9], [8,3,1], [2,2,8]]
result = [[0,0,0,], [0,0,0], [0,0,0]]

for i in range(len(mat_1)):
    for j in range(len(mat_1[0])):
        result[i][j] = mat_1[i][j] + mat_2[i][j]

print(result)