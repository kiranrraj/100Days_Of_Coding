# Author    : Kiran raj R.
# Date      : 21/08/2025
# Question  : Find the third largest number in the array


def third_largest(nums):
    # Remove duplicates
    unique_nums = list(set(nums)) 
    # less than 3 numbers 
    if len(unique_nums) < 3: 
        return None  

    # float('-inf'), is a special floating-point number representing negative 
    # infinity. It is guaranteed to be smaller than any other number
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


# Test
nums = [10,4,3,7,5,9,8,1]
print(f"{nums} => Third largest number is {third_largest(nums)}")


# Time complexity:    O(n)
# Space complexity:   O(n)