# Title  : Reduce function with lambda
# Author : Kiran Raj R.
# Date   : 12/11/2020

from functools import reduce 

list1 = [1,2,3,4,5,6,7,8,9,10]

out = reduce(lambda x,y: x+y, list1)
print(out)

product = reduce(lambda x,y: x*y, list1)
print(product)

list1 = [3,4,22,5,6,7,3,4,8,9,11]
less_than = reduce(lambda x,y: x if x<y else y, list1)
print(less_than)

list1 = [3,4,22,5,6,7,3,4,8,9,11]
greater_than = reduce(lambda x,y: x if x>y else y, list1)
print(greater_than)

list1 = [3,4,0,5,6,0,3,4,8,0,11]
less_than = reduce(lambda x,y: True if x and y else False, list1)
print(less_than)