# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : Private Variables 


# private variables behave in inheritance
class Base:
    def __init__(self):
        self.__a = 100
    
    def showVal(self):
        return self.__a

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__a = 200

    def showValChild(self):
        return self.__a

c = Child()
print(f"Give me valu of a from Base class: {c.showVal()}") 
# Give me valu of 'a' from Base class: 100

print(f"Give me valu of a from Child class: {c.showValChild()}")
# Give me valu of 'a' from Child class: 200

print(c.__dict__)
# {'_Base__a': 100, '_Child__a': 200}
# In Base, __a is mangled to _Base__a.
# In Child, __a is mangled to _Child__a.
# When you inherit, each class keeps its own version of private 
# variables because of name mangling. They don’t override each 
# other like normal variables would.

print(c._Base__a)   # 100
print(c._Child__a)  # 200

# Private variables are class-specific.
# Name mangling prevents accidental overriding.
# Direct access is possible (not recommended)