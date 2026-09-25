#Sorting
numbers = [42,7,1,9,100,3]
numbers.sort() #sort ascending
print(numbers)
numbers.sort(reverse = True)
print(numbers)

#add a value to a list
colors = ["red","green"]
colors.append("orange")#end of the list
colors.insert(1,"fuschia")
print(colors)

#extend with another list
added_list = ["pink","purple"]
colors.extend(added_list)
print(colors)

colors[1:3] = added_list
print(colors)

#removing values
pets = ["dogs","cats","birds","dragons","unicorns"]
removed_pet = pets.pop(2)#removes the element and returns the value
print(f"removed {removed_pet}")
print(pets)

#remove the element
del pets[3]
print(pets)

#remove by value
pets.remove("cats")
print(pets)

#removing a value that does not exist is an error
# pets.remove("dodo bird")

cities = ["Edmonton","Calgary","Red Deer","Lethbridge","Camrose"]
found = "Edmontonnnnnnnnn" in cities#returns True or False
print(f"Edmonton is in the list? {found}")

if "Edmonton" in cities:
    cities.remove("Edmonton")

#index of a value
print(f"The index of Red Deer is: {cities.index("Red Deer")}")

#count of occurences of a value
cities = ["Edmonton","Calgary","Red Deer","Lethbridge","Camrose","Edmonton"]
print(cities.count("Edmonton"))

#clear a list
cities.clear()

