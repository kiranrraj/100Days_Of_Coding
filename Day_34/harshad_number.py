# Title  : Harshad number
# Author : Kiran Raj R.
# Date   : 17/11/2020

user_num = int(input("Enter a number : "))
sumDigi = 0
rem = 0
num = user_num

if user_num > 0:
    while user_num > 0:
        rem = user_num % 10
        sumDigi = sumDigi + rem
        user_num = user_num //10
# print(sumDigi)

result = num % sumDigi

if result == 0:
    print(f"The number '{num}' is a harshad number")
else:
    print(f"The number '{num}' is not a harshad number")