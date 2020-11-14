# Title  : Reduce vs Accumulate
# Author : Kiran Raj R.
# Date   : 12/11/2020

from itertools import accumulate
from functools import reduce

list1 = [1,2,3,9,10,4,5,6,7,8]
out = list(accumulate(list1))
print(out)  #[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
out = reduce(lambda x,y: x+y, list1)
print(out)  #55



less_than = reduce(lambda x,y: x if x<y else y, list1)
print(less_than)

def lessthan(x,y):
    if x<y:
        return x
    else:
        return y

less_than = list(accumulate(list1, lessthan))
print(less_than)


greater_than = reduce(lambda x,y: x if x>y else y, list1)
print(greater_than)

def greaterthan(x,y):
    if x>y:
        return x
    else:
        return y

greater_than = list(accumulate(list1, greaterthan))
print(greater_than)