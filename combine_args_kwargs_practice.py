# Write movie_night(*movies, **details). Print a "Movies:" heading and each movie with a dash. Then print a "Details:" heading and each key-value pair. If there are no movies, print "No movies selected." under the first heading. If there are no details, print "No details supplied." under the second heading.
# Sample calls
# movie_night("Shrek", "Toy Story", snack="Popcorn", start="7 PM")
# Expected output
# Movies:
# - Shrek
# - Toy Story
# Details:
# snack: Popcorn
# start: 7 PM

def movie_night(*movies, **details):
    print("Movies:")
    if len(movies) == 0:
        print("No movies selected.")
    for movie in movies:
        print("-", movie)
        
    print("Details:")
    if len(details) == 0:
        print("No details supplied.")
    for key, value in details.items():
        print(f"{key}: {value}")