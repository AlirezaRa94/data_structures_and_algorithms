"""
Binary Search Algorithm.
"""


class BinarySearch:
    @staticmethod
    def iterative(data: list, target):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == data[mid]:
                return mid
            elif target < data[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def recursive_(self, data: list, target, left: int, right: int):
        if left > right:
            return -1
        mid = (left + right) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return self.recursive_(data, target, left, mid - 1)
        else:
            return self.recursive_(data, target, mid + 1, right)

    def recursive(self, data: list, target):
        left = 0
        right = len(data) - 1
        return self.recursive_(data, target, left, right)
