from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, rank, desc, to_date, col, round, count, sum, when
from pyspark.sql.types import DoubleType
from pyspark.sql.window import Window


# #######################################################################
# ##                                                                   ##
# ## 1. load transactions_large.csv into a DataFrame.                  ##
# ##        partition by transaction_date and save to parquet file     ##
# ##                                                                   ##
# ## 2. Use a Window function to rank employees by salary by           ##
# ##        within each each department                                ##
# ##                                                                   ##
# ## 3. Implement a rolling average of revenue in a DataFrame using    ##
# ##        a Window specification.                                    ##
# ##                                                                   ##
# ## 4. broadcast join between a large sales DataFrame and a small     ##
# ##      departments DataFrame.                                       ##
# ##                                                                   ##
# ## 5. Drop duplicate employee names from employees.csv               ##
# ##                                                                   ##
# ## 6. Replacing missing salary values with 0 in employees.csv.       ##
# ##                                                                   ##
# ## 7. Write employees DataFrame into Parquet with Snappy compression ##
# ##                                                                   ##
# #######################################################################

spark = SparkSession.builder.appName("SparkTutorial").getOrCreate()


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 1. -------------------- partition and save to parquet -------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
# transaction = spark.read.csv("./data/transactions_large.csv", header=True, inferSchema=True)


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 2. ---------------------------- Window Rank  ---------------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
# employees = spark.read.csv("./data/employees.csv", header=True, inferSchema=True)
# emp_clean = employees.withColumn(
#     "salary",
#     when(
#         col("salary").try_cast(DoubleType()).isNotNull(),
#         col("salary").try_cast(DoubleType()),
#     ).otherwise(0),
# )

## emp_clean.show()

# departments = spark.read.csv("./data/departments.csv", header=True, inferSchema=True)

# emp_clean = emp_clean.join(departments, on="department_id", how="left")

# # Define window specification: partition by department_id, order by salary descending
# windowSpec = Window.partitionBy("department_id").orderBy(desc("salary"))

# # Add a rank column
# df_ranked = emp_clean.withColumn("salary_rank", rank().over(windowSpec))

# # df_ranked.select("employee_id", "name", "department_id", "salary", "salary_rank").show()
# df_ranked.select("employee_id", "name", "department_name", "salary", "salary_rank").show()


# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 3. ----------------------- rolling sum operations  ---------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

sales = spark.read.csv("./data/sales.csv", header=True, inferSchema=True)

sales = sales.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))

# 4. Define a Window specification
#    We'll order by order_date and calculate a rolling average over the last 3 rows as an example
windowSpec = Window.orderBy("order_date").rowsBetween(
    -2, 0
)  # rolling over current row + 2 previous

sales = sales.withColumn(
    "sales_amount",
    when(
        col("sales_amount").try_cast(DoubleType()).isNotNull(),
        col("sales_amount").try_cast(DoubleType()),
    ).otherwise(0),
)

# 5. Add a rolling average column
df_with_rolling_avg = sales.withColumn(
    "rolling_avg_sales",
    round(avg(col("sales_amount")).over(windowSpec), 4),
    # avg(col("sales_amount")).over(windowSpec)
)

# 6. Show the result
df_with_rolling_avg.orderBy("order_date").show()

# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 4. ------------------------ Union and aggregation ----------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

# sales1 = spark.read.csv(
#     path="./data/sales_2024-01-01.csv", header=True, inferSchema=True
# )

# sales2 = spark.read.csv(
#     path="./data/sales_2024-01-02.csv", header=True, inferSchema=True
# )

# # Union the DataFrames
# sales_df = sales1.unionByName(sales2)
# sales_df.printSchema()

# sales_df = sales_df.withColumn("sales_amount", col("sales_amount").cast("double"))
# sales_df.printSchema()

# grouped_df = sales_df.groupBy("product").agg(sum("sales_amount").alias("sales"))

# grouped_df.show()


# total_sales = sales_df.agg(sum(col("sales_amount")).alias("total_sales"))
# total_sales.show()

# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 5. ---------------------- Duplicate identification ---------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

# df_unique = employees.dropDuplicates(["name"])

# # employees.show()
# df_unique.show()


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 6. ---------------------- handeling missing values ---------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
# df_clean = employees.withColumn("salary", col("salary").try_cast(DoubleType()))

# df_clean.show()

# df_clean = df_clean.withColumn(
#     "salary",
#     when(
#         col("salary").cast("double").isNotNull(), col("salary").cast("double")
#     ).otherwise(0),
# )

# df_clean = employees.withColumn(
#     "salary",
#     when(
#         col("salary").try_cast(DoubleType()).isNotNull(),
#         col("salary").try_cast(DoubleType()),
#     ).otherwise(0),
# )

# df_clean.show()


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 7. -------------------- Write to Parquet with snappy -------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
# df_clean.write.mode("overwrite").option("compression", "snappy").parquet(
#     "./output/employees_snappy.parquet"
# )

# df_clean.write.parquet(
#     "transactions_partitioned.parquet",
#     mode="overwrite",
#     partitionBy=["ProductCategory", "TransactionDate"]
# )

# df_clean.write.parquet("./output/employees_snappy", compression="snappy")

## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 7. ------------------------- Cache the DataFrame ------------------------ ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##

# df_clean.cache()  # Cache in memory

# Stop Spark session (optional)
spark.stop()
