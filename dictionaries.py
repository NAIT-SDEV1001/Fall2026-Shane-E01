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

# Dictionaries as values
inventory = {
            "apples":{"stock_count":5,"price":.30},
            "bananas":{"stock_count":15,"price":.20},
            "oranges":{"stock_count":45,"price":.25}
}

#price of apples
print(inventory["apples"]["price"])

#loop through dictionary
grades = {"Homer":30,"Lisa":98,"Bart":40,"Marge":70}

#Keys
for key in grades.keys(): #.keys() is optional as it is the default
    print(f"{key}: {grades[key]}")

#dictionary["key"]
#values
total = 0
for value in grades.values():
    total += value
print(f"Average grade: {total/len(grades)}")

#keys and the values
for name, grade in grades.items():
    print(f"{name}: {grade}")

#sort by the key
for name, grade in sorted(grades.items()):
    print(f"{name}: {grade}")
#reverse sort
for name, grade in sorted(grades.items(),reverse=True):
    print(f"{name}: {grade}")

inventory = {"apples":0,"bananas":0,"oranges":0}
purchases = ["apples","bananas","apples","oranges","apples"]    
#add the boxes to inventory

#result should be
#inventory = {"apples":3,"bananas":1,"oranges":1}
#print
# apples: 3
# bananas: 1
# oranges: 1

