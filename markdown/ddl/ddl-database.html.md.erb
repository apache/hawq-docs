---
title: Creating and Managing Databases
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

Your HAWQ deployment may have multiple databases. This is different from some database management systems \(such as Oracle\) where the database instance *is* the database. Although you can create many databases in a HAWQ system, client programs can connect to and access only one database at a time — you cannot cross-query between databases.

## <a id="topic3"></a>About Template Databases 

Each new database you create is based on a *template*. HAWQ provides a default database, `template1`. HAWQ uses `template1` to create databases unless you specify another template. Do not create any objects in `template1` unless you want those objects to be in every database you create.

HAWQ uses two other database templates internally, `template0` and `postgres`. Do not drop or modify `template0` or `postgres`. You can use `template0` to create a completely clean database containing only the standard objects predefined by HAWQ at initialization. This may be necessary if you have modified `template1`.

## <a id="topic4"></a>Creating a Database 

You must have appropriate privileges or be a HAWQ superuser to create a database. If you do not have the correct privileges, you cannot create a database. The HAWQ administrator must either grant you the necessary privileges or create a database for you.

The [CREATE DATABASE](../reference/sql/CREATE-DATABASE.html) command creates a new database. For example:

``` sql
=# CREATE DATABASE <new_dbname>;
```

You can also use the client program `createdb` to create a database. For example, running the following command connects to HAWQ on the host named `hmaster` at port `5432` and creates a database named `mydatabase`:

``` shell
$ createdb -h hmaster -p 5432 mydatabase
```

The host name and port must match the host name and port of the HAWQ master node.

Some objects, such as roles, are shared by all of the databases in a HAWQ deployment. Other objects, such as tables that you create, are known only to the database in which you create them.

### <a id="topic5"></a>Cloning a Database 

By default, a new database is created by cloning the standard system database template, `template1`. You can identify an alternate template to use for database creation. As mentioned in the section above, you can specify `template0` as the template:

``` sql
=# CREATE DATABASE <new_dbname> WITH TEMPLATE template0;
```

## <a id="topic6"></a>Viewing the List of Databases 

You can use the `\l` meta-command of the `psql` client subsystem to display the list of databases and templates in your HAWQ deployment. If you are a database superuser, you can query the list of databases from the `pg_database` system catalog table. For example:

``` sql
=# SELECT datname FROM pg_database;
```

## <a id="topic7"></a>Altering a Database 

Use the [ALTER DATABASE](../reference/sql/ALTER-DATABASE.html) command to update database attributes including owner or name. You can also use ALTER DATABASE to update a database's default configuration. For example, the following command alters the `search_path` server configuration parameter to change the default schema search path for database `mydatabase`:

``` sql
=# ALTER DATABASE mydatabase SET search_path TO myschema, public, pg_catalog;
```

To alter a database, you must be the owner of the database or a superuser.

## <a id="topic8"></a>Dropping a Database 

The [DROP DATABASE](../reference/sql/DROP-DATABASE.html) command drops \(deletes\) a database. It removes the system catalog entries for the database and deletes the data on disk. You must be the database owner or a superuser to drop a database, and you cannot drop a database while you or anyone else is connected to it. Connect to `template1` \(or another database\) before dropping a database. For example:

``` shell
=# \c template1
```
``` sql
=# DROP DATABASE mydatabase;
```

You can also use the client program `dropdb` to drop a database. For example, the following command connects to HAWQ on the host named `hmaster` at port `5432` and drops the database named `mydatabase`:

``` shell
$ dropdb -h hmaster -p 5432 mydatabase
```

**Warning:** Dropping a database cannot be undone.
