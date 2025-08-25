# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : Private Variables 


# encapsulation in Python OOP + Private variables
class Computer:
    # constructor
    def __init__(self):
        # Python uses name mangling for private attributes: 
        # internally __maxprice becomes _Computer__maxprice.
        # This prevents accidental access or modification from 
        # outside the class.
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    # it provides a controlled way to change the private variable.
    # It updates the actual private attribute _Computer__maxprice, 
    # so now the sell() method prints the new price
    def setMaxPrice(self, price):
        self.__maxprice = price
    
c = Computer()
c.sell()            # Selling Price: 900

# This does not change the real private variable. Instead, Python 
# creates a new attribute __maxprice in the object’s namespace 
# (not _Computer__maxprice).That’s why the price didn’t update.
c.__maxprice = 1000
c.sell()            # Selling Price: 900

c.setMaxPrice(1100)
c.sell()            # Selling Price: 1100

# object._ClassName__attribute
print(f"Access private variable before update: {c._Computer__maxprice}")
# Because Python’s “private” is not strict privacy — it’s just name mangling
c._Computer__maxprice = 2000
print(f"Access private variable after update: {c._Computer__maxprice}")
# Even though you can set private variables this way, 
# it breaks encapsulation and is discouraged.

# How Python Handles Private Variables
# Python does not have true private variables like Java or C++. Instead, it 
# uses a naming convention + name mangling: If an attribute starts with __
# and doesn’t end with double underscores, Python rewrites its name internally 
# to: _ClassName__attribute
# Can be accessed via object._ClassName__attribute

# Single underscore (_var): A weak convention meaning “for internal use only.”
# Python does not enforce it.

# Double underscore (__var): Triggers name mangling to reduce accidental 
# conflicts or misuse.