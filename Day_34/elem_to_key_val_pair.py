# Title  : Convert the element into the key value pair
# Author : Kiran Raj R.
# Date   : 17/11/2020

list_1 = [112233, 23232, 34454, 67457457, 636345]
dict_1={}

for elem in list_1:
    mid = len(str(elem)) // 2
    key = str(elem)[:mid]
    val = str(elem)[mid:]
    dict_1.update({key : val})
print(dict_1)