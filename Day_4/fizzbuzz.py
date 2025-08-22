# Author    : Kiran raj R.
# Date      : 21/08/2025
# Question  : FizzBuzz

def fizzBuzz(limit):
    result = []
    for num in range(1, limit+1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("Fizzbuzz")
            continue
        elif num % 3 == 0:
            result.append("Fizz")
            continue
        elif num % 5 == 0:
            result.append("Buzz")
            continue
        else:
            result.append(num)
    return result


# Test 
num = 15
print(f"Limit {num}: Output: {fizzBuzz(num)}")


# Time complexity:    O(n)
# Space complexity:   O(n)


# Limit 15: Output: [
#   1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 
#   'Buzz', 11, 'Fizz', 13, 14, 'Fizzbuzz'
# ]


