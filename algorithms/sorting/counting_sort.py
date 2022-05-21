"""
Counting Sort Algorithm
"""


def counting_sort(arr: list):
    max_elem = max(arr) if arr else -1
    counts = [0] * (max_elem + 1)
    for num in arr:
        counts[num] += 1
    i = 0
    for j in range(max_elem + 1):
        for k in range(counts[j]):
            arr[i] = j
            i += 1
    return arr
