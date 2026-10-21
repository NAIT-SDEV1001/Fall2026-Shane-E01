# **kwargs accept any number of keyword arguments
# The keyword arguments are stored in a dictionary
# Dictionaries store key/value pairs

#print out the traits and values
def about_you (**traits):
    #loop throught the dictionary(traits)
    # display each key and value
    #loop through the dictionaries items and get the key and the value for each entry
    for key, value in traits.items():
        print(f"{key}: {value}")

#function call
about_you(name = "Shane",age = 54,favorite_color = "blue")

#This is what traits looks like with the above values passed
# {"name":"Shane","age":54,"favorite_color":"blue"}