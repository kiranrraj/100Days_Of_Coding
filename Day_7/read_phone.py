import re
index = 1

with open('phone_num.txt','r',encoding='utf-8') as file:
     data = file.read()
# Title  : Read from file to find a pattern
# Author : Kiran raj R.
# Date   : 21:10:2020

numformat = re.compile(r'\d\d\d\d \d\d\d\d\d\d\d')
phonenums = numformat.findall(data)
# findNum = numformat.search(data)
# print(findNum.group())

for phone in phonenums:
    print(f"{index}.Phone number {phone}")
    index+=1