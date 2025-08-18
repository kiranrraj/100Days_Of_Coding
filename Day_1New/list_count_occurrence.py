# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : Count occurrence

def countOccurrence(nums: list[int]) -> dict[int, int] | None:
    if not nums:
        return None
    
    counts = {}
    for i in nums:
        counts[i] = counts.get(i, 0) + 1

    return counts
    
print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(countOccurrence(nums1))  # {1: 5, 2: 1, 3: 1}
nums2 = [1,2,3,]
print(countOccurrence(nums2))  # {1: 1, 2: 1, 3: 1}
nums3 = []
print(countOccurrence(nums3))  # None
nums1 = [1,2,1,3,4,2,3,]
print(countOccurrence(nums1))  # {1: 2, 2: 2, 3: 2, 4: 1}



print("# use Counter from collections")
from collections import Counter
def countOccurrenceCounter(nums: list[int]) -> dict[int, int] | None:
    # if Counter(nums):
    #     return {k: v for k, v in Counter(nums).items()}
    # else:
    #     return None
    if not nums:
        return None
    return dict(Counter(nums))

print("----- Output -----")
nums1 = [1,1,1,1,1,2,3,]
print(countOccurrenceCounter(nums1))  # {1: 5, 2: 1, 3: 1}
nums2 = [1,2,3,]
print(countOccurrenceCounter(nums2))  # {1: 1, 2: 1, 3: 1}
nums3 = []
print(countOccurrenceCounter(nums3))  # None
nums1 = [1,2,1,3,4,2,3,]
print(countOccurrenceCounter(nums1))  # {1: 2, 2: 2, 3: 2, 4: 1}