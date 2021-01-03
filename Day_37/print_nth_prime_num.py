# Title  : Print nth prime number 
# Author : Kiran Raj R.
# Date   : 20/11/2020


def isPrime(userNum):
    # if userNum in [0, 1]:
    #     return False
    for num in range(2, userNum):
        if userNum % num == 0:
            # print(num)
            return False
    return True

def print_nth_prime(num):

    number = 2
    count = 0

    if num <1:
        return "Enter a number greater than 0"
    while True:
        if isPrime(number):
            count = count + 1
        
        if count == num:
            return number
            break
        number = number + 1


        
    # if num < 1:
    #     return "Number should be greater than zero"
    # count = 0
    # number = 1
    # while count != num and number < 3:
    #     number += 1
    #     if isPrime(number):
    #         count += 1
    # while count != num:
    #     number += 2
    #     if isPrime(number):
    #         count += 1
    # return number

print(print_nth_prime(11))
print(print_nth_prime(15))
print(print_nth_prime(0))
print(print_nth_prime(1))
print(print_nth_prime(2))
print(print_nth_prime(-1))