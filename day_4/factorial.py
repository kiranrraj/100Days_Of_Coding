# Title  : Factorial of a number
# Author : Kiran raj R.
# Date   : 18:10:2020


def factorial(n):
    if n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

try:
    userInput = input("Enter a number to find the factorial: ")
    num = int(userInput)
    if num == 0:
        print(f"Factorial of {num} is {num}")
    else:
        result = factorial(num)
    
    print(f"Factorial of {num} is {result}")

except:
    print(f"Please enter a number with out decimal value.\nYou entered {userInput}")



