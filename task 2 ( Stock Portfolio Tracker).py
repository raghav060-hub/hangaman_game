# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}")

    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Save result in file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total_investment))
file.close()

print("Result saved in portfolio.txt")
