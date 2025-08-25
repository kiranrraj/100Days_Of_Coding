# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : Class Attributes

#### Class Attributes
# 1. Defined directly inside the class body (not inside __init__).
# 2. Shared across all instances of the class.
# 3. Belong to the class itself, not to individual objects.


class Car:
    wheels = 4    # class attribute

    def __init__(self, brand):
        self.brand = brand  # instance attribute

a = Car("Toyota")
b = Car("BMW")

print(a.wheels, b.wheels)   # 4 4 
print(Car.wheels)           # 4 

#### Instance Attributes?
# 1. Defined inside methods (usually __init__) using self.
# 2. Unique to each object.
# 3. Belong to the instance, not the class.

print(a.brand, b.brand)     # Toyota BMW


# When you access obj.attr, Python checks:
# 1. If an attribute exists on the instance, Python uses that.
# 2. Otherwise, it falls back to the class attribute.

# | Feature      | Class Attribute               | Instance Attribute       |
# | ------------ | ----------------------------- | ------------------------ |
# | Defined in   | Class body                    | Usually in `__init__`    |
# | Belongs to   | Class (shared)                | Each instance (unique)   |
# | Accessed via | Class.attr or obj.attr        | obj.attr                 |
# | Storage      | Class.__dict__                | obj.__dict__             |
# | Shared?      | Shared across all instances   | Each object has its own  |
# | Use cases    | Constants, defaults, config   | Object-specific data     |

