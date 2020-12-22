# Lists (arrays): are mutable and can hold multiple data types

myList = [1,2,3]
myMixedList = ["String", 100, 23.2]

#length
print(len(myList))

# access at index
print(myList[0])

# concat
newList = myList + myMixedList
print(newList)

# mutable 
newList[0] = 10
print(newList)

# add to end of list
newList.append(6)
print(newList)

# remove from end of list
newList.pop()
print(newList)

# remove from specific index using pop
newList.pop(0)
print(newList)

# sort method: does not return anything
letterList = ['a', 'e', 'x', 'b', 'c']
numList = [4,5,2,7,0,1]

letterList.sort()
numList.sort()

print(letterList)
print(numList)

# reverse list
numList.reverse()

print(numList)
