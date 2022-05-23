"""
Jump Search Algorithm
"""
import math


def jump_search(data: list, target):
    n = len(data)
    block_size = int(math.sqrt(n))
    start = 0
    next_start = block_size
    while start < n and target > data[next_start - 1]:
        start += block_size
        next_start = min(start + block_size, n)

    for i in range(start, next_start):
        if data[i] == target:
            return i
    return -1
