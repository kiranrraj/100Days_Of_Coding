# Title  : Find middle element in linked list
# Author : Kiran raj R.
# Date   : 19:10:2020

# Return the middle node of a singly‑linked list (if even length, return the second middle).

def middle_node(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Time: O(n)
# Space: O(1)