# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : Find the Maximum and Minimum

def findMinMax(nums: list) -> list | None:
    
    if len(nums) == 0:
        return None
    
    if len(nums) == 1:
        return [nums[0], nums[0]]
    
    minNum = nums[0]
    maxNum = nums[0]

    for i in nums:
        if i < minNum:
            minNum = i
        if i > maxNum:
            maxNum = i
    return [minNum, maxNum]

print("----- Output -----")
print(findMinMax([]))           # None
print(findMinMax([5]))          # [5, 5]
print(findMinMax([3, 1, 9]))    # [1, 9]
print(findMinMax([-7, 0, 4]))   # [-7, 4]


print("# Use builtin functions to find min and max")
def findMinMaxBuildIn(nums: list) -> list | None:
    if len(nums) == 0:
        return None
    else:
        return [min(nums), max(nums)]

print("----- Output -----")
print(findMinMaxBuildIn([]))           # None
print(findMinMaxBuildIn([5]))          # [5, 5]
print(findMinMaxBuildIn([3, 1, 9]))    # [1, 9]
print(findMinMaxBuildIn([-7, 0, 4]))   # [-7, 4]