class PySparkJobInterface:
    def __init__(self):
        self.spark = self.init_spark_session()

    def init_spark_session(self):
        raise NotImplementedError

    def stop(self):
        self.spark.stop()