# PySpark In Jupyter

I jotted down the steps to setup Apache Spark and running [PySpark in Jupyter](https://towardsdatascience.com/how-to-use-pyspark-on-your-computer-9c7180075617) notebook on my local machine (Mac).

#### Setup Spark
1. Download Spark - http://spark.apache.org/downloads.html

1. Unzip - `$ tar -xzf spark-x.y.z-bin-hadoopx.y.tgz`

1. Copy to standard location (On Mac) - `mv spark-x.y.z-bin-hadoopx.y /usr/local/Cellar/spark/x.y.z`

1. Create symbolic link - `$ ln -s /usr/local/Cellar/spark/x.y.z /usr/local/opt/spark`

1. Set `SPARK_HOME` environment variable and add Spark to $PATH
```shell script
$ echo 'export SPARK_HOME=/usr/local/opt/spark' >> ~/.bash_profile
$ echo 'export PATH="$SPARK_HOME/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile
```

#### Install Jypyter
1. `$ pip3 install jupyter`

1. Update the PySpark driver environment variables
```shell script
$ echo 'export PYSPARK_DRIVER_PYTHON=jupyter' >> ~/.bash_profile
$ echo 'export PYSPARK_DRIVER_PYTHON_OPTS=notebook' >> ~/.bash_profile
$ echo 'export PYSPARK_PYTHON=python3' >> ~/.bash_profile 
$ source ~/.bash_profile
```

#### Launch PySpark
```shell script
$ pyspark
```

#### Run Jupyter Notebook
```shell script
$ jupyter notebook
```

You will be redirected to http://localhost:8888/tree

### Note: So far what I've done, can be achieved quickly using the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)

#### Start a container with the Notebook server listening on port 8888
```shell script
$ docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```

### Note: Jupyter might fail to work on a system with Java 1.8+. I had Java 1.13.0 and I was getting error: Exception: Java gateway process exited before sending its port number. Multiple JDKs can be managed the following way..

#### Manage multiple JDKs through [jEnv](https://github.com/jenv/jenv)

1. Install
```shell script
$ brew install jenv
```

2. Add to PATH
```shell script
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(jenv init -)"' >> ~/.bash_profile
$ source ~/.bash_profile
```

3. Add multiple JDKs to jenv
```shell script
$ jenv add /Library/Java/JavaVirtualMachines/openjdk64-1.8.0.241.jdk/Contents/Home
$ jenv add /Library/Java/JavaVirtualMachines/openjdk64-1.8.0.242.jdk/Contents/Home
$ jenv add /Library/Java/JavaVirtualMachines/openjdk64-13.0.2.jdk/Contents/Home
```

4. List all JDKs
```shell script
$ jenv versions
```

5. To configure java version, say 1.8.0.242, for a particular project
```shell script
$ cd /path/to/project/dir/
$ jenv local 1.8.0.242 
```

6. Verify java version for that project
```shell script
$ java --version
```






