#We want to trap exceptions. 
#We can then print "Nice error messages" AND keep the program running
#Trap exceptions gracefully
#Use try/except

# sum = 0
# count = 0

# while True:
#     number = int(input("Enter a number: "))
#     if number == -1:
#         break
#     sum += number
#     count += 1

# average = sum/count
# print(f"The average is: {average}")
# #What exeptions could occur:
# #User enters a string instead of number - ValueError
# #divide by 0 - ZeroDivisionError

# #rewrite without exception handling
# #denominator of 0 is easy to handle but the ValueError is more difficult
# sum = 0
# count = 0
# average = 0

# while True:
#     number = int(input("Enter a number: "))
#     if number == -1:
#         break
#     sum += number
#     count += 1
# if count != 0:
#     average = sum/count
# print(f"The average is: {average}")

#Use Try/Except
# sum = 0
# count = 0

# while True:   
#     try: 
#         number = int(input("Enter a number: "))
#     #catch any ValueErrors in the try block
#     #the python error message will be in error_message (optional)
#     except ValueError as error_message:
#         print(f"Must be a number. Error message is: {error_message}")
#         continue
#     if number == -1:
#         break
#     sum += number
#     count += 1
# try:
#     average = sum/count
#     print(f"The average is: {average}")
# except ZeroDivisionError:
#     print("No numbers were entered.")

#else
# sum = 0
# count = 0

# while True:   
#     try: 
#         number = int(input("Enter a number: "))
#     #catch any ValueErrors in the try block
#     #the python error message will be in error_message (optional)
#     except ValueError as error_message:
#         print(f"Must be a number. Error message is: {error_message}")
#         continue
#     else:#executes if no exception occurs
#         print("Number accepted")
#     if number == -1:
#         break
#     sum += number
#     count += 1
# try:
#     average = sum/count
#     print(f"The average is: {average}")
# except ZeroDivisionError:
#     print("No numbers were entered.") 
# finally:  #Executes if an exception occured or not. 
#    print("Always executes")

#Multiple exceptions from one try
# try:
#     number = int(input("Enter a number: "))
#     result = 100/number
# except ValueError:
#     print("Must be a number")
# except ZeroDivisionError:
#     print("Number cannot be 0")
# else:
#     print(f"result is : {result}")    

#Raise a custom exception
sum = 0
count = 0

while True:   
    try: 
        number = int(input("Enter a number: "))
        if number < -1:

            raise ValueError ("Negative numbers not allowed, except -1")
    except ValueError as error_message:
        print("Invalid Input")
        continue
    else:#executes if no exception occurs
        print("Number accepted")
    if number == -1:
        break
    sum += number
    count += 1
try:
    average = sum/count
    print(f"The average is: {average}")
except ZeroDivisionError:
    print("No numbers were entered.") 
finally:  #Executes if an exception occured or not. 
   print("Always executes")



