from unittest import TestCase

from algorithms.sorting.bubble_sort import bubble_sort


class TestSortingAlgorithms(TestCase):
    def setUp(self) -> None:
        self.long_data = [12, -3, 34, 0, 22, 13, 11, 5, 54, 10, 13]
        self.two_data = [1, 0]
        self.one_data = [0]
        self.empty_data = []

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.long_data), sorted(self.long_data))
        self.assertEqual(bubble_sort(self.two_data), sorted(self.two_data))
        self.assertEqual(bubble_sort(self.one_data), sorted(self.one_data))
        self.assertEqual(bubble_sort(self.empty_data), sorted(self.empty_data))
