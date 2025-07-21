# Title  : Reverse the order of the first k elements of the queue
# Author : Kiran raj R.
# Date   : 21/07/2025

# Given a queue of integers and an integer k, write a function to reverse the order of the first k elements of the queue.

import collections

def reverse_k_elements(q: collections.deque, k: int):

    if not q or k <= 0 or k > len(q):
        print("Invalid input.")
        return

    stack = []
    
    # Dequeue the first k elements and push onto a stack
    for _ in range(k):
        stack.append(q.popleft())
        
    # Pop from the stack and enqueue back to the queue
    while stack:
        q.append(stack.pop())
        
    # Rotate the remaining n-k elements
    for _ in range(len(q) - k):
        q.append(q.popleft())

my_queue = collections.deque([10, 20, 30, 40, 50, 60])
k = 4

print(f"Original Queue: {list(my_queue)}")
reverse_k_elements(my_queue, k)
print(f"Queue after reversing first {k} elements: {list(my_queue)}")