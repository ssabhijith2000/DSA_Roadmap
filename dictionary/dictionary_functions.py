myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

print(myDict.get('age', 27))

# if we provide a key present in dictionary it will return the value of the key
# if the jey is not present in the dictionary, the specified value is returned back
# if no value is specified and key is not found in the dictionary, None is returned

print(myDict.keys())  # returns list of keys
print(myDict.items())  # returns list of key value pairs as tuples
# it deletes a random key value pair and returns the deleted pair
print(myDict.popitem())
# add the key(first) to dict with value(second parameter)  if keys doesnt exist
print(myDict.setdefault('name1', 'added'))
# if key already exists, set the value of the key
print(myDict)
print(myDict.pop('name1', 'not'))  # deletes key in first parameter
# else returns value in second parameter

print(myDict.values())  # returns list of values in dictionary

newDict = {'a': 1, 'b': 2, 'c': 3}
myDict.update(newDict)
# we can use update to add elemetns from one dictionary to another dictionary
print(myDict)

# in operatieon  in dictionary takes O(1) time and is efficient
print('edy' in myDict.values())
