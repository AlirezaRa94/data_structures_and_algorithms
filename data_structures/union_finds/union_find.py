"""
Implementation of union find data structure using quick union
"""


class UnionFind:
    def __init__(self, n: int):
        self.ids = list(range(n))
        self.sz = [1] * n

    def root(self, i: int):
        while self.ids[i] != i:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def find(self, p: int, q: int):
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        if i != j:
            if self.sz[i] < self.sz[j]:
                self.ids[i] = j
                self.sz[j] += self.sz[i]
            else:
                self.ids[j] = i
                self.sz[i] += self.sz[j]
