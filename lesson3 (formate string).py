first_name = "khalid"
last_name = "Elabd"


# Using f-string for formatting
formatted_string = f"My name is {first_name} {last_name}"
print(formatted_string)


# using string concatenation 
print("My name is " + first_name + " " + last_name )  


# using comma to separate values
print("My name is", first_name, last_name )  


# important note:
# f-string is more efficient than string concatenation
# f-string is more readable than string concatenation
# f-string is more efficient than using comma to separate values
# f-string is more readable than using comma to separate values
# f-string is the best way to format strings in Python


# Look at the following example:

print("My name is 'khalid'")
print('My name is "khalid"')

# using escape characters
print("My name is \"khalid\"")
print('My name is \'khalid\'')


# using triple quotes
print ("""My name is
khalid""")