# Title  : Find the common elements in two lists
# Author : Kiran raj R.
# Date   : 25:10:2020

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 34, 55]
list2 = [3, 4, 11, 12, 13, 14, 15, 16, 0, 1, 55]
common_list = []

for elem in list1:
    if any(elem == item for item in list2):
        common_list.append(elem)

print(f" Common elements :{common_list}")


# method 2 using set and intersection

set_list1 = set(list1)
set_list2 = set(list2)

out_list = list(set_list1.intersection(set_list2))
print(f" Common elements (using set) :{out_list}")
