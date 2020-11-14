# Title  : Print alphabets from mix string
# Author : Kiran Raj R.
# Date   : 04:11:2020

string_to_filter = "he712047070l13212l213*(&(ow76968o172830r%*&$d"

def check_alpha(c):
    if c.isalpha():
        return c

def check_num(c):
    if c.isnumeric():
        return c


out = "".join(list(filter(check_alpha, string_to_filter)))
print(out)

out = "".join(list(filter(check_num, string_to_filter)))
print(out)