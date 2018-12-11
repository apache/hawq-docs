---
title: Introduction to HAWQ Tables
---

## <a id="tut_introhawqtbldisc"></a>Discussion 

DISCUSS HAWQ TABLES HERE

In this exercise, you will create a HAWQ table, add data to the table, and perform simple queries. You will also load the Retail sample data set into HAWQ tables and perform more complicated queries.

## <a id="tut_introhawqtblprereq"></a>Prerequisites

Ensure that you have a running HAWQ installation and have downloaded the tutorial work files, including the Retail example data set and HAWQ scripts.

## <a id="tut_excreatehawqtblsteps"></a>Steps

Perform the following steps to create a HAWQ database and associated tables to represent the Retail data set. 

1. In a terminal window, navigate to the tutorial work files base directory.

    ``` shell
    $ cd $HAWQTUTBASE
    ```

2. Run the `createdb` command at the shell prompt to create a database named `hawqintro_tbl1`: 

	 ``` shell
	 $ createdb hawqintro_tbl1
	 ```

3. Run the PostgreSQL interpreter `psql` and connect to database `hawqintro_tbl1`:

    ``` shell
    $ psql -d hawqintro_tbl1
    ```

	 You will enter the `psql` interpreter:
    
    ``` sql
    hawqintro_tbl1=#
    ```
    
    Notice that the `psql` prompt is the database name followed by `=#`.

4. Create the table `id_tbl1` with a single column named `id` of type `integer`:

	 ``` sql
	 hawqintro_tbl1=# create table id_tbl1 (id int);
	 ```

5. Add some data to `id_tbl1`:

	 ``` sql
	 hawqintro_tbl1=# insert into id_tbl1 select generate_series(1,100);
	 ```
	
	This `insert` command adds 100 rows to `id_tbl1`, incrementing and writing the `id` for each row.

6. Query the table:

    ``` sql
    hawqintro_tbl1=# select * from id_tbl1 where id > 97;
    ```
    ``` shell
    ** id  
    -----
      98
      99
     100
    (3 rows)**
    ```
    
    The query returns all rows in the table where the `id` is greater than 97.  The query also returns the number of rows returned.
    
7.  Quit and restart `psql`.

    ``` sql
    hawqintro_tbl1=#\q
    ```
    
    ``` shell
    $ cd $HAWQTUTBASE/sample_data
    $ psql
    ```

8. Create a schema named `retail_demo` to represent the Retail data set:

	``` sql
	gpadmin=# CREATE SCHEMA retail_demo;
	```
	
	A schema is a namespace for the database. It contains named objects like tables, data types, functions, and operators.  These named objects are accessed by qualifying their name with `schemaname.` (or `retail_demo.` in this exercise) as a prefix. You may also set a search path that includes schema name(s).
    
7. Use the provided scripts to create tables for, load, and verify the Retail demo data set:
    
    ``` sql
    gpadmin=#\i ../hawq/hawq_tables/create_hawq_tables.sql
    gpadmin=#\q
    ```	
    The `create_hawq_tables.sql` script deletes each table before creating.  If this is your first time performing this exercise, ignore the `psql` "table does not exist, skipping" messages.
    
    View the `create_hawq_tables.sql` script. Notice the use of the `retail_demo.` prefix to the table name:
    
    ``` sql
    CREATE TABLE retail_demo.categories_dim_hawq
(   
    category_id integer NOT NULL,
    category_name character varying(400) NOT NULL
)
WITH (appendonly=true, compresstype=zlib) DISTRIBUTED RANDOMLY;
    ```
    
    Load data into the tables and verify the load succeeded.  You will run a script that displays the row count of tables in the `retail_demo` schema:

    ``` shell
    $ ../hawq/hawq_tables/load_hawq_tables.sh
    $ cd ../hawq/hawq_tables
    $ ./verify_load_hawq_tables.sh
    ```

    The output of the script should match the following:

    ``` shell						    
        Table Name               |    Count 
    -----------------------------+------------------------
 customers_dim_hawq           |   401430  
 categories_dim_hawq          |   56 
 customer_addresses_dim_hawq  |   1130639
 email_addresses_dim_hawq     |   401430
 order_lineitems_hawq         |   1024158
 orders_hawq                  |   512071
 payment_methods_hawq         |   5
 products_dim_hawq            |   698911
  -----------------------------+------------------------
    ```

8. Determine the top ten postal codes by order revenue by running the following query on the `retail_demo.orders_hawq` table:

    ``` shell
    $ psql
    ```
    
    ``` sql
    gpadmin=# select billing_address_postal_code,
      sum(total_paid_amount::float8) as total,
      sum(total_tax_amount::float8) as tax
        from retail_demo.orders_hawq
    group by billing_address_postal_code
    order by total desc limit 10;
    ```

    Compare your output to the following:
 
    ``` shell
 billing_address_postal_code |   total   |    tax    
----------------------------+-----------+-----------
 48001                       | 111868.32 | 6712.0992
 15329                       | 107958.24 | 6477.4944
 42714                       | 103244.58 | 6194.6748
 41030                       |  101365.5 |   6081.93
 50223                       | 100511.64 | 6030.6984
 03106                       |  83566.41 |         0
 57104                       |  77383.63 | 3095.3452
 23002                       |  73673.66 |  3683.683
 25703                       |  68282.12 | 4096.9272
 26178                       |   66836.4 |  4010.184
(10 rows)
Time: 2120.214 ms
    ```