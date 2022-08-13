# write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
from http.client import NOT_EXTENDED
from inspect import currentframe
from linked_list import LinkedList


def partition(ll, value):
    currentNode = ll.head
    ll.tail = ll.head
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < value:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
partition(customLL, 60)
print(customLL)
