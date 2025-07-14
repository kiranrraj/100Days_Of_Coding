# Title  : Find the largest element
# Author : Kiran raj R.
# Date   : 14/07/2025

def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max


print(find_max([1,2,3,4,5,6]))
print(find_max([6,4,3,8,1,5,2]))