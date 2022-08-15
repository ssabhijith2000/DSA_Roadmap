import re


class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "The element is not in the queue"
        else:
            # if 0 is given as a parameter in pop, first element is deleted
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "The element is not in the queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.dequeue()
print(customQueue)
