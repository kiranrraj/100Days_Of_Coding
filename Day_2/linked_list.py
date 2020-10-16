class Node:
    """Creates a node of a link list"""

    def __init__(self,value):
        self.value = value
        self.link = None

class SingleLinkedList:

    def __init__(self):
        """Set the head of the linked list to None(empty linked list)"""
        self.start = None

    def createList(self):
        try:
            num = int(input("Enter the number of nodes : "))
            for index in range(num):
                val = int(input(f"Enter the value for node {index+1} : "))
                insert_atEnd(val)

    def print_linkList(self):
        """Print the nodes in the linked list"""
        if self.start == None:
            print('The list is empty.')
        else:
            elem = self.start
            while elem is not None:
                print(f"{elem.info} ", end="")
                elem = elem.link
            print()
    
    def numNodes(self):
        """Return the number of nodes in the linked list """
        elem = self.start
        count = 0
        while elem is not None:
            count +=1
        print(F"The link list contain(s) {count} nodes.")

    def searchNode(self, val):
        """Search for a node with value"""
        elem = self.start
        index = 1
        while elem is not None:
            if elem.value == val:
                print(f"The {val} is found at position {index}")
            index+=1
            elem = elem.link
        else:
            print(f"{val} not found !!")

    def insert_front(self, val):
        """Insert a new node at the front of the linked list"""
        temp = Node(val)
        temp.link = self.start
        self.start = temp

    def insert_atEnd(self, val):
        """Insert an element at the end of the linked list"""
        temp = Node(val)
        while self.start is None:
            self.start = temp
        else:
            elem = self.start
            while elem is not None:
                elem = elem.link
            elem.link = temp  

    def insert_before(self, new_val, val):
        """Insert a before after a node in linked list"""
        if self.start is None:
            print("The list is empty")
            return

        if val == self.start.value:
            new_elem = Node(new_val)
            new_elem.link = self.start
            self.start = new_elem
            return 

        elem = self.start
        while elem.link is not None:
            if elem.link.value == val:
                break
            elem = elem.link

        if elem.link is None:
            print(f"{val} not found in the linked list.")
        else:
            new_elem = Node(new_val)
            new_elem.link = elem.link
            elem.link = new_elem

    def insert_after(self, new_val, val):
        """Insert a value after a node in linked list"""
        elem = self.start
        while elem is not None:
            if elem.value == val:
                break
            elem = elem.link

        if elem is None:
            print(f"{val} not found in the linked list.")
        else:
            new_elem = Node(new_val)
            new_elem.link = elem.link
            elem.link = new_elem


    def del_firstNode(self):
        """Delete the first node in linked list"""
        if self.start == None:
            return
        self.start = self.start.linked

    def del_LastNodet(self):
        """Delete the last node in linked list"""
        if self.start == None:
            return
        if self.start.link == None:
            self.start = None
            return
        elem = self.start
        while elem.link.link is not None:
            elem = elem.link
        elem.link = None

    def del_Node(self, val):
        """Delete a node in linked list"""
        if self.start ==None:
            print("List is empty")
            return
        if self.start.info == val:
            self.start = self.start.link
            return
        elem = self.start
        while elem.link is not None:
            if elem.link.info == val:
                break
            elem = elem.link

        if elem.link is None:
            print(f"{val} not found in the linked list")
        elem.link = elem.linl.link
        
    def reverse_LL(self):
        """To reverse a linked list"""
        prevElem = None
        elem = self.start
        while elem is not None:
            nextElem = elem.link
            elem.link = prevElem
            prevElem = elem
            elem = nextElem
        self.start = prevElem


    


list = SingleLinkedList()
list.create_list()

option = int(input("Enter your choice :"))