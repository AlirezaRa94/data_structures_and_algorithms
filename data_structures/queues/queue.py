"""
Queue Data Structure.
"""


class Queue:
    def __init__(self):
        self.items = list()
        self.front = 0

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            first_item = self.items[self.front]
            self.front += 1
            return first_item

    def peek(self):
        if not self.is_empty():
            return self.items[self.front]
