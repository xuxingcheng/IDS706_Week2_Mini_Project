import pandas as pd


def calculate_average_gold_price(df):
    return df["GLD"].mean()


def get_high_gold_days(df):
    average = calculate_average_gold_price(df)
    return df[df["GLD"] > average]


def add_year_column(df):
    result = df.copy()
    result["Year"] = pd.to_datetime(result["Date"]).dt.year
    return result


if __name__ == "__main__":
    data = pd.read_csv("gold_data_2015_25.csv")
    print("Average gold price:", round(calculate_average_gold_price(data), 2))
    print("Days above average:", len(get_high_gold_days(data)))
