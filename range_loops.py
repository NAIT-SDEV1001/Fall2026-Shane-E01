#range() - generates a sequence of numbers (think of it as a list of numbers)
#can be used as a loop counter

#syntax
#range(start, stop, step)
#start is inclusive, stop is exclusive

#print numbers 1 to 5
for number in range(1,6):#loops 5 times
    print(number)

#print the cubes of numbers 0 to 4
for number in range (0,5):
    print(f"{number} cubed is {number ** 3}")

#OR    
for number in range (5):
    print(f"{number} cubed is {number ** 3}")

#print even numbers from 4 to 20
for number in range (4,21,2):
    print (number)

#print hello 5 times
for number in range(0,5):
    print("Hello")

#count down
for number in range(5,0,-1):
    print(number)

#odd numbers between 1 and 100
odd_numbers = list(range(1,100,2))
print (odd_numbers)

#ask the user how many times to print "Happy Thursday!"
how_many = int(input("How many Happy Thursday? "))
for number in range(0, how_many):
    print("Happy Thursday")

#a string is a list of characters
#"Shane" is actually ["S","h","a","n","e"]
#ask the user for a letter their name and tell if it is in their name
name = input("Enter your name: ")
character = input("Enter a character: ")
if character in name:
    print(f"{character} is in {name}")
else:
    print(f"{character} is not in {name}")


