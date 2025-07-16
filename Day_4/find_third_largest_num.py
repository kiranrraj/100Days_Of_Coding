# Title  : Find the third largest number in the array
# Author : Kiran raj R.
# Date   : 16/07/2025

def third_largest(nums):
    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 3: # less than 3 numbers
        return None  

    first = second = third = float('-inf')

    for num in unique_nums:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num

    return third

# Time: O(n)
# Space: O(n) for set(nums)