"""
Merge Sort Algorithm
"""


class MergeSort:
    @staticmethod
    def _merge(list1: list, list2: list, merged: list):
        i = 0
        j = 0
        while i + j < len(merged):
            if i >= len(list1) or (j < len(list2) and list2[j] < list1[i]):
                merged[i + j] = list2[j]
                j += 1
            else:
                merged[i + j] = list1[i]
                i += 1

    def sort(self, arr):
        # Divide arr into half
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2

        # sort each half
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])

        self._merge(left, right, arr)
        return arr
