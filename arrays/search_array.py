# Find an element in an array
import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


def findNumber(array, number):
    for x in range(len(array)):
        if array[x] == number:
            print(x)


findNumber(myArray, 6)
