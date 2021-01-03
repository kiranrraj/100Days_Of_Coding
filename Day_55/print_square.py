# Title  : Print square of number, limit specified by the user.
# Author : Kiran raj R.
# Date   : 24:10:2020

userInput = input(
    "Enter the limit till you need to print the sqaure of numbers :")
square_list = []

for i in range(1, int(userInput)+1):
    square_list.append(i**2)

print(square_list)
