# Title  : Python matrix calculations
# Author : Kiran Raj R.
# Date   : 27/11/2020

dia = int(input("Enter the diamension of the matrix: ")) 
print(f"The dimension is {dia}") 
result = [list(range(1 + dia * i, 1 + dia * (i + 1))) for i in range(dia)] 

print(f"The Matrix is : {result}") 

value_k = int(input("Enter the colum number: "))
k_column = [sub[value_k] for sub in result] 
  
# printing result 
print(f"The Kth column of matrix is : {k_column}") 