from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
import requests
import json

spark = SparkSession.builder.appName("AcademicGraphIngestion").getOrCreate()

url = "https://api.openalex.org/works?filter=concepts.id:C41008148&per-page=10"
response = requests.get(url)
data = response.json()["results"]

json_strings = [json.dumps(item) for item in data]

rdd = spark.sparkContext.parallelize(json_strings)
df_raw = spark.read.json(rdd)

df_authors = df_raw.select(
    col("id").alias("paper_id"),
    col("title"),
    explode(col("authorships")).alias("authorship")
)

df_authors = df_authors.select(
    "paper_id",
    "title",
    col("authorship.author.display_name").alias("author_name"),
    col("authorship.author.id").alias("author_id")
)

df_authors.show(truncate=False)
df_authors.printSchema()

df_authors.write.parquet("authors.parquet", mode="overwrite")