# Title  : Arrange tuples by number of elements
# Author : Kiran raj R.
# Date   : 15:10:2020

tuple_list = [(3, 23, 6, 13), (10, 40, 30), (72, 36),
              (1, 2, 3, 4, 5), (1,), (2, 3)]


# def elementLen(items):
#     len_list = []
#     for item in items:
#         len_list.append(len(item))
#     return len_list


def length_tuple(tn):
    return len(tn)


# for tuple_in in tuple_list:
#     print(length_tuple(tuple_in))


[tuple_list.sort(key=length_tuple)]
print(tuple_list)
