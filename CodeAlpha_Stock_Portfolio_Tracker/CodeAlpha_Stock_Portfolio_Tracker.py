# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL":150,
    "AMZN": 300,
    "MSFT": 400
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks: " + ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock. Try again.")
        continue
    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity
    total_value += quantity * stock_prices[stock]

print(f"Total investment value: ${total_value}")

# Optionally save to CSV
import csv
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Value"])
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        writer.writerow([stock, qty, stock_prices[stock], value])
    writer.writerow(["Total", "", "", total_value])

print("Portfolio saved to portfolio.csv")