# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : Find duplicates in a list

def findDuplicates(nums: list[int]) -> dict[int, int] | None:
    if not nums:
        return None
    
    seen = set()
    duplicates = {}

    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            # if not duplicates.keys(): 
            # if not duplicates: both are same
            if i in duplicates:
                duplicates[i]+=1
            else:
                duplicates[i] = 2

    return duplicates if duplicates else {}

print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(findDuplicates(nums1))  # {1: 5}
nums2 = [1,2,3,]
print(findDuplicates(nums2))  # {}
nums3 = []
print(findDuplicates(nums3))  # None
nums1 = [1,2,1,3,4,2,3,]
print(findDuplicates(nums1))  # {1: 2, 2: 2, 3: 2}


print("# Using Counter from collections")
from collections import Counter
def findDuplicatesCounter(nums: list[int]) -> dict[int, int] | None:
    if not nums:
        return None
    counts = Counter(nums)
    return {k: v for k, v in counts.items() if v > 1}

print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(findDuplicatesCounter(nums1))  # {1: 5}
nums2 = [1,2,3,]
print(findDuplicatesCounter(nums2))  # {}
nums3 = []
print(findDuplicatesCounter(nums3))  # None
nums1 = [1,2,1,3,4,2,3,]
print(findDuplicatesCounter(nums1))  # {1: 2, 2: 2, 3: 2}