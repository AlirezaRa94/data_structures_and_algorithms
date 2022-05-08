from unittest import TestCase

from data_structures.hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.ht = HashTable(100)

    def test_hashing(self):
        self.assertEqual(self.ht.hashing("hello"), self.ht.hashing("hello"))
        self.assertTrue(self.ht.hashing("hello") < self.ht.capacity)

    def test_insert(self):
        self.assertEqual(self.ht.size, 0)
        self.ht.insert("test_key", "test_value")
        self.assertEqual(self.ht.size, 1)
        self.assertEqual(
            self.ht.buckets[self.ht.hashing("test_key")].value,
            "test_value"
        )

    def test_find(self):
        self.assertEqual(self.ht.size, 0)
        obj = "hello"
        self.ht.insert("key1", obj)
        self.assertEqual(obj, self.ht.find("key1"))
        obj = ["this", "is", "a", "list"]
        self.ht.insert("key2", obj)
        self.assertEqual(obj, self.ht.find("key2"))

    def test_remove(self):
        self.assertEqual(self.ht.size, 0)
        obj = "test object"
        self.ht.insert("key1", obj)
        self.assertEqual(1, self.ht.size)
        self.assertEqual(obj, self.ht.remove("key1"))
        self.assertEqual(0, self.ht.size)
        self.assertEqual(None, self.ht.remove("some random key"))

    def test_capacity(self):
        # Test all public methods in one run at a large capacity
        for i in range(0, 1000):
            self.assertEqual(i, self.ht.size)
            self.ht.insert("key" + str(i), "value" + str(i))
        self.assertEqual(self.ht.size, 1000)
        for i in range(0, 1000):
            self.assertEqual(1000 - i, self.ht.size)
            self.assertEqual(
                self.ht.find("key" + str(i)),
                self.ht.remove("key" + str(i))
            )
