# Title  : Remove duplicate list
# Author : Kiran raj R.
# Date   : 23:10:2020

def remove_dup(nested_list):
    out_list = []
    for i in range(len(nested_list)):
        for j in range(1, len(nested_list)):
            if nested_list[i] == nested_list[j]:
                break
        if i == j:
            out_list.append(nested_list[i])
    print(f"List without duplicates : {out_list}")


remove_dup([[1, 2, 3], [1, 2, 3], [4, 5], [9, 7], [8, 9], [8, 9]])


def remove_empty(nested_list):
    out_list = []
    for i in range(len(nested_list)):
        if len(nested_list[i]) != 0:
            out_list.append(nested_list[i])
    print(f"List without empty lists : {out_list}")


remove_empty([[2, 3], [], [56], [1, 2, 3], [], [8, 9, 0], []])
