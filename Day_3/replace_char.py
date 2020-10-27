# Title  : Replace a character with a user specified, user will ask a charater to be retained
# Author : Kiran raj R.
# Date   : 17:10:2020

list1 = "kiran raj r"
char = "r"
withChar = "$"


def replace_char(str_input, retain_char, withChar):
    out = [char if char == retain_char else withChar for char in str_input]
    print(out)


replace_char(list1, char, withChar)

list2 = "hello my dear"
withChar = "*"
char = "l"

replace_char(list2, char, withChar)
