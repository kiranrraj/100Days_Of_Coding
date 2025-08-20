# Title  : Amstrong
# Author : Kiran raj R.
# Date   : 16:10:2020

digi_list = []

try:
    userInput = int(
        input("Enter a number to find whether it is amstrong or not :"))
    user_in = userInput
except:
    print("Please enter a valid number")


while userInput > 0:
    digit = userInput % 10
    digi_list.append(digit)
    userInput = userInput//10


def amstrong_number(numList):

    exp = len(numList)
    sum = 0

    for num in numList:
        sum = sum + num ** exp

    if sum == user_in:
        print(f"{user_in} is a amstrong number")
    else:
        print(f"{user_in} is not a amstrong number")


amstrong_number(digi_list)

# print(digi_list)
