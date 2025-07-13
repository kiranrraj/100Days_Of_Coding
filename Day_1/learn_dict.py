# A dictionary is an unordered, mutable, and indexed collection of key-value pairs.
# Keys must be unique and immutable (str, int, tuple). Values can be any type.

# Creating dictionaries in different ways
dict1 = {"name": "Kiranraj", "age": 30}                         # Literal syntax
dict2 = dict(name="Kiranraj", age=30)                           # Using constructor
dict3 = dict([("name", "Kiranraj"), ("age", 30)])               # From list of tuples
print(dict1, dict2, dict3)

# Accessing items safely using get()
print(dict1.get("name"))                        # Output: Kiranraj
print(dict1.get("email", "Not found"))          # Output: Not found

# Adding or updating key-value pairs
dict1["name"] = "Kiranraj R"                    # Updates name
dict1["email"] = "kiran@google.com"             # Adds email
print(dict1)

# Deleting elements
del dict1["age"]                                 # Deletes age
print(dict1)
dict1["age"] = 50                               

# pop() removes a key and returns its value
print(dict1.pop("age"))                          # Output: 50
print(dict1)                                     # age is now gone

# popitem() removes the last inserted item (Python 3.7+)
dict1["age"] = 50
print(dict1.popitem())                           # Output: (age, 50)
print(dict1)

# setdefault(): returns value if key exists, otherwise sets it
print(dict1.setdefault("age", 100))              # Adds age: 100
print(dict1)


person_info = {
    "name": "kiran",
    "age": 28,
    "email": "kiran@google.com",
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "address": {
        "street": "kiran ops",
        "city": "tvm",
        "zip": "695001"
    },
    "is_active": True,
    "projects": [
        {"title": "Weather App", "status": "completed"},
        {"title": "Stick it App", "status": "in progress"}
    ]
}

# Extract keys
keys = []
for key in person_info.keys():
    keys.append(key)
print(keys)

# Extract values
values = []
for value in person_info.values():
    values.append(value)
print(values)

# Extract key-value pairs
pairs = []
for key, value in person_info.items():
    pairs.append((key, value))
print(pairs)


person_info_2 = {
    "name": "John",
    "age": 32,
    "email": "john.doe@example.com",
    "skills": ["JavaScript", "React", "Node.js"],
    "address": {
        "street": "street1",
        "city": "Kochi",
        "zip": "690111"
    },
    "is_active": False,
    "projects": [
        {"title": "E-commerce Website", "status": "completed"},
        {"title": "Portfolio Site", "status": "pending"}
    ]
}

print("=================================")
persons = {}
persons.update(person_info)
persons.update(person_info_2)
print(persons)  # Shows only John's data for overlapping keys
