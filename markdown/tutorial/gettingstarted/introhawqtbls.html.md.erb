---
title: Lesson 5 - HAWQ Tables
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

HAWQ writes data to, and reads data from, HDFS natively. HAWQ tables are similar to tables in any relational database, except that table rows (data) are distributed across the different segments in the cluster.

In this exercise, you will run scripts that use the SQL `CREATE TABLE` command to create HAWQ tables. You will load the Retail demo fact data into the HAWQ tables using the SQL `COPY` command. You will then perform simple and complex queries on the data.


## <a id="tut_introhawqtblprereq"></a>Prerequisites

Ensure that you have:

- [Set Up your HAWQ Runtime Environment](introhawqenv.html#tut_runtime_setup)
- [Created the HAWQ Tutorial Database](basicdbadmin.html#tut_ex_createdb)
- [Downloaded the Retail Data and Script Files](dataandscripts.html#tut_exdownloadfilessteps)
- [Created the Retail Demo HAWQ Schema](dataandscripts.html#tut_dsschema_ex)
- Started your HAWQ cluster.

## <a id="tut_excreatehawqtblsteps"></a>Exercise: Create, Add Data to, and Query HAWQ Retail Demo Tables

Perform the following steps to create and load HAWQ tables from the sample Retail demo data set. 

1. Navigate to the HAWQ script directory:

    ``` shell
    gpadmin@master$ cd $HAWQGSBASE/tutorials/getstart/hawq
    ```

2. Create tables for the Retail demo fact data using the script provided:
    
    ``` shell
    gpadmin@master$ psql -f ./create_hawq_tables.sql 
    psql:./create_hawq_tables.sql:2: NOTICE:  table "order_lineitems_hawq" does not exist, skipping
    DROP TABLE
    CREATE TABLE
    psql:./create_hawq_tables.sql:41: NOTICE:  table "orders_hawq" does not exist, skipping
    DROP TABLE
    CREATE TABLE
    ```
	
    **Note**: The `create_hawq_tables.sql` script deletes each table before attempting to create it. If this is your first time performing this exercise, you can safely ignore the `psql` "table does not exist, skipping" messages.)
    
3. Let's take a look at the `create_hawq_tables.sql` script; for example:

    ``` shell
    gpadmin@master$ vi create_hawq_tables.sql
    ```

    Notice the use of the `retail_demo.` schema name prefix to the `order_lineitems_hawq` table name:
    
    ``` sql
    DROP TABLE IF EXISTS retail_demo.order_lineitems_hawq;
    CREATE  TABLE retail_demo.order_lineitems_hawq
    (
        order_id TEXT,
        order_item_id TEXT,
        product_id TEXT,
        product_name TEXT,
        customer_id TEXT,
        store_id TEXT,
        item_shipment_status_code TEXT,
        order_datetime TEXT,
        ship_datetime TEXT,
        item_return_datetime TEXT,
        item_refund_datetime TEXT,
        product_category_id TEXT,
        product_category_name TEXT,
        payment_method_code TEXT,
        tax_amount TEXT,
        item_quantity TEXT,
        item_price TEXT,
        discount_amount TEXT,
        coupon_code TEXT,
        coupon_amount TEXT,
        ship_address_line1 TEXT,
        ship_address_line2 TEXT,
        ship_address_line3 TEXT,
        ship_address_city TEXT,
        ship_address_state TEXT,
        ship_address_postal_code TEXT,
        ship_address_country TEXT,
        ship_phone_number TEXT,
        ship_customer_name TEXT,
        ship_customer_email_address TEXT,
        ordering_session_id TEXT,
        website_url TEXT
    )
    WITH (appendonly=true, compresstype=zlib) DISTRIBUTED RANDOMLY;
    ```
    
    The `CREATE TABLE` statement above creates a table named `order_lineitems_hawq` in the `retail_demo` schema. `order_lineitems_hawq` has several columns. `order_id` and `customer_id` provide keys into the orders fact and customers dimension tables. The data in `order_lineitems_hawq` is distributed randomly and is compressed using the `zlib` compression algorithm.
    
    The `create_hawq_tables.sql` script also creates the `orders_hawq` fact table.

6. Take a look at the `load_hawq_tables.sh` script:

    ``` shell
    gpadmin@master$ vi load_hawq_tables.sh
    ```

    Again, notice the use of the `retail_demo.` schema name prefix to the table names. 
    
    Examine the `psql -c` `COPY` commands:
    
    ``` shell
    zcat $DATADIR/order_lineitems.tsv.gz | psql -d hawqgsdb -c "COPY retail_demo.order_lineitems_hawq FROM STDIN DELIMITER E'\t' NULL E'';"
    zcat $DATADIR/orders.tsv.gz | psql -d hawqgsdb -c "COPY retail_demo.orders_hawq FROM STDIN DELIMITER E'\t' NULL E'';"
    ```
    The `load_hawq_tables.sh` shell script uses the `zcat` command to uncompress the `.tsv.gz` data files. The SQL `COPY` command copies `STDIN` (i.e. the output of the `zcat` command) to the HAWQ table. The `COPY` command also identifies the `DELIMITER` used in the file (tab) and the `NULL` string ('').
    
6. Use the `load_hawq_tables.sh` script to load the Retail demo fact data into the newly-created tables. This process may take some time to complete.

    ``` shell
    gpadmin@master$ ./load_hawq_tables.sh
    ```

6. Use the provided script to verify that the Retail demo fact tables were loaded successfully:

    ``` shell
    gpadmin@master$ ./verify_load_hawq_tables.sh
    ```

    The output of the `verify_load_hawq_tables.sh` script should match the following:

    ``` shell						    
        Table Name                |    Count 
    ------------------------------+------------------------
     order_lineitems_hawq         |   744196
     orders_hawq                  |   512071
    ------------------------------+------------------------
    ```
    
7. Run a query on the `order_lineitems_hawq` table that returns the `product_id`, `item_quantity`, `item_price`, and `coupon_amount` for all order line items associated with order id `8467975147`:

    ``` shell
    gpadmin@master$ psql
    hawqgsdb=# SELECT product_id, item_quantity, item_price, coupon_amount 
                 FROM retail_demo.order_lineitems_hawq 
                 WHERE order_id='8467975147' ORDER BY item_price;
     product_id | item_quantity | item_price | coupon_amount 
    ------------+---------------+------------+---------------
     1611429    | 1             | 11.38      | 0.00000
     1035114    | 1             | 12.95      | 0.15000
     1382850    | 1             | 17.56      | 0.50000
     1562908    | 1             | 18.50      | 0.00000
     1248913    | 1             | 34.99      | 0.50000
     741706     | 1             | 45.99      | 0.00000
    (6 rows)
    ```
    
    The `ORDER BY` clause identifies the sort column, `item_price`. If you do not specify an `ORDER BY` column(s), the rows are returned in the order in which they were added to the table.

7. Determine the top three postal codes by order revenue by running the following query on the `orders_hawq` table:

    ``` sql
    hawqgsdb=# SELECT billing_address_postal_code,
                 sum(total_paid_amount::float8) AS total,
                 sum(total_tax_amount::float8) AS tax
               FROM retail_demo.orders_hawq
                 GROUP BY billing_address_postal_code
                 ORDER BY total DESC LIMIT 3;
    ```
    
    Notice the use of the `sum()` aggregate function to add the order totals (`total_amount_paid`) and tax totals (`total_tax_paid`) for all orders. These totals are grouped/summed for each `billing_address_postal_code`.
    
    Compare your output to the following:
 
    ``` pre
     billing_address_postal_code |   total   |    tax    
    ----------------------------+-----------+-----------
     48001                       | 111868.32 | 6712.0992
     15329                       | 107958.24 | 6477.4944
     42714                       | 103244.58 | 6194.6748
    (3 rows)
    ```

10. Run the following query on the `orders_hawq` and `order_lineitems_hawq` tables to display the `product_id`, `item_quantity`, and `item_price` for all line items identifying a `product_id` of `1869831`:

    ``` sql
    hawqgsdb=# SELECT retail_demo.order_lineitems_hawq.order_id, product_id, item_quantity, item_price
                 FROM retail_demo.order_lineitems_hawq, retail_demo.orders_hawq
               WHERE retail_demo.order_lineitems_hawq.order_id=retail_demo.orders_hawq.order_id AND retail_demo.order_lineitems_hawq.product_id=1869831
                 ORDER BY retail_demo.order_lineitems_hawq.order_id, product_id;
      order_id  | product_id | item_quantity | item_price 
    ------------+------------+---------------+------------
     4831097728 | 1869831    | 1             | 11.87
     6734073469 | 1869831    | 1             | 11.87
    (2 rows)
    ```
   
11. Exit the `psql` subsystem:

    ``` sql
    hawqgsdb=# \q
    ```

## <a id="tut_introhawqtbl_summary"></a>Summary
In this lesson, you created and loaded Retail order and order line item data into HAWQ fact tables. You also queried these tables, learning how to filter the data to your needs. 

In Lesson 6, you use PXF external tables to similarly access dimension data stored in HDFS.
 
**Lesson 6**: [HAWQ Extension Framework (PXF)](intropxfhdfs.html)
