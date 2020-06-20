# Ref: https://spark.apache.org/docs/latest/quick-start.html#self-contained-applications
# A self contained application using the Python API (PySpark).
# This program just counts the number of lines containing 'a' and the number containing 'b' in a text file.

import findspark
findspark.init()

from pyspark.sql import SparkSession

logFile = "/usr/local/opt/spark/README.md"

# we use a SparkSession to create Datasets.
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()


# Run using spark-submit: $ spark-submit --master local[4] SimpleApp.py
# Run using Python interpreter: $ python3 SimpleApp.py