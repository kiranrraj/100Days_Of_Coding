# Title  : Majority Nummber in Array [Method 1]
# Author : Kiran raj R.
# Date   : 15/07/2025

def majority_element(arr):
    n = len(arr)
    freq = {}

    for num in arr:
        # freq.get(num, 0) tries to get the current count of num.
        # If num doesn't exist yet in the dictionary, it returns 0 by default.
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num

    return -1


# Time: O(n)
# Space: O(n) Frequency dict