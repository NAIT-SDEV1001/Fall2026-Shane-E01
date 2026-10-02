
sold_out = ["mushrooms", "bacon"]
banned_toppings = ["pineapple"]
toppings = []
topping_count = 0
TOPPING_PRICE = 2

#get 5 toppings from user and add to a list
toppings.append(input("Enter topping 1: ").lower().strip())
toppings.append(input("Enter topping 2: ").lower().strip())
toppings.append(input("Enter topping 3: ").lower().strip())
toppings.append(input("Enter topping 4: ").lower().strip())
toppings.append(input("Enter topping 5: ").lower().strip())
print()
#print the 5 toppings
print("Requested toppings:")
for number, topping in enumerate(toppings, start = 1):
    print(f"{number}. {topping}")
print()
#print adding, sold out or banned accordingly
for topping in toppings:
    if topping in sold_out:
        print(f"Sorry, {topping} is sold out")
    elif topping in banned_toppings:
        print(f"Sorry, {topping} is banned")
    else:
        print(f"Adding {topping}")
        topping_count += 1 #shortcut of count = count + 1

#using continue (not the best for this solution)
for topping in toppings:
    if topping in sold_out:
        print(f"Sorry, {topping} is sold out")
        continue
    if topping in banned_toppings:
        print(f"Sorry, {topping} is banned")
        continue
    print(f"Adding {topping}")
    topping_count += 1 #shortcut of count = count + 1

total = topping_count * TOPPING_PRICE

print()  
#print number of added toppings and cost
print(f"{topping_count} toppings added")
print(f"Topping cost: ${total:.2f}")




