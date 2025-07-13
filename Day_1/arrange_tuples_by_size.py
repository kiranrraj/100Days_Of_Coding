# Title  : Arrange tuples by number of elements
# Author : Kiran raj R.
# Date   : 15:10:2020

# List of tuples with varying lengths
tuple_list = [(3, 23, 6, 13), (10, 40, 30), (72, 36),
              (1, 2, 3, 4, 5), (1,), (2, 3)]

# Function to return the length of a tuple
def length_tuple(tn):
    return len(tn)

# Sort the list in-place by length of each tuple
tuple_list.sort(key=length_tuple)

# Print the sorted list
print(tuple_list)