def print_delivery(customer, city, parcels):
    print(f"{customer} has {parcels} parcels going to {city}.")

delivery = ("Maya", "Edmonton", 3) 
print_delivery(*delivery)