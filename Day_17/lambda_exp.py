# Title  : Lambda example
# Author : Kiran raj R.
# Date   : 31:10:2020

def higher_o_func(x, func): return x + func(x)


result1 = higher_o_func(2, lambda x: x * x)
# result1  x = 2, (2*2) + 2, x = 6

result2 = higher_o_func(2, lambda x: x + 3)
# result2 x=2, (2 + 3) + 2, x = 7

result3 = higher_o_func(4, lambda x: x*x)
# result3 = (4 * 4) + 4, x = 20

result4 = higher_o_func(4, lambda x: x + 3)
# result4 (4 + 3) + 4, x = 11

print(result1, result2)
print(result3, result4)


# add = lambda x, y: x+y
def add(x, y):
    return x+y


result5 = add(3, 4)
print(result5)

print((lambda x: x % 2 and 'odd' or 'even')(3))
# odd

# bool(2%2) => False
# bool(2%3) => True
#
