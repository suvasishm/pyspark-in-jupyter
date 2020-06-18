# PySpark In Jupyter

I jotted down the steps to setup Apache Spark and use PySpark in Jupyter notebook on my local machine (Mac).

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


## Note: So far what I've done, can be acieved quickly using the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)

#### Start a container with the Notebook server listening on port 8888
```
$ docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```




