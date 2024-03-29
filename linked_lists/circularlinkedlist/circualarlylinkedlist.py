class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class CircularlyLinkedList:
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

# creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "the CSLL has been created"

    def insert(self, value, location):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully iinserted"

    def traversalCSSL(self):
        if self.head is None:
            print("There is no eleemtns")
        else:
            tempNode = self.head

            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def search(self, nodeValue):
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return tempNode.value
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                return "The node does not eist in this csll"

    def deleteNode(self, position):
        if self.head is None:
            print("there is not any node in csll")

        else:
            if position == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif position == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circularCLL = CircularlyLinkedList()
circularCLL.createCSLL(1)
circularCLL.insert(3, 0)
circularCLL.insert(22, 1)
circularCLL.insert(11, 2)
circularCLL.traversalCSSL()
circularCLL.deleteNode(0)
# print(circularCLL.search(22))
print([node.value for node in circularCLL])
