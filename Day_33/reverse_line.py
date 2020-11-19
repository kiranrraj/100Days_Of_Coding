# Title  : Reverse a line
# Author : Kiran Raj R.
# Date   : 16/11/2020

new_line = []

with open('words.txt') as file:
    for line in file:
        new_line.append(line[-1::-1])

with open('output.txt', 'w') as file2:
    for line in new_line:
        line = line.strip() + '\n'
        file2.writelines(line)