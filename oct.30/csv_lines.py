import csv #to use dictreader
from pathlib import Path
from pprint import pprint #used to make more readable output for collections
def read_artists(file_path):
    all_artists = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for artist in reader:
             #  pprint(artist)
             all_artists.append(artist)
        
        
    
    except FileNotFoundError:
        print(f"Error! The file{file_path} does not exist")
    return all_artists

def add_listeners_new_member(file_path):
    artists = read_artists(file_path)
    for artist in artists: # for each dictionary in the list
        #Cast to int's for the division calculation
        listeners = int(artist['monthly_listeners'])
        members = int(artist['members'])
        artist['listeners_per_member'] = round(listeners/members)

def main():
    data_dir = Path(__file__).parent
    file_path = data_dir/"music_artists.csv"
    artists = read_artists(file_path)
    pprint(artists)
    
    
    
if __name__ == "__main__":
    main()
    
    
#Read the file
#add a listeners_per_member that divides each band's monthly listeners by their member count