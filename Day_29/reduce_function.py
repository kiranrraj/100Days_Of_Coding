# Title  : Filter function with lambda
# Author : Kiran Raj R.
# Date   : 12/11/2020
from functools import reduce 

list1 = [1,2,3,4,5,6,7,8,9,10]

out = reduce(lambda x,y: x+y, list1)
print(out)

product = reduce(lambda x,y: x*y, list1)
print(product)