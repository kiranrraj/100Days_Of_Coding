# Title  : Map function in python
# Author : Kiran raj R.
# Date   : 31:10:2020

def getSquare(n):
    return n * n


numbers = [1, 2, 3, 4, 5]

result = map(getSquare, numbers)
square = set(result)

print(square)

result = list(map(lambda x: x+3, numbers))
print(result)
