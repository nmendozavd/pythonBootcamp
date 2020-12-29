from random import shuffle

myList = [1,2,3]

# call this to get help in terminal about method
# help(myList.insert(1, 3))
# inserts element (param 2) in index before provided (param 1)
myList.insert(1, 3)

# functions (def keyword) using snake casing (lowercase with underscores between words) to name functions

def say_hello(name):
  print(f'Hello {name} how are you?')

#say_hello('Noel')

def add_num(num1, num2):
  return num1 + num2

#print(add_num(1,5))


def even_check(num_list):
  even_list = []
  for num in num_list:
    if(num % 2 == 0):
      even_list.append(num)
  return even_list
#print(even_check([1,2,3,4]))


# using tuple unpacking in functions
work_hours =[('Bill', 200),('Jill', 400),('Cassie',800)]

def employee_check(work_hours):
  max = 0
  employee_of_month = ''

  for employee, hours in work_hours:
    if hours > max:
      max = hours
      employee_of_month = employee
  return (employee_of_month, max)

# print(employee_check(work_hours))

# interactions between functions


def shuffle_list(mylist):
  shuffle(mylist)
  return mylist

def player_guess():
 
  guess = ' '

  while guess not in ['0', '1', '2']:
    guess = input("Pick a number: 0, 1 or 2...")
  
  return int(guess)

def check_guess(mylist, guess):
  if mylist[guess] == 'O':
    print("Correct!")
  else:
    print("Wrong Guess!")
    return f"The list was: {mylist}"

# create list
my_list = [' ', ' ', 'O']
# shuffle list
mixed_list = shuffle_list(my_list)
# user guess
guess = player_guess()
# check guess
print(check_guess(mixed_list, guess))
