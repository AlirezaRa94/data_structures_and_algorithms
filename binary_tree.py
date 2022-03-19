class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _is_leaf(root: Node):
        return not root.left_child and not root.right_child

    def height(self):
        return self._height(self.root)

    def _height(self, root: Node):
        if not root:
            return -1
        if self._is_leaf(root):
            return 0

        return 1 + max(self._height(root.left_child), self._height(root.right_child))

    def min(self):
        return self._min(self.root)

    def _min(self, root: Node):
        if self._is_leaf(root):
            return root.value

        return min(root.value, self._min(root.left_child), self._min(root.right_child))

    def is_binary_search_tree(self, tree):
        if not tree:
            return False
        return self._is_binary_search_tree(tree.root, minimum=float('-inf'), maximum=float('inf'))

    def _is_binary_search_tree(self, node: Node, minimum: float, maximum: float):
        if not node:
            return True
        return minimum < float(node.value) < maximum\
            and self._is_binary_search_tree(node.left_child, minimum=minimum, maximum=float(node.value))\
            and self._is_binary_search_tree(node.right_child, minimum=float(node.value), maximum=maximum)
