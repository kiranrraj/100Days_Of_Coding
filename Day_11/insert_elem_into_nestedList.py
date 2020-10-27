# Title  : Insert elements of two nested list into one list
# Author : Kiran raj R.
# Date   : 25:10:2020

list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
list2 = [[11, 12], [13, 14], [15, 16], [17, 18]]

single_list = [a + b for a, b in zip(list1, list2)]
print(single_list)
