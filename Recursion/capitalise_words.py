def capitialise_words(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitialise_words(arr[1:])


words = ['i', 'am', 'learning', 'recursion']
print(capitialise_words(words))  # ['I', 'AM', 'LEARNING', 'RECURSION']
