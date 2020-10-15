# Title  : Reverse a given number
# Author : Kiran raj R.
# Date   : 15:10:2020

number = input("Enter a number to reverse: ")
def reverseNumber(str_num):        
    if str_num[0] == '-':                           # for negative number
        return int(str_num[-1:0:-1]) * -1 
    # elif str_num[-1] =='0':                       # for numbers ending with zero
    #     return '0' + str_num[-2::-1]              # no need ;)
    else:
        return str_num[-1::-1]

print(reverseNumber(number))



def justCheck(num):
    return num[-1::-1]

print(justCheck(number))       # Enter a number to reverse: -1234  =>  4321-