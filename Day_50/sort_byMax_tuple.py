# Title  : Sort tuple by max value in tuple
# Author : Kiran raj R.
# Date   : 16:10:2020

list1 = [(10, 90, 23, 7), (90, 101, 10, 1), (20, 34, 15), (77, 66, 55)]


def getMax(elem):
    return max(elem)


list1.sort(key=getMax)
print(list1)
