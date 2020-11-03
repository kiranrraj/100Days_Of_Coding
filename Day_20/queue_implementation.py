# Title  : Queue implementation using lists
# Author : Kiran Raj R.
# Date   : 03:11:2020

class Queue:
    def __init__(self):
        self._queue = []
        self.head = self.length()

    def length(self):
        return len(self._queue)

    def print_queue(self):
        if self.length == self.head:
            print("The queue is empty")
            return
        else:
            print("[", end="")
            for i in range(self.length()):
                print(self._queue[i], end=" ")
            print("]")
        return

    def enqueue(self, elem):
        self._queue.append(elem)
        print(f"{elem} added. The queue now {self._queue}")
        return

    def dequeue(self):
        if self.length() == self.head:
            print(f"The queue is empty")
            return
        else:
            elem = self._queue.pop(self.head)
            print(
                f"Removed {elem}. The queue now {self._queue}")
        return


queue_1 = Queue()
queue_1.enqueue(10)
queue_1.enqueue(20)
queue_1.enqueue(30)
queue_1.enqueue(40)
queue_1.enqueue(50)
queue_1.enqueue(60)
queue_1.dequeue()
queue_1.dequeue()
queue_1.print_queue()
