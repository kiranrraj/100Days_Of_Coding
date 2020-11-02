# Title  : Find the missing number
# Author : Kiran raj R.
# Date   : 01:11:2020

# limit = int(input("Enter the number of elements to be entered: "))
# nums = []

# for num in range(limit):
#     nums.append(num)


def find_smallest(list_in):
    num_sum = sum(list_in)
    length = len(list_in)+1

    full_sum = length * (length + 1)//2
    print(f"Missing number is :  {full_sum - num_sum}")
    # print(full_sum, num_sum)


nums1 = [1, 2, 3, 4, 6, 7]
find_smallest(nums1)

nums2 = [1, 2, 3, 4, 5, 7]
find_smallest(nums2)
