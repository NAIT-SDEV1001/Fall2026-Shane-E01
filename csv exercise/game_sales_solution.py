"""Instructor key: read CSV sales and write games earning at least $100."""
import csv
from pathlib import Path


def read_sales(file_path):
    sales = []#list of dictionaries from the file
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for sale in reader:
                sales.append(sale)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    return sales


def get_popular_games(sales):
    popular_games = []
    for sale in sales:
        # DictReader supplies strings, so convert before calculating.
        price = float(sale['Price'])
        quantity = int(sale['Quantity'])
        revenue = price * quantity
        if revenue >= 100:
            popular_games.append({
                'Game': sale['Game'],
                'Category': sale['Category'],
                'Revenue': f"{revenue:.2f}"
            })
    return popular_games


def write_report(file_path, games):
    # Explicit names allow a header-only report when games is empty.
    fieldnames = ['Game', 'Category', 'Revenue']
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for game in games:
            writer.writerow(game)


def main():
    data_dir = Path(__file__).parent / 'data'
    input_path = data_dir / 'game_sales.csv'
    output_path = data_dir / 'popular_games.csv'
    sales = read_sales(input_path)
    # None means missing file; [] means a successfully read empty file.
    if sales is None:
        return
    popular_games = get_popular_games(sales)
    write_report(output_path, popular_games)
    
    print(f"Sales records read: {len(sales)}")
    if popular_games:
        print("\nGames earning at least $100:")
        for game in popular_games:
            print(f"{game['Game']}: ${game['Revenue']}")
    else:
        print("\nNo games earned at least $100.")
    print(f"\nReport saved to {output_path.name}")


if __name__ == '__main__':
    main()
