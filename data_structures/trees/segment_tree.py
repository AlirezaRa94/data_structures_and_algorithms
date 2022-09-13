"""
Segment Tree Data Structure
"""


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * 2 * self.n
        self.build(arr)

    def size(self):
        return len(self.tree)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, ind, val):
        ind += self.n
        diff = val - self.tree[ind]
        while ind > 0:
            self.tree[ind] += diff
            ind >>= 1

    def query(self, left, right):
        left += self.n
        right += self.n
        s = 0
        while left < right:
            if left & 1:
                s += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                s += self.tree[right]
            left >>= 1
            right >>= 1
        return s
