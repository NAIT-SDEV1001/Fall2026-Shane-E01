#tuple is a list but cannot change
#created with () instead of []

#ask the user for a month name and print if it is a winter month
winter_months = ("December", "January", "February")
month = input("Enter a month: ")
if month in winter_months:
    print("Winter")
else:
    print("Not Winter")
#OR
print(f"{"Winter" if month in winter_months else "Not Winter"}")

#unpacking a tuple
name = ("Shane","Bell")
first_name,last_name = name
print(f"Hello {first_name} {last_name}")
#OR
first_name = name[0]
last_name = name[1]
print(f"Hello {first_name} {last_name}")

characters = [("Darth","Vader"),("Luke","Skywalker"),("R2","D2")]
print(characters)
index = int(input("Enter an index to see the character: "))
print(f"The character is: {characters[index][0]} {characters[index][1]}")