from pathlib import Path

#with will open and close the connection
#file_path is where your file is
#'r' means read, others are 'w','a'
#as file - refer to the connection by that name (file)
def read_games(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            #read all the lines on the file into a list
            games = file.readlines()
            #use list comprehension to return a clean list of values from the file
            #if the row on the file has a value, after strip(), then add it to the new list
            clean_list = [game.strip() for game in games if game.strip()]
            print(clean_list)
        return clean_list
    except FileNotFoundError:
        return None


def main():
    #__file__ is the path to this file.
    #.parent is the parent folder of this file
    file_path = Path(__file__).parent/"games.txt"
    games = read_games(file_path)

    if games is None:
        print("The text file was not found")
    else:
        print("Games on the list:")
        for game in games:
            print(game) 

if __name__ == "__main__":
    main()
    