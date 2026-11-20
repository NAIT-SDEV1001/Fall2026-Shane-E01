#import datetime class to work with dates and time
from datetime import datetime

#string representation of your birthdate
my_birthday = "01/20/1972"

#make a datetime object from the string
#use .date() to just return the date component
my_birthday_object = datetime.strptime(my_birthday,"%m/%d/%Y").date()

#print the object
print(my_birthday_object)

#create date string from a datetime object
my_birthday_string = my_birthday_object.strftime("%B/%A/%y")

print(my_birthday_string)

print(f"I was born on a {my_birthday_object.strftime("%A")}")

# %m	Month number	11
# %d	Day of the month	18
# %y	Two-digit year	26
# %Y	Four-digit year	2026
# %b	Abbreviated month name	Nov
# %B	Full month name	November
# %a	Abbreviated weekday name	Wed
# %A	Full weekday name	Wednesday
