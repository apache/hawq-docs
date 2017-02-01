---
title: CREATE DATABASE
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

Creates a new database.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE DATABASE <database_name> [s[WITH] <database_attribute>=<value> [ ... ]]
```
where \<database\_attribute\> is:
 
``` pre
	[OWNER=<database_owner>]
    [TEMPLATE=<template>]
    [ENCODING=<encoding>]
    [TABLESPACE=<tablespace>]
    [CONNECTION LIMIT=<connection_limit>]
```

## <a id="topic1__section3"></a>Description

`CREATE DATABASE` creates a new database. To create a database, you must be a superuser or have the special `CREATEDB` privilege.

The creator becomes the owner of the new database by default. Superusers can create databases owned by other users by using the `OWNER` clause. They can even create databases owned by users with no special privileges. Non-superusers with `CREATEDB` privilege can only create databases owned by themselves.

By default, the new database is created by cloning the standard system database template named `template1`. You can specify a different template by including the `WITH TEMPLATE=<template>` clause in the `CREATE DATABASE` command. In particular, specifying `WITH TEMPLATE=template0` creates a clean database containing only the standard objects predefined by HAWQ. This is useful if you wish to avoid copying any installation-local objects that may have been added to `template1`.

## <a id="topic1__section4"></a>Parameters

<dt>\<database_name\></dt>
<dd>The name of a database to create.

**Note:** HAWQ reserves the database name `hcatalog` for system use.</dd>

<dt>OWNER=\<database_owner\> </dt>
<dd>The name of the database user who will own the new database, or `DEFAULT` to use the default owner (the user executing the command).</dd>

<dt>TEMPLATE=\<template\> </dt>
<dd>The name of the template from which to create the new database, or `DEFAULT` to use the default template (`template1`).</dd>

<dt>ENCODING=\<encoding\> </dt>
<dd>Character set encoding to use in the new database. Specify a string constant (such as `'SQL_ASCII'`), an integer encoding number, or `DEFAULT` to use the default encoding.</dd>

<dt>TABLESPACE=\<tablespace\> </dt>
<dd>The name of the tablespace that will be associated with the new database, or `DEFAULT` to use the template database's tablespace. This tablespace will be the default tablespace used for objects created in this database.</dd>

<dt>CONNECTION LIMIT=\<connection_limit\></dt>
<dd>The maximum number of concurrent connections possible. The default of -1 means there is no limitation.</dd>

## <a id="topic1__section5"></a>Notes

`CREATE DATABASE` cannot be executed inside a transaction block.

Only template databases may be specified in the `WITH TEMPLATE=<template>` clause. When you specify `template1` or `template0` as the database template, no other sessions can be connected to the template database during the create operation. New connections to the template database are locked out until `CREATE DATABASE` completes.

The `CONNECTION LIMIT` is not enforced against superusers.

## <a id="topic1__section6"></a>Examples

To create a new database using the default template:

``` pre
CREATE DATABASE gpdb;
```

To create a database named `sales` owned by user `salesapp` with a default tablespace of `salesspace`:

``` pre
CREATE DATABASE sales OWNER=salesapp TABLESPACE=salesspace;
```

To create a database named `music` which supports the ISO-8859-1 character set:

``` pre
CREATE DATABASE music ENCODING='LATIN1';
```

## <a id="topic1__section7"></a>Compatibility

There is no `CREATE DATABASE` statement in the SQL standard. Databases are equivalent to catalogs, whose creation is implementation-defined.

## <a id="topic1__section8"></a>See Also

[DROP DATABASE](DROP-DATABASE.html)
