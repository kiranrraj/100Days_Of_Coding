# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : String rotate

# Check if Two Strings are Rotations
def areRotations(s1, s2):
    if len(s1) != len(s2):
        return None
    return s2 in (s1 + s1)

print(areRotations("abcde", "deabc")) # True 
print(areRotations("abc", "acb"))     # False