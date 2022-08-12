from telnetlib import DO


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


doublyll = DoublyLinkedList()
doublyll.createdll(5)
doublyll.insertNode(0, 0)
print([node.value for node in doublyll])
