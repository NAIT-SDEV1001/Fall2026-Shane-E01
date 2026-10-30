

def get_valid_positive_integer(prompt):
    #ask the user for a quantity
    while True:
    #keep looping until a valid quantity is entered (integer > 0)
        try:
            value = int(input(f"{prompt}: "))            
        except ValueError:
            print("Please enter a whole number")
            continue
        
        if value > 0:
            break
        print("Must be > 0")

    #return the valid quantity
    return value

def get_non_empty_string(prompt):
    while True:        
        value = input(f"{prompt}: ")
        if value.strip():#strip off extra spaces  ""
            break
        print("Cannot be empty")
    return value
        

# x = "Hello"
# if x:#does x have a value
#     print("Hello to you as well")
# else:
#     print("Nothing to say?")
