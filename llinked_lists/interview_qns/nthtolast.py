# implement an algorithm to find the nth to last element of a singly linked list.
from linked_list import LinkedList


def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


customLL = LinkedList()
customLL.generate(10, 1, 99)
print(customLL)
print(nthToLast(customLL, 3))
