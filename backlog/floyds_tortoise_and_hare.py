# Title  : Find circle in linked list(Floyd's tortorse and hare)
# Author : Kiran raj R.
# Date   : 17/07/2025

# If there is a node in the list that you can reach again by following .next links, 
# the list has a cycle; otherwise it’s acyclic 

# Logic
# A naïve way is to keep a set of visited nodes and on each step check 
# if the next node is already in the set—this uses O(n) extra space. 
# Floyd’s algorithm uses two pointers:
#   Slow pointer moves one step at a time.
#   Fast pointer moves two steps at a time.
# If there is no cycle, the fast pointer will reach the end (None) first.
# If there is a cycle, fast will eventually “lap” slow inside the loop, causing them to land on the same node.

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

# Time: O(n)        Each pointer moves forward; 
# Space: O(1)       Only two extra pointers, regardless of list size.