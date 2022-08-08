from lib2to3.pytree import Node
from mimetypes import init
from operator import truediv
from tokenize import single_quoted


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
