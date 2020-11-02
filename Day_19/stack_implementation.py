# Title  : Implement stack
# Author : Kiran Raj R.
# Date   : 02:11:2020

class Stack_imp:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.stack)

    def print_stack(self):
        if self.is_empty:
            length = self.length()
            for i in range(length):
                print(self.stack[i], end=" ")
            print()
        else:
            print("Stack is empty")

    def add_item(self, item):
        self.stack.append(item)
        print(f"{item} added. Stack now: {self.stack}")

    def remove_item(self, item):
        i = 0
        if self.is_empty():
            print("Stack is empty")

        while i < self.length():
            if self.stack[i] == item:
                return self.stack.pop(i)
            i += 1
        else:
            print(f"{item} not found in {self.stack}")
            return


stack1 = Stack_imp()
print(stack1.is_empty())
stack1.add_item(10)
stack1.add_item(20)
stack1.add_item(30)
stack1.add_item(40)
stack1.add_item(10)
stack1.add_item(20)
stack1.add_item(30)
stack1.add_item(40)
print(stack1.is_empty())
stack1.remove_item(30)
stack1.print_stack()
stack1.remove_item(30)
stack1.print_stack()
