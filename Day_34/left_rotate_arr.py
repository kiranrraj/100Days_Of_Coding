# Title  : Left and right rotate array
# Author : Kiran Raj R.
# Date   : 17/11/2020

arr1 = [2,3,4,5,6,7,8]
length = len(arr1)
for i in range(length):
    arr = arr1[i:(length)]+arr1[:i]
    print(arr)
print(arr1)

print("-----------------------")
for i in range(length):
    arr2 = arr1[length-i:length] + arr1[:(length-i)]
    print(arr2)
print(arr1)
