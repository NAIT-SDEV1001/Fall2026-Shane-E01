rows = int(input("Enter number of rows: "))
seats = int(input("Enter number of seats per row: "))
purchased_seats = []

for row in range(1,rows + 1):
    for seat in range(1,seats + 1):
        name = input(f"Enter name for Row {row}, Seat {seat}: ")
        purchased_seats.append((row,seat,name))
        print(f"Row {row}, Seat {seat}, {name}") 

#ask the user for the name of the person in each seat

#as the names are being entered create a list of tuples 
# [(1,1,"Bob"),(1,2,"Sue"),......]
#print the list
print(purchased_seats)

print (f"\nSEATING REPORT")
print(f"{"ROW":<6}{"SEAT":<6}{"NAME":<20}")
print("-" * 32)
#print out the values for each row, seat and name
#use unpacking
for row, seat, name in purchased_seats:
    print(f"{row:<6}{seat:<6}{name:<20}") 





