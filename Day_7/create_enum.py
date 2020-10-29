# Title  : Implement a simple singly linked list
# Author : Kiran raj R.
# Date   : 21:10:2020

class Node:
    """Creates a node of a link list"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:

    def __init__(self):
        """Set the head of the linked list to None(empty linked list)"""
        self.start = None

    def createList(self):
        num = int(input("Enter the number of nodes : "))
        for index in range(num):
            val = int(input(f"Enter the value for node {index+1} : "))
            # print(val)
            self.insert_atEnd(val)

    def insert_atEnd(self, val):
        """Insert an element at the end of the linked list"""
        temp = Node(val)
        # print(temp.next, temp.value)
        while self.start is None:
            self.start = temp
            # print(self.start)
        else:
            elem = self.start
            while elem is not None:
                print(elem.next, elem.value)
                elem = elem.next
                elem.next = temp

    def print_linkList(self):
        """Print the nodes in the linked list"""
        if self.start == None:
            print('The list is empty.')
        else:
            elem = self.start
            while elem is not None:
                print(f"{elem.info} ", end="")
                elem = elem.next
            print()


myList = SingleLinkedList()

myList.createList()
