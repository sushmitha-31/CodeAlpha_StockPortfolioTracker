import csv

stock_prices = {
    "RELIANCE": 1373,
    "INFOSYS": 1447,
    "TCS": 3022,
    "WIPRO": 246,
    "ITC": 411
}

def display_stocks():
    print("\nAvailable Stocks and Prices (per share):")
    for stock, price in stock_prices.items():
        print(f"{stock}: ₹{price}")

def calculate_portfolio():
    portfolio = {}
    total_investment = 0

    while True:
        stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity

    return portfolio, total_investment

def save_to_file(portfolio, total_investment):
    choice = input("Do you want to save the portfolio to a file? (y/n): ").lower()
    if choice == "y":
        file_type = input("Enter file type (txt/csv): ").lower()

        if file_type == "txt":
            with open("portfolio.txt", "w", encoding="utf-8") as file:
                for stock, qty in portfolio.items():
                    file.write(f"{stock}: {qty} shares, {stock_prices[stock]} each\n")
                file.write(f"Total Investment: ₹{total_investment}\n")
            print("Portfolio saved to portfolio.txt")

        elif file_type == "csv":
            import csv
            with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Stock", "Quantity", "Investment"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock] * qty])
                writer.writerow(["Total", "", total_investment])
            print("Portfolio saved to portfolio.csv")

        else:
            print("❌ Invalid file type. Skipping save.")

def main():
    print("📈 Stock Portfolio Tracker")
    display_stocks()
    portfolio, total_investment = calculate_portfolio()

    if portfolio:
        print("\nYour Portfolio:")
        for stock, qty in portfolio.items():
            print(f"{stock}: {qty} shares, ₹{stock_prices[stock] * qty}")
        print(f"\n💰 Total Investment: ₹{total_investment}")
        save_to_file(portfolio, total_investment)
    else:
        print("No stocks purchased.")

if __name__ == "__main__":
    main()