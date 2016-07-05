---
title: Connecting with psql
---

Depending on the default values used or the environment variables you have set, the following examples show how to access a database via `psql`:

``` bash
$ psql -d gpdatabase -h master_host -p 5432 -U `gpadmin`
```

``` bash
$ psql gpdatabase
```

``` bash
$ psql
```

If a user-defined database has not yet been created, you can access the system by connecting to the `template1` database. For example:

``` bash
$ psql template1
```

After connecting to a database, `psql` provides a prompt with the name of the database to which `psql` is currently connected, followed by the string `=>` \(or `=#` if you are the database superuser\). For example:

``` sql
gpdatabase=>
```

At the prompt, you may type in SQL commands. A SQL command must end with a `;` \(semicolon\) in order to be sent to the server and executed. For example:

``` sql
=> SELECT * FROM mytable;
```
