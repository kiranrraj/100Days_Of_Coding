# Title  : Print all numbers, where digits are even number
# between a user specified limit
# Author : Kiran raj R.
# Date   : 24:10:2020

down_limit = int(input("Enter a lower limit (greater than 1000) : "))
up_limit = int(input("Enter a upper limit (less than 10000): "))
list_num = []

if (down_limit < up_limit) and down_limit > 1000 and up_limit < 10000:
    for num in range(down_limit, up_limit):
        strNum = str(num)
        if (int(strNum[0]) % 2 == 0) and (int(strNum[1]) % 2 == 0) and (int(strNum[2]) % 2 == 0) and (int(strNum[3]) % 2 == 0):
            list_num.append(strNum)

print(list_num)
