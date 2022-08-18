# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
#  People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receiv the oldest animal of that type).
# They cannot select which specific animal they qould like. Create the data structures to maintain this system and
# implement oiperations such as enqueue, dequeue. Any, dequeue Dog, and dequeue Cat

from collections import deque


class AnimalShelter:
    def __init__(self) -> None:
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeCat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0)

    def dequeDog(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.dogs.pop(0)

    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result


customQueue = AnimalShelter()
customQueue.enqueue("Cat1", "Cat")
customQueue.enqueue("Cat2", "Cat")
customQueue.enqueue("Dog1", "Dog")
customQueue.enqueue("Cat3", "Cat")
customQueue.enqueue("Cat3", "Cat")
customQueue.enqueue("Dog2", "Dog")
print(customQueue.dequeCat())
