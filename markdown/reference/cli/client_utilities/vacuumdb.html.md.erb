---
title: vacuumdb
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

Garbage-collects and analyzes a database.

`vacuumdb` is typically run on system catalog tables. It has no effect when run on HAWQ user tables.

## <a id="topic1__section2"></a>Synopsis

``` pre
vacuumdb [<connection_options>] [<vacuum_options>] [<database_name>]
    
vacuumdb [-? | --help]

vacuumdb --version
```
where:

```
<connection_options> =
    [-h <host> | --host <host>] 
    [-p <port> | --port <port>] 
    [-U <username> | --username <username>] 
    [-w | --no-password]
    [-W | --password] 
    
<vacuum_options> =
    [(-a | --all) | (-d <dbname> | --dbame <dbname>)]
    [-e | --echo]
    [-f | --full] 
    [-F | --freeze] 
    [-t <tablename> [( column [,...] )] | --table <tablename> [( column [,...] )] ]
    [(-v | --verbose) | (-q | --quiet)]
    [-z | --analyze] 

```

## <a id="topic1__section3"></a>Description

`vacuumdb` is a utility for cleaning a PostgreSQL database. `vacuumdb` will also generate internal statistics used by the PostgreSQL query optimizer.

`vacuumdb` is a wrapper around the SQL command `VACUUM`. There is no effective difference between vacuuming databases via this utility and via other methods for accessing the server.

## <a id="topic1__section4"></a>Options

<dt>**\<database\_name\>**</dt>
<dd>Identifies the name of the database to vacuum. If both this option and the `-d` option are not provided, the environment variable `PGDATABASE` is used. If that is not set, the user name specified for the connection is used.</dd>

**\<vacuum_options\>**

<dt>-a, -\\\-all  </dt>
<dd>Vacuums all databases.</dd>

<dt>\-d, \-\\\-dbname \<dbname\>  </dt>
<dd>The name of the database to vacuum. If this option is not specified, \<database\_name\> is not provided, and `--all` is not used, the database name is read from the environment variable `PGDATABASE`. If that is not set, the user name specified for the connection is used.</dd>

<dt>-e, -\\\-echo  </dt>
<dd>Show the commands being sent to the server.</dd>

<dt>-f, -\\\-full  </dt>
<dd>Selects a full vacuum, which may reclaim more space, but takes much longer and exclusively locks the table.

**Warning:** A `VACUUM FULL` is not recommended in HAWQ.</dd>

<dt>-F, -\\\-freeze  </dt>
<dd>Freeze row transaction information.</dd>

<dt>-q, -\\\-quiet  </dt>
<dd>Do not display a response.</dd>

<dt>-t, -\\\-table \<tablename\>\[(\<column\>)\]  </dt>
<dd>Clean or analyze this table only. Column names may be specified only in conjunction with the `--analyze` option. If you specify columns, you probably have to escape the parentheses from the shell.</dd>

<dt>-v, -\\\-verbose  </dt>
<dd>Print detailed information during processing.</dd>

<dt>-z, -\\\-analyze  </dt>
<dd>Collect statistics for use by the query planner.</dd>

**\<connection_options\>**

<dt>-h, -\\\-host \<host\>  </dt>
<dd>Specifies the host name of the machine on which the HAWQ master database server is running. If not specified, reads from the environment variable `PGHOST` or defaults to localhost.</dd>

<dt>-p, -\\\-port \<port\>  </dt>
<dd>Specifies the TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `PGPORT` or defaults to 5432.</dd>

<dt>-U, -\\\-username \<username\>  </dt>
<dd>The database role name to connect as. If not specified, reads from the environment variable `PGUSER` or defaults to the current system user name.</dd>

<dt>-w, -\\\-no-password  </dt>
<dd>Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.</dd>

<dt>-W, -\\\-password  </dt>
<dd>Force a password prompt.</dd>

## <a id="topic1__section6"></a>Notes

`vacuumdb` might need to connect several times to the master server, asking for a password each time. It is convenient to have a `~/.pgpass` file for such cases.

## <a id="topic1__section7"></a>Examples

To clean the database `test`:

``` shell
$ vacuumdb testdb
```

To clean and analyze a database named `bigdb`:

``` shell
$ vacuumdb --analyze bigdb
```

To clean a single table `foo` in a database named `mydb`, and analyze a single column `bar` of the table:

``` shell
$ vacuumdb --analyze --verbose --table 'foo(bar)' mydb
```

Note the quotes around the table and column names to escape the parentheses from the shell.