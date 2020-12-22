# Tuples: similar to list, but they're immutable to protect data integrity

# tuple
myTuple = (1,2,3)

# list
myList = [1,2,3]

# get length
len(myTuple)
 
# access index
myTuple[0]

# returns the count amount of elements are in tuple
myTuple.count(1)

# returns index of element passed in
myTuple.index(1)

# CANNOT reassign in tuple 
myTuple[0] = "New"