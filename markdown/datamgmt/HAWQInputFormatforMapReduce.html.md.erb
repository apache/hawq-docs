---
title: HAWQ InputFormat for MapReduce
---

<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

MapReduce is a programming model developed by Google for processing and generating large data sets on an array of commodity servers. You can use the HAWQ InputFormat class to enable MapReduce jobs to access HAWQ data stored in HDFS.

To use HAWQ InputFormat, you need only to provide the URL of the database to connect to, along with the table name you want to access. HAWQ InputFormat fetches only the metadata of the database and table of interest, which is much less data than the table data itself. After getting the metadata, HAWQ InputFormat determines where and how the table data is stored in HDFS. It reads and parses those HDFS files and processes the parsed table tuples directly inside a Map task.

This chapter describes the document format and schema for defining HAWQ MapReduce jobs.

## <a id="supporteddatatypes"></a>Supported Data Types

HAWQ InputFormat supports the following data types:

| SQL/HAWQ                | JDBC/JAVA                                        | setXXX        | getXXX        |
|-------------------------|--------------------------------------------------|---------------|---------------|
| DECIMAL/NUMERIC         | java.math.BigDecimal                             | setBigDecimal | getBigDecimal |
| FLOAT8/DOUBLE PRECISION | double                                           | setDouble     | getDouble     |
| INT8/BIGINT             | long                                             | setLong       | getLong       |
| INTEGER/INT4/INT        | int                                              | setInt        | getInt        |
| FLOAT4/REAL             | float                                            | setFloat      | getFloat      |
| SMALLINT/INT2           | short                                            | setShort      | getShort      |
| BOOL/BOOLEAN            | boolean                                          | setBoolean    | getBoolean    |
| VARCHAR/CHAR/TEXT       | String                                           | setString     | getString     |
| DATE                    | java.sql.Date                                    | setDate       | getDate       |
| TIME/TIMETZ             | java.sql.Time                                    | setTime       | getTime       |
| TIMESTAMP/TIMSTAMPTZ    | java.sql.Timestamp                               | setTimestamp  | getTimestamp  |
| ARRAY                   | java.sq.Array                                    | setArray      | getArray      |
| BIT/VARBIT              | com.pivotal.hawq.mapreduce.datatype.             | setVarbit     | getVarbit     |
| BYTEA                   | byte\[\]                                         | setByte       | getByte       |
| INTERVAL                | com.pivotal.hawq.mapreduce.datatype.HAWQInterval | setInterval   | getInterval   |
| POINT                   | com.pivotal.hawq.mapreduce.datatype.HAWQPoint    | setPoint      | getPoint      |
| LSEG                    | com.pivotal.hawq.mapreduce.datatype.HAWQLseg     | setLseg       | getLseg       |
| BOX                     | com.pivotal.hawq.mapreduce.datatype.HAWQBox      | setBox        | getBox        |
| CIRCLE                  | com.pivotal.hawq.mapreduce.datatype.HAWQCircle   | setVircle     | getCircle     |
| PATH                    | com.pivotal.hawq.mapreduce.datatype.HAWQPath     | setPath       | getPath       |
| POLYGON                 | com.pivotal.hawq.mapreduce.datatype.HAWQPolygon  | setPolygon    | getPolygon    |
| MACADDR                 | com.pivotal.hawq.mapreduce.datatype.HAWQMacaddr  | setMacaddr    | getMacaddr    |
| INET                    | com.pivotal.hawq.mapreduce.datatype.HAWQInet     | setInet       | getInet       |
| CIDR                    | com.pivotal.hawq.mapreduce.datatype.HAWQCIDR     | setCIDR       | getCIDR       |

## <a id="hawqinputformatexample"></a>HAWQ InputFormat Example

The following example shows how you can use the `HAWQInputFormat` class to access HAWQ table data from MapReduce jobs.

