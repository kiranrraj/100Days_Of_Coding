# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : Find the sum of numbers in a list

def findSum(nums: list) -> int|None:
    
    if len(nums) == 0:
        return None

    sumNums = 0

    for i in nums:
        sumNums+=i

    return sumNums

print("----- Output -----")
print(findSum([1,2,3,4,5]))  # 15
print(findSum([0,0,3,-3]))   # 0
print(findSum([]))           # None


print("# Using built in function 'sum'")
def findSumBuildIn(nums: list) -> int|None:
    return sum(nums)

print("----- Output -----")
print(findSumBuildIn([1,2,3,4,5]))  # 15
print(findSumBuildIn([0,0,3,-3]))   # 0
print(findSumBuildIn([]))           # 0


print("# Using built in function "sum" [Change made to print None if empty]")
def findSumBuildIn1(nums: list) -> int | None:
    return None if len(nums) == 0 else sum(nums)

print("----- Output -----")
print(findSumBuildIn1([1,2,3,4,5]))  # 15
print(findSumBuildIn1([0,0,3,-3]))   # 0
print(findSumBuildIn1([]))           # None