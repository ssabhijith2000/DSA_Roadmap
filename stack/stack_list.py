import re


class Stack:
    def __init__(self) -> None:
        self.list = []

    def __st__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no elemnt to pop"
        else:
            return self.list.pop()
    # peek

    def peek(self):
        if self.isEmpty():
            return "There is no element in the space"
        else:
            return(self.list[len(self.list)-1])

    # delete
    def delete(self):
        self.list = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
