# Title  : Prime Number
# Author : Kiran raj R.
# Date   : 16:10:2020

userInput = int(input("Enter a number : "))


def isPrime(userNum):
    if userNum in [0, 1]:
        return "Not a prime number"

    for num in range(2, userNum):
        if userNum % num == 0:
            return"Not a prime number"

    return "Prime Number"


print(isPrime(userInput))
