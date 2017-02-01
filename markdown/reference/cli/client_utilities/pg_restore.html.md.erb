---
title: pg_restore
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

Restores a database from an archive file created by `pg_dump`.

## <a id="topic1__section2"></a>Synopsis

``` pre
pg_restore [<general_options>] [<restore_options>] [<connection_options>] <filename>
```
where:

``` pre
<general_options>
    [-d | --dbname=dbname ]
    [-f outfilename | --file=outfilename ]
    [-F t|c | --format=tar | custom ] 
    [-i | --ignore-version ]
    [-l | --list ]
    [-v  | --verbose ]
    [--help]
    [--version]
<restore_options> =
    [-a | --dataonly ]
    [-c | --clean ]
    [-C | --create ]
    [-I | --index=index ]
    [-L <list-file> | --use-list=<list-file> ]
    [-n | --schema <schema> ]
    [-O, --no-owner ]
    [-P ’<function-name(<argtype> [, …])’ | --function=’<function-name>(<argtype> [, …])’]
    [-s | --schema-only]
    [-S <username>   | --superuser=<username> ]
    [-t <table>, --table <table> ]
    [-T <trigger> | --trigger=<trigger> ]
    [-x | --no-privileges | --no-acl] 
    [--disable-triggers] 
    [--use-set-session-authoriztion]
    [--no-data-for-failed-tables]
    [-1 | --single-transaction ]  
<connection_options> =
    [-h <host> | --host <host>] 
    [-p <port> | -- port <port>] 
    [-U <username> | --username <username>] 
    [-W | --password] 
    [-e] | --exit-on-error ]  
```

## <a id="topic1__section3"></a>Description

