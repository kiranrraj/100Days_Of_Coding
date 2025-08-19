# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : Learn Tuples in Python
#----------------------------------------------------------
# A tuple is an ordered, indexed, "immutable" collection of items. 
# Tuples are often used to group related data. 
# Duplicates allowed, Heterogeneous.
# Use a tuple when you have a collection of items that should not 
# change.

# Tuples are generally more memory efficient and faster than lists. 
# Because their size is fixed, Python can allocate a single block 
# of memory for the tuple, which is more efficient than the dynamic 
# memory allocation required for lists.

tempty = ()
t0 = (1,) # Remember the tailing comma in single element in tuple,
          # if not provided, python will not consider it as tuple.
t1 = (1, 2, 3)
t2 = ("John", 25, True)
t3 = (1, [2,3], (4,5))
t4 = (10, 20, 30, 40, 50, 60, 70, 80, 80, 70, 60)


# once a tuple is created, you cannot change its contents. 
# If you try to modify it, you'll get an error.
print("Trying to set first element to 999")
try:
    t4[0] = 999
except TypeError as e:
    print("!!!Error: Tuple is immutable. ", e)
# However, if a tuple contains mutable objects like a list, 
# you can modify the mutable object itself.
my_tuple = ("apple", [1, 2, 3], "cherry")
my_tuple[1][0] = 99
print(my_tuple)


# Length
print("------ Length ------")
print(f"Length: {len(t4)}")


# Indexing
print("------ Indexing ------")
print(f"First element: {t4[0]}")     
print(f"Last element: {t4[-1]}")


# Slicing
# The slice [start:end] includes the start index but 
# excludes the end index.
print("------ Slicing ------")
print(f"Print elements at index 1 and 2: {t4[1:3]}")
print(f"Print all elements excluding last two elements: {t4[:-2]}")
print(f"Print alternate elements: {t4[::2]}")


# Count occurrences
print(f"Count of 70 in the tuple {t4} is {t4.count(70)}")
# Index of first occurrence
print(f"Index of first occurance of 60 is: {t4.index(60)}")


print("----- Packing/Unpacking -----")
# Packing
person = ("Ram", 30, "Developer")
# Unpacking
name, age, job = person
print(f"{name}, {age}, {job}")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *rest) = fruits
print(green)
print(yellow)
print(rest)


# Tuple operation
print("----- Tuple operation -----")
a = (1, 2, 3, 4, 5, 6)
b = (10, 11, 12, 13, 14)


# Concatenation
print(f"{a} + {b} is {a+b}") 
print(f"{a} * 2 is {a*2}") 


# Membership test
print(f"20 in {t4} ? {20 in t4}")   
print(f"1000 in {t4} ? {1000 in t4}") 


# Buitin functions 
print(f"Max value in {t4}: {max(t4)}") 
print(f"Min value in {t4}: {min(t4)}")
print(f"Sum of elements in {t4} is: {sum(t4)}") 
print(f"Sorted: {sorted(t4)}")


# Tuples are hashable, meaning their value is constant over 
# time, so they can be used as keys in a dictionary. 
my_dictionary = { ("John", 30): "Engineer", ("Doe", 25): "Doctor" }
print(my_dictionary[("John", 30)])


print("----- Trying Tuple Mutations  -----")
try:
    t4.append(100)
except AttributeError as e:
    print("Cannot append to a tuple:", e)
try:
    t4.insert(1, 200)
except AttributeError as e:
    print("Cannot insert into a tuple:", e)
try:
    del t4[0]
except TypeError as e:
    print("Cannot delete item from a tuple:", e)