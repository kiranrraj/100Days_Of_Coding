# Title  : Print N binary numbers
# Author : Kiran raj R.
# Date   : 21/07/2025

import collections

def generate_binary_numbers(n: int):

    if n <= 0:
        return

    q = collections.deque()
    q.append("1")
    
    print(f"Binary numbers from 1 to {n}:")
    
    # Loop n times to generate n binary numbers
    for i in range(n):
        # Dequeue the current number and print it
        current = q.popleft()
        print(current)
        
        # Enqueue the next two numbers by appending '0' and '1'
        q.append(current + "0")
        q.append(current + "1")

generate_binary_numbers(10)