# Title  : Jump search
# Author : Kiran Raj R.
# Date   : 03:11:2020

import math

def jump_search(arr, num):

    prev =0
    jump = int(math.sqrt(len(arr)))
    length = len(arr)

    for i in range(0, length, jump):
        if arr[i] < num:
            prev = i
        elif arr[i] == num:
            return f"Found {arr[i]} at {i+1}"
        else:
            break
    
    for j in range(prev,length):
        if arr[j]== num:
            return f"Found {arr[j]} at {j+1}"
        j+=1
    return "Not found"

print(jump_search([2,4,6,8,9,10,13,16,19], 19))
print(jump_search([2,4,6,8,9,10,13,16,19], 16))
print(jump_search([2,4,6,8,9,10,13,16,19], 29))
print(jump_search([2,4,6,8,9,10,13,16,19], 9))
print(jump_search([2,4,6,8,9,10,13,16,19], 2))