# *args allow a function to accept any number of positional arguments
# values passed to an arg are stored in a tuple
# The * that makes a param an arg

def add_sum(*numbers):#numbers will hold the arguments in a tuple
    #add up all the numbers and return the sum
    sum = 0
    for number in numbers:
        sum += number

    return sum

print(add_sum(2,4,6,8,10))