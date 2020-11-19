# Title  : Return a list of unique characters in dictionary
# Author : Kiran Raj R.
# Date   : 16/11/2020

dict_val ={
    'a':[1,2,3,4,5,6],
    'b':[1,2,3,4,5,6],
    'c':[7,8,9,0,11,12,13],
    'd':[1,2,3,4,50,9,8,7]
}

list_val = []

for elem in dict_val:
    list_val.extend(dict_val[elem])

print(set(list_val))

out = {elem for val in dict_val.values() for elem in val}
print(out)