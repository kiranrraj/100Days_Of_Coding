# Title  : Star triangle
# Author : Kiran Raj R.
# Date   : 09:11:2020

def print_star_left(length):
    for i in range(length):
        print(" "*(length-i),"*" *i)
print_star_left(5)

def print_star_right(length):
    for i in range(length):
        print("*" *i," "*(length-i))
print_star_right(5)

def print_star(length):
    for i in range(length):
        star = 2*i + 1
        print(" "*(length-i-1),"*"*star)
print_star(5)