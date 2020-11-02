# Title  : Linked list :- adding element into the list
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

    def add_elem_front(self, elem):
        elem.next = self.head
        self.head = elem

    def add_elem_end(self, elem):
        # print(elem.next, elem.value)
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.next = elem
                elem.next = None
            temp = temp.next

    def add_element_b4(self, elem, key):
        temp = self.head
        while temp != None:
            if temp.next.value == key:
                elem.next = temp.next
                temp.next = elem
                return
            temp = temp.next

    def add_element_after(self, elem, key):
        temp = self.head
        while temp != None:
            if temp.value == key:
                elem.next = temp.next
                temp.next = elem
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


new_elem = Node(0)

sl_list.add_elem_front(new_elem)
sl_list.printList()

new_elem_last = Node(7)
sl_list.add_elem_end(new_elem_last)
sl_list.printList()


new_elem = Node(4.4)
sl_list.add_element_b4(new_elem, 5)
sl_list.printList()

new_elem = Node(5.4)
sl_list.add_element_after(new_elem, 5)
sl_list.printList()
