# Title  : Find anagram words from the list
# Author : Kiran raj R.
# Date   : 16/07/2025

# Check if two strings s and t are anagrams — they must have:
#   The same characters
#   In the same frequency
#   In any order


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        # This line creates a key that represents the "sorted version" of the word.
        # Sorting the letters ensures all anagrams will have the same sorted key.
        key = tuple(sorted(word))

        if key in groups:
            # If yes: append the current word to that key’s list.
            groups[key].append(word)
        # If no: create a new list with that word.
        else:
            groups[key] = [word]

    return list(groups.values())


# Example usage
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))