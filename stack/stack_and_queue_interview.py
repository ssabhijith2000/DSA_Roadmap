# Describe how you could use a single python list to implement three stacks


class MultiStack:
    def __init__(self, stackSize) -> None:
        self.numberstacks = 3
        self.custList = [0] * (stackSize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stackSize = stackSize

    def isFull(self, stackNum):
        if self.sizes[stackNum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stackNum):
        if self.sizes[stackNum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stackSize
        return offset + self.sizes[stacknum] - 1

    def push(self, value, stackNum):
        if self.isFull(stackNum):
            return "the stack is full"
        else:
            self.sizes[stackNum] += 1
            self.custList[self.indexOfTop(stackNum)] = value

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return "is empty"
        else:

            value = self.custList[self.indexOfTop(stackNum)] = 0
            self.custList[self.indexOfTop(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            return "stack is empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)] = 0
            return value


customStack = MultiStack(4)
customStack.push(1, 1)
customStack.push(2, 1)
customStack.push(3, 1)
print(customStack.peek(1))
print(customStack.isFull(0))
