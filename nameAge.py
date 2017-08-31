#Gary Li
#8/31/17
#nameAge.py

name = input('Enter your first and last name: ')
age = int(input('Enter your age: '))
firstname, lastname = name.split()
print('Your first name has', len(firstname), 'letters')
print('Your last name has', len(lastname), 'letters')
print('Next year you will be', age+1, 'years old')