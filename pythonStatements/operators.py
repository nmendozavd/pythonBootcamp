from random import shuffle, randint

# Operators
myList = [1,2,3]

# prints num until not including 10
for num in range(10):
  print(num)

# prints from starting at 3 not including 10
for num in range(3, 10):
  print(num)

# prints from starting at 0 not including 10, every two nums
for num in range(0, 10, 2):
  print(num)

# generator creating a list starting at 0 until 10 every two numbers
print(list(range(0,11,2)))


# enumerate: index count in form of tuples
word = 'abcde'

for item in enumerate(word):
  print(item)

# zip function: combine two lists or more in form of tuple

mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']

# for item in zip(mylist1, mylist2):
#   print(item)

# check if something is in list
print('x' in [1,2,3])

min(myList)
max(myList)

# shuffle function (imported)
shuffle(myList)
print(myList)

#  random function (imported) (from, end)
print(randint(0, 100))

# accepts user input: converts into a string
#result = input('Enter a number here:')
#print(result)

# list comprehension 

myList3 = []
myString = 'hello'

for letter in myString:
  myList3.append(letter)

print(myList3)

# same as above in list
myList4 = [letter for letter in myString]
print(myList4)

# perform opertaions as well

celcius = [0,10,20,34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)
