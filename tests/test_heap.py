from unittest import TestCase

from data_structures.trees.heap import Heap


class TestHeap(TestCase):
    def setUp(self) -> None:
        self.heap = Heap()
        self.sample_data = [1, 10, 3, 8, 12, 9, 4, 15, 24]

    def insert_items(self):
        for number in self.sample_data:
            self.heap.insert(number)

    def test_insert_empty_heap(self):
        self.assertEqual(self.heap.size, 0)
        self.heap.insert(15)
        self.assertEqual(self.heap.size, 1)
        self.assertEqual(self.heap.heap, [15])

    def test_insert(self):
        self.assertEqual(self.heap.size, 0)
        self.insert_items()
        self.assertEqual(self.heap.size, 9)
        self.assertEqual(self.heap.heap, [24, 15, 9, 12, 8, 3, 4, 1, 10])

    def test_remove_empty_heap(self):
        self.assertEqual(self.heap.size, 0)
        with self.assertRaises(IndexError) as context:
            self.heap.remove()
            self.assertTrue("Heap is empty!" in context.exception)

    def test_remove(self):
        self.insert_items()
        self.assertEqual(self.heap.size, 9)
        removed_item = self.heap.remove()
        self.assertEqual(removed_item, max(self.sample_data))
        self.assertEqual(self.heap.size, 8)
        self.assertEqual(self.heap.heap[0], 15)

    def test_heap_sort_asc(self):
        self.assertEqual(self.heap.size, 0)
        sorted_data = self.heap.heap_sort_asc([*self.sample_data])
        self.assertEqual(sorted_data, sorted(self.sample_data))

    def test_heap_sort_desc(self):
        self.assertEqual(self.heap.size, 0)
        sorted_data = self.heap.heap_sort_desc([*self.sample_data])
        self.assertEqual(sorted_data, sorted(self.sample_data, reverse=True))

    def test_heapify(self):
        self.assertEqual(self.heap.size, 0)
        data = Heap.heapify([*self.sample_data])
        self.assertEqual(data, [24, 15, 9, 10, 12, 3, 4, 1, 8])

    def test_kth_largest_element(self):
        self.assertEqual(self.heap.size, 0)
        self.assertEqual(
            self.heap.kth_largest_element(self.sample_data, 3),
            12
        )
