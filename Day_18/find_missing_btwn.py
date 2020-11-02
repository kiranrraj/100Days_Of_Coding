# Title  : Find the missing number between a limit
# Author : Kiran raj R.
# Date   : 01:11:2020


def find_smallest(list_in):
    smallest = min(list_in)
    num_sum = sum(list_in)
    largest = max(list_in)

    if smallest > 0:
        if smallest == 1:
            smallest_sum = 1
        else:
            smallest_sum = 0
            for i in range(smallest):
                smallest_sum += i

    full_sum = largest * (largest + 1)//2
    print(f"Missing number is :  {full_sum - (num_sum + smallest_sum)}")
    print(full_sum, num_sum, smallest_sum)


nums1 = [3, 4, 6, 7]
find_smallest(nums1)

nums2 = [3, 4, 5, 7]
find_smallest(nums2)

nums = [3, 5, 6, 7]
find_smallest(nums)
