# Title  : Fibonacce #Method 1
# Author : Kiran Raj R.
# Date   : 07:11:2020

def fibonacci_1(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
       return fibonacci_1(n-1) + fibonacci_1(n-2)
   
print(fibonacci_1(11))