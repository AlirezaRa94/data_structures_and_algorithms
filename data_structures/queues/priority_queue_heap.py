"""
Implementation of Priority Queue Using Heap Data Structure
"""
from data_structures.trees.heap import Heap


class PriorityQueueWithHeap:
    def __init__(self):
        self.items = Heap()

    def __len__(self):
        return self.items.size

    def is_empty(self):
        return self.items.size == 0

    def enqueue(self, value: int):
        return self.items.insert(value)

    def dequeue(self):
        try:
            return self.items.remove()
        except IndexError:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items.heap[0]
