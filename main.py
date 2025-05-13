import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_FILE = "finance_data.csv" # class variable to create the csv file
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    # This will only have access to the class itself and not an instance of the class

    def initialize_csv(cls):
        # Try to read the CSV File and if its not there, create it
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # create file
            df = pd.DataFrame(columns=cls.COLUMNS)
            # Export the data frame to a csv file
            df.to_csv(cls.CSV_FILE, index=False)


    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline= "") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transaction found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")

            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

    def add():
        CSV.initialize_csv()
        date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date", allow_default=True)
        amount = get_amount()
        category = get_category()
        description = get_description()
        CSV.add_entry(date, amount, category, description)

CSV.add()