# function to return the product of all elements in an array
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])


print(productOfArray([1, 2, 3]))  # 6
print(productOfArray([1, 2, 3, 10]))  # 60
