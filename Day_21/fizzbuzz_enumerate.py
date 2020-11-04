# Title  : FizzBuss using enumerate
# Author : Kiran Raj R.
# Date   : 04:11:2020

list_num = [21, 25, 30, 31, 34, 37, 41, 45, 47, 50]


def fizzbuss(list_n):
    for i, num in enumerate(list_n):
        if num % 3 == 0 and num % 5 == 0:
            list_n[i] = "fizzbuss"
        elif num % 5 == 0:
            list_n[i] = "buzz"
        elif num % 3 == 0:
            list_n[i] = "fizz"
    return list_n


print(fizzbuss(list_num))
