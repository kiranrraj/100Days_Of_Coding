# Title  : Pythagorean triple
# Author : Kiran Raj R.
# Date   : 21/11/2020


# Returns the product of a,b,c which are Pythagorean Triplet 
# at satisfies the following:
# 1. a < b < c
# 2. a**2 + b**2 = c**2

def pythagorean(arr):
    if arr[0] < arr[1] < arr[2]:
        if arr[0]**2 + arr[1]**2 == arr[2]**2:
                return arr[0] * arr[1] * arr[2]
    
    return "Not Pythagorean triple"

print(pythagorean([3,4,5]))
print(pythagorean([3,4,6]))
print(pythagorean([5,12,13]))
print(pythagorean([3,12,13]))
