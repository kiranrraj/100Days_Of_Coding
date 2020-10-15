# Title  : Stack implementation
# Author : Kiran raj R.
# Date   : 15:10:2020

class Stack_implementation:
    """A stack implementation using list"""
    
    def __init__(self):
        """Returns an empty list(stack)"""
        container = []

    def length(self, container):
        i = 0
        for i in container:
            i+=1
        return i

    def check_empty(self, container):
        """Checks whether a stack is empty"""
        if length(container) == 0:
            return -1
        else:
            return len(container)

    def push_item(self, container, elem):
        container.append(elem)    
        return container

    def pop_item(self, container):
        if not check_empty(container) == -1:
            return pop_item.pop()
        else:
            return "Stack is empty"

print("----------------------------------")
print("Enter your choice")
print("1. Push item")
print("2. Pop item")
print("3. Check if the stack is empty")

# User input needed 
#not complete