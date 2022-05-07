from data_structures.trees.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self, root):
        super().__init__(root)

    def _insert(self, start: BinaryTree.Node, value):
        if value < start.value:
            if start.left:
                self._insert(start.left, value)
            else:
                start.left = self.Node(value)
        elif value > start.value:
            if start.right:
                self._insert(start.right, value)
            else:
                start.right = self.Node(value)
        else:
            raise ValueError("This value already exists in the tree!")

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

    def _min(self, root: BinaryTree.Node):
        if not root:
            raise TypeError('Empty tree has no minimum value!')
        current = root
        while current.left:
            current = current.left
        return current.value

    def _max(self, root: BinaryTree.Node):
        if not root:
            raise TypeError('Empty tree has no maximum value!')
        current = root
        while current.right:
            current = current.right
        return current.value

    def swap_root(self):
        self.root.left, self.root.right = self.root.right, self.root.left

    def _get_nodes_at_k_distance(self, root: BinaryTree.Node, dist: int,
                                 nodes: list):
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

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, root: BinaryTree.Node):
        if not root:
            return True
        balance_factor = self._height(root.left) - self._height(root.right)
        if balance_factor < -1 or balance_factor > 1:
            return False
        return self._is_balanced(root.left) and self._is_balanced(root.right)

    def is_perfect(self):
        return self._is_perfect(self.root)

    def _is_perfect(self, root: BinaryTree.Node):
        if not root:
            return True
        height = self._height(root)
        size = self._size(root)
        return size == 2 ** (height + 1) - 1


if __name__ == "__main__":
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
    t.print_tree(traversal_type="inorder")
    print("Pre order:")
    t.print_tree(traversal_type="preorder")
    print("Post order:")
    t.print_tree(traversal_type="postorder")
    print("Level Order:")
    t.print_tree(traversal_type="level_order")
    print(f"height: {t.height()}")
    print(f"min: {t.min()}")
    print(f"max: {t.max()}")
    print(f"t is equal q: {t.equals(q)}")
    print(f"Tree is binary search tree: {t.is_binary_search_tree()}")
    print(f"Nodes at distance 2: {t.get_nodes_at_k_distance(2)}")
    print(f"size: {t.size()}")
    print(f"Count of leaves: {t.count_leaves()}")
    print(f"Tree contains 5: {t.contains(5)}")
    print(f"Are 8 and 10 siblings?: {t.are_siblings(8, 10)}")
    print(t.get_ancestors(10))
    print(t.is_balanced())
    print(t.is_perfect())
