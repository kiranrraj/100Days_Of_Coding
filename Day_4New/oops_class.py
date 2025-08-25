# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : OOP -- Class


# a class is a blueprint for creating objects (instances). 
# it bundles data (attributes) and behavior (methods).
class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def spec(self):
        return f"{self.brand} @ ₹{self.price}"

c = Computer("Dell", 50000)
print(c.spec())