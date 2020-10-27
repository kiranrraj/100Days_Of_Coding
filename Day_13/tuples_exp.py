# Title  : Tuple examples
# Author : Kiran raj R.
# Date   : 27:10:2020

# Tuple into list
tuple1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
out = [elem for tup in tuple1 for elem in tup]
print(out)

# remove duplicate tuples
tuple1 = [(1, 2), (3, 4), (5, 6), (2, 8), (1, 2), (3, 4)]
print(set(tuple1))

# print tuples that contain a specific element
item = 2
out = [tup for tup in tuple1 if item in tup]
print(out)

# print tuple based on a condition. Here all the elements of the tuples are upper case
list1 = [('aBc', 'ABc'), ('ABC', 'abc'), ('a', 'A'), ('A', 'B'), ('AB', 'ABC')]
out = [tup for tup in list1 if all(t.isupper() for t in tup)]
print(out)

# print tuple based on a condition. Here all elements are divible by 6
list1 = [(6, 12, 18, 24), (6, 12, 3), (6, 9), (1, 2, 3), (6, 6)]
out = [tup for tup in list1 if all(t % 6 == 0 for t in tup)]
print(out)

# print nested elements from tuple into a string
list1 = [('k', 'i', 'r', 'a', 'n'), ('r', 'a', 'j'), ('c', 'a', 'r')]
out = ["".join(tup) for tup in list1]
print(out)
