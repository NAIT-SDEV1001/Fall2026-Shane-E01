#elif
movie = input("Enter a movie name: ")
if movie.upper() == "STAR WARS" or movie.upper() == "SHREK 2":
    print ("Awesome!")
elif movie.upper() == "DUNE":
    print("Get the spice")
elif movie.upper() == "SHARKNADO":
    print("Sharks are cool")
else:
    print("Unknown movie")

#match case
match movie.upper():
    case "STAR WARS" | "SHREK 2":
        print ("Awesome!")
    case "DUNE":
        print("Get the spice")
    case "SHARKNADO":
        print("Sharks are cool")
    case _:
        print("Unknown Movie")


