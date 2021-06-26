#!/usr/bin/python3
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, to_date
from datetime import datetime

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

spark = SparkSession.builder \
    .master('local') \
    .config('spark.driver.extraClassPath',
            os.path.join(project_dir, 'libs/mysql-connector-java-8.0.11.jar')) \
    .appName('covid-etl').getOrCreate()

# Extract
case_df = spark.read.csv(os.path.join(project_dir, "data/Indonesia_coronavirus_daily_data.csv"), header=True,
                         inferSchema=True)
case_df.printSchema()
case_df.show()
zone_df = spark.read.csv(os.path.join(project_dir, "data/zone_reference.csv"), header=True, inferSchema=True)
zone_df.printSchema()
zone_df.show()

# Transform
grouped_case_df = case_df.filter(to_date(col('Date'), 'dd/mm/yyyy') >= datetime.strptime('01-01-2021', '%d-%m-%Y')) \
    .groupby('Province').agg(sum('Daily_Case').alias("Total_Case"))

grouped_case_df.show()

# Load
