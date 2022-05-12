"""
Trie Data Structure
"""


class Trie:
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = dict()
            self.is_end_of_word = False

        def __str__(self):
            return f"value = {self.value}"

        def has_child(self, char: str):
            return char in self.children

        @property
        def has_children(self):
            return len(self.children) > 0

        def add_child(self, char: str):
            self.children[char] = self.__class__(char)

        def remove_child(self, char: str):
            del self.children[char]

        def get_child(self, char: str):
            return self.children.get(char)

        def get_children(self):
            return self.children.values()

    def __init__(self):
        self.root = self.Node(None)

    def insert(self, word: str):
        current = self.root
        for letter in word:
            if not current.has_child(letter):
                current.add_child(letter)
            current = current.get_child(letter)
        current.is_end_of_word = True

    def contains(self, word: str):
        current = self.root
        for letter in word:
            if not current.has_child(letter):
                return False
            current = current.get_child(letter)
        return current.is_end_of_word

    def contains_recursive(self):
        pass

    def count_words(self):
        pass

    def _remove(self, word: str, node, index: int):
        if index == len(word):
            node.is_end_of_word = False
            return
        child = node.get_child(word[index])
        if child is None:
            return
        self._remove(word, child, index + 1)
        if not child.has_children and not child.is_end_of_word:
            node.remove_child(word[index])

    def remove(self, word: str):
        self._remove(word, self.root, 0)

    def _preorder_traversal(self, start, items: list):
        """
        In pre-ordered traversal we should visit the root first and then go
        down
        ":param start: The root of our sub-trie
        """
        items.append(start)
        for child in start.get_children():
            self._preorder_traversal(child, items)
        return items

    def preorder_traversal(self):
        nodes = self._preorder_traversal(self.root, [])
        print(" ".join(
            [node.value for node in nodes if node.value is not None]
        ))

    def _postorder_traversal(self, start, items: list):
        """
        In post-ordered traversal we should visit leaves and then go up
        :param start: The root of our sub-trie
        """
        for child in start.get_children():
            self._postorder_traversal(child, items)
        items.append(start)
        return items

    def postorder_traversal(self):
        nodes = self._postorder_traversal(self.root, [])
        print(" ".join(
            [node.value for node in nodes if node.value is not None]
        ))

    def _get_last_node(self, string: str):
        last_node = self.root
        for letter in string:
            if not last_node.has_child(letter):
                return None
            last_node = last_node.get_child(letter)
        return last_node

    def _auto_completion(self, word: str, node, words: list):
        if node is None:
            return words
        if node.is_end_of_word:
            words.append(word)
        for child in node.get_children():
            self._auto_completion(word+child.value, child, words)
        return words

    def auto_completion(self, start: str):
        words = list()
        last_node = self._get_last_node(start)
        return self._auto_completion(start, last_node, words)

    def longest_common_prefix(self):
        pass
