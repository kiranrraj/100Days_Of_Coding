# Title  : Linked list implementation in python with search
# Author : Kiran raj R.
# Date   : 30:10:2020

class Node:
    """Create a node with value provided, the pointer to next is set to None"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Simply_linked_list:
    """create a empty singly linked list """

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def search_list(self, item):
        temp = self.head
        while temp.next != None:
            temp = temp.next

            if temp.value == item:
                print(f"Found {temp.value}")
                break


sl_list = Simply_linked_list()
sl_list.head = Node(1)
node2 = Node(2)
node3 = Node(3)

sl_list.head.next = node2
node2.next = node3

sl_list.printList()
sl_list.search_list(20)
sl_list.search_list(2)
sl_list.search_list(3)
