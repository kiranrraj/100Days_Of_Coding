# Title  : Find the positive missing element in the list
# Author : Kiran raj R.
# Date   : 31:10:2020


def find_positive_missing(list_in):

    length = len(list_in)
    positive_list = []

    for i in range(length):
        if list_in[i] > 0:
            positive_list.append(list_in[i])

    smallest = min(positive_list)
    num_sum = sum(positive_list)
    largest = max(positive_list)

    if smallest > 0:
        if smallest == 1:
            smallest_sum = 1
        else:
            smallest_sum = 0
            for i in range(smallest):
                smallest_sum += i

    full_sum = largest * (largest + 1)//2
    print(f"Missing number is :  {full_sum - (num_sum + smallest_sum)}")
    # print(full_sum, num_sum, smallest_sum)


nums1 = [3, -1, -3, 0, 4, -5, -7, 6, 0, 0, -1, 7]
find_positive_missing(nums1)

nums2 = [3, 0, 0, 0, -1.-2.-3, 4, -1, -10, -11, 5, 0, -1, -2, 7]
find_positive_missing(nums2)

nums = [3, 5, 6, 7]
find_positive_missing(nums)
