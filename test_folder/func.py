import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('unit-test') \
                    .getOrCreate()

def load_data(path):
    df= spark.read.csv(path,header=True, inferSchema=True)
    return df

def count_by_year(df):
    return df.groupBy("Year").count()

def delay_count_by_flightnum(df):
    return df.filter("IsArrDelayed == 'YES'").groupBy("FlightNum").count()

def main():
    path= "dbfs:/databricks-datasets/airlines/part-00000"
    df= load_data(path)
    count_df= count_by_year(df)
    delay_df= delay_count_by_flightnum(df)
    return df, count_df, delay_df

df, count_df, delay_df= main()