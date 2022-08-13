

from locale import currency


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # creation of circular doubly linked list
    def createDll(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "CDLL is created successfully"

    def insertDLL(self, value, location):
        if self.head is None:
            return "the CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
            return "the node is created "

    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node fot traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseCDLL(self):
        if self.head is None:
            print("There is not any node fot traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def search(self, value):
        if self.tail is None:
            return "there is no elements in the linked list"
        else:
            tempNode = self.head
            index = 0
            while tempNode != self.tail:
                if tempNode.value == value:
                    return index
                index += 1
                tempNode = tempNode.next
            return "no such element"

    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    index += 1
                    currentNode = currentNode.next
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("node is deleted")

    def deleteAll(self):
        if self.head is None:
            print("No elements to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


circulardll = CircularDoublyLinkedList()
circulardll.createDll(15)
circulardll.insertDLL(12, 0)
circulardll.insertDLL(13, 1)
circulardll.insertDLL(22, 0)
circulardll.insertDLL(13, 3)
circulardll.reverseCDLL()
print(circulardll.search(13))
print([node.value for node in circulardll])
