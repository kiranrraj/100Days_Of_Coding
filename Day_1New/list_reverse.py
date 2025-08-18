# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : Reverse a list

def reverseList(nums: list) -> list:
    reverse_list = nums[:]
    left, right = 0, len(reverse_list)-1
    while left < right:
        reverse_list[left], reverse_list[right] = reverse_list[right], reverse_list[left]
        left+=1
        right-=1
    return reverse_list

print("----- Output -----")
list1 = [3,2,1,0,4,5,6,]
print(reverseList(list1))       # [6, 5, 4, 0, 1, 2, 3]


print("# Reverse the list using slice")
def reverseListSlicing(nums: list) -> list:
    return nums[::-1]

print("----- Output -----")
list2 = [3,2,1,0,4,5,6,]
print(reverseListSlicing(list2)) # [6, 5, 4, 0, 1, 2, 3]


print("# Reverse the list using built in reverse function")
print("----- Output -----")
list3 = [3,2,1,0,4,5,6,]
list3.reverse()
print(list3)                     # [6, 5, 4, 0, 1, 2, 3]