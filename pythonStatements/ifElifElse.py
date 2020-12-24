# IF ELIF ELSE
# indentation and white space is necessary 

# if some_condition:
#   execute some code
# elif 
#   execute some code
# else:
#   execute some code

hungry = False

if hungry:
  print('feed me')
else:
  print('not hungry')


loc = 'auto shop'

if loc == 'auto shop':
  print('cars are cool')
elif loc == 'store':
  print('welcome to the stor')
elif loc == 'bank':
  print('money is cool')
else:
  print('not in location lists')

name = 'Noel'

if name == 'Frankie':
  print('Hello {}'.format(name))
elif name == 'Sammy':
  print('Hello {}'.format(name))
else:
  print('Hello {}'.format(name))