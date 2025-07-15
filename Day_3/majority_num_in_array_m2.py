# Title  : Majority Nummber in Array [Method 2]
# Author : Kiran raj R.
# Date   : 15/07/2025

# Boyer-Moore Voting Algorithm
# If an element appears more than n/2 times, it will survive the cancellation and emerge as the candidate.

def find_majority_element(nums):
    candidate = None
    count = 0

    # Find a candidate using Boyer-Moore Voting
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Verify if candidate is truly the majority
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1

arr = [2, 2, 1, 1, 2, 2, 2]
print(find_majority_element(arr))
