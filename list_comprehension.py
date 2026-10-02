#Given a list of [2,4,6,8], use a loop to create a NEW list of each value doubled -> [4,8,12,16]
numbers = [2,4,6,8]
doubled = []
for number in numbers:
    doubled.append(number * 2)
print(doubled)
#With list Comprehension
#This is a short way to create a new list using a loop
numbers = [2,4,6,8]
doubled = [number * 2 for number in numbers]
print(doubled)
#new_list = [expression for item in existing_list]

#given a list of three names, create a new list of those names in Upper Case
names = ["Bart","Homer","Marge"]
upper_case_names = [name.upper() for name in names]
print(upper_case_names)

#if
#create a new list of only numbers > 10
#without list comprehension
large_numbers = []
numbers = [3,8,12,5,20]
for number in numbers:
    if number > 10:
        large_numbers.append(number)
print(large_numbers)

#if with list comprehension
numbers = [3,8,12,5,20]
large_numbers = [number for number in numbers if number > 10]
print(large_numbers)









