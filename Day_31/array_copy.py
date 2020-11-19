# Title  : Create a copy of array
# Author : Kiran Raj R.
# Date   : 14/11/2020

arr1 = [23,13,34,56,78,11]
arr2 = [None] * len(arr1)

for i in range(len(arr1)):
    arr2[i] = arr1[i]

print(f"Array 1: {arr1}\nArray 2: {arr2}")