``` java
package com.mycompany.app;
import com.pivotal.hawq.mapreduce.HAWQException;
import com.pivotal.hawq.mapreduce.HAWQInputFormat;
import com.pivotal.hawq.mapreduce.HAWQRecord;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
import org.apache.hadoop.io.IntWritable;

import java.io.IOException;
public class HAWQInputFormatDemoDriver extends Configured
implements Tool {

    // CREATE TABLE employees (
    // id INTEGER NOT NULL, name VARCHAR(32) NOT NULL);
    public static class DemoMapper extends
        Mapper<Void, HAWQRecord, IntWritable, Text> {
       int id = 0;
       String name = null;
       public void map(Void key, HAWQRecord value, Context context)
        throws IOException, InterruptedException {
        try {
        id = value.getInt(1);
        name = value.getString(2);
        } catch (HAWQException hawqE) {
        throw new IOException(hawqE.getMessage());
        }
        context.write(new IntWritable(id), new Text(name));
       }
    }
    private static int printUsage() {
       System.out.println("HAWQInputFormatDemoDriver
       <database_url> <table_name> <output_path> [username]
       [password]");
       ToolRunner.printGenericCommandUsage(System.out);
       return 2;
    }
 
    public int run(String[] args) throws Exception {
       if (args.length < 3) {
        return printUsage();
       }
       Job job = Job.getInstance(getConf());
       job.setJobName("hawq-inputformat-demo");
       job.setJarByClass(HAWQInputFormatDemoDriver.class);
       job.setMapperClass(DemoMapper.class);
       job.setMapOutputValueClass(Text.class);
       job.setOutputValueClass(Text.class);
       String db_url = args[0];
       String table_name = args[1];
       String output_path = args[2];
       String user_name = null;
       if (args.length > 3) {
         user_name = args[3];
       }
       String password = null;
       if (args.length > 4) {
         password = args[4];
       }
       job.setInputFormatClass(HAWQInputFormat.class);
       HAWQInputFormat.setInput(job.getConfiguration(), db_url,
       user_name, password, table_name);
       FileOutputFormat.setOutputPath(job, new
       Path(output_path));
       job.setNumReduceTasks(0);
       int res = job.waitForCompletion(true) ? 0 : 1;
       return res;
    }
    
    public static void main(String[] args) throws Exception {
       int res = ToolRunner.run(new Configuration(),
         new HAWQInputFormatDemoDriver(), args);
       System.exit(res);
    }
}
```

**To compile and run the example:**

1.  Create a work directory:

    ``` shell
    $ mkdir mrwork
    $ cd mrwork
    ```
 
2.  Copy and paste the Java code above into a `.java` file.

    ``` shell
    $ mkdir -p com/mycompany/app
    $ cd com/mycompany/app
    $ vi HAWQInputFormatDemoDriver.java
    ```

3.  Note the following dependencies required for compilation:
    1.  `HAWQInputFormat` jars (located in the `$GPHOME/lib/postgresql/hawq-mr-io` directory):
        -   `hawq-mapreduce-common.jar`
        -   `hawq-mapreduce-ao.jar`
        -   `hawq-mapreduce-parquet.jar`
        -   `hawq-mapreduce-tool.jar`

    2.  Required 3rd party jars (located in the `$GPHOME/lib/postgresql/hawq-mr-io/lib` directory):
        -   `parquet-common-1.1.0.jar`
        -   `parquet-format-1.1.0.jar`
        -   `parquet-hadoop-1.1.0.jar`
        -   `postgresql-n.n-n-jdbc4.jar`
        -   `snakeyaml-n.n.jar`

    3.  Hadoop Mapreduce related jars (located in the install directory of your Hadoop distribution).

4.  Compile the Java program.  You may choose to use a different compilation command:

    ``` shell
    javac -classpath /usr/hdp/2.4.2.0-258/hadoop-mapreduce/*:/usr/local/hawq/lib/postgresql/hawq-mr-io/*:/usr/local/hawq/lib/postgresql/hawq-mr-io/lib/*:/usr/hdp/current/hadoop-client/* HAWQInputFormatDemoDriver.java
    ```
   
5.  Build the JAR file.

    ``` shell
    $ cd ../../..
    $ jar cf my-app.jar com
    $ cp my-app.jar /tmp
    ```
    
6.  Check that you have installed HAWQ and HDFS and your HAWQ cluster is running.

7.  Create sample table:
    1.  Log in to HAWQ:

        ``` shell
         $ psql -d postgres 
        ```

    2.  Create the table:

        ``` sql
        CREATE TABLE employees (
        id INTEGER NOT NULL,
        name TEXT NOT NULL);
        ```

        Or a Parquet table:

        ``` sql
        CREATE TABLE employees ( id INTEGER NOT NULL, name TEXT NOT NULL) WITH (APPENDONLY=true, ORIENTATION=parquet);
        ```

    3.  Insert one tuple:

        ``` sql
        INSERT INTO employees VALUES (1, 'Paul');
        \q
        ```
8.  Ensure the system `pg_hba.conf` configuration file is set up to allow `gpadmin` access to the `postgres` database.

