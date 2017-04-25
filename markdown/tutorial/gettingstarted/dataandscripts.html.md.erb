---
title: Lesson 4 - Sample Data Set and HAWQ Schemas
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

The sample Retail demo data set used in the tutorial exercises models an online retail store operation. The store carries different categories of products. Customers order the products. The company delivers the products to the customers.

This and later exercises operate on this example data set. The data set is provided in a set of `gzip`'d `.tsv` (tab-separated values) text files. The exercises also reference scripts and other supporting files that operate on the data set.

In this section, you are introduced to the Retail demo data schema. You will download and examine the data set and work files. You will also load some of the data into HDFS.

## <a id="tut_dataset_prereq"></a>Prerequisites

Ensure that you have [Created the HAWQ Tutorial Database](basicdbadmin.html#tut_ex_createdb) and that your HAWQ cluster is up and running.


## <a id="tut_exdownloadfilessteps"></a>Exercise: Download the Retail Demo Data and Script Files

Perform the following steps to download the sample data set and scripts:

1. Open a terminal window and log in to the HAWQ master node as the `gpadmin` user:

    ``` shell
    $ ssh gpadmin@<master>
    ```

3. Create a working directory for the data files and scripts:

    ``` shell
    gpadmin@master$ mkdir /tmp/hawq_getstart
    gpadmin@master$ cd /tmp/hawq_getstart
    ```
    
    You may choose a different base work directory. If you do, ensure that all path components up to and including the `hawq_getstart` directory have read and execute permissions for all.

4. Download the tutorial work and data files from `github`, checking out the appropriate tag/branch:

    ``` shell
    gpadmin@master$ git clone https://github.com/pivotalsoftware/hawq-samples.git
    Cloning into 'hawq-samples'...
    remote: Counting objects: 42, done.
    remote: Total 42 (delta 0), reused 0 (delta 0), pack-reused 42
    Unpacking objects: 100% (42/42), done.
    Checking out files: 100% (18/18), done.
    gpadmin@master$ cd hawq-samples
    gpadmin@master$ git checkout hawq2x_tutorial
    ```

5. Save the path to the work files base directory:

    ``` shell
    gpadmin@master$ export HAWQGSBASE=/tmp/hawq_getstart/hawq-samples
    ```
    
    (If you chose a different base work directory, modify the command as appropriate.) 
    
6. Add the `$HAWQGSBASE` environment variable setting to your `.bash_profile`.

7. Examine the tutorial files. Exercises in this guide reference data files and SQL and shell scripts residing in the `hawq-samples` repository.  Specifically:
  
    | Directory                                                    | Content                                                                                                                                                                                            |
    |----------------------------------------|----------------------------------------------------------------------------------|
    | datasets/retail/ | Retail demo data set data files (`.tsv.gz` format) |
    | tutorials/getstart/        | *Getting Started with HAWQ* guide work files |
    | tutorials/getstart/hawq/  | SQL and shell scripts used by the HAWQ tables exercises                    |
    | tutorials/getstart/pxf/   | SQL and shell scripts used by the PXF exercises                                                                                                                                                                                 |
    <p>

    (`hawq-samples` repository directories not mentioned in the table above are not used by the *Getting Started with HAWQ* exercises.)


## <a id="tut_dsschema_ex"></a>Exercise: Create the Retail Demo HAWQ Schema

A HAWQ schema is a namespace for a database. It contains named objects like tables, data types, functions, and operators. Access these objects by qualifying their name with the prefix `<schema-name>`.

Perform the following steps to create the Retail demo data schema:

1. Start the `psql` subsystem:

    ``` shell
    gpadmin@master$ psql
    hawqgsdb=#
    ```
    
    You are connected to the `hawqgsdb` database.

2. List the HAWQ schemas:

    ``` sql
    hawqgsdb=# \dn
           List of schemas
            Name        |  Owner  
    --------------------+---------
     hawq_toolkit       | gpadmin
     information_schema | gpadmin
     pg_aoseg           | gpadmin
     pg_bitmapindex     | gpadmin
     pg_catalog         | gpadmin
     pg_toast           | gpadmin
     public             | gpadmin
    (7 rows)
    ```
    
    Every database includes a schema named `public`. Database objects you create without specifying a schema are created in the default schema. The default HAWQ schema is the `public` schema, unless you explicitly set it to another schema. (More about this later.)

3. Display the tables in the `public` schema:

    ``` sql
    hawqgsdb=#\dt public.*
               List of relations
     Schema |    Name   | Type  |  Owner  |   Storage   
    --------+-----------+-------+---------+-------------
     public | first_tbl | table | gpadmin | append only
    (1 row)
    ```
    
    In Lesson 3, you created the `first_tbl` table in the `public` schema.

4. Create a schema named `retail_demo` to represent the Retail demo namespace:

    ``` sql
    hawqgsdb=# CREATE SCHEMA retail_demo;
    CREATE SCHEMA
    ```

5. The `search_path` server configuration parameter identifies the order in which HAWQ should search or apply schemas for objects. Set the schema search path to include the new `retail_demo` schema first:

    ``` sql
    hawqgsdb=# SET search_path TO retail_demo, public;
    SET
    ```
    
    `retail_demo`, the first schema in your `search_path`, becomes your default schema.
    
    **Note**: Setting `search_path` in this manner sets the parameter only for the current `psql` session. You must re-set `search_path` in subsequent `psql` sessions.

4. Create another table named `first_tbl`:

    ``` sql
    hawqgsdb=# CREATE TABLE first_tbl( i int );
    CREATE TABLE
    hawqgsdb=# INSERT INTO first_tbl SELECT generate_series(100,103);
    INSERT 0 4
    hawqgsdb=# SELECT * FROM first_tbl;
      i  
    -----
     100
     101
     102
     103
    (4 rows)
    ```
    
    HAWQ creates this table named `first_tbl` in your default schema since no schema was explicitly identified for the table. Your default schema is  `retail_demo` due to your current `search_path` schema ordering.

5. Verify that this `first_tbl` was created in the `retail_demo` schema by displaying the tables in this schema:

    ``` sql
    hawqgsdb=#\dt retail_demo.*
                         List of relations
       Schema    |         Name         | Type  |  Owner  |   Storage   
    -------------+----------------------+-------+---------+-------------
     retail_demo | first_tbl            | table | gpadmin | append only
    (1 row)
    ```

6. Query the `first_tbl` table that you created in Lesson 3:

    ``` sql
    hawqgsdb=# SELECT * from public.first_tbl;
      i 
    ---
     1
     2
     3
     4
     5
    (5 rows)
    ```

    You must prepend the table name with `public.` to explicitly identify the `first_tbl` table in which you are interested. 

7. Exit `psql`:

    ``` sql
    hawqgsdb=# \q
    ```

## <a id="tut_loadhdfs_ex"></a>Exercise: Load the Dimension Data to HDFS

The Retail demo data set includes the entities described in the table below. A fact table consists of business facts. Orders and order line items are fact tables. Dimension tables provide descriptive information for the measurements in a fact table. The other entities are represented in dimension tables. 

|   Entity   | Description  |
|---------------------|----------------------------|
| customers\_dim  |  Customer data: first/last name, id, gender  |
| customer\_addresses\_dim  |  Address and phone number of each customer |
| email\_addresses\_dim  |  Customer e-mail addresses |
| categories\_dim  |  Product category name, id |
| products\_dim  |  Product details including name, id, category, and price |
| date\_dim  |  Date information including year, quarter, month, week, day of week |
| payment\_methods  |  Payment method code, id |
| orders  |  Details of an order such as the id, payment method, billing address, day/time, and other fields. Each order is associated with a specific customer. |
| order\_lineitems  |  Details of an order line item such as the id, item id, category, store, shipping address, and other fields. Each line item references a specific product from a specific order from a specific customer. |

Perform the following steps to load the Retail demo dimension data into HDFS for later consumption:

1. Navigate to the PXF script directory:

    ``` shell
    gpadmin@master$ cd $HAWQGSBASE/tutorials/getstart/pxf
    ```

2. Using the provided script, load the sample data files representing dimension data into an HDFS directory named `/retail_demo`. The script removes any existing `/retail_demo` directory and contents before loading the data: 

    ``` shell
    gpadmin@master$ ./load_data_to_HDFS.sh
    running: sudo -u hdfs hdfs -rm -r -f -skipTrash /retail_demo
    sudo -u hdfs hdfs dfs -mkdir /retail_demo/categories_dim
    sudo -u hdfs hdfs dfs -put /tmp/hawq_getstart/hawq-samples/datasets/retail/categories_dim.tsv.gz /retail_demo/categories_dim/
    sudo -u hdfs hdfs dfs -mkdir /retail_demo/customer_addresses_dim
    sudo -u hdfs hdfs dfs -put /tmp/hawq_getstart/hawq-samples/datasets/retail/customer_addresses_dim.tsv.gz /retail_demo/customer_addresses_dim/
    ...
    ```
	
	 `load_to_HDFS.sh` loads the dimension data `.tsv.gz` files directly into HDFS. Each file is loaded to its respective `/retail_demo/<basename>/<basename>.tsv.gz` file path.
	 
3. View the contents of the HDFS `/retail_demo` directory hierarchy:

    ``` shell
    gpadmin@master$ sudo -u hdfs hdfs dfs -ls /retail_demo/*
    -rw-r--r--   3 hdfs hdfs        590 2017-04-10 19:59 /retail_demo/categories_dim/categories_dim.tsv.gz
    Found 1 items
    -rw-r--r--   3 hdfs hdfs   53995977 2017-04-10 19:59 /retail_demo/customer_addresses_dim/customer_addresses_dim.tsv.gz
    Found 1 items
    -rw-r--r--   3 hdfs hdfs    4646775 2017-04-10 19:59 /retail_demo/customers_dim/customers_dim.tsv.gz
    Found 1 items
    ...
    
    Because the retail demo data exists only as `.tsv.gz` files in HDFS, you cannot immediately query the data using HAWQ. In the next lesson, you create HAWQ external tables that reference these data files, after which you can query them via PXF.
    ```

## <a id="tut_dataset_summary"></a>Summary

In this lesson, you downloaded the tutorial data set and work files, created the `retail_demo` HAWQ schema, and loaded the Retail demo dimension data into HDFS. 

In Lessons 5 and 6, you will create and query HAWQ internal and external tables in the `retail_demo` schema.

**Lesson 5**: [HAWQ Tables](introhawqtbls.html)
