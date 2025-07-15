# Title  : Maximum consecutive vowels
# Author : Kiran raj R.
# Date   : 15/07/2025

def max_consecutive_vowels(s):
    vowels = set("aeiou")
    count = 0
    max_count = 0

    for char in s:
        if char in vowels:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

print(max_consecutive_vowels("helloooaeiouworldaa")) 