# Title  : Simple Decorator with pie syntax
# Author : Kiran Raj R.
# Date   : 12/11/2020

def me_or_you(function1):
    def inner_function(name):
        print("Inner function starts.....")
        function1(name)
        print("Inner function ends.....")
    return inner_function

@me_or_you
def hello(name):
    if name == "kiran":
        print(f"Hello {name}")
        print("You can enter")
    else:
        print("You are not allowed here")

hello("kiran")
hello("ram")