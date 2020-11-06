# Title  : Jump search
# Author : Kiran Raj R.
# Date   : 03:11:2020

import math

def jump_search(num,len,arr):
    step = int(math.sqrt(len))
    prev = 0

    while arr[min(step, len)-1] < num:
        prev = step
        step+= math.sqrt(len)
        if prev >= len:
            return -1
    while arr[int(prev)] < num:
        prev += 1

        if prev == min(step, len):
            return -1
    if arr[int(prev)] == num:
        return prev
    return -1