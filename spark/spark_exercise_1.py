from pyspark.sql import SparkSession


# #################################################
# ## 1. Create a SparkSession in PySpark and load   ##
# ##        employees.csv into a DataFrame.         ##
# ##                                                ##
# ## 2. Count the total number of employees         ##
# ##                                                ##
# ## 3. Select only the name and department         ##
# ##                                                ##
# ## 4. Filter salary >  80000                      ##
# ##                                                ##
# ## 5. sort by salary descending                   ##
# ##                                                ##
# ## 6. on a temporary view, get avg salary per     ##
# ##      dept                                      ##
# ###################################################


# Create SparkSession
spark = SparkSession.builder.appName("SparkTutorial").getOrCreate()

# Load CSV file into DataFrame
df = spark.read.csv(
    "./data/employees.csv",
    header=True,  # Use first row as column names
    inferSchema=True,  # Automatically detect column data types
)

# Print schema
df.printSchema()

# Show first 5 rows
df.show(5)


# 2.
total_employees = df.count()
print("Total number of employees:", total_employees)


# 3.
name_dept_df = df.select("name", "department")
name_dept_df.show()

# 4.
high_salary_df = df.filter(df.salary > 80000)
high_salary_df.show()

# 5.
sorted_df = df.orderBy(df.salary.desc())
sorted_df.show()

# 6.
df.createOrReplaceTempView("employees")

avg_salary_dept = spark.sql(
    """
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
"""
)

avg_salary_dept.show()

# Stop Spark session (optional)
spark.stop()
