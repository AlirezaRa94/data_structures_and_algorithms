"""
Implementation of Union find data structure using quick find
"""


class QuickFindUF:
    def __init__(self, n):
        self.ids = [i for i in range(n)]

    def connected(self, p: int, q: int):
        return self.ids[p] == self.ids[q]

    def union(self, p: int, q: int):
        pid = self.ids[p]
        qid = self.ids[q]
        for i in range(len(self.ids)):
            if self.ids[i] == pid:
                self.ids[i] = qid
