# Title  : Filter function
# Author : Kiran Raj R.
# Date   : 11/11/2020

import string

string_characters = string.ascii_letters


def filter_letters(c):
    char = c.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    out = []
    if char in vowels:
        out.append(c)
    return out

result = list(filter(filter_letters, string_characters))
print(result)