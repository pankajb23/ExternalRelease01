from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline01.config.ConfigStore import *
from pipeline01.udfs.UDFs import *

def newDS(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", StringType(), True), StructField("customer_id", StringType(), True), StructField("order_status", StringType(), True), StructField("order_category", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/0c20b5e57f5b408ad7113e426cc35916/OrdersDatasetInput.csv")
