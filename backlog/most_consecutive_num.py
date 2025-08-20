# Title  : Maximum consecutive number
# Author : Kiran raj R.
# Date   : 15/07/2025

def find_consecutive_num(arr, check_num):
    count = 0
    max_count = 0
    for num in arr:
        if num == check_num:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

print(find_consecutive_num([1,1,1,0,0,0,0,0,1,1,1,1], 1))