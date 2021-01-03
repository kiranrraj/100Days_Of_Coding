# Title  : Mono character elements in a list
# Author : Kiran raj R.
# Date   : 16:10:2020

list1 = [111, 2222333, 444, 1, 414,
         66666, 5555, 22222322, 34, 56]

for elem in list1:
    elem = str(elem)
    for char in elem:
        if not elem[0] == char:
            break
    else:
        print(elem)

out = [elem for elem in list1 if all(
    str(char) == str(elem)[0] for char in str(elem))]
print(f"Mono character elements are {out}")