8.  Use the following shell script snippet showing how to run the Mapreduce job:

    ``` shell
    #!/bin/bash
    
    # set up environment variables
    HAWQMRLIB=/usr/local/hawq/lib/postgresql/hawq-mr-io
    export HADOOP_CLASSPATH=$HAWQMRLIB/hawq-mapreduce-ao.jar:$HAWQMRLIB/hawq-mapreduce-common.jar:$HAWQMRLIB/hawq-mapreduce-tool.jar:$HAWQMRLIB/hawq-mapreduce-parquet.jar:$HAWQMRLIB/lib/postgresql-9.2-1003-jdbc4.jar:$HAWQMRLIB/lib/snakeyaml-1.12.jar:$HAWQMRLIB/lib/parquet-hadoop-1.1.0.jar:$HAWQMRLIB/lib/parquet-common-1.1.0.jar:$HAWQMRLIB/lib/parquet-format-1.0.0.jar
    export LIBJARS=$HAWQMRLIB/hawq-mapreduce-ao.jar,$HAWQMRLIB/hawq-mapreduce-common.jar,$HAWQMRLIB/hawq-mapreduce-tool.jar,$HAWQMRLIB/lib/postgresql-9.2-1003-jdbc4.jar,$HAWQMRLIB/lib/snakeyaml-1.12.jar,$HAWQMRLIB/hawq-mapreduce-parquet.jar,$HAWQMRLIB/lib/parquet-hadoop-1.1.0.jar,$HAWQMRLIB/lib/parquet-common-1.1.0.jar,$HAWQMRLIB/lib/parquet-format-1.0.0.jar
    
    # usage:  hadoop jar JARFILE CLASSNAME -libjars JARS <database_url> <table_name> <output_path_on_HDFS>
    #   - writing output to HDFS, so run as hdfs user
    #   - if not using the default postgres port, replace 5432 with port number for your HAWQ cluster
    HADOOP_USER_NAME=hdfs hadoop jar /tmp/my-app.jar com.mycompany.app.HAWQInputFormatDemoDriver -libjars $LIBJARS localhost:5432/postgres employees /tmp/employees
    ```
    
    The MapReduce job output is written to the `/tmp/employees` directory on the HDFS file system.

9.  Use the following command to check the result of the Mapreduce job:

    ``` shell
    $ sudo -u hdfs hdfs dfs -ls /tmp/employees
    $ sudo -u hdfs hdfs dfs -cat /tmp/employees/*
    ```

    The output will appear as follows:

    ``` pre
    1 Paul
    ```
        
10.  If you choose to run the program again, delete the output file and directory:
    
    ``` shell
    $ sudo -u hdfs hdfs dfs -rm /tmp/employees/*
    $ sudo -u hdfs hdfs dfs -rmdir /tmp/employees
    ```

## <a id="accessinghawqdata"></a>Accessing HAWQ Data

You can access HAWQ data using the `HAWQInputFormat.setInput()` interface.  You will use a different API signature depending on whether HAWQ is running or not.

-   When HAWQ is running, use `HAWQInputFormat.setInput(Configuration conf, String db_url, String username, String password, String tableName)`.
-   When HAWQ is not running, first extract the table metadata to a file with the Metadata Export Tool and then use `HAWQInputFormat.setInput(Configuration conf, String pathStr)`.

### <a id="hawqinputformatsetinput"></a>HAWQ is Running

``` java
  /**
    * Initializes the map-part of the job with the appropriate input settings
    * through connecting to Database.
    *
    * @param conf
    * The map-reduce job configuration
    * @param db_url
    * The database URL to connect to
    * @param username
    * The username for setting up a connection to the database
    * @param password
    * The password for setting up a connection to the database
    * @param tableName
    * The name of the table to access to
    * @throws Exception
    */
public static void setInput(Configuration conf, String db_url,
    String username, String password, String tableName)
throws Exception;
```

### <a id="metadataexporttool"></a>HAWQ is not Running

Use the metadata export tool, `hawq extract`, to export the metadata of the target table into a local YAML file:

``` shell
$ hawq extract [-h hostname] [-p port] [-U username] [-d database] [-o output_file] [-W] <tablename>
```

Using the extracted metadata, access HAWQ data through the following interface.  Pass the complete path to the `.yaml` file in the `pathStr` argument.

``` java
 /**
   * Initializes the map-part of the job with the appropriate input settings through reading metadata file stored in local filesystem.
   *
   * To get metadata file, please use hawq extract first
   *
   * @param conf
   * The map-reduce job configuration
   * @param pathStr
   * The metadata file path in local filesystem. e.g.
   * /home/gpadmin/metadata/postgres_test
   * @throws Exception
   */
public static void setInput(Configuration conf, String pathStr)
   throws Exception;
```


