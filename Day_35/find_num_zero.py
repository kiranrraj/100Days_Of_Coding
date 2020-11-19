# Title  : Find the number of zeros in a number
# Author : Kiran Raj R.
# Date   : 18/11/2020

def num_zero(num):

    count = 0

    while num != 0:
        rem = num % 10
        if rem == 0:
            count = count + 1
        num = num // 10

    return count
    

for i in range(997, 1012):
    count = num_zero(i)
    if count > 0:
        print(f"Number '{i}' contains {count} zero(s)")
