# Title  : Check whether a list is circular or not
# Author : Kiran raj R.
# Date   : 26:10:2020

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 34, 55]
list2 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
list3 = [1, 2, 3, 3, 2, 1]
list4 = [7, 22, 3, 45, 5, 88, 2, 8, 11, 34, 55]


def is_circularList(list_name):
    list_length = len(list_name)
    half = list_length//2
    if list_length % 2 == 0:
        list_fh = list_name[: half]
        list_sh = list_name[half:]
        list_sh.reverse()
    else:
        list_fh = list_name[: half]
        list_sh = list_name[half+1:]
        list_sh.reverse()

    if list_fh == list_sh:
        print(f"{list_name} is a circular list.")
    else:
        print(f"{list_name} not a circular list.")


is_circularList(list1)
is_circularList(list2)
is_circularList(list3)
is_circularList(list4)
