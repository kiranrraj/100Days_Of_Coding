# Title  : Bubble sort
# Author : Kiran raj R.
# Date   : 18:10:2020

def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


list = [3, 6, 2, 9, 7, 1, 5]
print(bubble_sort(list))


def bubble_sort(list_in):
    for i in range(len(list_in)):
        for j in range(0, len(list_in) - i - 1):

            if list_in[j] > list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j + 1], list_in[j]
