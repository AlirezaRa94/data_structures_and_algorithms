"""
Ternary Search Algorithm.
"""


class TernarySearch:
    @staticmethod
    def iterative(data: list, target):
        left = 0
        right = len(data) - 1
        while left <= right:
            partition_size = (right - left) // 3
            mid1 = left + partition_size
            mid2 = right - partition_size
            if target == data[mid1]:
                return mid1
            elif target == data[mid2]:
                return mid2
            elif target < data[mid1]:
                right = mid1 - 1
            elif data[mid2] < target:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        return -1

    def _recursive(self, data: list, target, left: int, right: int):
        if left > right:
            return -1
        partition_size = (right - left) // 3
        mid1 = left + partition_size
        mid2 = right - partition_size
        if target == data[mid1]:
            return mid1
        elif target == data[mid2]:
            return mid2
        elif target < data[mid1]:
            return self._recursive(data, target, left, mid1 - 1)
        elif data[mid2] < target:
            return self._recursive(data, target, mid2 + 1, right)
        else:
            return self._recursive(data, target, mid1 + 1, mid2 - 1)

    def recursive(self, data: list, target):
        left = 0
        right = len(data) - 1
        return self._recursive(data, target, left, right)
