# Title  : Number Pattern
# Author : Kiran Raj R.
# Date   : 10:11:2020


def print_num_pattern(num):
    for i in range(1, num+1):
        for j in range(0,i):
            print(i, end =" ")
        print()

print_num_pattern(5)

print("---------------------------")

def print_num_pattern(num):
    for i in range(1, num+1):
        for j in range(1,i+1):
            print(j, end =" ")
        print()

print_num_pattern(5)