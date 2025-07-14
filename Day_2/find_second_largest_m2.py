# Title  : Find the second largest number (Method-2)
# Author : Kiran raj R.
# Date   : 14/07/2025

def find_second_largest(arr):
    nums = list(set(arr))
    if len(nums) < 2:
        return "Array too short"
    nums.sort(reverse=True)
    return nums[1]

print(find_second_largest([20,30,20,10,5,50]))