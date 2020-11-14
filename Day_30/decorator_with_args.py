# Title  : Decorator function with argument
# Author : Kiran Raj R.
# Date   : 13/11/2020


def repeat(function=None, *, rep):
    def decorator(func):
        def inner_func(name):
            for _ in range(rep):
                func(name)
        return inner_func

    if function is None:
        return decorator
    else:
        return decorator(function)


@repeat(rep=3)
def greet(name):
    print(f"Hello {name}")

greet('kiran')