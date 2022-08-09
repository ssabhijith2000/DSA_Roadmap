class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverse(self):
        if self.head is None:
            print("Singly ;inked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, value):
        if self.head is None:
            return " the List is empty"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return "value does not exist"

    def delete(self, location):
        if self.head is not None:
            print("singly   linked list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            print('SLL does not exist')
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insert(1, 1)
singlyLinkedList.insert(2, 1)
singlyLinkedList.insert(3, 1)
singlyLinkedList.insert(21, 0)
print([node.value for node in singlyLinkedList])
# singlyLinkedList.traverse()
print(singlyLinkedList.search(4))
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
