# Title  : File operations
# Author : Kiran Raj R.
# Date   : 15/11/2020

with open ('content.txt') as file:
    count = 0
    for line in file:
        for word in line.split():
            count+=1
            print(word)
    print(f"Number od words in the file is: {count}")
