# Title  : Find the percentage of odd/even elements
# Author : Kiran raj R.
# Date   : 15:10:2020

list1 = [1, 2, 4, 0, 0, 8, 3, 5, 2, 3, 1, 34, 42]

def print_percentage(list_in):
    count_odd = 0
    count_even = 0
    count_0 = 0
    length = len(list_in)

    for elem in list_in:
        if elem == 0:
            count_0 += 1  # Count zero separately
        elif elem % 2 == 1:
            count_odd += 1  # Odd number
        else:
            count_even += 1  # Even number (not zero)

    # Calculate percentage for each type
    p_odd = (count_odd / length) * 100
    p_even = (count_even / length) * 100
    p_0 = (count_0 / length) * 100

    # Print results
    print(f"Percentage of odd numbers in the list : {p_odd:.2f}%")
    print(f"Percentage of even numbers in the list : {p_even:.2f}%")
    print(f"Percentage of zero's in the list       : {p_0:.2f}%")

print_percentage(list1)
