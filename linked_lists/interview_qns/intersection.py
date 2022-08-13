"""
Given two singly llinked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined on
reference, not value. That is, if the kth node of the first linked list 
is the exact same node as the jth node of the second linked list, then 
they are intersecting 
"""

from operator import add
from linked_list import LinkedList, Node


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA
    diff = len(longer) - len(shorter)
    shorterNode = shorter.head
    longerNode = longer.head
    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return shorterNode


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(3, 0, 99)

llB = LinkedList()
llB.generate(3, 0, 99)

addSameNode(llA, llB, 22)
addSameNode(llA, llB, 55)
print(llA)
print(llB)
print(intersection(llA, llB))
