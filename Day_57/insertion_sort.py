# Title  : Insertion Sort
# Author : Kiran raj R.
# Date   : 28:10:2020

def insertion_sort(list_in):

    for i in range(1, len(list_in)):  # starting point is one not zero
        key = list_in[i]

        j = i-1

        while j >= 0 and key < list_in[j]:
            list_in[j+1] = list_in[j]
            j = j-1
        list_in[j+1] = key

    return list_in


list1 = [4, 5, 6, 12, 3, 1, 2, 9, 8, 1, 3, 2, 100, 33]
print(insertion_sort(list1))
