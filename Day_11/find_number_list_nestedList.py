# Title  : Count the number of element list of a list
# Author : Kiran raj R.
# Date   : 25:10:2020

list1 = [[1, 2], 3, 4, [5, 6], 7, [8, 9, 10]]
list2 = [('a', 'b'), 'c', 'd', 'e', ['f', 'g', 'h']]

print(f"Number of elements in list1 {len(list1)}")
print(f"Number of elements in list2 {len(list2)}")


def list_in_list(list_name):
    return(sum(type(elem) == type([]) for elem in list_name))


print(f"Number of list inside list1 {list_in_list(list1)}")
print(f"Number of list inside list2 {list_in_list(list2)}")
