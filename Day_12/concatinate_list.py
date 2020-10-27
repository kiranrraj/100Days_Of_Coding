# Title  : Concatinate two lists
# Author : Kiran raj R.
# Date   : 26:10:2020

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 34, 55]
list2 = [3, 4, 11, 12, 13, 14, 15, 16, 0, 1, 55]

# concat two lists
concat_list = list1 + list2
print(concat_list)

# sorted concat list
concat_list = sorted(list1 + list2)
print(concat_list)

# sorted concat list with out duplicate elements
concat_list = sorted(set(list1) | set(list2))
print(concat_list)
