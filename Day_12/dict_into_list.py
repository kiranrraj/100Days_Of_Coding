# Title  : Convert dictionary key and values into a new list
# Author : Kiran raj R.
# Date   : 26:10:2020

# method 1 using dict.keys() and dict.values()
main_dict = {'a': 'apple', 'b': 'ball',
             'c': 'cat', 'd': 'dog', 'e': 'elephant'}

list_keys = list(main_dict.keys())
list_values = list(main_dict.values())

print(list_keys, list_values)


# method 2 using dict.items()
listkeys = []
listvalues = []

for keys, values in main_dict.items():
    listkeys.append(keys)
    listvalues.append(values)

print(listkeys, listvalues)
