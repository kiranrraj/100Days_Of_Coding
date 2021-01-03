# Title  : Nested list comprehension examples
# Author : Kiran raj R.
# Date   : 27:10:2020

# Print all elements in the nested list
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
out = [elem for listedlist in list1 for elem in listedlist]
print(out)

list2 = [[1, 2, ], [3], [4, 5, 6], [7, 8, 9], [11, 12, 13, 14]]
out = [elem for listedlist in list2 for elem in listedlist]
print(out)


# Return elements in a nested list which satisfy certain condition
list2 = [[1, 2, ], [3], [4, 5, 6], [7, 8, 9], [11, 12, 13, 14]]
out = [elem for listedlist in list2 for elem in listedlist if elem < 10]
print(out)


# find the maximum values of each sub list
list2 = [[1, 2], [3], [4, 5, 6], [7, 8, 9], [11, 12, 13, 14]]
out = [max(listedlist) for listedlist in list2]
print(out)


# Find the max value in the nested list
list2 = [[100, 2], [3], [49, 5, 6], [99, 8, 9], [11, 120, 13, 14]]
out = max([elem for listedlist in list2 for elem in listedlist])
print(out)

# Remove duplicate elements
list1 = [[1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 7, 1], [2, 5, 8]]
out = list(set([elem for linked in list1 for elem in linked]))
print(out)

# Convert element string in the list to list element
list2 = ['a', 'abc', 'abcd', 'b', 'c', 'abcde']
out = [char for elem in list2 for char in elem]
print(out)

# tuple into dictionary using list comprehension
list_tuple = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0)]
out = [{elem[0]: elem[1]} for elem in list_tuple]
print(out)
