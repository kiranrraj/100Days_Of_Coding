# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : Find All Permutations of a String


def stringPermutations(s: str) -> list[str]:
    # Base case
    if len(s) == 1:
        return [s]
    
    perms = []
    
    # Loop over every index and character
    for i, char in enumerate(s):
        # Remaining string after removing the current char
        remaining = s[:i] + s[i+1:]
        
        # Recursively get permutations of the remaining string
        for p in stringPermutations(remaining):
            # char + p = we add the fixed character in front of each permutation.
            # perms.append() = add that new string into our result list.
            perms.append(char + p)
    
    return perms

print(stringPermutations("abcd"))

# Think recursively:
# Choice: Pick each character in s to be the first character.
# Subproblem: Permute the remaining s minus that chosen character.
# Combine: Prepend the chosen character to each of the sub-permutations.

# perms(s):
#   for each index i:
#     char = s[i]
#     rest = s without s[i]
#     for p in perms(rest):
#       emit char + p