# Title  : Print the nested list with max sum
# Author : Kiran raj R.
# Date   : 23:10:2020

def max_nested_sum(n_list):
    max_sum = 0
    for list_in in n_list:
        sum_num = 0
        for i in range(len(list_in)):
            sum_num = sum_num+list_in[i]
        if max_sum < sum_num:
            max_sum = sum_num
            max_list = list_in
    print(f"The nested list {max_list} has the maximum sum: {max_sum}")


max_nested_sum([[1], [2], [3], [4, 5], [6, 7, 8], [9, 0, 1]])
max_nested1 = [[1], [2], [3], [4, 5], [6, 7, 8], [9, 0, 1]]
print(max(max_nested1, key=sum))

max_nested_sum([[1], [200], [3, 33], [4, 11], [6, 7, 8], [9, 0, 1]])
max_nested2 = [[1], [200], [3, 33], [4, 11], [6, 7, 8], [9, 0, 1]]
print(max(max_nested2, key=sum))

max_nested_sum([[1], [2, 22, 33], [3], [4, 5], [6, 7, 8], [9, 0, 1]])
max_nested3 = [[1], [2, 22, 33], [3], [4, 5], [6, 7, 8], [9, 0, 1]]
print(max(max_nested3, key=sum))
