# Title  : Python matrix calculations
# Author : Kiran Raj R.
# Date   : 27/11/2020

dia=4  
print(f"The dimension is {dia}") 
res = [list(range(1 + dia * i, 1 + dia * (i + 1))) for i in range(dia)] 
print(f"Matrix of dimension {dia}: {res}") 