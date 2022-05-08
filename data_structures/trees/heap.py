"""
Heap Data Structure
"""


class Heap:
    def __init__(self):
        self.heap = list()
        self.size = 0

    @staticmethod
    def _parent_index(index: int):
        return (index - 1) // 2

    @staticmethod
    def _left_index(index: int):
        return index * 2 + 1

    @staticmethod
    def _right_index(index: int):
        return index * 2 + 2

    def _get_value(self, index: int):
        if 0 <= index < self.size:
            return self.heap[index]
        return None

    def _left(self, index: int):
        left_index = self._left_index(index)
        return self._get_value(left_index)

    def _right(self, index: int):
        right_index = self._right_index(index)
        return self._get_value(right_index)

    def _parent(self, index: int):
        parent_index = self._parent_index(index)
        return self._get_value(parent_index)

    def _max_child(self, index):
        max_child_index = index
        max_child = self.heap[index]
        left_child = self._left(index)
        if left_child:
            if left_child > max_child:
                max_child_index = self._left_index(index)
                max_child = left_child
            right_child = self._right(index)
            if right_child and right_child > max_child:
                max_child_index = self._right_index(index)
                max_child = right_child

        return max_child_index, max_child

    def _swap(self, a: int, b: int):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def _bubble_up(self):
        index = self.size - 1
        while index > 0 and self.heap[index] > self._parent(index):
            parent_index = self._parent_index(index)
            self._swap(index, parent_index)
            index = parent_index

    def _bubble_down(self):
        index = 0
        max_child_index, max_child = self._max_child(index)
        while self.heap[index] < max_child:
            self._swap(index, max_child_index)
            index = max_child_index
            max_child_index, max_child = self._max_child(max_child_index)

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._bubble_up()
        return self.heap

    def remove(self):
        if not self.heap:
            raise IndexError("Heap is empty!")
        # We should remove the root and replace it with the last element
        self._swap(0, -1)
        self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self._bubble_down()
        return self.heap

    def heap_sort_asc(self, numbers: list):
        self.heap = list()
        n = len(numbers)
        for number in numbers:
            self.insert(number)
        for i in range(n):
            numbers[i] = self.remove()
        return numbers

    def heap_sort_desc(self, numbers: list):
        self.heap = list()
        n = len(numbers)
        for number in numbers:
            self.insert(number)
        for i in range(n):
            numbers[n - 1 - i] = self.remove()
        return numbers
