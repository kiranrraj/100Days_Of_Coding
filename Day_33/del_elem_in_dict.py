# Title  : Delete element from dictionary
# Author : Kiran Raj R.
# Date   : 16/11/2020

dict_1 = {
    'a': 'apple',
    'b': 'ball',
    'c': 'cat',
    'd': 'dog',
    'e': 'elephant',
    'f': 'fox',
    'g': 'goat'
}

print(dict_1)

del dict_1['a']
print(dict_1)

dict_1.pop('b')
print(dict_1)

out = {key: val for key, val in dict_1.items() if key != 'c' }
print(out)