"""
Linear Search Algorithm.
"""


def linear_search(data: list, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1
