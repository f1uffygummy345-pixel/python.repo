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
    write_artists_to_file(file_path,artists)

#write a file
def write_artists_to_file(file_path, artists):
    #list of the headers to be used as headers
    
    fieldnames = list(artists[0].keys())
    with open(file_path, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for artist in artists:
            writer.writeheader()
            writer.writerow(artist)
            
def filter_by_min_listeners(file_path, artists, minimum):
    artists = read_artists(file_path)
    return[artist for artist in artists if int(artist["monthly_listeners"]) < minimum]
def main():
    data_dir = Path(__file__).parent
    file_path = data_dir/"music_artists.csv"
    artists = read_artists(file_path)
    pprint(artists) #display the dictionaries AFTER the new KEY was added
    pprint(add_listeners_new_member(file_path))
    
    #write a file
    
    

if __name__ == "__main__":
    main()
    
    
#Read the file
#add a listeners_per_member that divides each band's monthly listeners by their member count