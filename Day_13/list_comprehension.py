# Title  : List comprehension examples
# Author : Kiran raj R.
# Date   : 27:10:2020


# Transpose of a matrix
list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
out = [[row[i] for row in list1] for i in range(2)]
print(out)


# Square of elements
square = [i*i for i in range(1, 11)]
print(square)


# Print vowels
name = "kiran raj r"
vowels_in_name = [i for i in name if i in 'aeiou']
print(vowels_in_name)


# Print only positive values(including zero)
val = [1, -2, 3, 4, -5, -6, 7, 0]
positive_val = [i if i >= 0 else 0 for i in val]
print(positive_val)


# Print even numbers
even_num = [num for num in range(1, 21) if num % 2 == 0]
print(even_num)


# Create a dictionary
odd_dict = {num: num**3 for num in range(1, 21) if num % 2 != 0}
print(odd_dict)

# Create a dictionary
list1 = ['Trivandrum', 'Chennai', 'Mumbai', 'Jaipur']
list2 = ['kerala', 'tamil nadu', 'maharastra', 'rajasthan']

out = {x: y for x, y in zip(list1, list2)}
print(out)
