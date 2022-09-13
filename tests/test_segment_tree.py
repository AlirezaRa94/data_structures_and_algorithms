from typing import Optional, List
from unittest import TestCase

from data_structures.trees.segment_tree import SegmentTree


class TestHeap(TestCase):
    def setUp(self) -> None:
        self.segment_tree: Optional[SegmentTree] = None
        self.sample_data: List = [1, 10, 3, 8, 12, 9, 4, 15, 24]

    def build_sample(self):
        self.segment_tree = SegmentTree(self.sample_data)

    def test_build(self):
        self.build_sample()
        self.assertEqual(self.segment_tree.size(), len(self.sample_data) * 2)
        self.assertEqual(self.segment_tree.tree[1], sum(self.sample_data))

    def test_update(self):
        self.build_sample()
        new_val = 20
        ind = 2
        self.segment_tree.update(ind, new_val)
        tree_ind = ind + len(self.sample_data)
        self.assertEqual(self.segment_tree.tree[tree_ind], new_val)
        self.assertEqual(
            self.segment_tree.tree[1],
            sum(self.sample_data) + new_val - self.sample_data[ind]
        )

    def test_query(self):
        self.build_sample()
        l, r = 2, 7
        q = self.segment_tree.query(l, r)
        self.assertEqual(q, sum(self.sample_data[l:r]))
