# I/O with Basic Files in Python

# open file
# myFile = open('test.txt')
# read file
# print("Read Once:", myFile.read())
# seek file back to 0 since it was already read once
# myFile.seek(0)
# call read again successfully
# print("Read again:", myFile.read())

# read line one by one
# myFile.seek(0)
# print("Readline First:", myFile.readline())
# print("Readline Second:", myFile.readline())
# print("Readline Third:", myFile.readline())

# readlines method to read everyline in list (array)
# myFile.seek(0)
# print("Readlines:", myFile.readlines())

# need to close file (not necessary using with open function below)
#myFile.close()

# mode options
# r in mode is read, 
# w is overwrite files or create new, 
# a is to add lines
# r+ is reading and writing
# w+ writing and reading (overwrites existing files or creates new files)

# addes this line to file everytime I run the program
with open('test.txt', mode='a') as myFile:
  myFile.write("\nAdding a fourth line")
# reads the file
with open('test.txt', mode='r') as myFile:
  print(myFile.read())

# creates file if it doesn't exist
with open('createFile.txt', mode= 'w') as f:
  f.write('I created this file')
# reads file contents I created
with open('createFile.txt', mode='r') as f:
  print(f.read())
 
