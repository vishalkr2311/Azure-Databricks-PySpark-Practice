# Databricks notebook source
# MAGIC %md
# MAGIC # Employee CSV Ingestion using PySpark
# MAGIC ## Bronze Layer - Data Ingestion
# MAGIC

# COMMAND ----------

spark

# COMMAND ----------

spark.version

# COMMAND ----------

employee_csv_path = "/Volumes/dbw_dev_practice/default/raw_files/employees.csv"

# COMMAND ----------

spark.read.csv(employee_csv_path)

# COMMAND ----------

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(employee_csv_path)
)

# COMMAND ----------

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC #Display Only Required Columns

# COMMAND ----------

df.select("EmpId", "Name").display()

# COMMAND ----------

# MAGIC %md
# MAGIC #Filter Employees from IT Department
# MAGIC

# COMMAND ----------

df.filter(df.Department == "IT").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Filter Employees with Salary Greater Than 50,000

# COMMAND ----------

df.filter(df.Salary > 50000).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Rename a Column

# COMMAND ----------

df = df.withColumnRenamed("Salary", "MonthlySalary")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Add a New Column

# COMMAND ----------

from pyspark.sql.functions import lit
df = df.withColumn("country", lit("India"))
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Derived Column
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import col
df = df.withColumn("AnnualSalary", col("MonthlySalary") * 12)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Create a Salary Grade using when() and otherwise()

# COMMAND ----------

from pyspark.sql.functions import when
df = df.withColumn(
    "SalaryGrade",
    when(col("MonthlySalary") >= 60000, "High")
    .when(col("MonthlySalary") >= 50000, "Medium")
    .otherwise("Low")
)
display(df)

# COMMAND ----------

df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Summary
# MAGIC
# MAGIC ## Completed
# MAGIC - Read employee CSV file
# MAGIC - Inferred schema automatically
# MAGIC - Displayed and validated data
# MAGIC - Renamed Salary column
# MAGIC - Added Country column
# MAGIC - Created AnnualSalary column
# MAGIC - Created SalaryGrade using when() and otherwise()
# MAGIC
# MAGIC Notebook Status: Completed

# COMMAND ----------

