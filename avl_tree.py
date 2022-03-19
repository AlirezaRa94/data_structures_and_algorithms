class AVLTree:
    def __init__(self):
        self.root = None

    class AVLNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.height = 0

        def __str__(self):
            return "Value = " + str(self.value)

    @staticmethod
    def _height(node: AVLNode):
        return -1 if not node else node.height

    def _set_height(self, node: AVLNode):
        node.height = max(self._height(node.right_child), self._height(node.left_child)) + 1

    def _balance_factor(self, node: AVLNode):
        return 0 if not node else self._height(node.left_child) - self._height(node.right_child)

    def is_left_heavy(self, node: AVLNode):
        return self._balance_factor(node) > 1

    def is_right_heavy(self, node: AVLNode):
        return self._balance_factor(node) < -1

    def _left_rotate(self, root: AVLNode):
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root

        self._set_height(root)
        self._set_height(new_root)

        return new_root

    def _right_rotate(self, root: AVLNode):
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root

        self._set_height(root)
        self._set_height(new_root)

        return new_root

    def _balance(self, root: AVLNode):
        if self.is_left_heavy(root):
            print(f"{root.value} is heavy left.")
            if self._balance_factor(root.left_child) < 0:
                root.left_child = self._left_rotate(root.left_child)
            root = self._right_rotate(root)
        elif self.is_right_heavy(root):
            print(f"{root.value} is heavy right.")
            if self._balance_factor(root.right_child) > 0:
                root.right_child = self._right_rotate(root.right_child)
            root = self._left_rotate(root)
        return root

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root: AVLNode, value: int):
        if not root:
            return self.AVLNode(value)

        if value < root.value:
            root.left_child = self._insert(root.left_child, value)
        elif value > root.value:
            root.right_child = self._insert(root.right_child, value)
        else:
            raise ValueError("This value already exists in tree!")

        self._set_height(root)

        return self._balance(root)


t = AVLTree()
t.insert(10)
t.insert(20)
t.insert(30)
t.insert(15)
print(t.root.height)
print(t.root)
print(t.root.right_child)
print(t.root.left_child)
print(t.root.left_child.right_child)
