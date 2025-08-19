# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : Longest word

def longestWord(sentence: str) -> str:
    words = sentence.split()
    # key=len means: compare the items based on 
    # their length instead of alphabetical order.
    return max(words, key=len) if words else ""

print(longestWord("Python is easy"))  # Python
print(longestWord(""))                # ""