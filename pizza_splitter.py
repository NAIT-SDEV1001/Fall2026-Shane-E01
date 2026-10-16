print("Question 1 - Pizza Splitter")

try:
    cost = float(input("Enter the total pizza cost: "))
    people = int(input("Enter the number of people: "))
    cost_per_person = cost / people
except ValueError:
    print("Cost must be a number and people must be a whole number")
except ZeroDivisionError:
    print("You cannot split the bill between 0 people")
else:
    print(f"The cost per person is ${cost_per_person:.2f}")

print("Have a groovy day!")