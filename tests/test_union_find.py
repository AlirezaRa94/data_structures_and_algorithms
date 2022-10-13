from unittest import TestCase

from data_structures.union_finds.union_find import UnionFind


class TestUnionFind(TestCase):
    def setUp(self) -> None:
        self.union_find = UnionFind(10)

    def test_find(self):
        self.assertTrue(self.union_find.connected(1, 1))
        self.assertFalse(self.union_find.connected(0, 1))

    def test_union(self):
        self.union_find.union(1, 2)
        self.union_find.union(3, 5)
        self.union_find.union(1, 5)
        self.assertTrue(self.union_find.connected(1, 2))
        self.assertTrue(self.union_find.connected(1, 3))
        self.assertFalse(self.union_find.connected(1, 8))
