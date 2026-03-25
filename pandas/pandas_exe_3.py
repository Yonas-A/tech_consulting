import pandas as pd

DASH_LINES = "\n" + "-" * 80 + "\n"

# #################################################
# ## 1. Remove duplicate transactions            ##
# ## 2. Handle invalid amount                    ##
# ## 3. Filter only Completed transactions       ##
# ## 4. Total revenue by region                  ##
# ## 5. Identify top customer                    ##
# ## 6. Count failed transactions                ##
# #################################################

df = pd.read_csv("./data/transactions.csv")
df.info()
print(DASH_LINES, end="\n\n")

## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 1. ------------------- Remove duplicate transactions -------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
df = df.drop_duplicates(subset=["customer_id", "region", "amount", "status"])
print("No duplicates: \n\n", df, DASH_LINES, end="\n\n")


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 2. ----------------------- Handle invalid amount ------------------------ ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")  # invalid to NaN
df["amount"] = df["amount"].fillna(df["amount"].median())

df.info()
print(DASH_LINES, end="\n\n")

## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 3. ----------------- Filter only Completed transactions ----------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##

# completed = df[df['status'].isin(['Completed'])].reset_index(drop=True)
completed_transaction = df[df["status"] == "Completed"]
completed_transaction = completed_transaction.reset_index(drop=True)

print("completed transaction\n\n", completed_transaction, DASH_LINES, end="\n\n")


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 4. ---------------------- Total revenue by region ----------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##

revenue = df.groupby("region")["amount"].sum().reset_index(name="total_revenue")

print("Total Revenue by region\n\n", revenue, DASH_LINES, end="\n\n")

## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 5. ------------------------ Identify top customer ----------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##

top_customer = (
    df.groupby("customer_id")["amount"]
    .sum()  # Series
    .reset_index(name="total_revenue")  # DataFrame, assign column name
    .sort_values("total_revenue", ascending=False)  # dataframe sorted
    .head(1)
)

# top_customer = (
#     df.groupby("customer_id")["amount"]
#     .sum()  # Series
#     .sort_values(ascending=False)  # Series sorted
#     .reset_index()  # DataFrame
#     .head(1)
# )

print("Top Customer:\n\n", top_customer, DASH_LINES, end="\n\n")

## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 6. --------------------- Count failed transactions ---------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
failed_count = (df["status"] == "Failed").sum()
print(f"failed count: {failed_count} \n")
