# Title  : Print Prime Number till the specified limit
# Author : Kiran raj R.
# Date   : 16:10:2020

userInput = int(input("Enter the limit of the prime number : "))


def primeLimit(limit):

    for num in range(2, limit):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


primeLimit(userInput)
