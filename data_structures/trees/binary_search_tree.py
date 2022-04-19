class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def _insert(self, start: Node, value):
        if value < start.value:
            if start.left:
                self._insert(start.left, value)
            else:
                start.left = Node(value)
        elif value > start.value:
            if start.right:
                self._insert(start.right, value)
            else:
                start.right = Node(value)
        else:
            raise ValueError("This value already exists in tree!")

    def insert(self, value):
        self._insert(self.root, value)

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def traverse_in_order(self):
        self._traverse_in_order(self.root)

    def _traverse_in_order(self, root: Node):
        if root:
            self._traverse_in_order(root.left)
            print(root.value)
            self._traverse_in_order(root.right)

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, root: Node):
        if root:
            print(root.value)
            self._traverse_pre_order(root.left)
            self._traverse_pre_order(root.right)

    def traverse_post_order(self):
        self._traverse_post_order(self.root)

    def _traverse_post_order(self, root: Node):
        if root:
            self._traverse_post_order(root.left)
            self._traverse_post_order(root.right)
            print(root.value)

    @staticmethod
    def _is_leaf(node: Node):
        return not node.left and not node.right

    def _height(self, node: Node):
        if not node:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    def height(self):
        return self._height(self.root)

    def min(self):
        if not self.root:
            raise TypeError('Empty tree has no minimum value!')
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def _max(self, root: Node):
        if not self.root:
            raise TypeError('Empty tree has no maximum value!')
        if not root.right:
            return root.value
        return self._max(root.right)

    def max(self):
        return self._max(self.root)

    def _equals(self, node1: Node, node2: Node):
        if not node1 and not node2:
            return True
        if node1 and node2:
            node_equals = node1.value == node2.value
            left_equals = self._equals(node1.left, node2.left)
            right_equals = self._equals(node1.right, node2.right)
            return node_equals and left_equals and right_equals
        return False

    def equals(self, tree):
        if not tree:
            return True if not self.root else False
        return self._equals(self.root, tree.root)

    def swap_root(self):
        self.root.left, self.root.right = self.root.right, self.root.left

    def _is_binary_search_tree(self, start: Node, minimum: float,
                               maximum: float):
        if not start:
            return True
        val = float(start.value)
        root_is_bst = minimum < val < maximum
        left_is_bst = self._is_binary_search_tree(start.left, minimum, val)
        right_is_bst = self._is_binary_search_tree(start.right, val, maximum)
        return root_is_bst and left_is_bst and right_is_bst

    def is_binary_search_tree(self):
        return self._is_binary_search_tree(
            start=self.root,
            minimum=float('-inf'),
            maximum=float('inf')
        )

    def _get_nodes_at_k_distance(self, root: Node, dist: int, nodes: list):
        if not root:
            return
        if dist == 0:
            nodes.append(root.value)
            return
        dist -= 1
        self._get_nodes_at_k_distance(root.left, dist, nodes)
        self._get_nodes_at_k_distance(root.right, dist, nodes)

    def get_nodes_at_k_distance(self, dist: int):
        nodes_at_k_distance = list()
        self._get_nodes_at_k_distance(self.root, dist, nodes_at_k_distance)
        return nodes_at_k_distance

    def traverse_level_order(self):
        for k in range(self.height() + 1):
            for node in self.get_nodes_at_k_distance(k):
                print(node)

    def _size(self, root: Node):
        if not root:
            return 0
        return 1 + self._size(root.left) + self._size(root.right)

    def size(self):
        return self._size(self.root)

    def _count_leaves(self, root: Node):
        if not root:
            return 0
        if self._is_leaf(root):
            return 1
        return self._count_leaves(root.left) + self._count_leaves(root.right)

    def count_leaves(self):
        return self._count_leaves(self.root)

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, root: Node, value: int):
        if not root:
            return False
        left_contains = self._contains(root.left, value)
        right_contains = self._contains(root.right, value)
        return root.value == value or left_contains or right_contains

    def _are_siblings(self, root, value1, value2):
        if not root:
            return False

        if root.left and root.right:
            left = root.left.value
            right = root.right.value
            equality_1 = left == value1 and right == value2
            equality_2 = right == value1 and left == value2
            if equality_1 or equality_2:
                return True

        ans = False
        if root.left:
            ans = ans or self._are_siblings(root.left, value1, value2)
        if root.right:
            ans = ans or self._are_siblings(root.right, value1, value2)
        return ans

    def are_siblings(self, value1, value2):
        return self._are_siblings(self.root, value1, value2)

    def _get_ancestors(self, root: Node, value: int, ancestors: list):
        if self._contains(root, value):
            ancestors.append(root.value)
            self._get_ancestors(root.left, value, ancestors)
            self._get_ancestors(root.right, value, ancestors)

    def get_ancestors(self, value):
        ancestors = list()
        self._get_ancestors(self.root, value, ancestors)
        return ancestors

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, root: Node):
        if not root:
            return True
        balance_factor = self._height(root.left) - self._height(root.right)
        if balance_factor < -1 or balance_factor > 1:
            return False
        return self._is_balanced(root.left) and self._is_balanced(root.right)

    def is_perfect(self):
        return self._is_perfect(self.root)

    def _is_perfect(self, root: Node):
        if not root:
            return True
        balance_factor = self._height(root.left) - self._height(root.right)
        if balance_factor != 0:
            return False
        return self._is_perfect(root.left) and self._is_perfect(root.right)


t = BinarySearchTree(7)
t.insert(4)
t.insert(9)
t.insert(1)
t.insert(6)
t.insert(8)
t.insert(10)
q = BinarySearchTree(7)
q.insert(4)
q.insert(9)
q.insert(1)
q.insert(6)
q.insert(8)
q.insert(10)
print("In order:")
t.traverse_in_order()
print("Pre order:")
t.traverse_pre_order()
print("Post order:")
t.traverse_post_order()
print("Level Order:")
t.traverse_level_order()
print(f"height: {t.height()}")
print(f"min: {t.min()}")
print(f"max: {t.max()}")
print(f"t is equal q: {t.equals(q)}")
print(f"Tree is binary search tree: {t.is_binary_search_tree()}")
print(f"Nodes at distance 2: {t.get_nodes_at_k_distance(2)}")
print(f"size: {t.size()}")
print(f"Count of leaves: {t.count_leaves()}")
print(f"Tree contains 5: {t.contains(5)}")
print(f"Are 8 and 10: {t.are_siblings(8, 10)}")
print(t.get_ancestors(10))
print(t.is_balanced())
print(t.is_perfect())
