from .validation import get_valid_age, get_valid_quantity
from .display import display_receipt,display_welcome
from .pricing import get_ticket_price, calculate_total


def main():
    display_welcome()
    age = get_valid_age()
    quantity = get_valid_quantity()
    ticket_price = get_ticket_price(age)
    total = calculate_total(quantity,ticket_price)
    display_receipt(quantity,ticket_price,total)

#main guard 
if __name__ == "__main__":
    main()
