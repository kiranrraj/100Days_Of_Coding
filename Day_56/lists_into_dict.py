# Title  : Create a dictionary from list, one list element as key.
# Author : Kiran raj R.
# Date   : 25:10:2020

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list2 = [10, 11, 12, 13, 14, 15]

out_list = {elem: [] for elem in list2}
# print(out_list)

for x, y in zip(list2, list1):
    out_list[x].append(y)
print(out_list)

for x in range(len(list2)):
    inner = []
    for y in range(x*2, (2*x)+2):
        inner.append(list1[y])
    out_list[list2[x]] = inner
print(out_list)
