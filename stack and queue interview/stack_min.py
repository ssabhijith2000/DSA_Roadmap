# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum elenment? Push, pop and min should all operate in O(1)

class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        else:
            return self.minNode.value

    def push(self, value):
        if self.minNode.value < value:
            self.minNode = Node(self.minNode.value, self.minNode)
        else:
            self.minNode = Node(value, self.minNode)
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item


customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
