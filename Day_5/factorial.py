# Author    : Kiran raj R.
# Date      : 22/08/2025
# Question  : Factorial of a number


def factorial(n):
    if n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result


# Test
try:
    userInput = input("Enter a number to find the factorial: ") or 5
    num = int(userInput)
    if num < 3:
        print(f"Factorial of {num} is {num}")
    else:
        result = factorial(num)

    print(f"Factorial of {num} is {result}")

except:
    print(
        f"Please enter a number with out decimal value.\nYou entered {userInput}")


# Time complexity:    O(n)
# Space complexity:   O(n)