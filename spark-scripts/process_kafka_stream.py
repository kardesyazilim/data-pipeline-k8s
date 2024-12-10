from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("KafkaStreamProcessor") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "orders") \
    .load()

validated_df = df.filter(col("value").isNotNull())

validated_df.writeStream \
    .format("console") \
    .start() \
    .awaitTermination()
