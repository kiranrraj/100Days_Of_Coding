# Author    : Kiran raj R.
# Date      : 20/08/2025
# Question  : Learn Regular Expression
#----------------------------------------------------------


####  Common Special Sequences  ####
# \A:   Matches if the specified characters are at the start of a string.

# \b:   Matches if the specified characters are at the beginning or end 
#       of a word.

# \B:   Opposite of \b. Matches if the specified characters are not at the 
#       beginning or end of a word.

# \d:   Matches any digit (0-9).

# \D:   Matches any non-digit character.

# \w:   Matches any alphanumeric character and "_". 
#       Equivalent to [a-zA-Z0-9_].

# \W:   Matches any non-word character. 
#       Equivalent to [^a-zA-Z0-9_]

# \s:   Matches any whitespace character (space,tab,newline). 
#       Equivalent to [ \t\n\r\f\v].

# \S:   Matches any non-whitespace character. 
#       Equivalent to [^ \t\n\r\f\v].

# \Z:   Matches if the specified characters are at the end of a string.



#### Common Metacharacters ####
# . (Dot): Matches any single character (except a newline).
#   Example: r.t matches "rat", "hat", "cat", etc.

# ^ (Caret): Matches the beginning of the string.
#   Example: ^Hello matches a string that starts with "Hello."

# $ (Dollar): Matches the end of the string.
#   Example: world$ matches a string that ends with "world."

# * (Asterisk): Matches the preceding character zero or more times.
#   Example: a* matches "", "a", "aa", "aaa", etc.

# + (Plus): Matches the preceding character one or more times.
#   Example: a+ matches "a", "aa", "aaa", but not "".

# ? (Question Mark): Matches the preceding character zero or one time.
#   Example: colou?r matches "color" and "colour."

# [] (Square Brackets): Defines a character set. 
#    Matches any single character within the set.
#    Example: [aeiou] matches any lowercase vowel. [0-9] matches any digit.

# | (Pipe): Acts as an OR operator.
#   Example: cat|dog matches either "cat" or "dog."

# {} (Braces): This means at least n, and at most m repetitions of the pattern left to it. 
#   Example: a{2,3} matches "daat", "aabc", "daaat". Not "abc", "dat"
#   [0-9]{2, 4} matches "ab123csde", not "1 and 2"

# () (Parentheses): Parentheses () is used to group sub-patterns. 
#   Example, (a|b|c)xz match any string that matches either a or b 
#   or c followed by xz


#### re package ####

## re.search(pattern, string): 
#  This function scans through the entire string and returns the first 
#  match object it finds. It returns None if no match is found.
#  Example: re.search(r'is', 'This is a test') would find a match.

## re.match(pattern, string): 
#  This function only looks for a match at the beginning of the string. 
#  It returns a match object if the pattern matches the start of the 
#  string; otherwise, it returns None.
#  Example: re.match(r'is', 'This is a test') would return None.

## re.findall(pattern, string): 
#  This function finds all non-overlapping matches in the string and 
#  returns them as a list of strings. If the pattern is not found, 
#  re.findall() returns an empty list.
#  Example: re.findall(r'is', 'This is a test') would return ['is', 'is'].

## re.sub(pattern, replacement, string): 
#  This function replaces all occurrences of the pattern in the string 
#  with the replacement string. If the pattern is not found, re.sub() 
#  returns the original string. You can pass count as a fourth parameter 
#  to the re.sub() method. If omited, it results to 0. This will replace 
#  all occurrences.
#  Example: re.sub(r'\s', '-', 'Hello World') would return 'Hello-World'.

## re.subn(pattern, replacement, string)
# The re.subn() is similar to re.sub() except it returns a tuple of 2 
# items containing the new string and the number of substitutions made.

## re.split(pattern, string): 
#  This function splits a string by the occurrences of the pattern. If 
#  the pattern is not found, re.split() returns a list containing the 
#  original string. You can pass maxsplit argument to the re.split() method. 
#  It's the maximum number of splits that will occur. By the way, the 
#  default value of maxsplit is 0; meaning all possible splits.
#  Example: re.split(r'\s', 'Hello World') would return ['Hello', 'World'].


#### Problems ####

# Find words that contain "err"
import re
data_list = ["apple", "banana", "cherry", "grape", "blueberry"]
pattern = "err"
matching_items = []
for item in data_list:
    if re.search(pattern, item):
        matching_items.append(item)

print(matching_items)  # ['cherry', 'blueberry']

# Pattern to find version numbers like 'vX.Y'
file_names = ["document_v1.0.txt", "report_v1.1.txt", "image_v1.2.jpg"]
new_version_number = "2.0"
version_pattern = r"v\d+\.\d+"
updated_files = []

for name in file_names:
    newFile = re.sub(version_pattern, f"v{new_version_number}", name)
    updated_files.append(newFile) 
print(updated_files) # ['document_v2.0.txt', 'report_v2.0.txt', 'image_v2.0.jpg']