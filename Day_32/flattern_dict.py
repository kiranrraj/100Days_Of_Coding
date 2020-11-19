# Title  : Flattern the dictionary to a tuple
# Author : Kiran Raj R.
# Date   : 15/11/2020

dict_val ={
    'a':[1,2,3,4,5,6],
    'b':[1,2,3,4,5,6],
    'c':[7,8,9,0,11,12,13],
    'd':[1,2,3,4,50,9,8,7]
}

out = [(elem[0],) + tuple(el) for elem in dict_val.items() for el in elem[1:]]
print(out)

