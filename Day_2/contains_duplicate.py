# Title  : Check for duplicates
# Author : Kiran raj R.
# Date   : 14/07/2025

def contains_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([11,22,33,4,4,5]))
print(contains_duplicate([1,2,3,4,5,6]))