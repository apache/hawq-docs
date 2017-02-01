---
title: createdb
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

createdb [<connection_options>] [<database_options>] [-e | --echo] [<dbname> ['<description>']]

createdb --help 

createdb --version

```
where:

``` pre
<connection_options> =
	[-h <host> | --host <host>] 
	[-p <port> | -- port <port>] 
	[-U <username> | --username <username>] 
    [-W | --password] 
         
<database_options> =
    [-D <tablespace> | --tablespace <tablespace>]
    [-E <encoding> | --encoding <encoding>]
    [-O <username> | --owner <username>] 
    [-T <template>| --template <template>] 
```

## <a id="topic1__section3"></a>Description

`createdb` creates a new database in a HAWQ system.

Normally, the database user who executes this command becomes the owner of the new database. However a different owner can be specified via the `-O` option, if the executing user has appropriate privileges.

`createdb` is a wrapper around the SQL command `CREATE DATABASE`.

## <a id="topic1__section4"></a>Options

<dt>**\<dbname\>**</dt>
<dd>The name of the database to be created. The name must be unique among all other databases in the HAWQ system. If not specified, reads from the environment variable `PGDATABASE`, then `PGUSER` or defaults to the current system user.</dd>

<dt>\<description\></dt>
<dd>Optional comment to be associated with the newly created database. Descriptions containing white space must be enclosed in quotes.</dd>

<dt>-e, --echo </dt>
<dd>Echo the commands that createdb generates and sends to the server.</dd>

**\<database_options\>**

<dt>-D, -\\\-tablespace \<tablespace\>  </dt>
<dd>The default tablespace for the database.</dd>

<dt>-E, -\\\-encoding \<encoding\> </dt>
<dd>Character set encoding to use in the new database. Specify a string constant (such as `'UTF8'`), an integer encoding number, or `DEFAULT` to use the default encoding.</dd>

<dt>-O, -\\\-owner \<username\>  </dt>
<dd>The name of the database user who will own the new database. Defaults to the user executing this command.</dd>

<dt>-T, -\\\-template \<template\>  </dt>
<dd>The name of the template from which to create the new database. Defaults to `template1`.</dd>

**\<connection_options\>**
 
<dt>-h, -\\\-host \<hostname\>  </dt>
<dd>The host name of the machine on which the HAWQ master database server is running. If not specified, reads from the environment variable `PGHOST` or defaults to localhost.</dd>

<dt>-p, -\\\-port \<port\>  </dt>
<dd>The TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `PGPORT` or defaults to 5432.</dd>

<dt>-U, -\\\-username \<username\>  </dt>
<dd>The database role name to connect as. If not specified, reads from the environment variable `PGUSER` or defaults to the current system role name.</dd>

<dt>-w, -\\\-no-password  </dt>
<dd>Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dd>

<dt>-W, -\\\-password  </dt>
<dd>Force a password prompt.</dd>


**Other Options**

<dt>-\\\-help  </dt>
<dd>Displays the online help.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

## <a id="topic1__section6"></a>Examples

To create the database `testdb` using the default options:

``` shell
$ createdb testdb
```

To create the database `demo` using the HAWQ master on host `gpmaster`, port `54321`, using the `LATIN1` encoding scheme:

``` shell
$ createdb -p 54321 -h gpmaster -E LATIN1 demo
```
