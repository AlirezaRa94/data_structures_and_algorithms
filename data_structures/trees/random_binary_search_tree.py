"""
A binary search tree with the ability to return a random node from the tree
"""
from typing import Optional
from random import randint


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.children = 0


class RandomBinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, val: int):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
            while True:
                cur.children += 1
                if val < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = new_node
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = new_node
                        break

    def find(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    @staticmethod
    def _get_children(root):
        if root.left is None:
            return 0
        return 1 + root.left.children

    def _get_random_node(self, root, rand):
        if root is None:
            return None
        ind = self._get_children(root)
        if rand == ind:
            return root.val
        if rand < ind:
            return self._get_random_node(root.left, rand)
        else:
            return self._get_random_node(root.right, rand - ind - 1)

    def get_random_node(self):
        if self.root is None:
            return None
        rand = randint(0, self.root.children)
        return self._get_random_node(self.root, rand)
