"""
Implementation of union find data structure using quick union
"""


class UnionFind:
    def __init__(self, n: int):
        self.ids = list(range(n))
        self.sz = [1] * n

    def find(self, i: int):
        while self.ids[i] != i:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        if i != j:
            if self.sz[i] < self.sz[j]:
                self.ids[i] = j
                self.sz[j] += self.sz[i]
            else:
                self.ids[j] = i
                self.sz[i] += self.sz[j]
