from data_structures.queues.queue import Queue
from data_structures.stack import Stack


class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, root):
        self.root = self.Node(root)

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

    def _size(self, root: Node):
        """
        This method will return the number of children of the node including
         itself
        """
        if not root:
            return 0
        return 1 + self._size(root.left) + self._size(root.right)

    def size(self):
        """
        This method will return the number of nodes of the tree
        """
        return self._size(self.root)

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

    def min(self):
        """
        This method will return the minimum value of the binary tree
        :return: The minimum value of the binary tree
        """
        return self._min(self.root)

    def _max(self, root: Node):
        """
        This method will return the maximum value of all children of the given
         node
        :param root: The given node
        :return: The maximum value of the node's children
        """
        if self._is_leaf(root):
            return root.value

        return max(root.value, self._min(root.left), self._min(root.right))

    def max(self):
        """
        This method will return the maximum value of the binary tree
        :return: The maximum value of the binary tree
        """
        return self._max(self.root)

    def _equals(self, start1: Node, start2: Node):
        """
        This method will check that if two trees are equal
        :return: True if they are equal
        """
        if not start1 and not start2:
            return True
        if start1 and start2:
            node_equals = start1.value == start2.value
            left_equals = self._equals(start1.left, start2.left)
            right_equals = self._equals(start1.right, start2.right)
            return node_equals and left_equals and right_equals
        return False

    def equals(self, tree):
        """
        This method will check that if the given tree is equal to our tree?
        :return: True if they are equal
        """
        if not tree:
            return True if not self.root else False
        return self._equals(self.root, tree.root)

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

    def _traverse_preorder(self, node: Node):
        """
        Depth-first
        root -> left -> right
        """
        if node:
            print(' ', node.value, end='')
            self._traverse_preorder(node.left)
            self._traverse_preorder(node.right)

    def _traverse_inorder(self, node: Node):
        """
        Depth-first
        left -> root -> right
        """
        if node:
            self._traverse_inorder(node.left)
            print(' ', node.value, end='')
            self._traverse_inorder(node.right)

    def _traverse_postorder(self, node: Node):
        """
        Depth-first
        left -> right -> root
        """
        if node:
            self._traverse_postorder(node.left)
            self._traverse_postorder(node.right)
            print(' ', node.value, end='')

    @staticmethod
    def _traverse_level_order(start: Node):
        """
        Breadth-first
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
    def _traverse_reverse_level_order(start: Node):
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
            self._traverse_preorder(self.root)
        elif traversal_type == "inorder":
            self._traverse_inorder(self.root)
        elif traversal_type == "postorder":
            self._traverse_postorder(self.root)
        elif traversal_type == "level_order":
            self._traverse_level_order(self.root)
        elif traversal_type == "reverse_level_order":
            self._traverse_reverse_level_order(self.root)
        else:
            print(
                "Traversal type " + str(traversal_type) + " is not supported.",
                end=''
            )
        print()

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


if __name__ == "__main__":
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
    my_tree.root.left = BinaryTree.Node(2)
    my_tree.root.right = BinaryTree.Node(3)
    my_tree.root.left.left = BinaryTree.Node(4)
    my_tree.root.left.right = BinaryTree.Node(5)
    my_tree.root.right.left = BinaryTree.Node(6)
    my_tree.root.right.right = BinaryTree.Node(7)
    my_tree.print_tree(traversal_type="preorder")
    my_tree.print_tree(traversal_type="inorder")
    my_tree.print_tree(traversal_type="postorder")
    my_tree.print_tree(traversal_type="level_order")
    my_tree.print_tree(traversal_type="reverse_level_order")
    print(my_tree.height())
    print(my_tree.size())
