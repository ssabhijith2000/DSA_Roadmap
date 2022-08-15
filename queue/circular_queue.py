# queue with fixed capacity
class Queue:
    def __init__(self, maxSize) -> None:
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("The queue is full")
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            print(" no element in queue")
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return " no element in queue"
        else:
            self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


customQueue = Queue(3)
print(customQueue)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.dequeue()
print(customQueue)
