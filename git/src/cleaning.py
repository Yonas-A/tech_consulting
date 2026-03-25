import pandas as pd
import logging

logging.basicConfig(
    filename="output/cleaning.log",
    filemode="a",  # 'a' for append (default), 'w' for overwrite
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Reading ./output/.sales_data.csv file.")

# df = pd.read_csv("./data/sales_data.csv")
df = pd.read_csv(
    "./data/sales_data.csv", parse_dates=["order_date"], date_format="%Y-%m-%d"
)

logging.info("Handling invalid columns")

# Handle invalid amount
df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")

logging.info("replacing null values with median for sales_amount column")
df["sales_amount"] = df["sales_amount"].fillna(df["sales_amount"].median())
# fill empty values with median

logging.info("creating a tax column")
df["tax"] = df["sales_amount"] * 0.15

logging.info("writing the clean dataframe to output/sales_data.csf file")
df.to_csv("output/sales_data.csv", index=False)
