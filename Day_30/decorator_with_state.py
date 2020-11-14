# Title  : Decorator function with state
# Author : Kiran Raj R.
# Date   : 13/11/2020


def count(func):
    def inner_f(args):
        inner_f.num += 1
        print(f"Count {inner_f.num}")
        return func(args)
    inner_f.num = 0
    return inner_f

@count
def greet(name):
    print(f"Hello {name}")

greet('kiran')
greet('kiran')
greet('kiran')
greet('kiran')

