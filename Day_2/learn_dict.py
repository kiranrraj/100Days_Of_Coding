# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : Learn Dictionary in Python
#----------------------------------------------------------
# A dictionary is an unordered, mutable, and indexed collection of 
# key-value pairs. Keys must be unique and immutable 
# (str, int, tuple). Values can be any type.

# Creating dictionaries
# Literal syntax
dict1 = {"name": "Kiranraj", "age": 30} 
# Using constructor
dict2 = dict(name="Kiranraj", age=30)   
# From list of tuples
dict3 = dict([("name", "Kiranraj"), ("age", 30)]) 


# Accessing items
dict4 = {"brand": "Ford", "model": "Mustang"}
# Using square brackets
# If the key does not exist, this method will raise a KeyError
print(dict4["brand"])


# get() method
# The get() method is safer because it returns None 
# or a specified default value, if the key is not found, 
# rather than raising an error.
dict1 = {"name": "Kiranraj", "age": 30} 
print(dict1.get("name"))                
print(dict1.get("email", "Not found")) 


# Adding key-value pairs
my_dict = {"brand": "Ford", "model": "Mustang"}
my_dict["color"] = "red"
print(my_dict)


# Changing value
my_dict["color"] = "blue"
print(my_dict)


# Deleting elements
dict1 = {"name": "Kiranraj", "age": 30} 
del dict1["age"]  
print(dict1) # {'name': 'Kiranraj'}
dict1["age"] = 50                               


# pop() removes a key and returns its value
print(dict1.pop("age"))  # 50
print(dict1) 


# popitem() removes the last inserted item (Python 3.7+)
dict1["age"] = 50
print(dict1.popitem()) # ('age', 50)
print(dict1) # {'name': 'Kiranraj'}


# setdefault(): returns value if key exists, otherwise sets it
print(dict1.setdefault("age", 100)) # 100
print(dict1) # {'name': 'Kiranraj', 'age': 100}


person_info = {
    "name": "kiran",
    "age": 28,
    "email": "kiran@google.com",
    "skills": ["Python", "Machine Learning"],
}

# Extract keys
keys = []
for key in person_info.keys():
    keys.append(key)
print(keys) # ['name', 'age', 'email', 'skills']


# Extract values
values = []
for value in person_info.values():
    values.append(value)
print(values) 
# ['kiran', 28, 'kiran@google.com', ['Python', 'Machine Learning']] 


# Extract key-value pairs
pairs = []
for key, value in person_info.items():
    pairs.append((key, value))
print(pairs)
# [
#   ('name', 'kiran'), 
#   ('age', 28), 
#   ('email', 'kiran@google.com'), 
#   ('skills', ['Python', 'Machine Learning'])
# ]


person_info_2 = {
    "name": "John",
    "age": 32,
}

persons = {}
persons.update(person_info)
persons.update(person_info_2)
print(persons)  
# Shows only John's data for overlapping keys
# {
#   'name': 'John', 
#   'age': 32, 
#   'email': 'kiran@google.com', 
#   'skills': ['Python', 'Machine Learning']
# }


# Dictionary Comprehensions
list1 = [1,2,3,4,5]
dict1 = {x: x**2 for x in list1}
print(dict1) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Create a new dictionary with only even values
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}
print(even_dict) # {'b': 2, 'd': 4}


# Merge dict
# If there are duplicate keys, the value from the dictionary 
# on the right-hand side of the operator will overwrite the 
# value from the left.
dict1 = {"a": 1, "b": 2, "e": 10}
dict2 = {"c": 3, "d": 4, "e": 100}
merged_dict = dict1 | dict2
print(merged_dict) # {'a': 1, 'b': 2, 'e': 100, 'c': 3, 'd': 4}
merged_dict2 = dict2 | dict1
print(merged_dict2) # {'c': 3, 'd': 4, 'e': 10, 'a': 1, 'b': 2}

# Data Structure	Lookup Time (Average)	Use Case
# Dictionary	    O(1)	                Storing and retrieving values by a unique key.
# List	            O(n)	                Ordered collections where element position matters.
# Set	            O(1)	                Storing unique items for fast membership checks.