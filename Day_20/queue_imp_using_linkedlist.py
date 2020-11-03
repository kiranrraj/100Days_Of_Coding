# Title  : Queue implementation using linked list
# Author : Kiran Raj R.
# Date   : 03:11:2020

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.head = None

    def print_queue(self):
        if self.head == None:
            print("The queue is empty")
            return
        else:
            print("The queue is : [", end="")
            temp = self.head
            while temp != None:
                print(temp.value, end=" ")
                temp = temp.next
            print("]")
        return

    def enqueue(self, elem):
        temp = self.head
        new_elem = Node(elem)
        # print(new_elem.value, new_elem.next)
        if self.head == None:
            self.head = new_elem
            return
        else:
            while temp != None:
                if temp.next == None:
                    temp.next = new_elem
                    return
                temp = temp.next
        return

    def dequeue(self):
        if self.head == None:
            print(f"The queue is empty")
            return
        else:
            self.head = self.head.next
        return


queue_1 = Queue()
queue_1.enqueue(10)
queue_1.enqueue(20)
queue_1.enqueue(30)
queue_1.enqueue(40)
queue_1.enqueue(50)
queue_1.enqueue(60)
queue_1.print_queue()
queue_1.dequeue()
queue_1.dequeue()
queue_1.print_queue()
