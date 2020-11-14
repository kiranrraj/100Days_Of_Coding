# Title  : Simple Decorator
# Author : Kiran Raj R.
# Date   : 12/11/2020

def my_decorator(function):
    def inner_function(name):
        print("This is a simple decorator function output")
        function(name)
        print("Finished....")
    return inner_function

def greet_me(name):
    print(f"Hello, Mr.{name}")

decor = my_decorator(greet_me)
decor('kiran')

def me_or_you(function1, function2):
    def inner_function(name):
        if name == 'kiran':
            function1(name)
        else:
            function2(name)
    return inner_function

def hello_me(name):
    print(f"Hello {name}")
    print("You can enter")

def hello_you(name):
    print(f"Sorry {name} not allowed here")


decor2 = me_or_you(hello_me, hello_you)
decor2('kiran')
decor2('ram')