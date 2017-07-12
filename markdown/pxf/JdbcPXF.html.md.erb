---
title: Accessing External SQL Databases with JDBC (Beta)
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

Some of your data may already reside in an external SQL database. The PXF JDBC plug-in reads data stored in SQL databases including MySQL, ORACLE, PostgreSQL, and Hive.

This section describes how to use PXF with JDBC, including an example of creating and querying an external table that accesses data in a MySQL database table.

## <a id="jdbcplugin_prereq"></a>Prerequisites

Before accessing external SQL databases using HAWQ and PXF, ensure that:

-   The JDBC plug-in is installed on all cluster nodes. See [Installing PXF Plug-ins](InstallPXFPlugins.html) for PXF plug-in installation information.
-   The JDBC driver JAR files for the external SQL database are installed on all cluster nodes.
-   The file locations of external SQL database JDBC JAR files are added to `pxf-public.classpath`. If you manage your HAWQ cluster with Ambari, add the JARS via the Ambari UI. If you managed your cluster from the command line, edit the `/etc/pxf/conf/pxf-public.classpath` file directly.


## <a id="hdfsplugin_queryextdata"></a>Querying External SQL Data
The PXF JDBC plug-in supports the single profile named `Jdbc`.

Use the following syntax to create a HAWQ external table representing external SQL database tables you access via JDBC: 

``` sql
CREATE [READABLE | WRITABLE] EXTERNAL TABLE <table_name>
    ( <column_name> <data_type> [, ...] | LIKE <other_table> )
LOCATION ('pxf://<host>[:<port>]/<jdbc-schema-name>.<jdbc-database-name>.<jdbc-table-name>
    ?PROFILE=Jdbc[&<custom-option>=<value>[...]]')
FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
```

JDBC-plug-in-specific keywords and values used in the [CREATE EXTERNAL TABLE](../reference/sql/CREATE-EXTERNAL-TABLE.html) call are described in the table below.

| Keyword  | Value |
|-------|-------------------------------------|
| \<column-name\>    | The name of the PXF external table column. The PXF \<column-name\> must exactly match the \<column-name\> used in the external SQL table.|
| \<data-type\>    | The data type of the PXF external table column. The PXF \<data-type\> must be equivalent to the data type used for \<column-name\> in the SQL table.|
| \<host\>    | The PXF host. While \<host\> may identify any PXF agent node, use the HDFS NameNode as it is guaranteed to be available in a running HDFS cluster. If HDFS High Availability is enabled, \<host\> must identify the HDFS NameService. |
| \<port\>    | The PXF port. If \<port\> is omitted, PXF assumes \<host\> identifies a High Availability HDFS Nameservice and connects to the port number designated by the `pxf_service_port` server configuration parameter value. Default is 51200. |
| \<jdbc-schema-name\>    | The schema name. The default schema name is `default`. |
| \<jdbc-database-name\>    | The database name. The default database name is determined by the external SQL server. |
| \<jdbc-table-name\>    | The table name. |
| PROFILE    | The `PROFILE` keyword must specify `Jdbc`. |
| \<custom-option\>  | The custom options supported by the `Jdbc` profile are discussed later in this section.|
| FORMAT 'CUSTOM' | The JDBC `CUSTOM` `FORMAT` supports only the built-in `'pxfwritable_import'` `FORMATTER` property. |

**Note**: When creating PXF external tables, you cannot use the `HEADER` option in your `FORMAT` specification.


### <a id="profile_jdbcoptipns"></a>JDBC Custom Options

You include custom options in the `LOCATION` URI. Preface each option with an ampersand `&`.

The JDBC plug-in `Jdbc` profile supports the following \<custom-option\>s. The JDBC connection set up options are required.

| Option Name   | Description
|---------------|--------------------|
| JDBC_DRIVER | The JDBC driver class name. (Required) |
| DB_URL | The URL to the database; includes the hostname, port, and database name. (Required) |
| USER | The database user name. (Required) |
| PASS | The database password for USER. (Required) |
| PARTITION_BY | The partition column, \<column-name\>:\<column-type\>. The JDBC plug-in supports `date`, `int`, and `enum` \<column-type\>s. Use the  `yyyy-MM-dd` format for the `date` \<column-type\>. A null `PARTITION_BY` defaults to a single fragment. |
| RANGE | (Used only when `PARTITION_BY` is specified.) The query range, \<start-value\>[:\<end-value\>]. \<end-value\> may be empty for an `int` \<column-type\>. The `RANGE` is left closed, right open. That is, the range includes the \<start-value\> but does *not* include the \<end-value\>.|
| INTERVAL | (Used only when `PARTITION_BY` is specified.) The interval, \<interval-num\>[:\<interval-unit\>], of one fragment.  `INTERVAL` may be empty for an `enum` \<column-type\>. \<interval-unit\> may be empty for an `int` \<column-type\>. |

Example JDBC \<custom-option\> connection string:

