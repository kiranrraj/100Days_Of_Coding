# Title  : Anagram or not
# Author : Kiran raj R.
# Date   : 16/07/2025

# Check if two strings s and t are anagrams — they must have:
#   The same characters
#   In the same frequency
#   In any order

def is_anagram(s, t):
    # If length does not match
    if len(s) != len(t):
        return False

    count = {}
    # Count characters in s using a dictionary.
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Subtract counts using characters from t.
    for char in t:
        # Is missing from the dictionary
        if char not in count:
            return False
        count[char] -= 1
        # Has a negative count
        if count[char] < 0:
            return False

    return True

print(is_anagram("kiran", "raj"))
print(is_anagram("kiran", "irank"))

# Time: O(n) — one pass through s, one pass through t
# Space: O(1)
