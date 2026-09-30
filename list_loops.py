# bands = ["Abba", "ACDC", "Tool", "Queen", "Chase Atlantic"]

# #for loop allows us to look at each value in a list
# #band is a variable which holds each value as it loops through the list
# for band in bands:
#     print(f"{band} is a great band!")


# #loop through the list and display an itemized list of bands
# #enumerate returns the index and the value
# for index, band in enumerate(bands, start = 1):
#     print(f"{index }. {band}")

# #Display only the characters that are not from the dark side of the force

# characters = ["Anakin Skywalker", "Darth Vader", "Yoda", "Darth Maul", "Princess leia" ]

# dark_side = ("Darth Vader","Darth Maul", "General Grievous")

# for character in characters:
#     if character not in dark_side:
#         print(character)

# #Using continue
# for character in characters:
#     if character in dark_side:
#         continue #will go to the next iteration of the loop
#     print(character)

#Using the following add code to create 2 new lists called rebellion and empire. Populate them with the appropriate characters from the character list using a for loop. Display the itemized values of each list.
characters = ["Anakin Skywalker", "Darth Vader", "Yoda", "Darth Maul", "Princess leia" ]

dark_side = ("Darth Vader","Darth Maul", "General Grievous")#Empire

rebellion = []
empire = []

for character in characters:
    if character not in dark_side:
        rebellion.append(character)
    else:
        empire.append(character)

print("Empire")
for index, character in enumerate(empire, start=1):
    print(f"{index}. {character}")

print("Rebellion")
for index, character in enumerate(rebellion, start=1):
    print(f"{index}. {character}")


