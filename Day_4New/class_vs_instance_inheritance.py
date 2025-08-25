# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : Inheriting Class Attributes

# Inheriting Class Attributes
class Parent:
    species = "Human"   # class attribute

class Child(Parent):
    pass

# Each instance looks up the attribute from its own 
# class, falling back to the parent if not found.
print(Parent.species)   # Human
# Child doesn’t define species, so lookups on Child fall back to Parent.
print(Child.species)    # Human

Parent.species = "Super Human"
print(Parent.species)   # Super Human
print(Child.species)    # Super Human


# Overriding Class Attributes
class Parent:
    species = "Human"

class Child(Parent):
    # Child defines its own species. This shadows/overrides the parent’s.
    # From this point, changing Parent.species won’t affect Child.species.
    # They’re separate attributes stored on different classes.
    species = "Super Human"

print(Parent.species)   # Human
print(Child.species)    # Super Human


c = Child()
print(c.species)            # Super Human
# It creates an attribute on that instance only.
c.species = "Ultra Human"
print(c.species)            # Ultra Human
print(Child.species)        # Super Human

# Attribute lookup order (simplified):
# 1. c.__dict__ (instance namespace)
# 2. Child.__dict__ (class namespace)
# 3. Parent classes


print(c.__dict__)                   # {'species': 'Ultra Human'}
print(Child.__dict__["species"])    # Super Human
print(Parent.__dict__["species"])   # Human

# Class attribute: 
#   lives on the class object; shared as a default by all instances (unless shadowed).

# Instance attribute: 
#   lives on a specific object (in obj.__dict__); affects only that object.

# Shadowing: 
#   if an attribute exists on the instance, it hides the class attribute of the same name for that instance.

# Inheritance: 
#   a child class inherits parent class attributes unless it defines its own with the same name.

### Once Child overrides, Parent changes won’t affect Child’s value.