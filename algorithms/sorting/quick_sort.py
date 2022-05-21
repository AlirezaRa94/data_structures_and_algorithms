"""
Quick Sort Algorithm
"""


class QuickSort:
    @staticmethod
    def _partitioning(arr: list, start: int, end: int):
        pivot = arr[end]
        b = start - 1
        for i in range(start, end + 1):
            if arr[i] <= pivot:
                b += 1
                arr[b], arr[i] = arr[i], arr[b]
        return b

    def _sort(self, arr: list, start: int, end: int):
        if start >= end:
            return arr
        b = self._partitioning(arr, start, end)
        self._sort(arr, start, b - 1)
        self._sort(arr, b + 1, end)
        return arr

    def sort(self, arr: list):
        return self._sort(arr, 0, len(arr) - 1)
