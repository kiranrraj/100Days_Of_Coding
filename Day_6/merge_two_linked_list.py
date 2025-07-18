# Title  : Merge Two Sorted Lists
# Author : Kiran raj R.
# Date   : 18/07/2025

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    # Create a dummy head node for the merged list.
    dummy_head = ListNode()
    # "current" pointer will traverse the merged list.
    current = dummy_head

    # Iterate while both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If one of the lists is not finished, append the rest of it.
    # Since both original lists are sorted, the remaining part is already sorted.
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # The merged list starts from dummy_head.next
    return dummy_head.next

# Helper function to create a linked list from a list of values
def create_linked_list(arr: list[int]) -> ListNode | None:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values for printing
def linked_list_to_list(head: ListNode | None) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Testing...
#-----------
list1_1 = create_linked_list([1, 2, 4])
list1_2 = create_linked_list([1, 3, 4])
merged_list1 = mergeTwoLists(list1_1, list1_2)
print(f"Test Case 1: Input: [1,2,4], [1,3,4], Output: {linked_list_to_list(merged_list1)}")

list2_1 = create_linked_list([])
list2_2 = create_linked_list([])
merged_list2 = mergeTwoLists(list2_1, list2_2)
print(f"Test Case 2: Input: [], [], Output: {linked_list_to_list(merged_list2)}")