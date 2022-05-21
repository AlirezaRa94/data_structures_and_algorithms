"""
Bucket Sort Data Structure
"""
import math


def bucket_sort(arr: list):
    number_of_buckets = 10
    buckets = [[] for _ in range(number_of_buckets)]
    max_elem = max(arr) if arr else 1
    min_elem = min(arr) if arr else 0
    arr_range = max_elem - min_elem + 1
    for item in arr:
        bucket_index = (number_of_buckets * (item - min_elem)) // arr_range
        buckets[bucket_index].append(item)
    i = 0
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        for j in range(len(bucket)):
            arr[i] = sorted_bucket[j]
            i += 1
    return arr
