# Title  : Disarium number
# Author : Kiran Raj R.
# Date   : 17/11/2020

user_num = input("Enter a number : ")
sumDigi = 0
rem = 0
length = len(user_num)
user_num = int(user_num)
num = user_num

if user_num > 0:
    while user_num > 0:
        rem = user_num % 10
        sumDigi = sumDigi + rem ** length
        user_num = user_num //10
        length-=1
# print(sumDigi)

if num == sumDigi:
    print(f"The number '{num}' is a disarium number")
else:
    print(f"The number '{num}' is not a disarium number")