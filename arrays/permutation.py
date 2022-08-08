# rotate a 3d array
from array import ArrayType
import numpy as np
myarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myarray)


def rotatematrix(matrix):
    n = len(myarray)
    for layer in range(n//2):
        first = layer
        last = n-layer - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-1-1]
