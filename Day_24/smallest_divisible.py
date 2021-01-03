# Title  : Find the smallest number divisible by 1 to 10
# Author : Kiran Raj R.
# Date   : 07:11:2020

def smallest_num(num_range):
    i = 0
    while 1:
        i += num_range * (num_range - 1)
        flag = 0
        for j in range(2, num_range):
            if i % j != 0:
                flag = 1
                break
        if flag == 0:
            if i == 0:
                i = 1
            return i

print(smallest_num(10))
