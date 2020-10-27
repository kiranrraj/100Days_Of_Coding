# Title  : Sort list by unique characters
# Author : Kiran raj R.
# Date   : 16:10:2020

list1 = ['abc', 'ab', 'aaaaa', 'bababa', 1234, 1, 5,
         'abcdeddd', 'aaaabbbbbcc', 'aaaaaabbbbbbb', 234, 567, 112211]


def sort_by_unique_char(list_in):
    return len(set(str(list_in)))


list1.sort(key=sort_by_unique_char)

print(list1)
