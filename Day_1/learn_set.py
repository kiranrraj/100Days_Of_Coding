# A set is an unordered, unindexed, mutable collection of unique elements.

# Create Sets
s1 = {1, 2, 3, 4}
print(f"Set1: {s1}")
s2 = {"apple", 3.14, True}
print(f"Set2: {s2}")
s3 = set([1, 22, 3, 3, 4, 4])
print(f"Set3: {s3}")
s4 = set("banana")
print(f"Set4: {s4}")

# Length and membership
s5 = {1, 7, 4, 9, 5, 8}
print(f"Length of set {s5} is: {len(s5)}")
print(f"2 is in {s5} ? {2 in s5}")

# Add elements to set
s5.add(10)
print(f"After adding 10 to set: {s5}")

s5.update([50, 60], (10, 80), {40, 20})
print(f"After update {s5}")

# Remove elements from a set using remove()
s5.remove(10)
print(f"After removing 10 from set: {s5}")
try:
    s5.remove(10)
except KeyError as e:
    print(f"Error due to element not found")

# Remove elements using discard()
try:
    s5.discard(10)
except KeyError as e:
    print(f"Error due to element not found")

# Remove random item using pop()
removedElem = s5.pop()
print(f"Element removed using pop(): {removedElem}")
print(f"Set now: {s5}")

# Built in functions
print(f"Min element: {min(s5)}") 
print(f"Max element: {max(s5)}") 
print(f"Sum of elements: {sum(s5)}") 
print(f"After sorting: {sorted(s5)}")

# Set operation
a = {1, 2, 3, 10}
b = {3, 4, 5, 6, 10}

# Union [ union() or | ]
# print(a.union(b))
print(f"Union operation of {a} and {b} is {a | b}")

# Intersection [ intersection() or & ]
# print(a & b)
print(f"Intersection operation of {a} and {b} is {a.intersection(b)}")

# Difference [ difference or -] 
# print(a - b) 
print(f"Difference of {a} and {b} is {a.difference(b)}")
print(f"Difference of {b} and {a} is {b-a}")

# Symmetric Difference [ symmetric_difference or ^]
# print(a ^ b)      
print(f"Symmetric difference of {a} and {b} is {a.symmetric_difference(b)}")

# Sets can't have mutable elements (like lists or other sets)
try:
    s = {1, 2, [3, 4]}
except TypeError as e:
    print("Set cannot have any mutable elements like list or other sets:", e)

# Frozen set
try: 
    frozen = frozenset([1, 2, 3])
    print(frozen)
    frozen.add(4)
except AttributeError as e:
    print("This is a frozenset, immutable")

# Set relations
x = {1, 2}
y = {1, 2, 3}

print(f" {x} subset of {y}? {x.issubset(y)}")
print(f" {y} superset of {x}? {y.issuperset(x)}")
print(f" {x} and {y} are disjoint sets ? {x.isdisjoint(y)}")
print(f" {x} and {10, 12, 14} are disjoint sets ? {x.isdisjoint({10, 12, 14})}")
