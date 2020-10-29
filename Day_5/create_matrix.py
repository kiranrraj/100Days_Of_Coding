# Title  : Create matrix
# Author : Kiran raj R.
# Date   : 19:10:2020

matrix1 = []
for i in range(1, 6):
    sub_matrix = []
    for j in range(1, 4):
        sub_matrix.append(i*j)
    matrix1.append(sub_matrix)

print(f"Generated matrix 1 : {matrix1}")

sub_matrix2 = [j for j in range(1, 6)]
matrix2 = [[i*x for i in range(1, 4)] for x in sub_matrix2]
print(f"Generated matrix 2 : {matrix2}")
