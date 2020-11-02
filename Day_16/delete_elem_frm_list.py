# Title  : Linked list :- delete element from the list
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
        linked_list = []
        temp = self.head
        while(temp):
            linked_list.append(temp.value)
            temp = temp.next
        print(f"The elements are {linked_list}")

    def search_list(self, item):
        temp = self.head
        while temp.next != None:
            temp = temp.next

            if temp.value == item:
                print(f"Found {temp.value}")
                break

    def delete_element(self, elem):
        temp = self.head

        if self.head == None:
            return print("Empty linked List")

        while temp != None:
            if temp.next.value == elem:
                temp.next = temp.next.next
                return
            temp = temp.next


sl_list = Simply_linked_list()
sl_list.head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

sl_list.head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sl_list.printList()
sl_list.delete_element(5)
sl_list.printList()
