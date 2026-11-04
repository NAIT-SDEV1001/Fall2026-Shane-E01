from pathlib import Path

def write_game(file_path,game):
    with open(file_path,'a',encoding='utf-8') as file:
        file.write(f"{game}\n")

def main():
    #if the file does not exist, it will create for you
    file_path = Path(__file__).parent/"games.txt"
    while True:
        game = input("Enter a game(q to quit): ").strip()

        if game.lower() == "q":
            break
        if not game:
            print("Please enter a game!")
            continue
        write_game(file_path,game)
        print("Entry saved")
    print("Have a groovy day!")

if __name__ == "__main__"              :
    main()