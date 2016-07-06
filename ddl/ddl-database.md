---
title: Creating and Managing Databases
---

A HAWQ system is a single instance of HAWQ. There can be several separate HAWQ systems installed, but usually just one is selected by environment variable settings. See your HAWQ administrator for details.

There can be multiple databases in a HAWQ system. This is different from some database management systems \(such as Oracle\) where the database instance *is* the database. Although you can create many databases in a HAWQ system, client programs can connect to and access only one database at a time — you cannot cross-query between databases.

## <a id="topic3"></a>About Template Databases 

Each new database you create is based on a *template*. HAWQ provides a default database, *template1*. Use *template1* to connect to HAWQ for the first time. HAWQ uses *template1* to create databases unless you specify another template. Do not create any objects in *template1* unless you want those objects to be in every database you create.

HAWQ uses two other database templates, *template0* and *postgres*, internally. Do not drop or modify *template0* or *postgres*. You can use *template0* to create a completely clean database containing only the standard objects predefined by HAWQ at initialization, especially if you modified *template1*.

## <a id="topic4"></a>Creating a Database 

The `CREATE DATABASE` command creates a new database. For example:

``` sql
=> CREATE DATABASE new_dbname;
```

To create a database, you must have privileges to create a database or be a HAWQ superuser. If you do not have the correct privileges, you cannot create a database. The HAWQ administrator must either give you the necessary privileges or to create a database for you.

You can also use the client program `createdb` to create a database. For example, running the following command in a command line terminal connects to HAWQ using the provided host name and port and creates a database named *mydatabase*:

``` shell
$ createdb -h masterhost -p 5432 mydatabase
```

The host name and port must match the host name and port of the installed HAWQ system.

Some objects, such as roles, are shared by all the databases in a HAWQ system. Other objects, such as tables that you create, are known only in the database in which you create them.

### <a id="topic5"></a>Cloning a Database 

By default, a new database is created by cloning the standard system database template, *template1*. Any database can be used as a template when creating a new database, thereby providing the capability to 'clone' or copy an existing database and all objects and data within that database. For example:

``` sql
=> CREATE DATABASE new_dbname TEMPLATE old_dbname
```

## <a id="topic6"></a>Viewing the List of Databases 

If you are working in the `psql` client program, you can use the `\l` meta-command to show the list of databases and templates in your HAWQ system. If using another client program and you are a superuser, you can query the list of databases from the `pg_database` system catalog table. For example:

``` sql
=> SELECT datname from pg_database;
```

## <a id="topic7"></a>Altering a Database 

The ALTER DATABASE command changes database attributes such as owner, name, or default configuration attributes. For example, the following command alters a database by setting its default schema search path \(the `search_path` configuration parameter\):

``` sql
=> ALTER DATABASE mydatabase SET search_path TO myschema, public, pg_catalog;
```

To alter a database, you must be the owner of the database or a superuser.

## <a id="topic8"></a>Dropping a Database 

The `DROP DATABASE` command drops \(or deletes\) a database. It removes the system catalog entries for the database and deletes the database directory on disk that contains the data. You must be the database owner or a superuser to drop a database, and you cannot drop a database while you or anyone else is connected to it. Connect to `template1` \(or another database\) before dropping a database. For example:

``` shell
=> \c template1
```
``` sql
=> DROP DATABASE mydatabase;
```

You can also use the client program `dropdb` to drop a database. For example, the following command connects to HAWQ using the provided host name and port and drops the database *mydatabase*:

``` shell
$ dropdb -h masterhost -p 5432 mydatabase
```

**Warning:** Dropping a database cannot be undone.
