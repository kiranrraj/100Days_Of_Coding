# Title  : Hexogonal Number
# Author : Kiran raj R.
# Date   : 


# Hexogonal Number
# H(n) = n*(2*n - 1)

import math

def findhexogonalNum(n):
    result = n * (2 * n - 1) 
    return result

for i in range(1,10):
    print(findhexogonalNum(i))


def findNum(hn):
    for i in range(1,hn):
        if hn == i * (2 * i - 1) :
            print(f"Found the number {i}")
            return
    print('Number not found');

findNum(6)
findNum(15)
findNum(28)