``` pre
&JDBC_DRIVER=com.mysql.jdbc.Driver&DB_URL=jdbc:mysql://<dbhost>:<dbport>/testdb&USER=user1&PASS=changeme
```

When specifying the `PARTITION_BY` option, tune the `INTERVAL` value and unit based upon the optimal number of JDBC connections to the target database and the optimal distribution of fragments across HAWQ segments. The `INTERVAL` low boundary is driven by the number of HAWQ segments (`default_hash_table_bucket_number`), while the high boundary is driven by the acceptable number of JDBC connections to the target database. `INTERVAL` settings influence the number of fragments, and should ideally not be set too high nor too low. Testing with multiple values may help you select the optimal settings. 

Example JDBC \<custom-option\> substrings identifying partitioning parameters:

``` pre
&PARTITION_BY=year:int&RANGE=2011:2013&INTERVAL=1
&PARTITION_BY=createdate:date&RANGE=2013-01-01:2016-01-01&INTERVAL=1:month
&PARTITION_BY=color:enum&RANGE=red:yellow:blue
```

### <a id="jdbc_example_mysql"></a>Example: Using the Jdbc Profile to Access a MySQL Database Table


#### <a id="ex_create_mysqltbl"></a>Create a MySQL Table

Perform the following steps to create a MySQL table named `mysql_table1` in the default schema of a database named `mtestdb`:

1. Connect to the default MySQL database as the root user:

    ``` shell
    $ mysql --user=root -p
    ```

2. Create a database named `mtestdb`:

    ``` sql
    mysql> CREATE DATABASE mtestdb;
    ```

2. Assign privileges to `mtestdb` to a user named `muser1` and then exit:

    ``` sql
    mysql> GRANT ALL on mtestdb.* TO 'muser1'@'localhost' IDENTIFIED BY 'muser1';
    mysql> \q
    ```
 
2. Connect to `mtestdb` as user `muser1`:

    ``` shell
    $ mysql --user=muser1 mtestdb -pmuser1
    ```

2. Create a table named `mysql_table1` and insert some data into this table:

    ``` sql
    mysql> CREATE TABLE mysql_table1(id int);
    mysql> INSERT INTO mysql_table1 VALUES (1);
    mysql> INSERT INTO mysql_table1 VALUES (2);
    mysql> INSERT INTO mysql_table1 VALUES (3);
    ```

3. Determine the MySQL server hostname and port:

    ``` sql
    mysql> SHOW VARIABLES LIKE 'hostname';
    +---------------+-----------------+
    | Variable_name | Value           |
    +---------------+-----------------+
    | hostname      | mydb.server.com |
    +---------------+-----------------+

    mysql> SHOW VARIABLES LIKE 'port';
    +---------------+-------+
    | Variable_name | Value |
    +---------------+-------+
    | port          | 3306  |
    +---------------+-------+
    1 row in set (0.00 sec)
    ```

    Make note of the hostname and port values returned.

4. Construct the JDBC connection string, substituting your MySQL server hostname and port number:

    ``` pre
    &JDBC_DRIVER=com.mysql.jdbc.Driver&DB_URL=jdbc:mysql://mydb.server.com:3306/mtestdb&USER=muser1&PASS=muser1
    ```

    Save this string for use later.

#### <a id="ex_jdbconfig"></a>Configure PXF

If not already present on your system, download and copy the MySQL connector JAR file to your system and update `pxf-public.classpath` with the location of this file.

For example, if you manage your HAWQ cluster with Ambari, and the MySQL connector jar file is located in the `/usr/share/java` directory, add the following line:

``` pre
/usr/share/java/mysql-connector*.jar
```

in the Ambari **PXF** service **Configs > Advanced pxf-public.classpath** pane and then use the **Restart** button to restart PXF.

If you manage your HAWQ cluster from the command line, directly edit the `/etc/pxf/conf/pxf-public.classpath` file, adding the MySQL connector JAR file path. Then restart PXF on *each* HAWQ node with the following command:

``` shell
root@hawq-node$ sudo service pxf-service restart
```

#### <a id="ex_usejdbc"></a>Query Using the Jdbc Profile

Perform the following steps to create and query an external PXF table to access the `mysql_table1` table you created in the previous section:

1. Use the `Jdbc` profile to create an external table to access the MySQL `mysql_table1` table. For example:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE pxf_jdbc_mysql_table1(id int)
                LOCATION ('pxf://<host>:51200/mtestdb.mysql_table1?PROFILE=JDBC&JDBC_DRIVER=com.mysql.jdbc.Driver&DB_URL=jdbc:mysql://<dbserver-host>:<port>/mtestdb&USER=hawquser1&PASS=hawquser1')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
    ```

    Substitute your PXF \<host\>, as well as the `DB_URL` string you constructed in the previous exercise.

2. Display all rows of the `pxf_jdbc_mysql_table1` table:

    ``` sql
    gpadmin=# SELECT * FROM pxf_jdbc_mysql_table1;
     id
    ----
      1
      2
      3
    (3 rows)
    ```

