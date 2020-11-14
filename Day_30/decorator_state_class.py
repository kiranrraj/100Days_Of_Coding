# Title  : Decorator class with state
# Author : Kiran Raj R.
# Date   : 13/11/2020

class Count:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, args):
        self.count += 1
        print(f"Count {self.count}")
        return self.func(args)

@Count
def greet(name):
    print(f"Hello {name}")

greet('kiran')
greet('kiran')
greet('kiran')
greet('kiran')