"""
Queue Data Structure.
"""


class Queue:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
