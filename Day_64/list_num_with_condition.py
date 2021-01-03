# Title  : Print all numbers between a range with some condition. 
# Author : Kiran raj R.
# Date   : 22:10:2020

user_limit = int(input("Enter a limit under 10000 :"))
user_not_multi = int(input("Enter a number you dont want a multipler of in the list :"))
user_multi = int(input("Enter a number you want a multipler of in the list :"))

def printNumber(limit, notNum, num):
    out_list = []
    # print(limit, notNum,num)

    for i in range(limit):
        if (i % user_not_multi != 0) and (i % user_multi == 0):
            out_list.append(i)

        # if i % notNum == 0:
        #     continue
        # if i % num == 0:
        #     out_list.append(i)

    return out_list

print( printNumber(user_limit, user_not_multi, user_multi))