# Lambda Expressions, Map, Filter Functions 

# Map: Built in function that applies function in param 1 to every element in param 2

def square(num):
    return num**2

num_list = [1,2,3,4,5]

# create loop (otherwise is just prints memory location of map)
for item in map(square, num_list):
    print(item)

# or get actual list
print(list(map(square, num_list)))

# another example with strings 
def splicer(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

# Filter: only passes/filters truthy values

def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))

# Lambda Expressions: (also known as an anonymous function)

# one liner (converted square function above to lambda expression)
lambda num: num ** 2
# use with map, instead of writing square code (same with filter)
list(map(lambda num: num ** 2, mynums))




