from data_structures.queue import Queue
from data_structures.stack import Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    @staticmethod
    def _is_leaf(node: Node):
        return not node.left and not node.right

    def height(self):
        """
        This method will return the height of the tree.
        :return: The height of the tree
        """
        return self._height(self.root)

    def _height(self, node: Node):
        """
        This method will return the height of the given node.
        :param node: The node which we want to calculate the height of it
        :return: The height of the node
        """
        if not node:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    def _size(self, node: Node):
        """
        This method will return the number of children of the node including
         itself
        """
        if not node:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def size(self):
        """
        This method will return the number of nodes of the tree
        """
        return self._size(self.root)

    def min(self):
        """
        This method will return the minimum value of the binary tree
        :return: The minimum value of the binary tree
        """
        return self._min(self.root)

    def _min(self, root: Node):
        """
        This method will return the minimum value of all children of the given
         node
        :param root: The given node
        :return: The minimum value of the node's children
        """
        if self._is_leaf(root):
            return root.value

        return min(root.value, self._min(root.left), self._min(root.right))

    def _preorder_print(self, node: Node):
        """
        root -> left -> right
        """
        if node:
            print(' ', node.value, end='')
            self._preorder_print(node.left)
            self._preorder_print(node.right)

    def _inorder_print(self, node: Node):
        """
        left -> root -> right
        """
        if node:
            self._inorder_print(node.left)
            print(' ', node.value, end='')
            self._inorder_print(node.right)

    def _postorder_print(self, node: Node):
        """
        left -> right -> root
        """
        if node:
            self._postorder_print(node.left)
            self._postorder_print(node.right)
            print(' ', node.value, end='')

    @staticmethod
    def _level_order_print(start: Node):
        """
        level 0(root) -> level 1 -> level 2 -> ...
        """
        if start:
            queue = Queue()
            queue.enqueue(start)
            while not queue.is_empty():
                node = queue.dequeue()
                print(' ', node.value, end='')

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)

    @staticmethod
    def _reverse_level_order_print(start: Node):
        """
        ... -> level 2 -> level 1 -> level 0(root)
        """
        if start:
            queue = Queue()
            stack = Stack()
            queue.enqueue(start)
            while not queue.is_empty():
                node = queue.dequeue()
                stack.push(node.value)

                if node.right:
                    queue.enqueue(node.right)
                if node.left:
                    queue.enqueue(node.left)

            while not stack.is_empty():
                print(' ', stack.pop(), end='')

    def print_tree(self, traversal_type: str):
        if traversal_type == "preorder":
            self._preorder_print(self.root)
        elif traversal_type == "inorder":
            self._inorder_print(self.root)
        elif traversal_type == "postorder":
            self._postorder_print(self.root)
        elif traversal_type == "level_order":
            self._level_order_print(self.root)
        elif traversal_type == "reverse_level_order":
            self._reverse_level_order_print(self.root)
        else:
            print(
                "Traversal type " + str(traversal_type) + " is not supported.",
                end=''
            )
        print()

    def is_binary_search_tree(self, tree):
        if not tree:
            return False
        return self._is_binary_search_tree(
            tree.root,
            minimum=float('-inf'),
            maximum=float('inf')
        )

    def _is_binary_search_tree(self, node: Node, minimum: float,
                               maximum: float):
        if not node:
            return True
        node_val = float(node.value)
        node_is_bst = minimum < node_val < maximum
        left_is_bst = self._is_binary_search_tree(
            node=node.left,
            minimum=minimum,
            maximum=node_val
        )
        right_is_bst = self._is_binary_search_tree(
            node=node.right,
            minimum=node_val,
            maximum=maximum
        )
        return node_is_bst and left_is_bst and right_is_bst


# preorder: 1-2-4-5-3-6-7
# inorder: 4-2-5-1-6-3-7
# postorder: 4-5-2-6-7-3-1
#               1
#             /   \
#            2      3
#           / \    / \
#          4   5  6   7

# Set up tree:
my_tree = BinaryTree(1)
my_tree.root.left = Node(2)
my_tree.root.right = Node(3)
my_tree.root.left.left = Node(4)
my_tree.root.left.right = Node(5)
my_tree.root.right.left = Node(6)
my_tree.root.right.right = Node(7)
my_tree.print_tree(traversal_type="preorder")
my_tree.print_tree(traversal_type="inorder")
my_tree.print_tree(traversal_type="postorder")
my_tree.print_tree(traversal_type="level_order")
my_tree.print_tree(traversal_type="reverse_level_order")
print(my_tree.height())
print(my_tree.size())
