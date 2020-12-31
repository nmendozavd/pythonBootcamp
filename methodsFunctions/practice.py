#  Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
def lesser_of_two_evens(a,b):
  if a % 2 == 0 and b % 2 == 0:
    if a < b:
      return a
    else:
      return b
  else:
    if a < b:
      return b
    else:
      return a

# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

# Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
  words = text.split(' ')
  return words[0][0].lower() == words[1][0].lower()

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))


# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1, n2):
  if n1 == 20 or n2 == 20:
    return True
  elif n1 + n2 == 20:
    return True
  return False

# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))


# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
  newName = ''
  for i in range(len(name)):
    if i == 0:
      newName += name[i].upper()
    elif i == 3:
      newName += name[i].upper()
    else:
      newName += name[i]
  return newName

#print(old_macdonald('macdonald'))

# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
  mylist = text.split(' ')
  reverseList = mylist[::-1]
  reverseString = " ".join(reverseList)
  return reverseString

#print(master_yoda('I am home'))

# Given an integer n, return True if n is within 10 of either 100 or 200¶
def almost_there(n):
  if n >= 90 and n <= 110:
    return True
  elif n >= 190 and n <= 210:
    return True
  else:
    return False

# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i + 1] == 3:
      return True
  return False

# print(has_33([1, 3, 3])) # → True
# print(has_33([1, 3, 1, 3])) # → False
# print(has_33([3, 1, 3])) # → False

# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
  newString = ''

  for i in range(len(text)):
    newString += text[i] * 3
  return newString

# print(paper_doll('Hello')) # - -> 'HHHeeellllllooo'
# print(paper_doll('Mississippi')) # - -> 'MMMiiissssssiiippppppiii')


# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
def blackjack(a,b,c):
  sum = a + b + c

  if sum <= 21:
    return sum
  elif sum > 21 and a == 11 or b == 11 or c == 11:
    sum -= 10
    if sum > 21:
      return 'BUST'
    else:
      return sum
  else:
    if sum > 21:
      return 'BUST'
    else:
      return sum

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

#  Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 
#  (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
  sum = 0
  innerSection = False

  for i in range(len(arr)):
    if arr[i] == 6 and not innerSection:
      innerSection = True
      continue
    elif arr[i] == 9 and innerSection:
      innerSection = False
      continue
    elif not innerSection:
      sum += arr[i]

  return sum

# print(summer_69([1, 3, 5])) # - -> 9
# print(summer_69([4, 5, 6, 7, 8, 9])) # - -> 9
# print(summer_69([2, 1, 6, 9, 11])) # - -> 14

# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
  code = [0,0,7,'x']
  
  for i in range(len(nums)):
    if nums[i] == code[0]:
      code.pop(0)
      
  return len(code) == 1

# print(spy_game([1, 2, 4, 0, 0, 7, 5])) # - -> True
# print(spy_game([1, 0, 2, 4, 0, 5, 7])) #- -> True
# print(spy_game([1, 7, 2, 0, 4, 5, 0])) # - -> False)


# Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
  # edge case: check for 0 and 1 input
  if num < 2:
    return 0
  
  # store our primes
  primes = [2]
  # counter 
  x = 3
  # x is going through every number up to input num
  while x <= num:
    # check here if x is prime
    for y in range(3,x,2):
      if x % y == 0:
        x += 2
        break
    # unique to py - for else
    else:
      # x is a prime
      primes.append(x)
      # increment x
      x += 2
  
  print(primes)
  return len(primes)

# print(count_primes(100)) # --> 25

