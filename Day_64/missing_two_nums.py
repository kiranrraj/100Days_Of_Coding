# Title  : Find the missing two numbers
# Author : Kiran raj R.
# Date   : 01:11:2020

import math


def find_two_miss_num(list_in):
    num_list = 0
    num_sqr_list = 0
    length = len(list_in) + 2  # 2 for missing two numbers

    for i in list_in:
        num_list += i  # sum of numbers
        num_sqr_list += (i*i)  # sum of square of numbers

    sum_num_list = length * (length + 1) // 2  # n*(n+1)/2
    sum_num_sqr_list = length * (length + 1) * \
        (2 * length + 1)//6  # n*(n+1)*(2n+1)/6

    d1 = sum_num_list - num_list
    d2 = sum_num_sqr_list - num_sqr_list
    # print(d1, d2)
    d_calc = 2*d2 - (d1 * d1)

    result = int(math.sqrt(d_calc))
    # print(result)

    num1 = (d1 - result) // 2
    num2 = (d1 + result) // 2

    print(f"{list_in} :- Missing numbers are {num1} and {num2}")


find_two_miss_num([1, 2, 5, 6, 7])
find_two_miss_num([1, 2, 3, 4, 7])
