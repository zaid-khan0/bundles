from func import *
import pyspark
from pyspark.sql import SparkSession
from pyspark.testing import assertDataFrameEqual

spark = SparkSession.builder \
                    .appName('unit-test') \
                    .getOrCreate()


def test_count_by_year():
    expected_df = spark.createDataFrame(data = [(1987, 10)], schema="Year INTEGER, count LONG")
    df=spark.read.table('dev.default.test_data')
    actual_df = count_by_year(df)
    assertDataFrameEqual(expected_df, actual_df)

def test_delay_count_by_flightnum():
    expected_df = spark.createDataFrame(data = [(1451,8)], schema="FlightNum INTEGER, count LONG")
    df=spark.read.table('dev.default.test_data')
    actual_df=delay_count_by_flightnum(df)
    assertDataFrameEqual(expected_df, actual_df)