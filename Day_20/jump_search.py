# Title  : Jump search
# Author : Kiran Raj R.
# Date   : 03:11:2020

import math
arr = [2,5,7,9,11,14,17,19,21]
num = 17
length = len(arr)
jump = int(math.sqrt(length))
left = 0

while(arr[min(jump, length)-1]<num):
    left = jump
    jump+= int(math.sqrt(length))

    if(left>=length):
        break

while(arr[left]<num):
    left =left + 1

    if(left== min(jump, length)):
        break
    
if(arr[left]==num):
        print(f"{arr[left]} found at index {left+1}")
