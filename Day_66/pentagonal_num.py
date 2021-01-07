# Title  : Pentagonal Number
# Author : Kiran raj R.
# Date   : 


# Pentagonal Number
# P(n) =(n * (3 *n - 1))/2 

import math

def findpentagonalNum(n):
    result = (n * (3 * n - 1))/2 
    return result

for i in range(1,10):
    print(findpentagonalNum(i))


def findNum(pn):
    for i in range(1,pn):
        if 2*pn == i * (3 * i - 1):
            print(f"Found the number- {i}")
            return
    print('Number not found');

findNum(5)
findNum(12)
findNum(22)