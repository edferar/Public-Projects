from pyspark.sql.functions import mean, max, min, count, col
from pyspark.sql import SparkSession


spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)


#lendo dados do enem 2019
enem = (
    spark
    .read
    .format("CSV")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-edneyferreira-edc/raw-data/enem/")
)

#escrevendo em parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-edneyferreira-edc/staging/enem")
)