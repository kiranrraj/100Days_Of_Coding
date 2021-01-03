# Title  : Implement stack using linked list
# Author : Kiran Raj R.
# Date   : 02:11:2020


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack_imp:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def length(self):
        if self.head == None:
            return 0
        else:
            temp = self.head
            count = 0
            while temp != None:
                count += 1
                temp = temp.next
        return count

    def print_stack(self):
        temp = self.head
        if self.head == None:
            print("Stack is empty")
            return
        else:
            while temp != None:
                print(temp.value, end=" ")
                temp = temp.next
        print()

    def add_item(self, item):

        new_elem = Node(item)
        if self.head == None:
            self.head = new_elem
            return
        else:
            temp = self.head
            while temp != None:
                if temp.next == None:
                    temp.next = new_elem
                    return
                temp = temp.next
        return

    def remove_item(self):
        temp = self.head
        if self.head == None:
            print("Stack is empty")
            return
        else:
            while temp != None:
                if temp.next.next == None:
                    temp.next = None
                    return
                temp = temp.next


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
print(stack1.length())
stack1.print_stack()

stack1.remove_item()
stack1.print_stack()
print(stack1.length())

stack1.remove_item()
stack1.print_stack()
print(stack1.length())
