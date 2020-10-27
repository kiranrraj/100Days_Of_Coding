# Title  : Find average number of digits in the list
# Author : Kiran raj R.
# Date   : 15:10:2020

list1 = [111, 2222333, 444, 1, 44,
         66666, 5555, 22222222]


def lengthElem(list_in):
    sumDigit = 0
    for elem in list_in:
        elem = str(elem)
        print(f"{elem} contain {len(elem)} digits")
        sumDigit += len(elem)
    print(
        f"Average digits per elements in the list is :{sumDigit/len(list_in)}")


lengthElem(list1)
