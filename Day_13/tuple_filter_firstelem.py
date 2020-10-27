# Title  : Filter tuple using first element
# Author : Kiran raj R.
# Date   : 27:10:2020

tuple1 = [(2, 20), (3, 30), (2, 11), (4, 100), (2, 'kiran')]
tuple_first = set()
out = [(x, y) for x, y in tuple1 if not(
    x in tuple_first or tuple_first.add(x))]
print(out)
