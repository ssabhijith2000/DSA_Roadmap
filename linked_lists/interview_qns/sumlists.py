"""
You have two numbers represented by a linked list,
where each node contains a single digit. The digit
are stored in reverse order, such that the 1's 
digit is at the head of the list. Write a function 
that adds the two numbers and returns the sum as a 
linked list.  
"""

from linked_list import LinkedList


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result/10
    return ll


llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print(llA)
print(llB)
print(sumList(llA, llB))
