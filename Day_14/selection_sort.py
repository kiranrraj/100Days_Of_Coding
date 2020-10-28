# Title  : Selection Sort
# Author : Kiran raj R.
# Date   : 28:10:2020

def selection_sort(list_in):
    length = len(list_in)
    for i in range(length):
        min_elem_index = i
        for j in range(i+1, length):
            if list_in[min_elem_index] > list_in[j]:
                min_elem_index = j

        list_in[i], list_in[min_elem_index] = list_in[min_elem_index], list_in[i]
    return list_in


list1 = [4, 5, 6, 12, 3, 1, 2, 9, 8, 1, 3, 2]
print(selection_sort(list1))
