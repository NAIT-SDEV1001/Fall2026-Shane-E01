print("Question 3 - Game Score Average")
total = 0
count = 0
invalid_count = 0  # Optional challenge

while True:
    try:
        score = int(input("Enter a score from 0 through 100 (-1 to quit): "))
        if score != -1 and (score < 0 or score > 100):#could also check <-1 . However, breaking out the clear conditions is good
            raise ValueError
    except ValueError:
        invalid_count += 1
        print(f"Invalid score. Scores must be from 0 through 100")
        continue

    if score == -1:
        break
    total += score
    count += 1

try:
    average = total / count
except ZeroDivisionError:
    print("No scores were entered, so there is no average.")
else:
    print(f"Average score: {average:.2f}")