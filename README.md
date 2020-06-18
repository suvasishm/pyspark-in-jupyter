# PySpark In Jupyter

I jotted down the steps to setup Apache Spark focusing PySpark on my local machine (Mac). For details, refer to the following:

1. https://towardsdatascience.com/how-to-use-pyspark-on-your-computer-9c7180075617

#### Setup Spark
1. Download Spark - http://spark.apache.org/downloads.html

1. Unzip - `$ tar -xzf spark-x.y.z-bin-hadoopx.y.tgz`

1. (On Mac) `mv spark-x.y.z-bin-hadoopx.y /usr/local/Cellar/spark/x.y.z`

1. Create symbolic link - `$ ln -s /usr/local/Cellar/spark/x.y.z /usr/local/opt/spark`

1. Add Spark to $PATH
```
echo 'export SPARK_HOME=/usr/local/opt/spark' >> ~/.bash_profile
echo 'export PATH="$SPARK_HOME/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

#### Install Jypyter
1. `$ pip3 install jupyter`

1. Update the PySpark driver environment variables
```
echo 'export PYSPARK_DRIVER_PYTHON=jupyter' >> ~/.bash_profile
echo 'export PYSPARK_DRIVER_PYTHON_OPTS="notebook"' >> ~/.bash_profile
source ~/.bash_profile
```

#### Launch PySpark
```
$ pyspark
```

You will be redirected to http://localhost:8888/tree



