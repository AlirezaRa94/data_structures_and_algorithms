from unittest import TestCase

from data_structures.queues.priority_queue import PriorityQueue


class TestPriorityQueue(TestCase):
    def setUp(self) -> None:
        self.pq = PriorityQueue()
        self.sample_data = [10, 3, 12, 5, 1, 4, 8, 7, 8]

    def enqueue_items(self):
        for item in self.sample_data:
            self.pq.enqueue(item)

    def test_enqueue_empty_priority_queue(self):
        self.assertEqual(len(self.pq), 0)
        self.pq.enqueue(10)
        self.assertEqual(len(self.pq), 1)
        self.assertEqual(self.pq.items, [10])

    def test_enqueue(self):
        self.assertEqual(len(self.pq), 0)
        self.enqueue_items()
        self.assertEqual(len(self.pq), len(self.sample_data))
        self.assertEqual(self.pq.items, sorted(self.sample_data))

    def test_dequeue_empty_priority_queue(self):
        self.assertEqual(len(self.pq), 0)
        self.assertIsNone(self.pq.dequeue())

    def test_dequeue(self):
        self.enqueue_items()
        self.assertEqual(self.pq.dequeue(), max(self.sample_data))
        self.assertEqual(len(self.pq), len(self.sample_data) - 1)

    def test_peek_empty_priority_queue(self):
        self.assertEqual(len(self.pq), 0)
        self.assertIsNone(self.pq.peek())

    def test_peek(self):
        self.enqueue_items()
        self.assertEqual(self.pq.peek(), max(self.sample_data))
        self.assertEqual(len(self.pq), len(self.sample_data))
