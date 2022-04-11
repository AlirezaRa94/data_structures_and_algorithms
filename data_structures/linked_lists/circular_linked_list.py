"""
Circular Linked List Data Structure
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
            if cur == self.head:
                break
        return length

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        last_node = self.head
        if self.head is None:
            new_node.next = new_node
        else:
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        if cur is None:
            self.head = new_node
            self.head.next = self.head
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(' ' + str(cur.data), end='')
            cur = cur.next
            if cur == self.head:
                break
        print()

    def delete_head(self):
        if len(self) < 2:
            self.head = None
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = self.head.next
            self.head = self.head.next

    def delete_by_value(self, key):
        """
        Delete a node based on the given key from the circular linked list
        :param key: The value of the node which we want to delete should match
        this key.
        """
        if self.head:
            prev = None
            cur = self.head
            while cur.data != key:
                prev = cur
                cur = cur.next
                if cur == self.head:
                    return
            if prev is not None:
                prev.next = cur.next
            else:
                self.delete_head()

    def delete_by_node(self, node):
        """
        This method will delete the given node from the circular linked list.
        :param node: The node which we want to remove from the linked list
        """
        if self.head:
            prev = None
            cur = self.head
            while cur != node:
                prev = cur
                cur = cur.next
                if cur == self.head:
                    return
            if prev is not None:
                prev.next = cur.next
            else:
                self.delete_head()

    def split_list(self):
        """
        This method will split the circular linked list into two separate
        circular linked lists.
        """
        size = len(self)
        if size < 2:
            return self.print_list()

        mid = size // 2
        count = 0

        prev = None
        cur = self.head
        while count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        cllist_2 = CircularLinkedList()
        while cur.next != self.head:
            cllist_2.append(cur.data)
            cur = cur.next
        cllist_2.append(cur.data)
        cur.next = cllist_2.head

        self.print_list()
        cllist_2.print_list()

    def josephus_circle(self, step):
        """
        This method will solve the “Josephus Problem” using the circular linked
         list data structure.
        :param step: It is the step-size of the problem and, it means in each
         step the kth node will be removed.
        :return: The answer of the problem which is the node that remains.
        """
        cur = self.head
        size = len(self)
        while size > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KILL:" + str(cur.data))
            self.delete_by_node(cur)
            size -= 1
            cur = cur.next
        return cur.data

    @staticmethod
    def is_circular_linked_list(input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur == input_list.head:
                return True
        return False
