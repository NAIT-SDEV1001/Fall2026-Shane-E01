print("Intro to Python")
# Comment - does not execute
# To comment
# multiple lines, highlite the lines
# and ctrl /

# Case Sensitive
# Extra spaces around commands, operators, etc.. do not matter
print                           ("Hello")
print("World")
# Spaces do matter for indentation to create code blocks
# Strings can use "" OR ''. "" more common, but be consistent
print ("It's a groovy day!")
# print ('It's a groovy day!')
# print ("It's a "groovy" day")

# Escape sequences
# provide a way to "escape" the string and perform an action
print ("It's a \"groovy\" day!")
print ('It\'s a "groovy" day!')
print ("Hello\nWorld") #New line
print ("Name:\tShane") #Tab
print ("\\n is how you go to the next line")

# Variables
# A named container that holds a value
# The value can change
# Variable names cannot start with a number, and only contain letters, numbers and _. Cannot be a keyword
# variable names are written in snake_case
# In Python we do not explicitly declare/create variables

# assigning values to variables
first_name = "Shane" # String - in quotes
age = 54 # integer
price = 23.45 # float
is_valid = True # Boolean (T/F)

print (age)
age = 24
print (age)

# String Concatonation
# + is a string concatonation operator

print ("Hello " + first_name + "!")

# Cannot concatonate non string variables with +
# print ("Hello " + first_name + "! I see you are " + age + " years old." )
#But you can Cast/Convert the age variable to a string
print ("Hello " + first_name + "! I see you are " + str(age) + " years old." )

# You can use , as well to concatonate any datatype
print ("Hello",first_name,"! I see you are",age,"years old." )

# Preferred way (f strings)
print (f"Hello {first_name}! I see you are {age} years old")

# Constants
# Gives a name to a value
# Coded in SCREAMING_SNAKE_CASE
GST_RATE = 0.05
gst = 100.00 * GST_RATE
print (gst)

# User Input
# input returns a string

# name = input("Enter your name: ")
# age = input("enter your age: ")

# print(f"Welcome {name}. You are {age} years old.")

# Prompt for 2 numbers
# Add them together
# Display the sum
# Remember input returns strings. Must cast to numbers to perform math
# number_one = int(input("Enter number 1: "))
# number_two = int(input("Enter number 2: "))

# sum  = number_one + number_two

# print(sum)

# Math operators
print (4 + 2) #6
print (4 - 2) #2
print (4 * 2) #8
print (4 / 2) #2 / returns a float answer
print (7 / 2) #3.5
print (9 // 4) #2 - Floor division (rounds down to whole number)
print (2 ** 3) #8 - exponent
print (9 % 4) #1 - Modulous

#ask for 2 numbers, multiply them and display:
# 5 * 6 = 30

number_one = int(input("Enter number 1: "))
number_two = int(input("Enter number 2: "))

product = number_one * number_two

print(f"{number_one} * {number_two} = {product}")
