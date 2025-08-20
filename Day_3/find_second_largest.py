# Author    : Kiran raj R.
# Date      : 20/08/2025
# Question  : Find the second largest number (Method-1)

def find_second_largest(arr):

    if len(arr) < 2:
        return "List too short"

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    if second != float('-inf'):
        return second
    else:
        return "No second largest"

print(find_second_largest([1,2,3,4,5,6] ))
print(find_second_largest([10,2,5,70,8,9,12,4,11,90]))