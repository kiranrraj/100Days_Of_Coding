# Title  : Insert new element before each element
# Author : Kiran raj R.
# Date   : 23:10:2020

def insert_b4(list_in, str_elem):

    out = [elem for list_elem in list_in for elem in (str_elem, list_elem)]
    print(f"After inserting element: {out}")


def insert_after(list_in, str_elem):

    out = [elem for list_elem in list_in for elem in (list_elem, str_elem)]
    print(f"After inserting element: {out}")


insert_b4([1, 2, 3, 4, 5], "$")
insert_after([1, 2, 3, 4, 5], "#")
