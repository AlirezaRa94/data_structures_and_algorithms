"""
Bubble Sort Algorithm.
"""


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        # This is for checking if array is already sorted, return it.
        is_sorted = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            return arr
    return arr
