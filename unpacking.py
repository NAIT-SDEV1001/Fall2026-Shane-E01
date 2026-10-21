#This function expects 2 arguments. name and age
def show_info(name, age):
    print(f"{name} is {age} years old")

#Store the persons name and age in a tuple
person = ("Alice",30)

# * unpacks the tuples into seperate positional arguments
show_info(*person) #unpacks into show_info("Alice",30)

#Store a persons info in a dictionary
another_person = {"name":"Shane","age":25}

# unpacks the dictionary into keyword arguments
show_info(**another_person)
#unpacks into show_info(name = "Shane",age = 25) 

#In a functions parameters, *args and **Kwargs collects arguments.
#In a function call, * and ** unpack values into arguments

