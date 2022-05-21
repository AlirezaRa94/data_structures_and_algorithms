from typing import Callable
from unittest import TestCase

from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import MergeSort
from algorithms.sorting.quick_sort import QuickSort
from algorithms.sorting.selection_sort import selection_sort


class TestSortingAlgorithms(TestCase):
    def setUp(self) -> None:
        self.long_data = [12, -3, 34, 0, 22, 13, 11, 5, 54, 10, 13]
        self.two_data = [1, 0]
        self.one_data = [0]
        self.empty_data = []

    def base_test_sort(self, function: Callable):
        self.assertEqual(function([*self.long_data]), sorted(self.long_data))
        self.assertEqual(function([*self.two_data]), sorted(self.two_data))
        self.assertEqual(function([*self.one_data]), sorted(self.one_data))
        self.assertEqual(function([*self.empty_data]), sorted(self.empty_data))

    def test_bubble_sort(self):
        self.base_test_sort(bubble_sort)

    def test_selection_sort(self):
        self.base_test_sort(selection_sort)

    def test_insertion_sort(self):
        self.base_test_sort(insertion_sort)

    def test_merge_sort(self):
        self.base_test_sort(MergeSort().sort)

    def test_quick_sort(self):
        self.base_test_sort(QuickSort().sort)
