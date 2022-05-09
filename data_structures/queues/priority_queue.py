"""
Priority Queue Data Structure
"""


class PriorityQueue:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value: int):
        if not self.is_empty():
            for i, item in enumerate(self.items):
                if value < item:
                    self.items.insert(i, value)
                    return self.items
        self.items.append(value)
        return self.items

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
