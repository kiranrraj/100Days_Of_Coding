# Title  : Quick Sort
# Author : Kiran Raj R.
# Date   : 06:11:2020


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [ i for i in arr[1:] if i<=pivot ]
        greater = [ i for i in arr[1:] if i>=pivot ]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([45,34,23,90,2,11,7,8,4,3]))