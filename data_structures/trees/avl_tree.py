from data_structures.trees.binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, value):
            super().__init__(value)
            self.height = 0

        def __str__(self):
            return "Value = " + str(self.value)

    def _height(self, node: Node):
        if not node:
            return -1
        return node.height

    def _set_height(self, node: Node):
        node.height = 1 + max(
            self._height(node.right), self._height(node.left)
        )

    def _balance_factor(self, node: Node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def is_left_heavy(self, node: Node):
        return self._balance_factor(node) > 1

    def is_right_heavy(self, node: Node):
        return self._balance_factor(node) < -1

    def _left_rotate(self, root: Node):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self._set_height(root)
        self._set_height(new_root)

        return new_root

    def _right_rotate(self, root: Node):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self._set_height(root)
        self._set_height(new_root)

        return new_root

    def _balance(self, root: Node):
        if self.is_left_heavy(root):
            print(f"{root.value} is left heavy.")
            # We need to check that if the left node is right heavy or not?
            # If so, first we need a left rotate at left node
            if self._balance_factor(root.left) < 0:
                root.left = self._left_rotate(root.left)
            root = self._right_rotate(root)
        elif self.is_right_heavy(root):
            print(f"{root.value} is right heavy.")
            # We need to check that if the right node is left heavy or not?
            # If so, first we need a right rotate at right node
            if self._balance_factor(root.right) > 0:
                root.right = self._right_rotate(root.right)
            root = self._left_rotate(root)
        return root

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root: Node, value: int):
        if not root:
            return self.Node(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        else:
            raise ValueError("This value already exists in the tree!")

        self._set_height(root)

        return self._balance(root)


if __name__ == "__main__":
    t = AVLTree(30)
    t.insert(15)
    t.insert(18)
    t.insert(10)
    t.insert(16)
    t.insert(7)
    t.insert(8)
    t.print_tree(traversal_type="inorder")
    print(t.is_balanced())
    print(t.is_perfect())