`pg_restore` is a utility for restoring a database from an archive created by [pg\_dump](pg_dump.html#topic1) in one of the non-plain-text formats. It will issue the commands necessary to reconstruct the database to the state it was in at the time it was saved. The archive files also allow `pg_restore` to be selective about what is restored, or even to reorder the items prior to being restored.

`pg_restore` can operate in two modes. If a database name is specified, the archive is restored directly into the database. Otherwise, a script containing the SQL commands necessary to rebuild the database is created and written to a file or standard output. The script output is equivalent to the plain text output format of `pg_dump`. Some of the options controlling the output are therefore analogous to `pg_dump` options.

`pg_restore` cannot restore information that is not present in the archive file. For instance, if the archive was made using the "dump data as `INSERT` commands" option, `pg_restore` will not be able to load the data using `COPY` statements.

## <a id="topic1__section4"></a>Options

<dt> *filename*   </dt>
<dd>Specifies the location of the archive file to be restored. If not specified, the standard input is used.</dd>

**General Options**

<dt>-d *dbname* , -\\\-dbname=*dbname*  </dt>
<dd>Connect to this database and restore directly into this database. The default is to use the `PGDATABASE` environment variable setting, or the same name as the current system user.</dd>

<dt>-f *outfilename* , -\\\-file=*outfilename*  </dt>
<dd>Specify output file for generated script, or for the listing when used with `-l`. Default is the standard output.</dd>

<dt>-F t |c , -\\\-format=tar|custom  </dt>
<dd>The format of the archive produced by [pg\_dump](pg_dump.html#topic1). It is not necessary to specify the format, since `pg_restore` will determine the format automatically. Format can be either `tar` or `custom`.</dd>

<dt>-i , -\\\-ignore-version  </dt>
<dd>Ignore database version checks.</dd>

<dt>-l , -\\\-list  </dt>
<dd>List the contents of the archive. The output of this operation can be used with the `-L` option to restrict and reorder the items that are restored.</dd>

<dt>-v , -\\\-verbose  </dt>
<dd>Specifies verbose mode.</dd>

<dt> -\\\-help  </dt>
<dd>Displays this help and exits.</dd>

<dt>-\\\-version  </dt>
<dd>Displays version number information for the database
, then exits.</dd>

**Restore Options**

<dt>-a , -\\\-data-only  </dt>
<dd>Restore only the data, not the schema (data definitions).</dd>

<dt>-c , -\\\-clean  </dt>
<dd>Clean (drop) database objects before recreating them.</dd>

<dt>-C , -\\\-create  </dt>
<dd>Create the database before restoring into it. (When this option is used, the database named with `-d` is used only to issue the initial `CREATE DATABASE` command. All data is restored into the database name that appears in the archive.)</dd>

<dt>-e , -\\\-exit-on-error  </dt>
<dd>Exit if an error is encountered while sending SQL commands to the database. The default is to continue and to display a count of errors at the end of the restoration.</dd>

<dt>-I *index* , -\\\-index=*index*  </dt>
<dd>Restore definition of named index only.</dd>

<dt>-L *list-file* , -\\\-use-list=*list-file*  </dt>
<dd>Restore elements in the *list-file* only, and in the order they appear in the file. Lines can be moved and may also be commented out by placing a `;` at the start of the line.</dd>

<dt>-n *schema* , -\\\-schema=*schema*  </dt>
<dd>Restore only objects that are in the named schema. This can be combined with the `-t` option to restore just a specific table.</dd>

<dt>-O , -\\\-no-owner  </dt>
<dd>Do not output commands to set ownership of objects to match the original database. By default, `pg_restore` issues `ALTER OWNER` or `SET SESSION AUTHORIZATION` statements to set ownership of created schema elements. These statements will fail unless the initial connection to the database is made by a superuser (or the same user that owns all of the objects in the script). With `-O`, any user name can be used for the initial connection, and this user will own all the created objects.</dd>

<dt>-P '*function-name*(*argtype* \[, ...\])' , -\\\-function='*function-name*(*argtype* \[, ...\])'  </dt>
<dd>Restore the named function only. The function name must be enclosed in quotes. Be careful to spell the function name and arguments exactly as they appear in the dump file's table of contents (as shown by the `--list` option).</dd>

<dt>-s , -\\\-schema-only  </dt>
<dd>Restore only the schema (data definitions), not the data (table contents). Sequence current values will not be restored, either. (Do not confuse this with the `--schema` option, which uses the word schema in a different meaning.)</dd>

<dt>-S *username* , -\\\-superuser=*username*  </dt>
<dd>Specify the superuser user name to use when disabling triggers. This is only relevant if `--disable-triggers` is used.

**Note:** HAWQ does not support user-defined triggers.</dd>

<dt>-t *table* , -\\\-table=*table*  </dt>
<dd>Restore definition and/or data of named table only.</dd>

<dt>-T *trigger* , -\\\-trigger=*trigger*  </dt>
<dd>Restore named trigger only.

**Note:** HAWQ does not support user-defined triggers.</dd>

<dt>-x , -\\\-no-privileges , -\\\-no-acl  </dt>
<dd>Prevent restoration of access privileges (`GRANT/REVOKE` commands).</dd>

<dt>-\\\-disable-triggers  </dt>
<dd>This option is only relevant when performing a data-only restore. It instructs `pg_restore` to execute commands to temporarily disable triggers on the target tables while the data is reloaded. Use this if you have triggers on the tables that you do not want to invoke during data reload. The commands emitted for `--disable-triggers` must be done as superuser. So, you should also specify a superuser name with `-S`, or preferably run `pg_restore` as a superuser.

**Note:** HAWQ does not support user-defined triggers.</dd>

<dt>-\\\-no-data-for-failed-tables  </dt>
<dd>By default, table data is restored even if the creation command for the table failed (e.g., because it already exists). With this option, data for such a table is skipped. This behavior is useful when the target database may already contain the desired table contents. Specifying this option prevents duplicate or obsolete data from being loaded. This option is effective only when restoring directly into a database, not when producing SQL script output.</dd>

<dt>-1 , -\\\-single-transaction  </dt>
<dd>Execute the restore as a single transaction. This ensures that either all the commands complete successfully, or no changes are applied.</dd>

**Connection Options**

<dt>-h *host* , -\\\-host *host*  </dt>
<dd>The host name of the machine on which the HAWQ master database server is running. If not specified, reads from the environment variable `PGHOST` or defaults to localhost.</dd>

<dt>-p *port* , -\\\-port *port*  </dt>
<dd>The TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `PGPORT` or defaults to 5432.</dd>

<dt>-U *username* , -\\\-username *username*  </dt>
<dd>The database role name to connect as. If not specified, reads from the environment variable `PGUSER` or defaults to the current system role name.</dd>

<dt>-W , -\\\-password  </dt>
<dd>Force a password prompt.</dd>

<dt>-e , -\\\-exit-on-error  </dt>
<dd>Exit if an error is encountered while sending SQL commands to the database. The default is to continue and to display a count of errors at the end of the restoration.</dd>

## <a id="topic1__section6"></a>Notes

If your installation has any local additions to the `template1` database, be careful to load the output of `pg_restore` into a truly empty database; otherwise you are likely to get errors due to duplicate definitions of the added objects. To make an empty database without any local additions, copy from `template0` not `template1`, for example:

``` sql
CREATE DATABASE foo WITH TEMPLATE template0;
```

When restoring data to a pre-existing table and the option `--disable-triggers` is used, `pg_restore` emits commands to disable triggers on user tables before inserting the data then emits commands to re-enable them after the data has been inserted. If the restore is stopped in the middle, the system catalogs may be left in the wrong state.

`pg_restore` will not restore large objects for a single table. If an archive contains large objects, then all large objects will be restored.

See also the `pg_dump` documentation for details on limitations of `pg_dump`.

Once restored, it is wise to run `ANALYZE` on each restored table so the query planner has useful statistics.

When running `pg_restore`, a warning related to the `gp_enable_column_oriented_table` parameter might appear. If it does, disregard it.

## <a id="topic1__section7"></a>Examples

Assume we have dumped a database called `mydb` into a custom-format dump file:

``` shell
$ pg_dump -Fc mydb > db.dump
```

To drop the database and recreate it from the dump:

``` shell
$ dropdb mydb
$ pg_restore -C -d template1 db.dump
```

To reload the dump into a new database called `newdb`. Notice there is no `-C`, we instead connect directly to the database to be restored into. Also note that we clone the new database from `template0` not `template1`, to ensure it is initially empty:

``` shell
$ createdb -T template0 newdb
$ pg_restore -d newdb db.dump
```

To reorder database items, it is first necessary to dump the table of contents of the archive:

``` shell
$ pg_restore -l db.dump > db.list
```

The listing file consists of a header and one line for each item, for example,

``` pre
; Archive created at Fri Jul 28 22:28:36 2006
;     dbname: mydb
;     TOC Entries: 74
;     Compression: 0
;     Dump Version: 1.4-0
;     Format: CUSTOM
;
; Selected TOC Entries:
;
2; 145344 TABLE species postgres
3; 145344 ACL species
4; 145359 TABLE nt_header postgres
5; 145359 ACL nt_header
6; 145402 TABLE species_records postgres
7; 145402 ACL species_records
8; 145416 TABLE ss_old postgres
9; 145416 ACL ss_old
10; 145433 TABLE map_resolutions postgres
11; 145433 ACL map_resolutions
12; 145443 TABLE hs_old postgres
13; 145443 ACL hs_old
```

Semicolons start a comment, and the numbers at the start of lines refer to the internal archive ID assigned to each item. Lines in the file can be commented out, deleted, and reordered. For example,

``` pre
10; 145433 TABLE map_resolutions postgres
;2; 145344 TABLE species postgres
;4; 145359 TABLE nt_header postgres
6; 145402 TABLE species_records postgres
;8; 145416 TABLE ss_old postgres
```

Could be used as input to `pg_restore` and would only restore items 10 and 6, in that order:

``` shell
$ pg_restore -L db.list db.dump
```

## <a id="topic1__section8"></a>See Also

[pg\_dump](pg_dump.html#topic1)