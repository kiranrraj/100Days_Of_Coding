# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate values.

nums = [10, 1, 12, 14, 3, 6, 11, 2, 5, 90, 40, 22, 18]
print(nums)
details = ["John Doe", 38, "software developer", 3000.33, ["CA", "USA" ]]
print(details)

print("\n--------Length------------")
print(f"Number of elements in the list: {len(nums)}")

print("\n--------Indexing------------")
# Indexing, access elements using index
print(f"First number {nums[0]}")
print(f"Last number {nums[-1]}")

print("\n--------Manipulation------------")
# Change element
print(f"Change number in position 2. Current elements {nums}")
nums[1] = 100
print(f"After change, Current elements {nums}")

print("\n--------Repetition------------")
zeros = [0] * 5
print(f"Repeating [0] five times: {zeros}")
ab = ['a', 'b'] * 3
print(f"Repeating ['a', 'b'] three times: {ab}")

print("\n--------Constructor------------")
# From a string
char_list = list("hello")
print(f"List from the string 'hello': {char_list}")

# From a tuple
num_tuple = (1, 2, 3)
num_list = list(num_tuple)
print(f"List from the tuple (1, 2, 3): {num_list}")

print("\n--------Slicing------------")
# Slicing of a list
print(f"First two elements: {nums[:2]}")
print(f"Omiting first two elements {nums[2:]}")
print(f"Listing element using [:] {nums[:]}")

print("\n--------Index------------")
# To get the index of the element use index()
print(f"Index of 14 is {nums.index(14)}")
# The list index() method can take three arguments:
# 1. element - the element to be searched
# 2. start (optional) - start searching from this index
# 3. end (optional) - search the element up to this index
# If the element is not found, a ValueError exception is raised.

print("\n--------Count------------")
# To get count of an elements use count()
print(f"Count number of 10 in the list {nums.count(10)}")
nums1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Count number of 4 in {nums1} is {nums1.count(4)}")

print("\n--------Reverse------------")
# To reverse a list use reverse()
# The reverse() method doesn't return any value. 
# It updates the existing list.
print(f"Current list: {nums}")
nums.reverse()
print(f"Reversed list: {nums}")
print(f"Reverse a list using slice nums[::-1]: {nums[::-1]}")

print("\n--------Sort------------")
# sort() method sorts the elements of a list.
# The sort() method can take two optional keyword arguments:
# reverse - If True is passed, the list is sorted in descending order.
# key - Comparion is based on this function.
print(f"Current list: {nums}")
nums.sort()
print(f"Sort the elements in the list: {nums}")
nums.sort(reverse = True)
print(f"Sort in descending order: {nums}")

print("\n--------Adding------------")
# Adding elements at the end using append()
nums.append(23)
print(f"Appending elements using nums.append(23): {nums}")

# To insert an element to the list at the specified index.
# The insert() method doesn't return anything; returns None. 
# It only updates the current list.
nums.insert(0, 1000)
print(f"Insert 1000 at start by nums.insert(0, 1000): {nums}")
nums.insert(3, 3000)
print(f"Insert 3000 at position 3 by nums.insert(3, 3000): {nums}")

# The extend() method adds all the items of the specified iterable, 
# such as list, tuple, dictionary, or string , to the end of a list.
# The extend() doesn't return anything; it modifies the original list.
nums1 = [3, 4, 5]
nums2 = [10, 20]
nums1.extend(nums2)
print(f"Extending {nums1} with {nums2}, result = {nums1}")
nums1 = [3, 4, 5]
nums2 = [10, 20]
print(f"Same result using + symbol {nums1 + nums2}")

print("\n--------Removing------------")
# The remove() method removes only the first matching element.
# If the element doesn't exist, it throws ValueError
# The remove() doesn't return any value (returns None).
nums.remove(1000)
print(f"List after element 1000 removed by remove(): {nums}")

# The list pop() method removes the item at the specified index. 
# The method also returns the removed item.
# Index is optional, the default value is -1(last element).
print(f"Current list: {nums}")
nums.pop(0)
print(f"After removing element at index 0: {nums}")

# The del statement can be used to delete an item at a given index.
print(f"Current list: {nums}")
del nums[:3]
print(f"After removing first 3 elements {nums}")

print("\n--------Copying------------")
# To copy the content to a new list 
numsCopy = []
print(f"Before copying numsCopy list is {numsCopy}")
numsCopy = nums.copy()
print(f"After copying numsCopy list is {numsCopy}")

print("\n--------Membership Test------------")
print(f"Is 22 in numsCopy? {'Yes' if 22 in numsCopy else 'No'}")
print(f"Is 999 not in numsCopy? {'Yes' if 999 not in numsCopy else 'No'}")

print("\n--------Aggregate Functions------------")
print(f"Max value in numsCopy: {max(numsCopy)}")
print(f"Min value in numsCopy: {min(numsCopy)}")
print(f"Sum of numsCopy: {sum(numsCopy)}")

print("\n--------Enumerate in Loop------------")
for idx, val in enumerate(numsCopy):
    print(f"Index {idx}, Value {val}")

print("\n--------Clear------------")
# To clear all the elements
nums.clear()
print(f"After calling clear on list is: {nums}")

# Create List 
squares = []
for i in range(5):
    squares.append(i * i)
print(f"Squares: {squares}")

# Using list comprehension
squares_comp = [i * i for i in range(5)]
print(f"Squares: {squares_comp}")

even_nums = [num for num in squares_comp if num % 2 == 0 and num != 0]
print(f"Even numbers from {squares_comp}: {even_nums}")

print("\n--------Zip Two Lists------------")
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped = list(zip(list1, list2))
print(f"Zipped list: {zipped}")

print("\n--------Any and All------------")
test_list = [True, True, False]
print(f"Any True? {any(test_list)}")
print(f"All True? {all(test_list)}")
