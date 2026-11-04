from pathlib import Path

def read_movies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            movies = file.readlines()

        return [movie.strip() for movie in movies if movie.strip]
    except FileNotFoundError:
        print("The movie file does not exist")
        return None

def write_movie(file_path, entry):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{entry}\n")    

def main():
    file_path = Path(__file__).parent / 'movies.txt'
    while True:
        print("\nMovie Menu")
        print("R - Read movies")
        print("W - Add a movie")
        print("Q - Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "r":
            movies = read_movies(file_path)

            if movies is None:
                continue

            if not movies:
                print("The movie list is empty.")
            else:
                print("\nMovie List:")
                for movie in movies:
                    print(movie)

        elif choice == "w":
            entry = input("Enter a movie title: ").strip()

            if not entry:
                print("Please enter a movie title.")
                continue

            write_movie(file_path, entry)
            print("Movie saved!")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Please choose R, W, or Q.")






if __name__== "__main__":
    main()