import requests
import json

class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares
        self.price = self.get_current_price()

    def get_current_price(self):
        api_key = 'sk-proj-8I3tzt0cOJ5ytAxu8ahcT3BlbkFJex2V7pJfmzhdTKnHLBpY'  # Replace with your Alpha Vantage API key
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        return float(data['Global Quote']['05. price'])

    def update_price(self):
        self.price = self.get_current_price()

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        self.stocks = [stock for stock in self.stocks if stock.symbol != symbol]

    def total_value(self):
        return sum(stock.shares * stock.price for stock in self.stocks)

    def update_prices(self):
        for stock in self.stocks:
            stock.update_price()

# Example usage:
portfolio = Portfolio()

# Add stocks to the portfolio
portfolio.add_stock(Stock('AAPL', 10))
portfolio.add_stock(Stock('GOOGL', 5))

# Display total value of the portfolio
print("Total Portfolio Value:", portfolio.total_value())

# Update stock prices
portfolio.update_prices()

# Display total value after updating prices
print("Total Portfolio Value after updating prices:", portfolio.total_value())

# Remove a stock
portfolio.remove_stock('GOOGL')

# Display total value after removing a stock
print("Total Portfolio Value after removing GOOGL:", portfolio.total_value())
