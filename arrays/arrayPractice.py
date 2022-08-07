from array import *

# 1. Create an array and traverse

my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print("Step 2")
print(my_array[0])

#3 Append any valu3 to the array using append() method
print("Step 3")
my_array.append(6)
print(my_array )

#4 Insert value in an array using insert() method
print("Step 4")
my_array.insert(3,11)

#5 Ext end python array using extend() method
my_array1 = array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)

 