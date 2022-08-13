from platform import node
import re
from telnetlib import DO
from unittest import defaultTestLoader


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creation of doublyLinked list

    def createdll(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    # insertion method in doubly linked list
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node canno be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            if location == 1:
                newNode.next = None
                newNode.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.prev = tempNode
                newNode.next = tempNode.next
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverseTraverse(self):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.prev)
                tempNode = tempNode.prev

    def searchDLL(self, nodeValue):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "the node does not eist in this list"

    def delete(self, location):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("Successfully defaultTestLoader")

    def deleteentiredll(self):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("dll deleted")


doublyll = DoublyLinkedList()
doublyll.createdll(5)
doublyll.insertNode(0, 0)
print([node.value for node in doublyll])
