# Dictionaries
# store key-value pairs
# keys are unique. Usually strings or numbers.
# value can be any datatype, including other dictionaries, lists, tuples...
# Useful for representing structured data

#Example
student = {"name":"Homer","age":42,"email":"Homer@gmail.com"}

#Access values by the key
print(student["name"])# retrieve a value
student["age"] = 44 #update a value
student["city"] = "Edmonton"#Add a new key-value pair

#remove a key and value
del student["city"]
#removing a key-value that does not exist is KeyError
#can check if its there then delete
if "city" in student:
    del student["city"]

#accessing a non existent key is KeyError
# print (student["Favorite_color"])

#use get() to define a return value for the key if it does not exist.
 
print (student.get("Favorite_color","N/A"))
# If there is no default return value provided None is returned
print (student.get("Favorite_color"))