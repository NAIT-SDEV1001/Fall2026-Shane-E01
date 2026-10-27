#A function is a block of code that performs a task. You define it once and call it whenever you need it!

#Why use functions?
#Code reuse
#break large problems into smaller problems
#make changes easily
#Test and debug small chunks of your program

#defines the display_welcome function
def display_welcome():
    print("Welcome to the Snack Shack!")
    print("Most Snacks are $4.00 each.")

def display_item(item_name):#item_name is called a parameter
    print(f"Preparing {item_name}")

def calculate_total(quantity,unit_price = 4):#parameters can have a default
    total = quantity * unit_price 
    return total    

def display_output(item_name, quantity, total):
    print(f"Snack: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")

#function to get a valid quantity from the user
def get_valid_quantity():
    #ask the user for a quantity
    while True:
    #keep looping until a valid quantity is entered (integer > 0)
        try:
            valid_quantity = int(input("Enter a quantity: "))            
        except ValueError:
            print("Please enter a whole number")
            continue
        
        if valid_quantity > 0:
            break
        print("Quantity must be > 0")

    #return the valid quantity
    return valid_quantity


UNIT_PRICE = 3

display_welcome() #calls the display_welcome function
item_name = input("Snack name: ")
display_item(item_name)#item_name is called an argument
quantity = get_valid_quantity()
# total = calculate_total(quantity,UNIT_PRICE)
#total = calculate_total(quantity) # Use the default
#total = calculate_total(quantity,8)#override the default
total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)#keyword arguments
display_output(item_name, quantity, total)




 


