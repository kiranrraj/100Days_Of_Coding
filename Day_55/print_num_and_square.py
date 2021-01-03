# Title  : Print number and square as tuple
# Author : Kiran raj R.
# Date   : 24:10:2020

userInput = input(
    "Enter the limit till you need to print the sqaure of numbers :")
square_tup = ()

for i in range(1, int(userInput)+1):
    square_tup += (i, i**2)

try:
    for j in range(0, len(square_tup), 2):
        print(f"({square_tup[j]}, {square_tup[j+1]})")

except IndexError:
    print("Finish printing")
