# Title  : Implements a data structure to find the first non-repeating character in a data stream using a Queue and a Hash Map.
# Author : Kiran raj R.
# Date   : 23:10:2020


from collections import deque

class StreamHandler:

    def __init__(self):
        self.queue = deque()   
        self.char_counts = {} 

    def add(self, char: str) -> None:
        # Increment the count of the character
        self.char_counts[char] = self.char_counts.get(char, 0) + 1

        # If this is the first time we see this character, add it to the queue
        if self.char_counts[char] == 1:
            self.queue.append(char)
        # If it's a repeat, we don't add it to the queue.
        # If it was already in the queue, it will be removed by getFirstUnique.

    def getFirstUnique(self) -> str:
        # Continuously remove characters from the front of the queue
        # if they are no longer unique (their count is > 1)
        while self.queue and self.char_counts[self.queue[0]] > 1:
            self.queue.popleft()

        # After cleaning, if the queue is not empty, the front element is the first unique
        if self.queue:
            return self.queue[0]
        else:
            return None # No unique character found

stream = StreamHandler()
print(f"add('a')")
stream.add('a')
print(f"getFirstUnique(): {stream.getFirstUnique()}")

print(f"add('b')")
stream.add('b')
print(f"getFirstUnique(): {stream.getFirstUnique()}") 

print(f"add('a')")
stream.add('a')
print(f"getFirstUnique(): {stream.getFirstUnique()}") 

print(f"add('c')")
stream.add('c')
print(f"getFirstUnique(): {stream.getFirstUnique()}")

print(f"add('b')")
stream.add('b')
print(f"getFirstUnique(): {stream.getFirstUnique()}") 

print(f"add('d')")
stream.add('d')
print(f"getFirstUnique(): {stream.getFirstUnique()}") 

print(f"add('c')")
stream.add('c')
print(f"getFirstUnique(): {stream.getFirstUnique()}")

print(f"add('d')")
stream.add('d')
print(f"getFirstUnique(): {stream.getFirstUnique()}") 
