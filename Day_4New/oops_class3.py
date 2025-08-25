# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : OOP -- Class


class Rectangle:
    # unit lives on the class, so every instance sees it unless 
    # it shadows it with its own unit. If you change Rectangle.unit, 
    # it affects all instances that haven’t shadowed it.
    unit = "cm"                 # class attribute

    # Runs when you create a new Rectangle
    def __init__(self, w, h):   # Constructors 
        self.w = w
        self.h = h

    # Always include self as the first parameter for instance methods.
    def area(self):             # instance method
        return self.w * self.h

    @classmethod
    def set_unit(cls, u):       # class method
        cls.unit = u

    @staticmethod
    def is_positive(*nums):     # static method
        return all(n > 0 for n in nums)

r = Rectangle(3, 4)
print(r.area())    # 12

# Rectangle.set_unit("mm") or r.set_unit("mm")
Rectangle.set_unit("mm")

# Shadowing
r.unit = "in" # now r has its own unit 
print(f"Class attribute unit's value: {Rectangle.unit}")  # "mm"
print(f"Shadow (Instance) of unit's value: {r.unit}")   # "in"

print(Rectangle.is_positive(3, 4))  # True
