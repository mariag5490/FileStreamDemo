from pyspark.sql import SparkSession

from lib.logger import Log4j

if __name__=='__main__' :
    spark=SparkSession \
        .builder \
        .master('local[3]') \
        .appName('FileStreamDemo') \
        .getOrCreate()

    logger = Log4j(spark)
