from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline01.config.ConfigStore import *
from pipeline01.udfs.UDFs import *
from prophecy.utils import *
from pipeline01.graph import *

def pipeline(spark: SparkSession) -> None:
    df_newDS = newDS(spark)
    df_Reformat_1 = Reformat_1(spark, df_newDS)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline01")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline01", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline01")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
