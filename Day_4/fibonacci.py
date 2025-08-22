# Author    : Kiran raj R.
# Date      : 21/08/2025
# Question  : Fibonacci


# The Fibonacci sequence is a series of numbers where each number is the 
# sum of the two that precede it. The sequence typically starts with 0 and 1
def fibonacci(num):
    output = []
    f1 = 0
    f2 = 1
    output.extend((f1, f2))
    for i in range(num-2):
        sum = f1 + f2
        f1 = f2
        f2 = sum
        output.append(sum)
    return output


# Test
try:
    userInput = input("Enter count of elements in the fibonacci series: ") or 10
    limit = int(userInput)
    print(f"Fibonacci series with {limit} elements => {fibonacci(limit)}")
except:
    print("Please enter a valid number.")


# Time complexity:    O(n)
# Space complexity:   O(n)
