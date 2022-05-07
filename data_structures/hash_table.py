class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.buckets: list = [None] * self.capacity

    def hashing(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hashing(key)
        node = self.buckets[index]
        new_node = Node(key, value)
        self.size += 1
        if node is None:
            self.buckets[index] = new_node
        else:
            while node.next is not None:
                node = node.next
            node.next = new_node

    def find(self, key):
        index = self.hashing(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.value

    def remove(self, key):
        index = self.hashing(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        result = node.value
        self.size -= 1
        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = node.next
        return result
