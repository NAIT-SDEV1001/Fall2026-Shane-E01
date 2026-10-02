days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_of_weekend = ("Saturday", "Sunday")

for index, day in enumerate(days_of_week):
    print(f"{day} is day number {index + 1} of the week")
    if day in days_of_weekend:
         print(f"{day} is a weekend day")
    else:
         print(f"{day} is a weekday")
         
