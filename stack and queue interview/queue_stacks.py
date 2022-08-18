# Implement a queue using two stacks
from distutils.sysconfig import customize_compiler
from queue import Queue


class Stack:
    def __init__(self) -> None:
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()


class QueueStack:
    def __init__(self) -> None:
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while(len(self.outStack)):
            self.inStack.push(self.outStack.pop())
        return result


customQueue = QueueStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
