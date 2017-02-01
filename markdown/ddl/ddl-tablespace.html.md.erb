---
title: Creating and Managing Tablespaces
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

Tablespaces allow database administrators to have multiple file systems per machine and decide how to best use physical storage to store database objects. They are named locations within a filespace in which you can create objects. Tablespaces allow you to assign different storage for frequently and infrequently used database objects or to control the I/O performance on certain database objects. For example, place frequently-used tables on file systems that use high performance solid-state drives \(SSD\), and place other tables on standard hard drives.

A tablespace requires a file system location to store its database files. In HAWQ, the master and each segment require a distinct storage location. The collection of file system locations for all components in a HAWQ system is a *filespace*. Filespaces can be used by one or more tablespaces.

## <a id="topic10"></a>Creating a Filespace 

A filespace sets aside storage for your HAWQ system. A filespace is a symbolic storage identifier that maps onto a set of locations in your HAWQ hosts' file systems. To create a filespace, prepare the logical file systems on all of your HAWQ hosts, then use the `hawq filespace` utility to define the filespace. You must be a database superuser to create a filespace.

**Note:** HAWQ is not directly aware of the file system boundaries on your underlying systems. It stores files in the directories that you tell it to use. You cannot control the location on disk of individual files within a logical file system.

### <a id="im178954"></a>To create a filespace using hawq filespace 

1.  Log in to the HAWQ master as the `gpadmin` user.

    ``` shell
    $ su - gpadmin
    ```

2.  Create a filespace configuration file:

    ``` shell
    $ hawq filespace -o hawqfilespace_config
    ```

3.  At the prompt, enter a name for the filespace, a master file system location, and the primary segment file system locations. For example:

    ``` shell
    $ hawq filespace -o hawqfilespace_config
    ```
    ``` pre
    Enter a name for this filespace
    > testfs
    Enter replica num for filespace. If 0, default replica num is used (default=3)
    > 

    Please specify the DFS location for the filespace (for example: localhost:9000/fs)
    location> localhost:8020/fs        
    20160409:16:53:25:028082 hawqfilespace:gpadmin:gpadmin-[INFO]:-[created]
    20160409:16:53:25:028082 hawqfilespace:gpadmin:gpadmin-[INFO]:-
    To add this filespace to the database please run the command:
       hawqfilespace --config /Users/gpadmin/curwork/git/hawq/hawqfilespace_config
    ```
       
    ``` shell
    $ cat /Users/gpadmin/curwork/git/hawq/hawqfilespace_config
    ```
    ``` pre
    filespace:testfs
    fsreplica:3
    dfs_url::localhost:8020/fs
    ```
    ``` shell
    $ hawq filespace --config /Users/gpadmin/curwork/git/hawq/hawqfilespace_config
    ```
    ``` pre
    Reading Configuration file: '/Users/gpadmin/curwork/git/hawq/hawqfilespace_config'

    CREATE FILESPACE testfs ON hdfs 
    ('localhost:8020/fs/testfs') WITH (NUMREPLICA = 3);
    20160409:16:57:56:028104 hawqfilespace:gpadmin:gpadmin-[INFO]:-Connecting to database
    20160409:16:57:56:028104 hawqfilespace:gpadmin:gpadmin-[INFO]:-Filespace "testfs" successfully created

    ```


4.  `hawq filespace` creates a configuration file. Examine the file to verify that the hawq filespace configuration is correct. The following is a sample configuration file:

    ```
    filespace:fastdisk
    mdw:1:/hawq_master_filespc/gp-1
    sdw1:2:/hawq_pri_filespc/gp0
    sdw2:3:/hawq_pri_filespc/gp1
    ```

5.  Run hawq filespace again to create the filespace based on the configuration file:

    ``` shell
    $ hawq filespace -c hawqfilespace_config
    ```


## <a id="topic13"></a>Creating a Tablespace 

After you create a filespace, use the `CREATE TABLESPACE` command to define a tablespace that uses that filespace. For example:

``` sql
=# CREATE TABLESPACE fastspace FILESPACE fastdisk;
```

Database superusers define tablespaces and grant access to database users with the `GRANT``CREATE`command. For example:

``` sql
=# GRANT CREATE ON TABLESPACE fastspace TO admin;
```

## <a id="topic14"></a>Using a Tablespace to Store Database Objects 

Users with the `CREATE` privilege on a tablespace can create database objects in that tablespace, such as tables, indexes, and databases. The command is:

``` sql
CREATE TABLE tablename(options) TABLESPACE spacename
```

For example, the following command creates a table in the tablespace *space1*:

``` sql
CREATE TABLE foo(i int) TABLESPACE space1;
```

You can also use the `default_tablespace` parameter to specify the default tablespace for `CREATE TABLE` and `CREATE INDEX` commands that do not specify a tablespace:

``` sql
SET default_tablespace = space1;
CREATE TABLE foo(i int);
```

The tablespace associated with a database stores that database's system catalogs, temporary files created by server processes using that database, and is the default tablespace selected for tables and indexes created within the database, if no `TABLESPACE` is specified when the objects are created. If you do not specify a tablespace when you create a database, the database uses the same tablespace used by its template database.

You can use a tablespace from any database if you have appropriate privileges.

## <a id="topic15"></a>Viewing Existing Tablespaces and Filespaces 

Every HAWQ system has the following default tablespaces.

-   `pg_global` for shared system catalogs.
-   `pg_default`, the default tablespace. Used by the *template1* and *template0* databases.

These tablespaces use the system default filespace, `pg_system`, the data directory location created at system initialization.

To see filespace information, look in the *pg\_filespace* and *pg\_filespace\_entry* catalog tables. You can join these tables with *pg\_tablespace* to see the full definition of a tablespace. For example:

``` sql
=# SELECT spcname AS tblspc, fsname AS filespc,
          fsedbid AS seg_dbid, fselocation AS datadir
   FROM   pg_tablespace pgts, pg_filespace pgfs,
          pg_filespace_entry pgfse
   WHERE  pgts.spcfsoid=pgfse.fsefsoid
          AND pgfse.fsefsoid=pgfs.oid
   ORDER BY tblspc, seg_dbid;
```

## <a id="topic16"></a>Dropping Tablespaces and Filespaces 

To drop a tablespace, you must be the tablespace owner or a superuser. You cannot drop a tablespace until all objects in all databases using the tablespace are removed.

Only a superuser can drop a filespace. A filespace cannot be dropped until all tablespaces using that filespace are removed.

The `DROP TABLESPACE` command removes an empty tablespace.

The `DROP FILESPACE` command removes an empty filespace.
