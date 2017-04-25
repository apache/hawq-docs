---
title: Identifying HAWQ Table HDFS Files
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

You can determine the HDFS location of the data file(s) associated with a specific HAWQ table using the HAWQ filespace HDFS location, the table identifier, and the identifiers for the tablespace and database in which the table resides. 

The number of HDFS data files associated with a HAWQ table is determined by the distribution mechanism (hash or random) identified when the table was first created or altered.

Only an HDFS or HAWQ superuser may access HAWQ table HDFS files.

## <a id="idhdfsloc"></a> HDFS Location

The format of the HDFS file path for a HAWQ table is:

``` pre
hdfs://<name-node>:<port>/<hawq-filespace-dir>/<tablespace-oid>/<database-oid>/<table-relfilenode>/<file-number>
```

The HDFS file path components are described in the table below.

|   Path Component   | Description  |
|---------------------|----------------------------|
| \<name-node\>  |  The HDFS NameNode host.  |
| \<port\>  |  The HDFS NameNode port. |
| \<hawq-filespace-dir\>  |  The HDFS directory location of the HAWQ filespace. The default HAWQ filespace HDFS directory is `hawq_default`. |
| \<tablespace-oid\>  |  The tablespace object identifier. The default HAWQ tablespace identifier is `16385`. |
| \<database-oid\>  |  The database object identifier. |
| \<table-relfilenode\>  |  The table object identifier. |
| \<file-number\>  |  The file number. |

**Note**: The HAWQ filespace name and its HDFS directory location must be identified when you create a new HAWQ filespace. You must know both to locate the HDFS files for a specific HAWQ table.

The \<name-node\>:\<port\>/\<default-hawq-filespace-dir\> together comprise the `hawq_dfs_url` server configuration parameter. To display the value of the HAWQ default filespace URL:

``` shell
gpadmin@master$ hawq config -s hawq_dfs_url
GUC      : hawq_dfs_url
Value    : <name-node>:8020/hawq_default
```

or view the **HAWQ** service **Configs > Advanced**, **General** pane, in your Ambari console.

You can determine the tablespace, database, and table object identifiers through HAWQ catalog queries. See the [Example](#ex_hdfslochash) below.


## <a id="idnumfiles"></a> Number of Data Files

The number of data files that are created for a HAWQ table differs for hash-distributed and randomly-distributed HAWQ tables.

Hash-distributed HAWQ tables use a fixed number of virtual segments (vsegs). This number is determined by the `default_hash_table_bucket_number` server configuration parameter setting, or the `BUCKETNUM` value you provide in the `CREATE TABLE` call. The number of HDFS files that HAWQ creates for a hash-distributed table also depends on the maximum number of concurrent inserts that have been executed against the table. The number of HDFS files is always the `default_hash_table_bucket_number` or `BUCKETNUM` value multiplied by the maximum number of concurrent inserts.

The number of HDFS files generated for a randomly-distributed HAWQ table varies depending on the total number of virtual segments that have written data to the table.


## <a id="ex_hdfslochash"></a> Example: Locating HDFS Files for a HAWQ Table

Perform the following steps to identify the HDFS location of the data files associated with a hash-distributed HAWQ table. The SQL queries used in this example are applicable to randomly-distributed HAWQ tables as well.

**Note**: Your HAWQ catalog object identifier query results may differ.

1. Start the `psql` subsystem:

    ``` shell
    gpadmin@master$ psql -d testdb
    ```
    
2. Create a hash-distributed table with 4 buckets and insert some data:

    ``` sql
    testdb=# CREATE TABLE hash_tbl (id int) WITH (BUCKETNUM=4) DISTRIBUTED BY (id);
    CREATE TABLE
    testdb=# INSERT INTO hash_tbl SELECT i FROM generate_series(1,100) AS i;
    INSERT 0 100
    ```

4. Determine the tablespace identifier for your filespace. You must know both the filespace and tablespace names. For example:

    ``` sql
    testdb=# SELECT fsname, spcname AS tablespace_name, tablespace_oid 
               FROM  pg_filespace, gp_persistent_tablespace_node, pg_tablespace 
               WHERE pg_tablespace.spcfsoid = gp_persistent_tablespace_node.filespace_oid 
                 AND pg_filespace.oid = pg_tablespace.spcfsoid 
                 AND fsname !~ '^pg_' ORDER BY 1;
       fsname   | tablespace_name | tablespace_oid 
    ------------+-----------------+----------------
     dfs_system | dfs_default     |          16385
     tryfs      | try_tablespace  |          16619
    (2 rows)
    ```
    
    The default HAWQ filespace name is `dfs_system`. The tablespace identifier associated with the default HAWQ tablespace named `dfs_default` is `16385`. Make note of this identifier.
    
    The example above includes a second HAWQ filespace named `tryfs`. The tablespace identifier associated with the tablespace named `try_tablespace` is `16619`.
    
3. Determine the object identifier of the database `testdb`:

    ``` sql
    testdb=# SELECT oid FROM pg_database WHERE datname = 'testdb';
      oid  
    -------
     16508
    (1 row)
    ```
    
    Make note of this identifier.
    
4.  Tables of the same name may reside in different schemas. The catalog query you use to determine the identifier for the `hash_tbl` table also includes the schema name (`public`):

    ``` sql
    testdb=# SELECT relname, relfilenode, nspname, relnamespace  
               FROM pg_class, pg_namespace  
               WHERE relname = 'hash_tbl' AND nspname = 'public' AND relnamespace=pg_namespace.oid;
     relname  | relfilenode |  nspname  | relnamespace 
    ----------+-------------+-----------+--------------
     hash_tbl |       55784 | public    |         2200
    (1 row)
    ```
    
    Make note of the `relfilenode` value for `hash_tbl`.

4. Construct an HDFS file path for `hash_tbl`. For example, using the HDFS directory location of the HAWQ default filespace:

    ``` pre
    hdfs://<name-node>:<port>/<hawq-filespace-name>/<tablespace-oid>/<database-oid>/<table-relfilenode>/<file-number>
    hdfs://<name-node>:8020/hawq_default/16385/16508/55784
    ```
    
    Substitute your HDFS NameNode for \<name-node\>.

4. Locate the HDFS file(s):

    ``` shell
    gpadmin@master$ hdfs dfs -ls hdfs://<name-node>:8020/hawq_default/16385/16508/55784
    Found 6 items
    -rw-------   3 gpadmin gpadmin        176 2017-04-17 15:24 hdfs://name-node:8020/hawq_default/16385/16508/55784/1
    -rw-------   3 gpadmin gpadmin        168 2017-04-17 15:24 hdfs://name-node:8020/hawq_default/16385/16508/55784/2
    -rw-------   3 gpadmin gpadmin        192 2017-04-17 15:24 hdfs://name-node:8020/hawq_default/16385/16508/55784/3
    -rw-------   3 gpadmin gpadmin        168 2017-04-17 15:24 hdfs://name-node:8020/hawq_default/16385/16508/55784/4
    ```
    
    As expected, `hash_tbl` is comprised of 4 HDFS data files, a multiple of the `BUCKETNUM` you specified when creating the table in Step 2.
