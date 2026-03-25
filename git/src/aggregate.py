import pandas as pd
import logging

logging.basicConfig(
    filename="output/aggregate.log",
    filemode="a",  # 'a' for append (default), 'w' for overwrite
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Reading ./output/.sales_data.csv file.")

df = pd.read_csv(
    "./output/sales_data.csv", parse_dates=["order_date"], date_format="%Y-%m-%d"
)

logging.info("creating a summary for the data frame")
summary_df = (
    df.groupby("region")
    .agg(
        count=("sales_amount", "count"),
        minimum=("sales_amount", "min"),
        maximum=("sales_amount", "max"),
        average=("sales_amount", "mean"),
        total=("sales_amount", "sum"),
    )
    .sort_values(by="total")
    .reset_index()
)

logging.info("Saving the summary to ./output/summary_table.csv file")
summary_df.to_csv("./output/summary_table.csv", index=False)
