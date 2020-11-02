# Title  : Palindrome and generators
# Author : Kiran raj R.
# Date   : 31:10:2020

def isPalindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    rev_num = 0

    while temp != 0:
        rev_num = (rev_num*10) + (temp % 10)
        temp = temp//10

    if rev_num == num:
        return num
    else:
        return False


# for i in range(1000):
#     p_num = isPalindrome(i)
#     # print(p_num)
#     if p_num:
#         print(p_num)


def range_num():
    num = 0
    while True:
        yield num
        num += 1
        print(isPalindrome(num))


yeild_ispalindrome = range_num()

next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
next(yeild_ispalindrome)
