from os import curdir


class Stack:
    def __init__(self, maxSize) -> None:
        self.list = []
        self.maxsize = maxSize

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Stack is full. Cannot insert into the stack")
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None


customStack = Stack(4)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
print(customStack)
