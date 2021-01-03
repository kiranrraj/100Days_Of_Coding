# Title  : Linked list :- delete element at front and back of a list
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

    def delete_fist_elem(self):
        if self.head == None:
            print("The linked list is empty")
        else:
            self.head = self.head.next

    def delete_elem_end(self):
        # print(elem.next, elem.value)
        if self.head == None:
            print("The linked list is empty")
        else:
            temp = self.head
            while temp != None:
                if temp.next.next == None:
                    temp.next = None
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
sl_list.search_list(20)
sl_list.search_list(2)
sl_list.search_list(3)

print("List before deletion at start: ", end="")
sl_list.printList()
sl_list.delete_fist_elem()
print(f"List after deletion at start: ", end="")
sl_list.printList()

print("List before deletion at end: ", end="")
sl_list.printList()
sl_list.delete_elem_end()
print(f"List after deletion at end: ", end="")
sl_list.printList()
