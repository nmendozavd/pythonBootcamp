# Loops - iterate through an object

# looping through a list 
myList = [1,2,3,4,5,6,7,8,9,10]

for num in myList:
  if num % 2 == 0:
    print(f"even: {num}")
  else:
    print(f"odd: {num}")


list_sum = 0

for num in myList:
  list_sum += num

print(list_sum)

# looping through a string
myString = "hello world"

for letter in myString:
  print(letter)

# looping through list with tuples (unpacking)

myList2 = [(1,2),(3,4),(5,6),(7,8)]

# unpacking the list with tuples 
for (a,b) in myList2:
  print(a,b)

# looping through a dictionary

myDict = {'k1': 1, 'k2': 2, 'k3': 3}

# by default grabs keys only
# items() gets key value in tuple form
# .values() gets values

for key, value in myDict.items():
  print(key)
  print(value)

for value in myDict.values():
  print(value)

