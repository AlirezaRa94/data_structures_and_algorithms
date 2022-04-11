"""
Doubly Linked List Data Structure
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node.prev = cur
            cur.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(' ', cur.data, end='')
            cur = cur.next
        print()

    def add_after_node(self, key, data):
        """
        This method will add new node after the node with key value.
        :param key: The value of the node which we want to add new node after
        it
        :param data: The value of the new node which we want to add
        """
        if self.head is None:
            self.append(data)
        else:
            cur = self.head
            new_node = Node(data)
            while cur and cur.data != key:
                cur = cur.next
            if cur is None:
                return
            new_node.next = cur.next
            new_node.prev = cur
            if cur.next:
                cur.next.prev = new_node
            cur.next = new_node

    def add_before_node(self, key, data):
        """
        This method will add new node before the node with key value.
        :param key: The value of the node which we want to add new node before
         it
        :param data: The value of the new node which we want to add
        """
        if self.head is None or self.head.data == key:
            self.prepend(data)
        else:
            cur = self.head
            new_node = Node(data)
            while cur and cur.data != key:
                cur = cur.next
            if cur is None:
                return
            new_node.prev = cur.prev
            new_node.next = cur
            cur.prev.next = new_node
            cur.prev = new_node

    def delete_by_value(self, key):
        """
        This method will delete the node with the given value.
        :param key: The value of the node which we want to delete
        """
        if self.head:
            cur = self.head
            if cur.data == key:
                if cur.next is None:
                    self.head = None
                else:
                    self.head = cur.next
                    self.head.prev = None
            else:
                while cur and cur.data != key:
                    cur = cur.next
                if cur is not None:
                    if cur.next is None:
                        cur.prev.next = None
                    else:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev

    def delete_by_node(self, node):
        """
        This method will delete the given node from the linked list.
        :param node: The node which we want to delete
        """
        if self.head:
            cur = self.head
            if cur == node:
                if cur.next is None:
                    self.head = None
                else:
                    self.head = cur.next
                    self.head.prev = None
            else:
                while cur and cur != node:
                    cur = cur.next
                if cur is not None:
                    if cur.next is None:
                        cur.prev.next = None
                    else:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev

    def reverse(self):
        """
        This method will reverse the linked list
        """
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        """
        This method will remove the duplicates from the linked list
        """
        data = set()
        cur = self.head
        while cur:
            value = cur.data
            if value in data:
                self.delete_by_node(cur)
                self.print_list()
            else:
                data.add(value)
            cur = cur.next

    def pairs_with_sum(self, sum_val):
        """
        This method will find all pairs from the linked list which sum to a
         specified number.
        :param sum_val: The sum of the pairs should match this value
        :return: A list which contains all pairs which sum to a specified
         number
        """
        seen = set()
        cur = self.head
        output = set()
        while cur:
            val = cur.data
            if sum_val - val in seen:
                pair = tuple(sorted((val, sum_val - val)))
                if pair not in output:
                    output.add(pair)
            else:
                seen.add(val)
            cur = cur.next
        return list(output)
