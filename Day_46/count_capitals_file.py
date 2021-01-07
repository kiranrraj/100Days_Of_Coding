# Title  : Count Capitals
# Author : Kiran Raj R.
# Date   : 29/11/2020

import os
os.chdir("D:\\gitHub\\100Days_Of_Coding\\Day_46")
with open('text_file.txt') as t:
    count = 0
    for i in t.read():
        if i.isupper():
            count+=1
    print(count)