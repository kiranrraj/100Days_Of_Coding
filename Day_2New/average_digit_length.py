# Author    : Kiran raj R.
# Date      : 19/08/2025
# Question  : Find average number of digits in the list

list1 = [111, 2222333, 444, 1, 44, 66666, 5555, 22222222]

# Function to calculate average number of digits
def lengthElem(list_in):
    sumDigit = 0 

    for elem in list_in:
        # Convert number to string to count digits
        elem = str(elem)  
        print(f"{elem} contain {len(elem)} digits")
        sumDigit += len(elem)

    avg = sumDigit / len(list_in)
    print(f"Average digits per elements in the list is : {avg}")

lengthElem(list1)
