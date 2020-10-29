# Title  : Read from file, find  pattern
# Author : Kiran raj R.
# Date   : 15:10:2020

import re
index = 1

with open('phone_num.txt', 'r', encoding='utf-8') as file:
    data = file.read()

numformat = re.compile(r'\d\d\d\d \d\d\d\d\d\d\d')
phonenums = numformat.findall(data)
# findNum = numformat.search(data)
# print(findNum.group())

for phone in phonenums:
    print(f"{index}.Phone number {phone}")
    index += 1
