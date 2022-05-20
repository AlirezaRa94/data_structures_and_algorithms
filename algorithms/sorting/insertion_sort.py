"""
Insertion Sort Algorithm
"""


def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr

