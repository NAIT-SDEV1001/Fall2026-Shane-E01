#__name__ has  value of __main__ if the module was run directly
#__name__ has  value of the imported module (snack_shack) if it was run from an import
# print(f"Module name: {__name__}")

from .display import display_item,display_output,display_welcome
from .pricing import calculate_total
from .validation import get_valid_positive_integer,get_non_empty_string

def main():
    UNIT_PRICE = 3
    display_welcome() #calls the display_welcome function
    item_name = get_non_empty_string("Enter the snack name")
    display_item(item_name)#item_name is called an argument
    quantity = get_valid_positive_integer("Enter the quantity")
    # total = calculate_total(quantity,UNIT_PRICE)
    #total = calculate_total(quantity) # Use the default
    #total = calculate_total(quantity,8)#override the default
    total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)#keyword arguments
    display_output(item_name, quantity, total)
#If this module was executed directly then call main() --> mainline
if __name__ == "__main__":
    main()


 


