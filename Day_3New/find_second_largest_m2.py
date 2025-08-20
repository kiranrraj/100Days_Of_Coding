# Author    : Kiran raj R.
# Date      : 20/08/2025
# Question  : Find the second largest number (Method-2)

def find_second_largest(arr):
    nums = list(set(arr))
    if len(nums) < 2:
        return "Array too short"
    nums.sort(reverse=True)
    return nums[1]

print(find_second_largest([20,30,20,10,5,50]))

# Time complexity O(n log n)  
# O(n) for set(arr) — creating a set takes linear time.
# O(k log k) for sort() — where k is the number of unique elements in arr.
# Space complexity O(k)