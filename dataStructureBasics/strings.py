# strings: single or double quotes

exampleString = "Hello world!"

print(exampleString, "has the length of:", len(exampleString))

print(exampleString[0]) # first element
print(exampleString[-1]) # last element 


print("Slice from index 0 to 5", exampleString[0: 5]) # slicing 

print("Stepping through string", exampleString[::2]) # stepping - goes through entire string and jumps every 2 indexes (not including also has a start and stop)

print("Reversing string", exampleString[::-1]) # reverse a string trick

# string properties and methods

# strings are immuatable (we need to reassign and can't use indexing to change indvidual elements)


x = "Hello World"

print("Upper case string", x.upper())
print("Original string", x)

x.split() # creates list on space

# split on every character

## Method 1
y = []
y[:] = x
print(y)

## Method 2
splitting = list(x)
print(splitting)

# String formatting with print

print("This is a string {}".format("INSERTED"))

print("The {2} {1} {0}".format('fox', 'brown', 'quick'))

print("The {q} {b} {f}".format(f="fox", q="quick", b="brown"))

result = 100/777

## value width precision of a float f
print("The result was {r:1.3f}".format(r=result))

## f string example
print(f"The result is {result}")








