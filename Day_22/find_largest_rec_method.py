# Title  : Find the largest using custom function w&wo recursive
# Author : Kiran Raj R.
# Date   : 05:11:2020

def find_max(arr):
    largest = 0
    for elem in arr:
        if elem > largest:
            largest = elem
    return largest

arr = [1,2,3,4,56,1,2,3,4]

print(find_max(arr))

def find_max_rec(arr):
    if len(arr) == 1:
        return arr[0]
    largest = arr[0]
    last_max = find_max_rec(arr[1:])
    # print(last_max, largest)
    if largest > last_max :
        return largest
    else:
        return last_max


print(find_max_rec(arr)) 