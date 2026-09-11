# Beginning Python Exercises
# 1.
# Ask the user for a temperature in Celsius and convert it to Fahrenheit.

#Get temp in celcius
celsius = float(input("Enter a temperature in celcius: "))
#convert celcius to Fahrenheit
fahrenheit = celsius * 9/5 + 32
#print Fahrenheit
print(f"Celsius: {celsius} => Fahrenheit: {fahrenheit}")

# 2.
# Ask the user for a name, an adjective, a verb (past tense) and a place. Print a silly sentence using them.


# 3.
# Ask the user for the width and height of a rectangle. There could be decimals. Calculate and display the width, height, area, and perimeter. Calculations print the results rounded to 3 decimal places.

# 4.
# Ask for the price of an item and the quantity purchased. Display the amount of the total including GST.


# 5.
# Ask the user for a number of miles and print out how many kilometres it is. Display to 2 decimal places.
# The conversion rate is 1 mile = 1.609344 kilometers



# 6.
# Ask the user for the distance they want to travel, the fuel consumption of their vehicle in l/100km and the price per litre. Display the cost for the trip!

#Get the distance, consumption and price from user
distance = float(input("Enter the distance in km: "))
fuel_consumption = float(input("Enter fule consumption in l/100km: "))
price_per_litre = float(input("Enter the price per litre: "))

#Calculate trip cost
    #Calculate litres needed for the distance
litres_needed = distance * fuel_consumption/100
    #Trip cost is litres * price per litre 
trip_cost = litres_needed * price_per_litre
#display trip cost

print(f"Fuel needed: {litres_needed} litres")
print(f"Trip Cost: ${trip_cost:.2f}")





