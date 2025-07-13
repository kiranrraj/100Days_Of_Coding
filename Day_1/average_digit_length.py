# Title  : Find average number of digits in the list
# Author : Kiran raj R.
# Date   : 15:10:2020

list1 = [111, 2222333, 444, 1, 44, 66666, 5555, 22222222]

# Function to calculate average number of digits
def lengthElem(list_in):
    sumDigit = 0  # Track total number of digits

    for elem in list_in:
        elem = str(elem)  # Convert number to string to count digits
        print(f"{elem} contain {len(elem)} digits")
        sumDigit += len(elem)  # Add digit count

    # Calculate and print average digits per number
    avg = sumDigit / len(list_in)
    print(f"Average digits per elements in the list is : {avg}")

lengthElem(list1)
