"""
Singly Linked List Data Structure.
"""
from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        """
        The prepend method will insert an element at the beginning of the
         linked list.
        :param data: The new data that we want to add to the linked list.
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_after_node(prev_node: Optional[Node], data):
        """
        The insert_after_node insert an element after a given node.
        :param prev_node: The previous node after which we have to insert the
         new node.
        :param data: The new data that we want to add to the linked list.
        """
        if not prev_node:
            print("Previous node does not exists")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        """
        The append method will insert an element at the end of the linked list.
        :param data: The new data that we want to add to the linked list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def delete_by_value(self, key):
        """
        Delete a node based on the given key from the linked list
        :param key: The value of the node which we want to delete should match
         this key.
        """
        prev = None
        cur_node = self.head
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        if prev is None:
            self.head = cur_node.next
        else:
            prev.next = cur_node.next

    def delete_at_pos(self, pos: int):
        """
            Delete a node based on the given key from the linked list
            :param pos: The position of the node which we want to delete.
        """
        prev = None
        cur_node = self.head
        cur_pos = 0
        while cur_node and cur_pos != pos:
            prev = cur_node
            cur_node = cur_node.next
            cur_pos += 1

        if cur_node is None:
            print("There is no node at this position")
            return

        if prev is None:
            self.head = cur_node.next
        else:
            prev.next = cur_node.next

    def print_list(self):
        """
        The print_list method will print out the entries of a linked list.
        """
        cur_node = self.head
        while cur_node:
            print(' ' + str(cur_node.data), end='')
            cur_node = cur_node.next
        print()

    def length(self):
        """
        The length method calculate number of nodes in the linked list.
        :return: The length of the linked list
        """
        cur_node = self.head
        length = 0
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length

    def swap_nodes(self, key_1, key_2):
        """
        The swap_nodes method takes two keys and swap the corresponding nodes.
        :param key_1: The value of the first node
        :param key_2: The value of the second node
        """
        if key_1 == key_2:
            return

        prev_1 = prev_2 = None
        cur_node_1 = cur_node_2 = self.head

        while cur_node_1 and cur_node_1.data != key_1:
            prev_1 = cur_node_1
            cur_node_1 = cur_node_1.next

        while cur_node_2 and cur_node_2.data != key_2:
            prev_2 = cur_node_2
            cur_node_2 = cur_node_2.next

        if cur_node_1 is None or cur_node_2 is None:
            return

        if prev_1:
            prev_1.next = cur_node_2
        else:
            self.head = cur_node_2

        if prev_2:
            prev_2.next = cur_node_1
        else:
            self.head = cur_node_1

        cur_node_1.next, cur_node_2.next = cur_node_2.next, cur_node_1.next

    def reverse(self):
        """
        The reverse method reverse the linked list in an iterative way.
        """
        prev = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev, cur_node = cur_node, next_node
        self.head = prev

    def rotate(self, k):
        """
        This method will rotate the nodes of the linked list around a
        specified pivot element.
        :param k: The index of the pivot element
        """
        p = self.head
        q = self.head
        i = 1
        while i != k:
            p = p.next
            q = q.next
            i += 1
            if not p:
                return

        while q.next:
            q = q.next

        q.next = self.head
        self.head = p.next
        p.next = None

    def _merge_sorted(self, list_1, list_2):
        """
        The _merge_sorted method gives two sorted linked list and merge them
         together to create a new sorted linked list.
        :param list_1: The first sorted linked list
        :param list_2: The second sorted linked list
        :return: A new sorted linked list
        """
        if not list_1:
            return list_2
        if not list_2:
            return list_1

        if list_1.data <= list_2.data:
            list_1.next = self._merge_sorted(list_1.next, list_2)
            return list_1
        else:
            list_2.next = self._merge_sorted(list_1, list_2.next)
            return list_2

    def merge_sorted(self, llist):
        """
        The merge_sorted method gives one sorted linked list and merge it with
         our sorted linked list.
        :param llist: A sorted linked list
        :return: A new sorted linked list
        """
        p = self.head
        q = llist.head

        return self._merge_sorted(p, q)

    def remove_duplicates(self):
        """
        The remove_duplicates method will remove duplicate entries from the
         linked list
        """
        prev = None
        cur_node = self.head
        data = set()
        while cur_node:
            if cur_node.data in data:
                prev.next = cur_node.next
            else:
                data.add(cur_node.data)
                prev = cur_node
            cur_node = cur_node.next

    def get_nth_from_last(self, n):
        """
        This method will print the Nth-to-Last Node from the linked list.
        """
        p = self.head
        q = self.head

        while n > 1:
            q = q.next
            n -= 1
            if not q:
                return

        while q.next:
            q = q.next
            p = p.next

        return p.data

    def count_occurrences(self, data):
        """
        This method will count the occurrences of nodes with specified data.
        :param data: The specified value of nodes
        :return: Number of occurrences of nodes
        """
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def is_palindrome(self):
        """
        This method will determine whether the linked list is palindrome or
        not.
        """
        s = ""
        cur = self.head
        while cur:
            s += str(cur.data)
            cur = cur.next
        return s == s[::-1]

    def move_tail_to_head(self):
        """
        This method will move the tail (or last) node of the linked list to the
        front of the linked list so that it becomes the new head of the linked
        list.
        """
        prev = None
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
        cur.next = self.head
        self.head = cur
        prev.next = None

    def sum(self, llist):
        """
        This method will add another linked list to the linked list
        :param llist: The linked list that should add to the linked list
        """
        prev = None
        p = self.head
        q = llist.head
        carry = 0
        while p or q:
            i = p.data if p else 0
            j = q.data if q else 0
            s = i + j + carry
            if s >= 10:
                carry = 1
                s %= 10
            else:
                carry = 0
            if p:
                p.data = s
                prev = p
                p = p.next
            else:
                prev.next = Node(s)
                prev = prev.next
            if q:
                q = q.next
