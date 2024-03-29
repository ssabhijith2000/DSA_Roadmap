# Question 1 - Remove Dups: write a code to remove duplicates from an unsorted linked list.
from linked_list import LinkedList


def removeDups(ll):  # O(n)
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll


def removeDupswithoutTemp(ll):  # O(n2)
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.next.value == currentNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
        return ll.head


customll = LinkedList()
customll.generate(10, 0, 99)
print(customll)
removeDups(customll)
print(customll)
