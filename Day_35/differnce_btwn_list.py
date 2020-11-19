# Title  : Find the difference between lists
# Author : Kiran Raj R.
# Date   : 18/11/2020

list_1 = [10,2,3,3,4,5,6,78,9]
list_2 = [1,2,3,40,5,6,7,8,9]

result1 = set(list_1) - set(list_2)
result2 = set(list_2) - set(list_1)
list1 = list(result1) + list(result2)
print(sorted(list1))