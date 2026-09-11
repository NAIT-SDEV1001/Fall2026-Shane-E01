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
# # 5 * 6 = 30

# number_one = int(input("Enter number 1: "))
# number_two = int(input("Enter number 2: "))

# product = number_one * number_two

# print(f"{number_one} * {number_two} = {product}")



#get 2 numbers from the user and place in variables
#print out the value that is in each variable:
    #number1: 50
    #number2: 80
#swap the numbers so that the value that was in number1 is now in number2 and vice versa
#print the value that is each variable after the swap
    #number1: 80
    #number2: 50

# #get number1 from user
# number1 = input("Enter number 1: ")
# #get number2 from user
# number2 = input("Enter number 2: ")
# #print values in each variable
# print(f"number1: {number1}")
# print(f"number2: {number2}")
# #swap the numbers
# temp = number1
# number1 = number2
# number2 = temp
# #print values in each variable
# print(f"number1: {number1}")
# print(f"number2: {number2}")

#Formatting numbers
total = 100.1234567

print(round(total,2)) # round to 2 decimal places (currency)
print(round(total,6))

print(f"{total:.2f}") #format total to 2 decimal places
print(f"{total:.6f}")

price = 100
print(f"{price:.2f}")

# Math functions
# import the math module which contains math functions and constants
import math

test_value = 5.245435
print(math.ceil(test_value)) # round up to the next whole number
print(math.floor(test_value)) # round down to the next whole number
print(math.pow(2,3)) # exponent
print(math.sqrt(9)) # square root
print(math.pi) # constant containing pi


print(max(1,5,3,77,5,73)) #maximum number
print(min(1,5,3,77,5,73)) #minimum number


