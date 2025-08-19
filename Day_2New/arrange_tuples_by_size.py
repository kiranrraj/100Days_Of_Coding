# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : Arrange tuples by number of elements



tuple_list = [
    (3, 23, 6, 13), 
    (10, 40, 30), 
    (72, 36),
    (1, 2, 3, 4, 5), 
    (1,), 
    (2, 3)
]

# Function to return the length of a tuple
def length_tuple(tn):
    return len(tn)

# Sort the list in-place by length of each tuple
tuple_list.sort(key=length_tuple)

print(tuple_list)