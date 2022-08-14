from distutils.sysconfig import customize_compiler
from inspect import ismemberdescriptor
from mimetypes import init
from re import S


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        if self.isEmpty():
            print('No elements to pop')
        else:
            nodevalue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodevalue

    def peep(self):
        if self.isEmpty():
            print('No elements in list')
        else:
            nodeValue = self.linkedList.head.value
            return nodeValue

    def delete(self):
        self.linkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)
print('popped:', customStack.pop())
print(customStack)
