
# Title  : Generators in python
# Author : Kiran raj R.
# Date   : 30:10:2020

def printNum():
    num = 0
    while True:
        yield num
        num += 1


result = printNum()
print(next(result))
print(next(result))
print(next(result))

result = (num for num in range(10000))
print(result)
print(next(result))
print(next(result))
print(next(result))
