# Title  : Filter the tuple by product of element
# Author : Kiran raj R.
# Date   : 27:10:2020

tuple1 = [(2, 3, 4), (5, 11, 2), (6, 9, 0), (5, 5, 5), (4, 5, 6)]


def prod_tup(elem):
    prod = 1
    for i in elem:
        prod *= i
    return prod


out = [tup for tup in tuple1 if prod_tup(tup) > 100]
print(out)
