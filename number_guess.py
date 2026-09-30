import random

#generate 3 random numbers and put in a list
random_numbers = [random.randint(1,10),random.randint(1,10),random.randint(1,10)]

#Get the users guess
user_guess = int(input("Enter a guess: "))

#Is guess in the list
if user_guess in random_numbers:
    print("You win!")
else:
    print("You lose!")

print (f"The numbers were: {random_numbers}")
