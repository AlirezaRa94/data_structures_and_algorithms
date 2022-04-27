"""
Linear Search Algorithm.
"""


def linear_search(data: list, target):
    for item in data:
        if item == target:
            return True
    return False
