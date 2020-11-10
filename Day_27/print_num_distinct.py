# Title  : Number Pattern distinct
# Author : Kiran Raj R.
# Date   : 10:11:2020

def print_num_pattern(num):
    k=0
    for i in range(0, num):
        for j in range(0,i):
            k+=1
            print(k, end =" ")
        print()

print_num_pattern(5)

print("-------------------------")
def print_num_pattern_invert(num):
    k=0
    for i in range(num, 0, -1):
        for j in range(1,i+1):
            print(k, end =" ")
            k+=1
        print()

print_num_pattern_invert(4)