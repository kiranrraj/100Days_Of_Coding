# Title  : Star triangle pattern
# Author : Kiran Raj R.
# Date   : 09:11:2020

def print_star(num):
    for i in range(0, num):
        for j in range(0,i):
            print("*", end =" ")
        print()

def print_star_invert(num):
    for i in range(num, 0, -1):
        for j in range(1,i+1):
            print("*", end =" ")
        print()


print_star(5)
print_star_invert(5)