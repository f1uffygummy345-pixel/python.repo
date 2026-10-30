from pathlib import Path
def read_all_games(file_path):
    try:
        with open(file_path,"r",encoding="utf-8" ) as file:
            games = file.readlines()
            clean_games = [game.strip() for game in games if game.strip()]
            return clean_games
    except FileNotFoundError:
        return None


def main():
    file_path = Path(__file__).parent/"games.txt"
    games = read_all_games(file_path)
    
    if games is None:
        print("The file was not found")
    else:
        for game in games:
            print(game)
    
    
    
if __name__ == "__main__":
    main()