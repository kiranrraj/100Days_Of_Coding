# Title  : Timing function with decorator
# Author : Kiran Raj R.
# Date   : 13/11/2020

import functools
import time

def timer_function(function):
    """Print time taken to execute a function"""
    @functools.wraps(function)
    def inner_function(name):
        start = time.perf_counter()
        function(name)
        end = time.perf_counter()
        total = end-start
        print(start, end)
        print(f"The function finished in {total:.4f}")
    return inner_function

@timer_function
def greet(name):
    i=0
    while i<1000:
        print(f"Hello,{name}")
        i+=1

greet("kiran")