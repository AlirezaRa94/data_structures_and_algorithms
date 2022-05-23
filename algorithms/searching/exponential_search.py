"""
Exponential Search Algorithm
"""
from algorithms.searching.binary_search import BinarySearch


def exponential_search(data: list, target):
    n = len(data)
    bound = 1
    while bound < n and target > data[bound]:
        bound *= 2
    left = bound // 2
    right = min(bound, n - 1)
    return BinarySearch().recursive_(data, target, left, right)
