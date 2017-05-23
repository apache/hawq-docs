---
title: Lesson 3 - Database Administration
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

The HAWQ `gpadmin` user and other users who are granted the necessary privileges can execute SQL commands to create HAWQ databases and tables. These commands may be invoked via scripts, programs, and from the `psql` client utility.

This lesson introduces basic HAWQ database administration commands and tasks using `psql`. You will create a database and a simple table, and add data to and query the table.

## <a id="tut_adminprereq"></a> Prerequisites

Ensure that you have [Set Up your HAWQ Runtime Environment](introhawqenv.html#tut_runtime_setup) and that your HAWQ cluster is up and running.


## <a id="tut_ex_createdb"></a>Exercise: Create the HAWQ Tutorial Database

In this exercise, you use the `psql` command line utility to create a HAWQ database.

1. Start the `psql` subsystem:

    ``` shell
    gpadmin@master$ psql -d postgres
    ```

    You enter the `psql` interpreter, connecting to the `postgres` database. `postgres` is a default template database created during HAWQ installation.
    
    ``` sql
    psql (8.2.15)
    Type "help" for help.

    postgres=# 
    ```
    
    The `psql` prompt is the database name followed by `=#` or `=>`. `=#` identifies the session as that of a database superuser. The default `psql` prompt for a non-superuser is `=>`.

2. Create a database named `hawqgsdb`:

    ``` sql
    postgres=# CREATE DATABASE hawqgsdb;
    CREATE DATABASE
    ```
    
    The `;` at the end of the `CREATE DATABASE` statement instructs `psql` to interpret the command. SQL commands that span multiple lines are not interpreted until the `;` is entered.

3. Connect to the `hawqgsdb` database you just created:

    ``` sql
    postgres=# \c hawqgsdb
    You are now connected to database "hawqgsdb" as user "gpadmin".
    hawqgsdb=#
    ```

4. Use the `psql` `\l` meta-command to list all HAWQ databases:

    ``` sql
    hawqgsdb=# \l
                         List of databases
          Name       |  Owner  | Encoding | Access privileges 
    -----------------+---------+----------+-------------------
     hawqgsdb        | gpadmin | UTF8     | 
     postgres        | gpadmin | UTF8     | 
     template0       | gpadmin | UTF8     | 
     template1       | gpadmin | UTF8     | 
    (4 rows)
    ```
    
    HAWQ creates two additional template databases during installation, `template0` and `template1`, as you see above. Your HAWQ cluster may list additional databases.

5. Exit `psql`:

    ``` sql
    hawqgsdb=# \q
    ```

## <a id="tut_ex_usepsql"></a>Exercise: Use psql for Table Operations

You manage and access HAWQ databases and tables via the `psql` utility, an interactive front-end to the HAWQ database. In this exercise, you use `psql` to create, add data to, and query a simple HAWQ table.

1. Start the `psql` subsystem:

    ``` shell
    gpadmin@master$ psql -d hawqgsdb
    ```

    The `-d hawqgsdb` option instructs `psql` to connect directly to the `hawqgsdb` database.
  

2. Create a table named `first_tbl` that has a single integer column named `i`:

    ``` sql
    hawqgsdb=# CREATE TABLE first_tbl( i int );
    CREATE TABLE 
    ```

3. Display descriptive information about table `first_tbl`:

    ``` sql
    hawqgsdb=# \d first_tbl
    Append-Only Table "public.first_tbl"
     Column |  Type   | Modifiers 
    --------+---------+-----------
     i      | integer | 
    Compression Type: None
    Compression Level: 0
    Block Size: 32768
    Checksum: f
    Distributed randomly
    ```
    
    `first_tbl` is a table in the HAWQ `public` schema. `first_tbl` has a single integer column, was created with no compression, and is distributed randomly.

4. Add some data to `first_tbl`:

    ``` sql
    hawqgsdb=# INSERT INTO first_tbl VALUES(1);
    INSERT 0 1
    hawqgsdb=# INSERT INTO first_tbl VALUES(2);
    INSERT 0 1 
    ```
    
    Each `INSERT` command adds a row to `first_tbl`, the first adding a row with the value `i=1`, and the second, a row with the value `i=2`. Each `INSERT` also displays the number of rows added (1).

4. HAWQ provides several built-in functions for data manipulation. The  `generate_series(<start>, <end>)` function generates a series of numbers beginning with `<start>` and finishing at `<end>`. Use the `generate_series()` HAWQ built-in function to add rows for `i=3`, `i=4`, and `i=5` to `first_tbl`:

    ``` sql
    hawqgsdb=# INSERT INTO first_tbl SELECT generate_series(3, 5);
    INSERT 0 3
    ```
    
    This `INSERT `command uses the `generate_series()` built-in function to add 3 rows to `first_tbl`, starting with `i=3` and writing and incrementing `i` for each new row.
        
5. Perform a query to return all rows in the `first_tbl` table:

    ``` sql
    hawqgsdb=# SELECT * FROM first_tbl;
     i  
    ----
      1
      2
      3
      4
      5
    (5 rows)
    ```
    
    The `SELECT *` command queries `first_tbl`, returning all columns and all rows. `SELECT` also displays the total number of rows returned in the query.

6. Perform a query to return column `i` for all rows in `first_tbl` where `i` is greater than 3:

    ``` sql
    hawqgsdb=# SELECT i FROM first_tbl WHERE i>3;
     i  
    ----
      4
      5
    (2 rows)
    ```
    
    The `SELECT` command returns the 2 rows (`i=4` and `i=5`) in the table where `i` is larger than 3 and displays the value of `i`.

7. Exit the `psql` subsystem:

    ``` sql
    hawqgsdb=# \q
    ```
    
8. `psql` includes an option, `-c`, to run a single SQL command from the shell command line. Perform the same query you ran in Step 7 using the `-c <sql-command>` option:

    ``` shell
    gpadmin@master$ psql -d hawqgsdb -c 'SELECT i FROM first_tbl WHERE i>3'
    ```
    
    Notice that you enclose the SQL command in single quotes.

9. Set the HAWQ `PGDATABASE` environment variable to identify `hawqsgdb`:

    ``` shell
    gpadmin@master$ export PGDATABASE=hawqgsdb
    ```

    `$PGDATABASE` identifies the default database to which to connect when invoking the HAWQ `psql` command.

10. Re-run the query from the command line again, this time omitting the `-d` option:

    ``` shell
    gpadmin@master$ psql -c 'SELECT i FROM first_tbl WHERE i>3'
    ```
    
    When no database is specified on the command line, `psql` attempts to connect to the database identified by `$PGDATABASE`.

11. Add the `PGDATABASE` setting to your `.bash_profile`:

    ``` shell
    export PGDATABASE=hawqgsdb
    ```  

    
## <a id="tut_dbadmin_summary"></a>Summary
You created the database you will use in later lessons. You also created, inserted data into, and queried a simple HAWQ table using`psql`.

For information on SQL command support in HAWQ, refer to the [SQL Command](../../reference/SQLCommandReference.html) reference. 

For detailed information on the `psql` subsystem, refer to the [psql](../../reference/cli/client_utilities/psql.html) reference page. Commonly-used `psql` meta\-commands are identified in the table below.

| Action                                                    | Command                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List databases | `\l` |
| List tables in current database   | `\dt`                                                                                         |
| Describe a specific table   | `\d <table-name>`                                                                                         |
| Execute an SQL script     | `\i <script-name>`                                                                                         |
| Quit/Exit    | `\q`                                                                                         |

Lesson 4 introduces the Retail demo, a more complicated data set used in upcoming lessons. You will download and examine the data set and work files. You will also load some of the data set into HDFS.
 
**Lesson 4**: [Sample Data Set and HAWQ Schemas](dataandscripts.html)
