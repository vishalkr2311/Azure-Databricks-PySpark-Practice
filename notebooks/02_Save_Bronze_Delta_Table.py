# Databricks notebook source
# MAGIC %md
# MAGIC ##  Save Employee Data to Bronze Delta Table
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## Objective
# MAGIC Read employee CSV data and save it as a Delta table in the Bronze layer.

# COMMAND ----------

employee_csv_path = "/Volumes/dbw_dev_practice/default/raw_files/employees.csv"

# COMMAND ----------

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load(employee_csv_path)

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## # Save DataFrame as Bronze Delta Table
# MAGIC

# COMMAND ----------

df.write \
        .format("delta") \
                .mode("overwrite") \
                        .saveAsTable("dbw_dev_practice.bronze.employees")

# COMMAND ----------

display(df)

# COMMAND ----------

bronze_df = spark.table("dbw_dev_practice.bronze.employees")

display(bronze_df)

# COMMAND ----------

bronze_df.printSchema()

# COMMAND ----------

bronze_df.count()

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select*
# MAGIC from dbw_dev_practice.bronze.employees;

# COMMAND ----------

