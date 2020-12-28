# Use for, .split(), and if to create a Statement that will print out words that start with 's':
s = 'Print only the words that start with s in this sentence'
words = s.lower().split()

for word in words:
  if(word.startswith('s')):
    print(word)

# Use range() to print all the even numbers from 0 to 10.
for item in range(0,11,2):
  print(item)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
listBy3 = [num for num in range(1,50) if num % 3 == 0]
print(listBy3)

#Go through the string below and if the length of a word is even print "even!"
t = 'Print every word in this sentence that has an even number of letters'

words1 = t.split()

for word in words1:
  if(len(word) % 2 == 0):
    print('even')


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz', num)
  elif num % 3 == 0:
    print('Fizz', num)
  elif num % 5 == 0:
    print('Buzz', num)

#Use List Comprehension to create a list of the first letters of every word in the string below:
u = 'Create a list of the first letters of every word in this string'

firstLetters = [word[0] for word in u.split()]
print(firstLetters)
