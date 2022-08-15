# How ould you design a stack which, in addition tto push and pop, has a function min which returns the minimum element? Push, pop and min shoul work in O(1)
from mimetypes import init
from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
            return string


class Stack():
    def __init__(self) -> None:
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self, item):
        if self.minNode and self.minNode.value < item:
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item


customStack = Stack()
customStack.push(5)
customStack.push(8)
customStack.push(3)
customStack.pop()
print(customStack.min())
