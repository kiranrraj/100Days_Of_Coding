# Title  : Number of tuple equal to a user specified value
# Author : Kiran raj R.
# Date   : 31:10:2020

def find_tuple(list_in, sum_in):
    length = len(list_in)
    count_tup = 0
    list_tuples = []

    if(sum(list_in) < sum_in) | length < 1:
        print(f"Cannot find any combination of sum {sum_in}")

    for i in range(length-2):
        tuple_with_sum = set()
        current_sum = sum_in - list_in[i]

        for j in range(i+1, length):
            if(current_sum - list_in[j]) in tuple_with_sum:
                count_tup += 1
            tuple_with_sum.add(list_in[j])
            for k in range(j+1, length):
                sub = [list_in[i], list_in[j], list_in[k]]
                if sum(sub) == sum_in:
                    list_tuples.append(sub)
    print(f"The number of tuples with sum {sum_in} is: {count_tup}")
    print(f"The tuples are: {list_tuples}")


find_tuple([1, 2, 3, 4, 7, 6], 7)
find_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
find_tuple([1, 3, 4, 5, 2], 9)
find_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
