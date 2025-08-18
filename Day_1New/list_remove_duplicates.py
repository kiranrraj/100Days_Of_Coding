# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : Find duplicates in a list

def removeDuplicates(nums: list[int]) -> list[int] | None:
    if not nums:
        return None
    
    seen = []
    
    for i in nums:
        if i not in seen:
            seen.append(i)
        else:
            continue

    return seen if seen else None

print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(removeDuplicates(nums1))  # [1, 2, 3]
nums2 = [1,2,3,]
print(removeDuplicates(nums2))  # [1, 2, 3]
nums3 = []
print(removeDuplicates(nums3))  # None
nums4 = [4,1,2,1,3,4,2,3,]
print(removeDuplicates(nums4))  # [4, 1, 2, 3]


print("# Using set to remove duplicate")
def removeDuplicatesSet(nums: list[int]) -> list[int] | None:
    return None if not list(set(nums)) else list(set(nums))

print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(removeDuplicatesSet(nums1))  # [1, 2, 3]
nums2 = [1,2,3,]
print(removeDuplicatesSet(nums2))  # [1, 2, 3]
nums3 = []
print(removeDuplicatesSet(nums3))  # None
nums4 = [4,1,2,1,3,4,2,3,]
print(removeDuplicatesSet(nums4))  # [1, 2, 3, 4]


print("# To order preserving logic (Python 3.7+)")
def removeDuplicatesOrdered(nums: list[int]) -> list[int] | None:
    if not nums:
        return None
    # print(dict.fromkeys(nums))
    return list(dict.fromkeys(nums))

print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(removeDuplicatesOrdered(nums1))  # [1, 2, 3]
nums2 = [1,2,3,]
print(removeDuplicatesOrdered(nums2))  # [1, 2, 3]
nums3 = []
print(removeDuplicatesOrdered(nums3))  # None
nums4 = [4,1,2,1,3,4,2,3,]
print(removeDuplicatesOrdered(nums4))  # [4, 1, 2, 3]
# print(dict.fromkeys(nums)) => {4: None, 1: None, 2: None, 3: None}