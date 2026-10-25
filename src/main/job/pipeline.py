from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from main.base import PySparkJobInterface

schema = "plantId string, temperature double"

class PySparkJob(PySparkJobInterface):
    def init_spark_session(self) -> SparkSession:
        return (
        SparkSession.builder
        .appName("Faulty Plants Detection")
        .getOrCreate()
        )


    def read_csv(self, input_path: str) -> DataFrame:
        return (
            self.spark.read.format("csv").schema(schema)
            .option("header","false")
            .load(input_path)
        )
    
    def calc_average_temperature(self, observed: DataFrame) -> DataFrame:
        return (
            observed.groupBy("plantId").agg(avg("temperature").alias("avg_temperature"))
        )

    def find_faulty_plants(self, avg_observed: DataFrame, required: DataFrame) -> DataFrame:
        return (
            required.alias("r").join(avg_observed.alias("o"),"plantId","inner").filter(abs(expr("r.temperature - o.avg_temperature")) >= 5).select("r.plantId","o.avg_temperature")
        )

    def save_as(self, data: DataFrame, output_path: str) -> None:
        data.write.format("csv").mode("overwrite").option("header","false").option("path",output_path).save()
