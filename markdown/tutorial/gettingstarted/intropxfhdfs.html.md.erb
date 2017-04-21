---
title: Lesson 6 - HAWQ Extension Framework (PXF)
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

Data in many HAWQ deployments may already reside in external sources. The HAWQ Extension Framework (PXF) provides access to this external data via built-in connectors called plug-ins. PXF plug-ins facilitate mapping a data source to a HAWQ external table definition. PXF is installed with HDFS, Hive, HBase, and JSON plug-ins.

In this exercise, you use the PXF HDFS plug-in to: 

- Create PXF external table definitions
- Perform queries on the data you loaded into HDFS
- Run more complex queries on HAWQ and PXF tables

## <a id="tut_intropxfprereq"></a>Prerequisites

Ensure that you have:

- [Set Up your HAWQ Runtime Environment](introhawqenv.html#tut_runtime_setup)
- [Created the HAWQ Tutorial Database](basicdbadmin.html#tut_ex_createdb)
- [Downloaded the Retail Data and Script Files](dataandscripts.html#tut_exdownloadfilessteps)
- [Created the Retail Demo HAWQ Schema](dataandscripts.html#tut_dsschema_ex)
- [Loaded the Dimension Data to HDFS](dataandscripts.html#tut_loadhdfs_ex)
- [Created the HAWQ Retail Demo Fact Tables](introhawqtbls.html#tut_excreatehawqtblsteps)
- Started your HAWQ cluster. 

You should also retrieve the hostname or IP address of the HDFS NameNode that you noted in [View and Update HAWQ Configuration](basichawqadmin.html#tut_ex_cmdline_cfg).

## <a id="tut_excreatepxftblsteps"></a>Exercise: Create and Query PXF External Tables

Perform the following steps to create HAWQ external table definitions to read the dimension data you previously loaded into HDFS.

1. Log in to the HAWQ master node as the `gpadmin` user:

    ``` shell
    $ ssh gpadmin@<master>
    ```

2. Navigate to the PXF script directory:

    ``` shell
    gpadmin@master$ cd $HAWQGSBASE/tutorials/getstart/pxf
    ```

6. Start the `psql` subsystem:

    ``` shell
    gpadmin@master$ psql
    hawqgsdb=#
    ```

8. Create a HAWQ external table definition to represent the Retail demo `customers_dim` dimension data you loaded into HDFS in Lesson 4; substitute your NameNode hostname or IP address in the \<namenode\> field of the `LOCATION` clause:

	 ``` sql
    hawqgsdb=# CREATE EXTERNAL TABLE retail_demo.customers_dim_pxf
                (customer_id TEXT, first_name TEXT,
                 last_name TEXT, gender TEXT)
               LOCATION ('pxf://<namenode>:51200/retail_demo/customers_dim/customers_dim.tsv.gz?profile=HdfsTextSimple')
               FORMAT 'TEXT' (DELIMITER = E'\t');
    CREATE EXTERNAL TABLE
    ```

    The `LOCATION` clause of a `CREATE EXTERNAL TABLE` statement specifying the `pxf` protocol must include:
    - The hostname or IP address of your HAWQ cluster's HDFS \<namenode\>.
    - The location and/or name of the external data source. You specified the HDFS file path to the `customer_dim` data file above.
    - The PXF `profile` to use to access the external data. The PXF HDFS plug-in supports the `HdfsTextSimple` profile to access delimited text format data.

    The `FORMAT` clause of a `CREATE EXTERNAL TABLE` statement specifying the `pxf` protocol and `HdfsTextSimple` profile must identify `TEXT` format and include the `DELIMITER` character used to access the external data source. You identified a tab delimiter character above.

5. The `create_pxf_tables.sql` SQL script creates HAWQ external table definitions for the remainder of the Retail dimension data. In another terminal window, edit `create_pxf_tables.sql`, replacing each occurrence of NAMENODE with the hostname or IP address you specified in the previous step. For example:

    ``` shell
    gpadmin@master$ cd $HAWQGSBASE/tutorials/getstart/pxf
    gpadmin@master$ vi create_pxf_tables.sql
    ```

6. Run the `create_pxf_tables.sql` SQL script to create the remainder of the HAWQ external table definitions, then exit the `psql` subsystem:

    ``` sql
    hawqgsdb=# \i create_pxf_tables.sql
    hawqgsdb=# \q
    ```
    	
    **Note**: The `create_pxf_tables.sql` script deletes each external table before attempting to create it. If this is your first time performing this exercise, you can safely ignore the `psql` "table does not exist, skipping" messages.
    
6. Run the following script to verify that you successfully created the external table definitions:

    ``` shell
    gpadmin@master$ ./verify_create_pxf_tables.sh 
    ```
   	 
    The output of the script should match the following:

    ``` pre
        Table Name                 |    Count 
    -------------------------------+------------------------
     customers_dim_pxf             |   401430  
     categories_dim_pxf            |   56 
     customer_addresses_dim_pxf    |   1130639
     email_addresses_dim_pxf       |   401430
     payment_methods_pxf           |   5
     products_dim_pxf              |   698911
    -------------------------------+------------------------
    ```

8. Display the allowed payment methods by running the following query on the `payment_methods_pxf` table:

    ``` sql
    gpadmin@master$ psql
    hawqgsdb=# SELECT * FROM retail_demo.payment_methods_pxf;
     payment_method_id | payment_method_code 
    -------------------+---------------------
                     4 | GiftCertificate
                     3 | CreditCard
                     5 | FreeReplacement
                     2 | Credit
                     1 | COD
    (5 rows)
    ```

8. Run the following query on the `customers_dim_pxf` and `customer_addresses_dim_pxf` tables to display the names of all male customers in the 06119 zip code:

    ``` sql
    hawqgsdb=# SELECT last_name, first_name
                 FROM retail_demo.customers_dim_pxf, retail_demo.customer_addresses_dim_pxf
               WHERE retail_demo.customers_dim_pxf.customer_id=retail_demo.customer_addresses_dim_pxf.customer_id AND
                 retail_demo.customer_addresses_dim_pxf.zip_code='06119' AND 
                 retail_demo.customers_dim_pxf.gender='M';
    ```

    Compare your output to the following:
 
    ``` shell
     last_name | first_name 
    -----------+------------
     Gigliotti | Maurice
     Detweiler | Rashaad
     Nusbaum   | Morton
     Mann      | Damian
     ...
    ```

11. Exit the `psql` subsystem:

    ``` sql
    hawqgsdb=# \q
    ```


## <a id="tut_exhawqpxfquerysteps"></a>Exercise: Query HAWQ and PXF Tables

Often, data will reside in both HAWQ tables and external data sources. In these instances, you can use both HAWQ internal and PXF external tables to relate and query the data.

Perform the following steps to identify the names and email addresses of all customers who made gift certificate purchases, providing an overall order total for such purchases. The orders fact data resides in a HAWQ-managed table and the customers data resides in HDFS.

1. Start the `psql` subsystem:

    ``` shell
    gpadmin@master$ psql
    hawqgsdb=#
    ```

2. The orders fact data is accessible via the `orders_hawq` table created in the previous lesson. The customers data is accessible via the `customers_dim_pxf` table created in the previous exercise. Using these internal and external HAWQ  tables, construct a query to identify the names and email addresses of all customers who made gift certificate purchases; also include an overall order total for such purchases:

    ``` sql
    hawqgsdb=# SELECT substring(retail_demo.orders_hawq.customer_email_address for 37) AS email_address, last_name, 
                 sum(retail_demo.orders_hawq.total_paid_amount::float8) AS gift_cert_total
               FROM retail_demo.customers_dim_pxf, retail_demo.orders_hawq
               WHERE retail_demo.orders_hawq.payment_method_code='GiftCertificate' AND 
                     retail_demo.orders_hawq.customer_id=retail_demo.customers_dim_pxf.customer_id
               GROUP BY retail_demo.orders_hawq.customer_email_address, last_name ORDER BY last_name;
    ```
    
    The `SELECT` statement above uses columns from the HAWQ `orders_hawq` and PXF external `customers_dim_pxf` tables to form the query. The `orders_hawq` `customer_id` field is compared with the `customers_dim_pxf` `customer_id` field to produce the orders associated with a specific customer where the `orders_hawq` `payment_method_code` identifies `GiftCertificate`.
    
    Query output:
    
    ``` pre
                 email_address             |   last_name    |   gift_cert_total    
    ---------------------------------------+----------------+-------------------
     Christopher.Aaron@phpmydirectory.com  | Aaron          |             17.16
     Libbie.Aaron@qatarw.com               | Aaron          |            102.33
     Jay.Aaron@aljsad.net                  | Aaron          |             72.36
     Marybelle.Abad@idividi.com.mk         | Abad           |             14.97
     Suellen.Abad@anatranny.com            | Abad           |            125.93
     Luvenia.Abad@mediabiz.de              | Abad           |            107.99
     ...
    ```
    
    Enter `q` at any time to exit the query results.

3. Exit the `psql` subsystem:

    ``` sql
    hawqgsdb=# \q
    ```

## <a id="tut_intropxf_summary"></a>Summary    
In this lesson, you created PXF external tables to access HDFS data and queried these tables. You also performed a query using this external data and the HAWQ internal fact tables created previously, executing business logic on both your managed and unmanaged data.

For additional information about PXF, refer to [Using PXF with Unmanaged Data](../../pxf/HawqExtensionFrameworkPXF.html).

Refer to [Accessing HDFS File Data](../../pxf/HDFSFileDataPXF.html) for detailed information about the PXF HDFS Plug-in.

This lesson wraps up the *Getting Started with HAWQ* tutorial. Now that you are familiar with basic environment set-up, cluster, database, and data management activities, you should feel more confident interacting with your HAWQ cluster.
 
**Next Steps**: View HAWQ documentation related to [Running a HAWQ Cluster](../../admin/RunningHAWQ.html).
