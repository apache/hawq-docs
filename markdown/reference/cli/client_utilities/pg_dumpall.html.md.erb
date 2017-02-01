---
title: pg_dumpall
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

Extracts all databases in a HAWQ system to a single script file or other archive file.

## <a id="topic1__section2"></a>Synopsis

``` pre
pg_dumpall [<options>] ...
```
where:

``` pre
<general options> =
    [-f | --filespaces] 
    [-i | --ignore-version ]
    [--help ]
    [--version]
<options controlling output content> =
    [-a   --dataonly ]
    [-c | --clean ]
    [-d | --inserts] 
    [-D | --column_inserts] 
    [-F | --filespaces ]
    [-g | --globals-only]
    [-o | --oids ]
    [-d | --inserts] 
    [-O | --no-owner] 
    [-r | --resource-queues] 
    [-s | --schema-only]
    [-S <username>  | --superuser=<username> ]
    [-v  | --verbose ]
    [-x | --no-privileges ] 
    [--disable-dollar-quoting] 
    [--disable-triggers] 
    [--use-set-session-authorization]         
    [--gp-syntax]     
    [--no-gp-syntax] 
<connection_options> =
    [-h <host> | --host <host>] 
    [-p <port> | -- port <port>] 
    [-U <username> | --username <username>] 
    [-w | --no-password]
    [-W | --password] 
    
```

## <a id="topic1__section3"></a>Description

`pg_dumpall` is a standard PostgreSQL utility for backing up all databases in a HAWQ (or PostgreSQL) instance, and is also supported in HAWQ. It creates a single (non-parallel) dump file.

