# Title  : Find the line number in which specified word exists.
# Author : Kiran Raj R.
# Date   : 16/11/2020

user_input = input("Enter the word to search: ")
count = 0
occurance = []

with open('words.txt') as file:
    for line in file:
        count+=1
        if user_input in line:
            occurance.append(count)
    if len(occurance) == 1:
        print(f"Found {user_input} in line number {occurance[0]}")
    elif len(occurance) > 1:
        print(f"Found {user_input} at line numbers {occurance}")
    elif len(occurance) == 0:
        print(f"{user_input} could not be found")

