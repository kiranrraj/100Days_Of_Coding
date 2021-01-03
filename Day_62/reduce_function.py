# Title  : Reduce function
# Author : Kiran Raj R.
# Date   : 11:11:2020

#Reduce implementation
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value


from functools import reduce

def my_add(x,y):
    return x+y

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [10,11,12,13,14,15,16,17]

out = reduce(my_add, list1)
print(out)

def my_add_with_init(x,y):
    sum_xy = x+y
    print(f"{x} + {y} = {sum_xy}")
    return sum_xy

out_with_init = reduce(my_add_with_init, list1, 100)
print(out_with_init)
