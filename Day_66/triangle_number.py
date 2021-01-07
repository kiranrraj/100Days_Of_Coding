# Title  : Triangle Number
# Author : Kiran raj R.
# Date   : 


# Triangle Number
# T(n) = (n * (n+1))/2 

import math

def findTriangelNum(n):
    result = (n*(n+1))/2
    return result

for i in range(1,10):
    print(findTriangelNum(i))


def findNum(tn):
    for i in range(1,tn):
        if 2*tn == i*(i+1):
            print(f"Found the number- {i}")
            return
    print('Number not found');

findNum(10)
findNum(15)
findNum(21)