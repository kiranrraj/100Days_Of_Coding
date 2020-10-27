# Title  : Find number of elements higher than the element in the list
# Author : Kiran raj R.
# Date   : 26:10:2020

list1 = [5, 6, 7, 8, 9, 11, 34, 55]
list2 = [1, 2, 3, 4, 5]
list3 = [10, 2, 45, 77, 14, 21]
list4 = [7, 22, 3, 45, 5, 88, 34, 55]


def count_higherElemnts(list_name):
    out = [sum(1 for elem in list_name if elem > i) for i in list_name]
    print(out)


count_higherElemnts(list1)
count_higherElemnts(list2)
count_higherElemnts(list3)
count_higherElemnts(list4)
