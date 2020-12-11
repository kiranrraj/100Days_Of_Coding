dia=4  
print(f"The dimension is {dia}") 
res = [list(range(1 + dia * i, 1 + dia * (i + 1))) for i in range(dia)] 
print(f"Matrix of dimension {dia}: {res}") 