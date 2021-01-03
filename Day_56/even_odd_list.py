# Title  : Create seperate list for odd and even numbers from a list
# Author : Kiran raj R.
# Date   : 26:10:2020

main_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
even_list = []
odd_list = []

for elem in main_list:
    if elem == 0 or elem % 2 == 0:
        even_list.append(elem)
    else:
        odd_list.append(elem)

print(f"Odd list {odd_list}")
print(f"Even list {even_list}")
