import math


class Heap:
    def __init__(self):
        self.heap = list()
        self.size = 0

    @staticmethod
    def _parent(index: int):
        return math.floor((index-1) / 2)

    @staticmethod
    def _left_index(index):
        return index * 2 + 1

    @staticmethod
    def _right_index(index):
        return index * 2 + 2

    def _left(self, index: int):
        left_index = self._left_index(index)
        if left_index < self.size:
            return self.heap[left_index]
        return None

    def _right(self, index: int):
        right_index = self._right_index(index)
        if right_index < self.size:
            return self.heap[right_index]
        return None

    def _max_child(self, index):
        max_child_index, max_child = index, self.heap[index]
        if self._left(index):
            if self.heap[index] < self._left(index):
                max_child_index, max_child = self._left_index(index), self._left(index)
            if self._right(index):
                if self._right(index) > max_child:
                    max_child_index, max_child = self._right_index(index), self._right(index)

        return max_child_index, max_child

    def _swap(self, first: int, second: int):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def _bubble_up(self):
        index = self.size - 1
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _bubble_down(self):
        index = 0
        max_child_index, max_child = self._max_child(index)
        while self.heap[index] < max_child:
            self._swap(index, max_child_index)
            max_child_index, max_child = self._max_child(max_child_index)

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._bubble_up()
        print(self.heap)

    def remove(self):
        if not self.heap:
            raise IndexError("Heap is empty!")
        self._swap(0, -1)
        self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self._bubble_down()
        print(self.heap)


h = Heap()
h.insert(10)
h.insert(5)
h.insert(17)
h.insert(4)
h.insert(22)
h.remove()
h.remove()
h.remove()
h.remove()
h.remove()
