# input function example

name = input('Enter your name: ') # input('') without string 
print('Hello, ' + name + '!')


# important note:
num = input('Enter a number: ')
# num is a string, not an integer
# to convert it to an integer, use int()
print('The number is: ' , int(num)+5) # type conversion - type casting 