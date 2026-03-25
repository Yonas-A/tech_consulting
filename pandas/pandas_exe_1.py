import pandas as pd

DASH_LINES = "\n" + "-" * 80 + "\n"

# #################################################
# ## 1. Convert sales_amount to numeric          ##
# ## 2. Remove invalid rows                      ##
# ## 3. Clean missing values.                    ##
# ## 4. Group by region, product, category       ##
# ## 5. Calculate revenue per region             ##
# ## 6. Multi-level groupby (region + category)  ##
# ## 7. Sort by highest revenue                  ##
# ## 8. Export clean data.                       ##
# ## 9. Export summary.                          ##
# #################################################

df = pd.read_csv("./data/sales.csv")
df.info()
print(DASH_LINES, end="\n\n")

## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 1. ----------------------- Handle invalid amount  ----------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##

df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")
df = df.dropna(subset=["sales_amount"])  # drop NaN sales_amount
print("\nClean Sales:\n", df, DASH_LINES, end="\n\n")

# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 4. ---------------- group by region, product, category ------------------ ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

## ------------------- Aggregate by region -------------------
group_region = df.groupby("region").agg({"sales_amount": "sum"}).reset_index()
print("Grouped by region:\n", group_region, DASH_LINES, "\n\n")


## ------------------- Aggregate by product -------------------
group_product = df.groupby("product").agg({"sales_amount": "sum"}).reset_index()
print("\nGrouped by product:\n", group_product, DASH_LINES, "\n\n")

## ------------------- Aggregate by category -------------------
group_category = df.groupby("category").agg({"sales_amount": "sum"}).reset_index()
print("\nGrouped by category:\n", group_category, DASH_LINES, "\n\n")


# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 6. -------------- Multi-level groupby (region + category) --------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

group_region_category = (
    df.groupby(["region", "category"])["sales_amount"]
    .sum()
    .reset_index(name="total_sales")
)
print("\ngroup by region + category:\n", group_region_category, DASH_LINES, "\n\n")

# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 7. ---------------------- Sort by highest revenue ----------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
group_region_category = group_region_category.sort_values(
    by="total_sales", ascending=False
).reset_index(drop=True)

print("\ngroup by region + category:\n", group_region_category, DASH_LINES, "\n\n")


# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 8. ------------------------- Export clean data -------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

df.to_csv("./output/sales_clean.csv", index=False)

# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 9. ------------------------ Export summary data ------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

group_region_category.to_csv("./output/sales_summary.csv", index=False)
