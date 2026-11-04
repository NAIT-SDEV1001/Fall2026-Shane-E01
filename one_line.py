from pathlib import Path

def display_games_one_line_at_a_time(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            #Read the first line
            line = file.readline()#reads the current line
            while line != "":
                #skip lines with only whitespace
                if line.strip():
                    print(line.strip()) 
                line = file.readline()
    except FileNotFoundError:
        print("That file does not exist")

def main():
    file_path = Path(__file__).parent/"games.txt"
    print("Reading one line at a time: ")
    display_games_one_line_at_a_time(file_path)

if __name__ == "__main__":
    main()




