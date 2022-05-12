from unittest import TestCase
from unittest.mock import patch

from data_structures.trees.trie import Trie


class TestTrie(TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

    def test_initialize_trie(self):
        self.assertIsNone(self.trie.root.value)
        self.assertEqual(len(self.trie.root.children), 0)
        self.assertIsInstance(self.trie.root, Trie.Node)

    def test_insert_empty_trie(self):
        word = "book"
        self.trie.insert(word)
        current = self.trie.root
        for char in word:
            self.assertTrue(current.has_child(char))
            current = current.get_child(char)
        self.assertTrue(current.is_end_of_word)

    def test_insert(self):
        word_1 = "bag"
        word_2 = "baggage"
        self.trie.insert(word_1)
        self.trie.insert(word_2)
        current = self.trie.root
        for char in word_1:
            self.assertTrue(current.has_child(char))
            current = current.get_child(char)
        self.assertTrue(current.is_end_of_word)
        for char in word_2[len(word_1):]:
            self.assertTrue(current.has_child(char))
            current = current.get_child(char)
        self.assertTrue(current.is_end_of_word)

    def test_contains(self):
        word = "bag"
        self.trie.insert(word)
        self.assertTrue(self.trie.contains(word))

    def test_not_contains(self):
        word_1 = "bag"
        word_2 = "book"
        self.trie.insert(word_2)
        self.assertFalse(self.trie.contains(word_1))

    def test_not_contains_not_end(self):
        word_1 = "bag"
        word_2 = "baggage"
        self.trie.insert(word_2)
        self.assertFalse(self.trie.contains(word_1))

    @patch('builtins.print')
    def test_preorder_traversal(self, mock_print):
        word = "book"
        self.trie.insert(word)
        self.trie.preorder_traversal()
        mock_print.assert_called_with(" ".join(word))

    @patch('builtins.print')
    def test_postorder_traversal(self, mock_print):
        word = "book"
        self.trie.insert(word)
        self.trie.postorder_traversal()
        mock_print.assert_called_with(" ".join(reversed(word)))

    def test_remove(self):
        word = "book"
        self.trie.insert(word)
        self.trie.remove(word)
        self.assertFalse(self.trie.contains(word))

    def test_remove_overlapping_words(self):
        word_1 = "care"
        word_2 = "car"
        self.trie.insert(word_1)
        self.trie.insert(word_2)
        self.trie.remove(word_1)
        self.assertFalse(self.trie.contains(word_1))
        self.assertTrue(self.trie.contains(word_2))

    def test_remove_not_exists_word(self):
        word_1 = "care"
        word_2 = "car"
        self.trie.insert(word_2)
        self.trie.remove(word_1)
        self.assertTrue(self.trie.contains(word_2))

    def test_remove_empty_word(self):
        self.trie.remove("")

    def test_auto_completion(self):
        sample_words = ["car", "care", "carpet", "cat", "egg"]
        start = "car"
        for word in sample_words:
            self.trie.insert(word)
        words = self.trie.auto_completion(start)
        self.assertEqual(
            words,
            [word for word in sample_words if word.startswith(start)]
        )

    def test_contains_recursive(self):
        pass

    def test_count_words(self):
        pass

    def test_longest_common_prefix(self):
        pass
