# Title  : Add elements of nested list
# Author : Kiran raj R.
# Date   : 25:10:2020

result = []
list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
list2 = [[11, 12], [13, 14], [15, 16], [17, 18]]

for a, b in zip(list1, list2):
    inner = []
    for i in range(len(a)):
        inner.append(a[i] + b[i])
    result.append(inner)

print(result)
