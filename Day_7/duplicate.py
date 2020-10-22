# Title  : Find matching elements
# Author : Kiran raj R.
# Date   : 21:10:2020

userStr1 = input("Enter your first string :")
userStr2 = input("Enter your second string :")

set_str_1 = set(userStr1)
set_str_2 = set(userStr2)

numMatchChar = set_str_1 & set_str_2
print(f"Matched character is {numMatchChar}")
print(f"Number of matched character is {len(numMatchChar)}")