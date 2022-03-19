class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        inserted_node = Node(value)
        if self.root:
            current = self.root
            while current:
                if value < current.value:
                    if not current.left_child:
                        break
                    current = current.left_child
                elif value > current.value:
                    if not current.right_child:
                        break
                    current = current.right_child
                else:
                    raise ValueError("This value already exists in tree!")

            if value < current.value:
                current.left_child = inserted_node
            else:
                current.right_child = inserted_node

        else:
            self.root = inserted_node

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:
                return True
        return False

    def traverse_in_order(self):
        self._traverse_in_order(self.root)

    def _traverse_in_order(self, root: Node):
        if not root:
            return
        self._traverse_in_order(root.left_child)
        print(root.value)
        self._traverse_in_order(root.right_child)

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, root: Node):
        if not root:
            return
        print(root.value)
        self._traverse_pre_order(root.left_child)
        self._traverse_pre_order(root.right_child)

    def traverse_post_order(self):
        self._traverse_post_order(self.root)

    def _traverse_post_order(self, root: Node):
        if not root:
            return
        self._traverse_post_order(root.left_child)
        self._traverse_post_order(root.right_child)
        print(root.value)

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
        if not self.root:
            raise TypeError('Empty tree has no minimum value!')
        current = self.root
        while True:
            if not current.left_child:
                return current.value
            current = current.left_child

    def max(self):
        return self._max(self.root)

    def _max(self, root: Node):
        if not self.root:
            raise TypeError('Empty tree has no maximum value!')
        if not root.right_child:
            return root.value
        return self._max(root.right_child)

    def equals(self, tree):
        if not tree:
            return True if not self.root else False
        return self._equals(self.root, tree.root)

    def _equals(self, node1: Node, node2: Node):
        if not node1 and not node2:
            return True
        if node1 and node2:
            return node1.value == node2.value\
                   and self._equals(node1.left_child, node2.left_child)\
                   and self._equals(node1.right_child, node2.right_child)

        return False

    def swap_root(self):
        self.root.left_child, self.root.right_child = self.root.right_child, self.root.left_child

    def is_binary_search_tree(self):
        return self._is_binary_search_tree(self.root, minimum=float('-inf'), maximum=float('inf'))

    def _is_binary_search_tree(self, root: Node, minimum: float, maximum: float):
        if not root:
            return True
        return minimum < float(root.value) < maximum \
            and self._is_binary_search_tree(root.left_child, minimum=minimum, maximum=float(root.value)) \
            and self._is_binary_search_tree(root.right_child, minimum=float(root.value), maximum=maximum)

    def get_nodes_at_k_distance(self, dist: int):
        nodes_at_k_distance = list()
        self._get_nodes_at_k_distance(self.root, dist, nodes_at_k_distance)
        return nodes_at_k_distance

    def _get_nodes_at_k_distance(self, root: Node, dist: int, nodes: list):
        if not root:
            return
        if dist == 0:
            nodes.append(root.value)
            return
        dist -= 1
        self._get_nodes_at_k_distance(root.left_child, dist, nodes)
        self._get_nodes_at_k_distance(root.right_child, dist, nodes)

    def traverse_level_order(self):
        for k in range(self.height() + 1):
            for node in self.get_nodes_at_k_distance(k):
                print(node)

    def size(self):
        return self._size(self.root)

    def _size(self, root: Node):
        if not root:
            return 0
        return 1 + self._size(root.left_child) + self._size(root.right_child)

    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, root: Node):
        if not root:
            return 0
        if self._is_leaf(root):
            return 1
        return self._count_leaves(root.left_child) + self._count_leaves(root.right_child)

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, root: Node, value: int):
        if not root:
            return False
        return root.value == value or self._contains(root.right_child, value) or self._contains(root.left_child, value)

    def are_siblings(self, value1, value2):
        return self._are_siblings(self.root, value1, value2)

    def _are_siblings(self, root, value1, value2):
        if not root.left_child or not root.right_child:
            return False
        left_child = root.left_child.value
        right_child = root.right_child.value
        check = (left_child == value1 and right_child == value2) or (right_child == value1 and left_child == value2)
        return check or self._are_siblings(root.left_child, value1, value2)\
            or self._are_siblings(root.right_child, value1, value2)

    def get_ancestors(self, value):
        ancestors = list()
        self._get_ancestors(self.root, value, ancestors)
        return ancestors

    def _get_ancestors(self, root: Node, value: int, ancestors: list):
        if self._contains(root, value):
            ancestors.append(root.value)
            self._get_ancestors(root.left_child, value, ancestors)
            self._get_ancestors(root.right_child, value, ancestors)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, root: Node):
        if not root:
            return True
        balance_factor = self._height(root.left_child) - self._height(root.right_child)
        if balance_factor < -1 or balance_factor > 1:
            return False
        return self._is_balanced(root.left_child) and self._is_balanced(root.right_child)

    def is_perfect(self):
        return self._is_perfect(self.root)

    def _is_perfect(self, root: Node):
        if not root:
            return True
        balance_factor = self._height(root.left_child) - self._height(root.right_child)
        if balance_factor != 0:
            return False
        return self._is_perfect(root.left_child) and self._is_perfect(root.right_child)


t = BinarySearchTree()
t.insert(7)
t.insert(4)
t.insert(9)
t.insert(1)
t.insert(6)
t.insert(8)
t.insert(10)
q = BinarySearchTree()
q.insert(7)
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
