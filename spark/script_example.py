from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType

conf = (
    SparkConf()
    .set("fs.s3a.endpoint", "http://172.19.0.2:9000")
    .set("fs.s3a.path.style.access", "true")
    .set("fs.s3a.connection.ssl.enabled", "false")
    .set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
)

sc = SparkContext(conf=conf).getOrCreate()

if __name__ == "__main__":
    spark = (
        SparkSession
        .builder
        .appName("S3 Read/Write Example")
        .getOrCreate()
        )
    
    spark.sparkContext.setLogLevel("INFO")
    
    schema = StructType([
        StructField("tconst", StringType(), True),       # Title ID
        StructField("averageRating", FloatType(), True),  # Average rating
        StructField("numVotes", IntegerType(), True)      # Number of votes
        ])
    
    s3_input_path = "s3a://default/title.ratings.tsv"
    s3_output_path = "s3a://default/pod/processed/title_ratings"

    df = spark.read.csv(s3_input_path, header=True,sep='\t', schema=schema)
    df.write.format('csv').mode('overwrite').save(s3_output_path)

    spark.stop()
