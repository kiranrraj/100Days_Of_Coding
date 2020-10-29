# Title  : Get binary numbers from user, convert it into integer
#           and print if it is an even number.
# Author : Kiran raj R.
# Date   : 24:10:2020

binary_list = input("Enter the binary numbers : ").split()

for binaryNum in binary_list:
    integerNum = int(binaryNum, 2)

    if integerNum % 2 == 0:
        print(f"Binary rep : {binaryNum} Integer rep: {integerNum}")
