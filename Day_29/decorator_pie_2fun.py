# Title  : Simple Decorator with pie syntax
# Author : Kiran Raj R.
# Date   : 12/11/2020

def me_or_you(function):
    def inner_function(name):
        if name == 'kiran':
            function(name)
        else:
            function(name)
    return inner_function

@me_or_you
def hello_me(name):
    print(f"Hello {name}")
    print("You can enter")

@me_or_you
def hello_you(name):
    print(f"Sorry {name}, you are not allowed here")


hello_me('kiran')
hello_you('Ram')