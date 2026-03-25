from pyspark.sql import SparkSession
from pyspark.sql.functions import substring, col, lit, count, max, sum, when
from pyspark.sql.types import DoubleType

# #######################################################################
# ##                                                                   ##
# ## 1. groupBy on students name’s first letter (use substring)        ##
# ##        Count students in each group.                              ##
# ##                                                                   ##
# ## 2. Join employees.csv with departments.csv using dept_id = id.    ##
# ##                                                                   ##
# ## 3. aggregate to find the maximum salary in each department.       ##
# ##                                                                   ##
# ## 4. union sales_2024-01-01.csv and sales_2024-01-02.csv into       ##
# ##     single DataFrame, and compute total sales.                    ##
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
## 1. ------------------------- Group By operation ------------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
# students = spark.read.csv("./data/students.csv", header=True, inferSchema=True)

# students.groupBy(
#     substring(col("first_name"), 1, 1).alias("letter_group")
# ).count().show()

# grouped_df = students.groupBy(
#     substring(col("first_name"), 1, 1).alias("letter_group")
# ).agg(count("*").alias("student_per_letter_group"))

# grouped_df.show()


## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
## 2. -------------------------- Join operations  -------------------------- ##
## ------------------------------------------------------------------------- ##
## ------------------------------------------------------------------------- ##
employees = spark.read.csv("./data/employees.csv", header=True, inferSchema=True)
# departments = spark.read.csv("./data/departments.csv", header=True, inferSchema=True)

# joined_df = employees.join(
#     departments, employees["department_id"] == departments["department_id"], "left"
# )

# # Select employee name and department name
# result = joined_df.select(employees["name"], departments["department_name"])

# # Show result
# result.show()

# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## 3. ----------------------- Aggregation operations  ---------------------- ##
# ## ------------------------------------------------------------------------- ##
# ## ------------------------------------------------------------------------- ##

# joined_df.groupBy("department_name").agg(
#     max("salary").alias("max_salary_per_dept")
# ).show()


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

df_clean = employees.withColumn(
    "salary",
    when(
        col("salary").try_cast(DoubleType()).isNotNull(),
        col("salary").try_cast(DoubleType()),
    ).otherwise(0),
)

df_clean.show()


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
