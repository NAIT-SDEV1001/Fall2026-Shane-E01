#While loops repeat a block of code while the condition is True
#Useful when you do now know how many times to loop

#counter controlled loop(could also be done with a for loop range())
number = int(input("Enter a number to count to: "))
counter = 1

while counter <= number:
    print (counter)
    counter += 1

#add up numbers entered by the user until they enter 'Done'
#Display the sum

#Using a True loop
sum = 0

while True:#an endless loop, unless break
    value = input("Enter a number to add. 'Done' to display the sum: ")
    if value.upper() == 'DONE':
        break
    sum += int(value)
print(sum)#print the sum after breaking out of the loop

#Boolean flag
sum = 0
keep_going = True

while keep_going:
    value = input("Enter a number to add. 'Done' to display the sum: ")
    if value.upper() == 'DONE':
        keep_going = False
    else:
        sum += int(value)
print(sum)
    
#while loops can execute 0 or many times
answer = input("Do you want to play the game?(y,n) ")
while answer.lower() == 'y':
    name = input("Enter your name: ")
    print(f"The name {name} in upper case is {name.upper()}")
    print("That was fun!")
    answer = input("Do you want to play the game again?(y,n) ")

print("Have a groovy day!")

                




