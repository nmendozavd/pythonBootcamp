import math
#

example = "Testing"

print(math.sqrt(100))
print(math.pow(10, 2), 10 ** 2, 10 * 10)

exampleList = []
exampleList.append(0)
exampleList.append(0)
exampleList.append(0)

list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'

list4 = [5,3,4,6,1]
list4.sort()

d = {'simple_key': 'hello'}
# Grab 'hello'

d1= {'k1': {'k2': 'hello'}}
# Grab 'hello'


# Getting a little tricker
d2 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
#Grab hello

# This will be hard and annoying!
d3 = {
  'k1': [1, 2,
 {'k2': ['this is tricky', 
 {'tough': [1, 2, ['hello']]}]}]}

# create a set with the list below
list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(example[::-1])
print(example[6], example[6:]) 
print([0,0,0], exampleList)
print(list3)
print(list4)
print(d['simple_key'])
print(d1['k1']['k2'])
print(d2['k1'][0]['nest_key'][1][0])
print(d3['k1'][2]['k2'][1]['tough'][2][0])
print('Tuples are (immutable), lists are [mutable]')
print(set(list5))
print(3 == 3.0)
print(4**0.5 != 2)

