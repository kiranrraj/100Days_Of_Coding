# Title  : Linked list insert element
# Author : Kiran Raj R.
# Date   : 09:11:2020

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        start = self.head
        while start:
            print(start.data)
            start = start.next

    def append_list(self, data):
        new_elem = Node(data)
        start = self.head
        
        if start is None:
            start = new_elem
            return
        
        while start.next is None:
            start = start.next
            start.next = new_elem

    def prepand_list(self, data):
        new_elem = Node(data)
        new_elem.next = self.head
        self.head = new_elem

    def index_after(self, index, data):
        start = self.head
        new_elem = Node(data)

        if not start:
            print("The list is empty")

        new_elem.next = index.next
        index.next = new_elem

    def index_before(self, index, data):

        start = self.head
        new_elem = Node(data)

        if not start:
            print("The list is empty")

        while start:
            if start.next == index:
                new_elem.next = start.next
                start.next =index
            start = start.next



