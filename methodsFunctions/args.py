# args: functions that can accept an arbituary number of parameters
# *args in parameter

def myfunc(*args):
  return sum(args)

print(myfunc(10,50,2,4,2,7,8,9))
print(myfunc(1, 2, 2))
print(myfunc(10, 20))

# **kwargs: lets you pass in an object to function params
def myfunc2(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('I did not find any fruit here.', kwargs)

print(myfunc2(fruit = 'apple', veggie = 'lettuce'))