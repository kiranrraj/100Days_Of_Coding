# Title  : Print number with zero
# Author : Kiran Raj R.
# Date   : 18/11/2020

rem = 0

def num_zero(num):
    org_num = num
    while num > 0:
        rem = num % 10
        if rem == 0:
            print(f"The number contains zero: {org_num}")
            return
        else:
            num = num //10
    return


for i in range(77, 145):
    num_zero(i)
