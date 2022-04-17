"""
Stack Data Structure.
"""


class Stack:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
print(myStack.pop())
print(myStack.is_empty())
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.is_empty())
