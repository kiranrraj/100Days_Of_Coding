# Title  : Find sub array of specified sum
# Author : Kiran raj R.
# Date   : 31:10:2020

def find_sub_array(list_in, sum_list):

    list_start = 0
    list_end = 0
    current_sum = list_in[0]
    length = len(list_in)

    if length < 1:
        print(f"List has length of zero")

    while list_end < length:
        if current_sum == sum_list:
            print(
                f"Sub array of sum {sum_list} is {list_in[list_start+1 : list_end+1]}")

        if current_sum < sum_list:
            list_end += 1
            current_sum += list_in[list_end]
        else:
            current_sum -= list_in[list_start]
            list_start += 1
    return -1


find_sub_array([1, 2, 3, 4, 5, 6, 7], 12)
