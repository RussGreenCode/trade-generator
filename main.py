import csv
import random
from datetime import datetime, timedelta

def read_trades_from_file(filename):
    """
    Reads in the existing trades from a CSV file and returns them as a list of dictionaries.
    """
    trades = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trades.append(row)
    return trades


def generate_random_trades(stocks, num_trades, start_date, end_date):
    """
    Generates a list of random trades for multiple stocks within a given time period.
    """
    trades = []
    for i in range(num_trades):
        # Choose a random stock
        stock = random.choice(list(stocks.keys()))

        # Choose a random order type
        order_type = random.choice(["Market", "Limit", "Stop Loss"])

        # Choose a random quantity
        quantity = random.randint(1, 100)

        # Choose a random price within a reasonable range for the stock
        if stock == "TSLA":
            price = round(random.uniform(1000, 1500), 2)
        elif stock == "AAPL" or stock == "AMZN":
            price = round(random.uniform(150, 250), 2)
        else:
            price = round(random.uniform(30, 150), 2)

        # Choose a random time in force
        time_in_force = random.choice(["Day", "Good till Cancelled", "Fill or Kill"])

        # Choose a random commission
        commission = round(random.uniform(5, 20), 2)

        # Choose a random settlement date
        settlement_date = (start_date + timedelta(days=random.randint(2, 5))).strftime("%Y-%m-%d")

        # Choose a random order status
        order_status = random.choice(["Filled", "Partially Filled", "Pending"])

        # Choose a random execution price within a reasonable range for the stock
        if stock == "TSLA":
            execution_price = round(random.uniform(950, 1600), 2)
        elif stock == "AAPL" or stock == "AMZN":
            execution_price = round(random.uniform(130, 270), 2)
        else:
            execution_price = round(random.uniform(25, 160), 2)

        # Choose a random trade date within the specified time period
        trade_date = (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime("%Y-%m-%d")

        # Create a new trade dictionary and add it to the list
        trade = {"Symbol": stock, "Quantity": quantity, "Order Type": order_type,
                 "Price": price, "Time in Force": time_in_force, "Account": None,
                 "Commission": commission, "Settlement Date": settlement_date,
                 "Order Status": order_status, "Execution Price": execution_price,
                 "Trade Date": trade_date}
        trades.append(trade)

    return trades

def assign_accounts_to_trades(trades, account_names):
    """
    Assigns account names to the list of trades in a round-robin fashion.
    """
    num_accounts = len(account_names)
    for i, trade in enumerate(trades):
        account_name = account_names[i % num_accounts]
        trade["Account"] = account_name


def write_trades_to_file(trades, filename):
    """
    Writes a list of trades to a CSV file.
    """
    with open(filename, 'w', newline='') as file:
        fieldnames = trades[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for trade in trades:
            writer.writerow(trade)


def main():
    # Define the symbols and stocks we will use
    stocks = {"ORCL": "Oracle Corporation", "IBM": "International Business Machines Corporation",
              "TSLA": "Tesla, Inc.", "LPL": "LG Display Co., Ltd.", "SAP": "SAP SE",
              "AAPL": "Apple Inc.", "GOOG": "Alphabet Inc.", "AMZN": "Amazon.com, Inc."}

    # Define the number of trades we want to generate for each account
    num_trades = 100

    # Define the start and end dates for the trades
    start_date = datetime(2023, 2, 1)
    end_date = datetime(2023, 2, 28)

    # Define the list of account names
    account_names = ["Investment Account 1", "Investment Account 2", "Investment Account 3",
                     "Investment Account 4", "Investment Account 5", "Investment Account 6",
                     "Investment Account 7", "Investment Account 8", "Investment Account 9",
                     "Investment Account 10"]

    # Read in the existing trades from a CSV file
    existing_trades = read_trades_from_file('sample_trades.csv')

    # Generate additional trades for each account
    trades = generate_random_trades(stocks, num_trades, start_date, end_date)
    assign_accounts_to_trades(trades, account_names)

    # Combine the existing and new trades into a single list
    trades += existing_trades

    # Write all the trades to a new CSV file
    write_trades_to_file(trades, 'all_trades.csv')