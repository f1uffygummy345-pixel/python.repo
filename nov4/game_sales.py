import csv
from pathlib import Path
from pprint import pprint

def read_sales(file_path):
    
    sales = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for sale in reader:
                sales.append(sale)
    except FileNotFoundError:
        print(f'Error: The file {file_path} does not exist')
        return None
    return sales

def main():
    file_path = Path(__file__).parent/'data'/'game_sales.csv'
    sales = read_sales(file_path)
    pprint(sales)
    data_folder = Path(__file__).parent / "data"

    input_file = data_folder / "game_sales.csv"
    output_file = data_folder / "popular_games.csv"

    sales = read_sales(input_file)

    if sales is None:
        return

    popular_games = get_popular_games(sales)

    print(f"Sales records read: {len(sales)}")

    if popular_games:
        print("\nQualifying games:")
        for game in popular_games:
            print(f"{game['Game']}: ${game['Revenue']}")
    else:
        print("No games earned at least $100")
        
    write_report(output_file, popular_games)

    print(f"\nReport written to: {output_file.name}")
    
def get_popular_games(sales):
    """Return games with revenue of at least $100."""
    popular_games = []

    for sale in sales:
        price = float(sale["Price"])
        quantity = int(sale["Quantity"])
        revenue = price * quantity

        if revenue >= 100:
            popular_games.append({
                "Game": sale["Game"],
                "Category": sale["Category"],
                "Revenue": f"{revenue:.2f}"
            })

    return popular_games


def write_report(file_path, games):
    """Write qualifying games to a CSV report."""
    fieldnames = ["Game", "Category", "Revenue"]
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(games)


if __name__ == '__main__': 
    main()
            