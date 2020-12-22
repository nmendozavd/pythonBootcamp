# Dictionaries (objects): unorderd mappings for storing objects (key, value) and mutable 

myDict = {'key': 'value', 'key2': 'value2'}
print(myDict['key'])

priceList = {'apple': 2.99, 'orange': 1.99, 'milk': 3.99}

# dictionary with nested objects
d = {'k1': 10, 'k2': [0,1,2], 'k3': { 'insideKey': 100}}

print(d['k2'][2])
print(d['k3']['insideKey'])

## methods

# get keys
print(d.keys())
# get values
print(d.values())
# get pairs
print(d.items())
