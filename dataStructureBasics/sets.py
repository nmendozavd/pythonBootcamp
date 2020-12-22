# Sets: unordered collections of UNIQUE elements

# create an instance of set
mySet = set()

mySet.add(1)
mySet.add(2)
# cannot add again since element is not unique
mySet.add(2)

print(mySet)

myList = [1,2,3,4,5,1,2,3,4,5,5,6,]

# can remove repeated elements in list by passing it into a set (not ordered)
print(set(myList))

# pass in a string
print(set('Mississippi'))
