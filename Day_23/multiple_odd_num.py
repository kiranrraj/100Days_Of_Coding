# Title  : Multiply all odd number
# Author : Kiran Raj R.
# Date   : 06:11:2020

def multiply_odd(num):
    """ Return sum of multiple of all odd number
    below user specified range """

    result = 1
    for i in range(1,num, 2):
        result*=i
    return result

print(multiply_odd(10))

def multiply_even(num):
    """ Return sum of multiple of all even number
    below user specified range """

    result = 1
    for i in range(2,num, 2):
        result*=i
    return result

print(multiply_even(11))