# 1 Product label
# A store keeps a product’s ID, name, and price together:
# product = (1042, "Wireless Mouse", 24.99)
# Use indexes to print:
# Expected output:
# Product 1042: Wireless Mouse costs $24.99
product = (1042, "Wireless Mouse", 24.99)
print(f"Product {product[0]}: {product[1]} costs ${product[2]:.2f}")

# 2 Student grade
# A teacher exports a student’s name, course, and grade:
# student_record = ("Avery Chen", "Python Basics", 87)
# Unpack the tuple into three variables. Then print:
# Expected output:
# Avery Chen earned 87% in Python Basics.

student_record = ("Avery Chen", "Python Basics", 87)
student_name, course, grade = student_record
print(f"{student_name} earned {grade}% in {course}.")

# can unpack list and tuples as well as comman seperated lists of values
x,y,z = 3,4,5
print(y)

# Delivery coordinates
# A delivery app stores each location as a pair of coordinates:
# warehouse = (53.5461, -113.4937)
# customer = (53.5550, -113.4700)
# Use indexes to print the two lines below. Then print whether the two locations are the same. The result should be False.
# Expected output:
# Pick up at: 53.5461, -113.4937
# Deliver to: 53.555, -113.47
# False

warehouse = (53.5461, -113.4937)
customer = (53.5550, -113.4700)

print(f"Pick up at: {warehouse[0]}, {warehouse[1]}")
print(f"Deliver to: {customer[0]}, {customer[1]}")

if warehouse[0] == customer[0] and warehouse[1] == customer[1]:
    print(True)
else:
    print(False)

#or
if warehouse == customer:#can compare the entire tuple against another tuple
    print(True)
else:
    print(False)

#or
print(True if warehouse == customer else False)

#OR
print(warehouse == customer)