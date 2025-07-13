# A tuple is an ordered, immutable collection of items. 
# Tuples are often used to group related data.
# Ordered, Indexed, Immutable, Duplicates allowed, Heterogeneous.
# Each item in a tuple is associated with a number, known as a index.

t0 = (1,) # Remember the tailing comma in single element in tuple 
t1 = (1, 2, 3)
t2 = ("John", 25, True)
t3 = (1, [2,3], (4,5))


# Length
print("------ Length ------")
t4 = (10, 20, 30, 40, 50, 60, 70, 80, 80, 70, 60)
print(f"Length: {len(t4)}")

# Slicing
print("------ Slicing ------")
print(f"Print elements at index 1 and 2: {t4[1:3]}")
print(f"Print all elements excluding last two elements: {t4[:-2]}")
print(f"Print even index elements: {t4[1::2]}")

# Indexing
print("------ Indexing ------")
print(f"First element: {t4[0]}")     
print(f"Last element: {t4[-1]}")


# Count occurrences
print(f"Count of 70 in the tuple {t4} is {t4.count(70)}")
# Index of first occurrence
print(f"Index of first occurance of 60 is: {t4.index(60)}")

print("Trying to set first element to 999")
try:
    t4[0] = 999
except TypeError as e:
    print("Tuple is immutable, Error occured when try to change element:", e)


# Packing
print("----- Packing/Unpacking -----")
person = ("Ram", 30, "Developer")
name, age, job = person
print(f"{name}, {age}, {job}")

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