`pg_dumpall` creates a single script file that contains SQL commands that can be used as input to [psql](psql.html#topic1) to restore the databases. It does this by calling [pg\_dump](pg_dump.html#topic1) for each database. `pg_dumpall` also dumps global objects that are common to all databases. (`pg_dump` does not save these objects.) This currently includes information about database users and groups, and access permissions that apply to databases as a whole.

Since `pg_dumpall` reads tables from all databases,  connect as a database superuser to assure producing a complete dump, as well as to execute the saved script, add users and groups, and to create databases.

The SQL script will be written to the standard output. Shell operators should be used to redirect it into a file.

`pg_dumpall` needs to connect to the HAWQ master server several times (once per database). If you use password authentication, a password could be requested for each connection, so using a `~/.pgpass` file is recommended. 

## <a id="topic1__section4"></a>Options

**General Options**
<dt>-f | -\\\-filespaces  </dt>
<dd>Dump filespace definitions.</dd>

<dt>-i | -\\\-ignore-version  </dt>
<dd>Ignore version mismatch between [pg\_dump](pg_dump.html#topic1) and the database server. `pg_dump` can dump from servers running previous releases of HAWQ (or PostgreSQL), but some older versions may not be supported. Use this option if you need to override the version check.</dd>

<dt>--help</dt>
<dd>Displays this help, then exits.</dt>

<dt>--version</dt>
<dd>Displays the version information for the output.</dd>

**Output Control Options**

<dt>-a | -\\\-data-only  </dt>
<dd>Dump only the data, not the schema (data definitions). This option is only meaningful for the plain-text format. For the archive formats, you can specify this option when you call [pg\_restore](pg_restore.html#topic1).</dd>

<dt>-c | -\\\-clean  </dt>
<dd>Output commands to clean (DROP) database objects prior to (the commands for) creating them. This option is only meaningful for the plain-text format. For the archive formats, you may specify the option when you call [pg\_restore](pg_restore.html#topic1).</dd>

<dt>-d | -\\\-inserts  </dt>
<dd>Dump data as `INSERT` commands (rather than `COPY`). This will make restoration very slow; it is mainly useful for making dumps that can be loaded into non-PostgreSQL-based databases. Also, since this option generates a separate command for each row, an error in reloading a row causes only that row to be lost rather than the entire table contents. Note that the restore may fail altogether if you have rearranged column order. The `-D` option is safe against column order changes, though even slower.</dd>

<dt>-D | -\\\-column-inserts  </dt>
<dd>Dump data as `INSERT` commands with explicit column names `(INSERT INTO table                                     (column, ...) VALUES ...)`. This will make restoration very slow; it is mainly useful for making dumps that can be loaded into non-PostgreSQL-based databases. Also, since this option generates a separate command for each row, an error in reloading a row causes only that row to be lost rather than the entire table contents.</dd>

<dt>-g | -\\\-globals-only  </dt>
<dd>Dump only global objects (roles and tablespaces), no databases.</dd>

<dt>-o | -\\\-oids  </dt>
<dd>Dump object identifiers (OIDs) as part of the data for every table. Use of this option is not recommended for files to be restored into HAWQ.</dd>

<dt>-O | -\\\-no-owner  </dt>
<dd>Do not output commands to set ownership of objects to match the original database. By default, [pg\_dump](pg_dump.html#topic1) issues `ALTER                                 OWNER` or `SET SESSION AUTHORIZATION` statements to set ownership of created database objects. These statements will fail when the script is run unless it is started by a superuser (or the same user that owns all of the objects in the script). To make a script that can be restored by any user, but will give that user ownership of all the objects, specify `-O`. This option is only meaningful for the plain-text format. For the archive formats, you may specify the option when you call [pg\_restore](pg_restore.html#topic1).</dd>

<dt>-r | -\\\-resource-queues  </dt>
<dd>Dump resource queue definitions.</dd>

<dt>-s | -\\\-schema-only  </dt>
<dd>Dump only the object definitions (schema), not data.</dd>

<dt>-S \<username\> | -\\\-superuser=\<username\>  </dt>
<dd>Specify the superuser user name to use when disabling triggers. This option is only relevant if `--disable-triggers` is used. Starting the resulting script as a superuser is preferred.

**Note:** HAWQ does not support user-defined triggers.</dd>

<dt>-x | -\\\-no-privileges | -\\\-no-acl  </dt>
<dd>Prevent dumping of access privileges (`GRANT/REVOKE` commands).</dd>

<dt>-\\\-disable-dollar-quoting  </dt>
<dd>This option disables the use of dollar quoting for function bodies, and forces them to be quoted using SQL standard string syntax.</dd>

<dt>-\\\-disable-triggers  </dt>
<dd>This option is only relevant when creating a data-only dump. It instructs `pg_dumpall` to include commands to temporarily disable triggers on the target tables while the data is reloaded. Use this if you do not want to invoke triggers on the tables during data reload. You need superuser permissions to perform commands issued for `--disable-triggers`. Either  specify a superuser name with the `-S` option, or start the resulting script as a superuser.

**Note:** HAWQ does not support user-defined triggers.</dd>

<dt>-\\\-use-set-session-authorization  </dt>
<dd>Output SQL-standard `SET SESSION AUTHORIZATION` commands instead of `ALTER OWNER` commands to determine object ownership. This makes the dump more standards compatible, but depending on the history of the objects in the dump, may not restore properly. A dump using `SET SESSION AUTHORIZATION` will require superuser privileges to restore correctly, whereas `ALTER                                 OWNER` requires lesser privileges.</dd>

<dt>-\\\-gp-syntax  </dt>
<dd>Output HAWQ syntax in the `CREATE                                 TABLE` statements. This allows the distribution policy (`DISTRIBUTED BY` or `DISTRIBUTED                                 RANDOMLY` clauses) of a HAWQ table to be dumped, which is useful for restoring into other HAWQ systems.</dd>

<dt>-\\\-no-gp-syntax </dt>
<dd>Do not use HAWQ syntax in the dump. This is the default if using postgresql. 

**Connection Options**

<dt>-h \<host\> | -\\\-host \<host\>  </dt>
<dd>The host name of the machine on which the HAWQ master database server is running. If not specified, reads from the environment variable `PGHOST` or defaults to `localhost`.</dd>

<dt>-l | -\\\-database \<database_name\>  </dt>
<dd>Connect to an alternate database.</dd>

<dt>-p \<port\> | -\\\-port \<port\>  </dt>
<dd>The TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `PGPORT` or defaults to 5432.</dd>

<dt>-U \<username\> | -\\\-username \<username\>  </dt>
<dd>The database role name to connect as. If not specified, reads from the environment variable `PGUSER` or defaults to the current system role name.</dd>

<dt>-w | -\\\-no-password  </dt>
<dd>Do not prompt for a password.</dd>

<dt>-W | -\\\-password  </dt>
<dd>Force a password prompt.</dd>

## <a id="topic1__section7"></a>Notes

Since `pg_dumpall` calls [pg\_dump](pg_dump.html#topic1) internally, some diagnostic messages will refer to `pg_dump`.

Once restored, it is wise to run `ANALYZE` on each database so the query planner has useful statistics. You can also run `vacuumdb -a                     -z` to analyze all databases.

All tablespace (filespace) directories used by `pg_dumpall` must exist before the restore. Otherwise, database creation will fail for databases in non-default locations.

## <a id="topic1__section8"></a>Examples

To dump all databases:

``` shell
$ pg_dumpall > db.out
```

To reload this file:

``` shell
$ psql template1 -f db.out
```

To dump only global objects (including filespaces and resource queues):

``` shell
$ pg_dumpall -g -f -r
```

## <a id="topic1__section9"></a>See Also

[pg\_dump](pg_dump.html#topic1)
