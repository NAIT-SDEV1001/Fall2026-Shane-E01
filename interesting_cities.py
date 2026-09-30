interesting_cities = [
    'Edmonton',
    'Paris',
    'Munich',
    'Berlin',
    'Amsterdam',
    'Prague',
]

interesting_cities.remove("Edmonton")
new_city = input("Enter a city that interests you: ")
interesting_cities.append(new_city)

interesting_cities.sort()
print("Our list of interesting cities in alphabetical order is:")
print(interesting_cities)