from typing import Callable
from unittest import TestCase

from algorithms.searching.binary_search import BinarySearch
from algorithms.searching.exponential_search import exponential_search
from algorithms.searching.jump_search import jump_search
from algorithms.searching.linear_search import linear_search
from algorithms.searching.ternary_search import TernarySearch


class TestSearchingAlgorithms(TestCase):
    def setUp(self) -> None:
        self.long_data = [-23, -5, -3, -1, 0, 2, 5, 8, 12, 13]
        self.one_data = [0]
        self.empty_data = []

    def base_test(self, function: Callable):
        self.assertEqual(self.long_data.index(12), function(self.long_data, 12))
        self.assertEqual(-1, function(self.long_data, -6))
        self.assertEqual(self.one_data.index(0), function(self.one_data, 0))
        self.assertEqual(-1, function(self.one_data, 2))
        self.assertEqual(-1, function(self.empty_data, 2))

    def test_linear_search(self):
        self.base_test(linear_search)

    def test_binary_search_iterative(self):
        self.base_test(BinarySearch.iterative)

    def test_binary_search_recursive(self):
        self.base_test(BinarySearch().recursive)

    def test_ternary_search_iterative(self):
        self.base_test(TernarySearch.iterative)

    def test_ternary_search_recursive(self):
        self.base_test(TernarySearch().recursive)

    def test_jump_search(self):
        self.base_test(jump_search)

    def test_exponential_search(self):
        self.base_test(exponential_search)
