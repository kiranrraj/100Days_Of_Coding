# Title  : Count characters in a file
# Author : Kiran Raj R.
# Date   : 15/11/2020

with open ('content.txt') as file:
    count = 0
    chars = 0
    lines=0
    for line in file:
        line = line.strip()
        if line !="":
            lines+=1
        for word in line.split():
            count+=1
            chars+=len(word)
            print(word)
        
    print(f"Number of lines in the file is: {lines}")
    print(f"Number of words in the file is: {count}")
    print(f"Number of characters in the file: {chars}")