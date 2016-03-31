---
title: Creating and Managing Tablespaces <a id="topic9"></a>
---

Tablespaces allow database administrators to have multiple file systems per machine and decide how to best use physical storage to store database objects. They are named locations within a filespace in which you can create objects. Tablespaces allow you to assign different storage for frequently and infrequently used database objects or to control the I/O performance on certain database objects. For example, place frequently-used tables on file systems that use high performance solid-state drives \(SSD\), and place other tables on standard hard drives.

A tablespace requires a file system location to store its database files. In HAWQ, the master and each segment require a distinct storage location. The collection of file system locations for all components in a HAWQ system is a *filespace*. Filespaces can be used by one or more tablespaces.

## Creating a Filespace <a id="topic10"></a>

A filespace sets aside storage for your HAWQ system. A filespace is a symbolic storage identifier that maps onto a set of locations in your HAWQ hosts' file systems. To create a filespace, prepare the logical file systems on all of your HAWQ hosts, then use the `hawq filespace` utility to define the filespace. You must be a database superuser to create a filespace.

**Note:** HAWQ is not directly aware of the file system boundaries on your underlying systems. It stores files in the directories that you tell it to use. You cannot control the location on disk of individual files within a logical file system.

### To create a filespace using hawq filespace <a id="im178954"></a>

1.  Log in to the HAWQ master as the `gpadmin` user.

    ```
    $ su - gpadmin
    ```

2.  Create a filespace configuration file:

    ```
    $ hawq filespace -o hawqfilespace_config
    ```

3.  At the prompt, enter a name for the filespace, a master file system location, and the primary segment file system locations. For example:

    ```
    Checking your configuration:

    Your system has 2 hosts with 2 primary segments
    per host.

    Configuring hosts: [sdw1, sdw2]

    Please specify 2 locations for the primary segments, one per line:
    primary location 1>
    primary location 2> /hawq_pri_filespc

    Enter a file system location for the master:
    master location> /hawq_master_filespc
    ```

4.  hawq filespace creates a configuration file. Examine the file to verify that the hawq filespace configuration is correct. The following is a sample configuration file:

    ```
    filespace:fastdisk
    mdw:1:/hawq_master_filespc/gp-1
    sdw1:2:/hawq_pri_filespc/gp0
    sdw2:3:/hawq_pri_filespc/gp1
    ```

5.  Run hawq filespace again to create the filespace based on the configuration file:

    ```
    $ hawq filespace -c hawqfilespace_config
    ```


## Creating a Tablespace <a id="topic13"></a>

After you create a filespace, use the `CREATE TABLESPACE` command to define a tablespace that uses that filespace. For example:

```
=# CREATE TABLESPACE fastspace FILESPACE fastdisk;
```

Database superusers define tablespaces and grant access to database users with the `GRANT``CREATE`command. For example:

```
=# GRANT CREATE ON TABLESPACE fastspace TO admin;
```

## Using a Tablespace to Store Database Objects <a id="topic14"></a>

Users with the `CREATE` privilege on a tablespace can create database objects in that tablespace, such as tables, indexes, and databases. The command is:

```
CREATE TABLE tablename(options) TABLESPACE spacename
```

For example, the following command creates a table in the tablespace *space1*:

```
CREATE TABLE foo(i int) TABLESPACE space1;
```

You can also use the `default_tablespace` parameter to specify the default tablespace for `CREATE TABLE` and `CREATE INDEX` commands that do not specify a tablespace:

```
SET default_tablespace = space1;
CREATE TABLE foo(i int);
```

The tablespace associated with a database stores that database's system catalogs, temporary files created by server processes using that database, and is the default tablespace selected for tables and indexes created within the database, if no `TABLESPACE` is specified when the objects are created. If you do not specify a tablespace when you create a database, the database uses the same tablespace used by its template database.

You can use a tablespace from any database if you have appropriate privileges.

## Viewing Existing Tablespaces and Filespaces <a id="topic15"></a>

Every HAWQ system has the following default tablespaces.

-   `pg_global` for shared system catalogs.
-   `pg_default`, the default tablespace. Used by the *template1* and *template0* databases.

These tablespaces use the system default filespace, `pg_system`, the data directory location created at system initialization.

To see filespace information, look in the *pg\_filespace* and *pg\_filespace\_entry* catalog tables. You can join these tables with *pg\_tablespace* to see the full definition of a tablespace. For example:

```
=# SELECT spcname as tblspc, fsname as filespc,
          fsedbid as seg_dbid, fselocation as datadir
   FROM   pg_tablespace pgts, pg_filespace pgfs,
          pg_filespace_entry pgfse
   WHERE  pgts.spcfsoid=pgfse.fsefsoid
          AND pgfse.fsefsoid=pgfs.oid
   ORDER BY tblspc, seg_dbid;
```

## Dropping Tablespaces and Filespaces <a id="topic16"></a>

To drop a tablespace, you must be the tablespace owner or a superuser. You cannot drop a tablespace until all objects in all databases using the tablespace are removed.

Only a superuser can drop a filespace. A filespace cannot be dropped until all tablespaces using that filespace are removed.

The `DROP TABLESPACE` command removes an empty tablespace.

The `DROP FILESPACE` command removes an empty filespace.
