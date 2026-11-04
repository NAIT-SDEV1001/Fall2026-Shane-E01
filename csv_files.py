#CSV files are comma, seperated values
#Used to store tabular data
import csv
from pathlib import Path
from pprint import pprint

#Read all the artists
def read_artists(file_path):
    all_artists = []
    with open(file_path,"r",encoding = "utf-8") as file:
        reader = csv.DictReader(file)#read a row from the file into a dictionary
        for artist in reader:#for each row on the file
            all_artists.append(artist)#append to the list of dictionaries
    return all_artists

#function to retun arists that have more than a mimnimum number of monthly listeners
def filter_by_minimum_listeners(file_path, minimum):
    artists = read_artists(file_path)
    return [artist for artist in artists if int(artist["monthly_listeners"]) > minimum]


def write_artists_to_file(file_path,artists):
    #create list of strings for the header row
    #get the keys from the first dictionary in the list
    fieldnames = list(artists[0].keys())
    #newline = "" means to allow csv.dictWriter to manage the new line returns. This will prevent extra lines between rows
    with open(file_path,"w",newline = "", encoding = "utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)

#add a new field/key to the file/dictionary
#add a listeners_per_member column that divides each bands monthly listeners by there member count
def add_listeners_per_member(file_path):
    artists = read_artists(file_path)
    for artist in artists:
        listeners = int(artist["monthly_listeners"])
        members = int(artist["members"])
        artist["listeners_per_member"] = round(listeners/members)
    write_artists_to_file(file_path,artists)

def main():

    file_path = Path(__file__).parent/"data"/"music_artists.csv"
    artists = read_artists(file_path)
    # pprint(artists)

    popular_artists = filter_by_minimum_listeners(file_path,18400000)
    # pprint(popular_artists)

    file_path = Path(__file__).parent/"data"/"popular_artists.csv"
    write_artists_to_file(file_path,popular_artists)

    add_listeners_per_member(file_path)

if __name__ == "__main__":
    main()