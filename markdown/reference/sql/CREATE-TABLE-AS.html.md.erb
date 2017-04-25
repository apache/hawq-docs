---
title: CREATE TABLE AS
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

Defines a new table from the results of a query.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE [ [GLOBAL | LOCAL] {TEMPORARY | TEMP} ] TABLE <table_name>
   [(<column_name> [, ...] )]
   [ WITH ( storage_parameter=<value> [, ... ] )
   [ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP}]
   [TABLESPACE <tablespace>]
   AS <query>
   [DISTRIBUTED BY (<column>, [ ... ] ) | DISTRIBUTED RANDOMLY]
```

where \<storage\_parameter\> is:

``` pre
   APPENDONLY={TRUE}
   BLOCKSIZE={8192-2097152} 
   bucketnum={<x>}
   ORIENTATION={ROW | PARQUET}
   COMPRESSTYPE={ZLIB | SNAPPY | GZIP | NONE}
   COMPRESSLEVEL={0-9 | 1}
   FILLFACTOR={10-100}
   OIDS=[TRUE | FALSE]
   PAGESIZE={1024-1073741823}
   ROWGROUPSIZE={1024-1073741823}
```

## <a id="topic1__section3"></a>Description

`CREATE TABLE AS` creates a table and fills it with data computed by a [SELECT](SELECT.html) command. The table columns have the names and data types associated with the output columns of the `SELECT`, however you can override the column names by giving an explicit list of new column names.

`CREATE TABLE AS` creates a new table and evaluates the query just once to fill the new table initially. The new table will not track subsequent changes to the source tables of the query.

## <a id="topic1__section4"></a>Parameters

<dt>GLOBAL | LOCAL  </dt>
<dd>These keywords are present for SQL standard compatibility, but have no effect in HAWQ.</dd>

<dt>TEMPORARY | TEMP  </dt>
<dd>If specified, the new table is created as a temporary table. Temporary tables are automatically dropped at the end of a session, or optionally at the end of the current transaction (see `ON COMMIT`). Existing permanent tables with the same name are not visible to the current session while the temporary table exists, unless they are referenced with schema-qualified names. Any indexes created on a temporary table are automatically temporary as well.</dd>

<dt> \<table\_name\>   </dt>
<dd>The name (optionally schema-qualified) of the new table to be created.</dd>

<dt> \<column\_name\>   </dt>
<dd>The name of a column in the new table. If column names are not provided, they are taken from the output column names of the query. If the table is created from an `EXECUTE` command, a column name list cannot be specified.</dd>

<dt>WITH (\<storage\_parameter\>=\<value\> )  </dt>
<dd>The `WITH` clause can be used to set storage options for the table or its indexes. Note that you can also set different storage parameters on a particular partition or subpartition by declaring the `WITH` clause in the partition specification. The following storage options are available:

**APPENDONLY** — Set to `TRUE` to create the table as an append-only table. If `FALSE`, an error message displays stating that heap tables are not supported.

**BLOCKSIZE** — Set to the size, in bytes for each block in a table. The `BLOCKSIZE` must be between 8192 and 2097152 bytes, and be a multiple of 8192. The default is 32768.

**bucketnum** — Set to the number of hash buckets to be used in creating a hash-distributed table. If changing the number of hash buckets, use `WITH` to specify `bucketnum` in creating a hash-distributed table. If distribution is specified by column, the table will inherit the value.

**ORIENTATION** — Set to `row` (the default) for row-oriented storage, or `parquet`. This option is only valid if `APPENDONLY=TRUE`. Heap-storage tables can only be row-oriented.

**COMPRESSTYPE** — Set to `ZLIB`, `SNAPPY`, or `GZIP` to specify the type of compression used. ZLIB provides more compact compression ratios at lower speeds. Parquet tables support `SNAPPY` and `GZIP` compression. Append-only tables support `SNAPPY` and `ZLIB` compression.  This option is valid only if `APPENDONLY=TRUE`.

**COMPRESSLEVEL** — Set to an integer value from 1 (fastest compression) to 9 (highest compression ratio). If not declared, the default is 1. This option is valid only if `APPENDONLY=TRUE` and `COMPRESSTYPE=[ZLIB|GZIP]`.

**OIDS** — Set to `OIDS=FALSE` (the default) so that rows do not have object identifiers assigned to them. Do not enable OIDS when creating a table. On large tables, such as those in a typical HAWQ system, using OIDs for table rows can cause wrap-around of the 32-bit OID counter. Once the counter wraps around, OIDs can no longer be assumed to be unique, which not only makes them useless to user applications, but can also cause problems in the HAWQ system catalog tables. In addition, excluding OIDs from a table reduces the space required to store the table on disk by 4 bytes per row, slightly improving performance.</dd>

<dt>ON COMMIT  </dt>
<dd>The behavior of temporary tables at the end of a transaction block can be controlled using `ON COMMIT`. The three options are:

**PRESERVE ROWS** — No special action is taken at the ends of transactions for temporary tables. This is the default behavior.

**DELETE ROWS** — All rows in the temporary table will be deleted at the end of each transaction block. Essentially, an automatic `TRUNCATE` is done at each commit.

**DROP** — The temporary table will be dropped at the end of the current transaction block.</dd>

<dt>TABLESPACE \<tablespace\>   </dt>
<dd>The tablespace is the name of the tablespace in which the new table is to be created. If not specified, the database's default tablespace is used.</dd>

<dt>AS \<query\>   </dt>
<dd>A [SELECT](SELECT.html) command, or an [EXECUTE](EXECUTE.html) command that runs a prepared `SELECT` query.</dd>

<dt>DISTRIBUTED BY (\<column\>, \[ ... \] )  
DISTRIBUTED RANDOMLY  </dt>
<dd>Used to declare the HAWQ distribution policy for the table. The default is RANDOM distribution. `DISTIBUTED BY` can use hash distribution with one or more columns declared as the distribution key. If hash distribution is desired, it can be specified using `bucketnum` attribute, using the first eligible column of the table as the distribution key.</dd>

## <a id="topic1__section5"></a>Notes

This command is functionally similar to [SELECT INTO](SELECT-INTO.html), but it is preferred since it is less likely to be confused with other uses of the `SELECT INTO` syntax. Furthermore, `CREATE TABLE AS` offers a superset of the functionality offered by `SELECT INTO`.

`CREATE TABLE AS` can be used for fast data loading from external table data sources. See [CREATE EXTERNAL TABLE](CREATE-EXTERNAL-TABLE.html).

## <a id="topic1__section6"></a>Examples

Create a new table `films_recent` consisting of only recent entries from the table `films`:

``` pre
CREATE TABLE films_recent AS SELECT * FROM films WHERE 
date_prod >= '2007-01-01';
```

Create a new temporary table `films_recent`, consisting of only recent entries from the table films, using a prepared statement. The new table has OIDs and will be dropped at commit:

``` pre
PREPARE recentfilms(date) AS SELECT * FROM films WHERE 
date_prod > $1;
CREATE TEMP TABLE films_recent WITH (OIDS) ON COMMIT DROP AS 
EXECUTE recentfilms('2007-01-01');
```

## <a id="topic1__section7"></a>Compatibility

`CREATE TABLE AS` conforms to the SQL standard, with the following exceptions:

-   The standard requires parentheses around the subquery clause; in HAWQ, these parentheses are optional.
-   The standard defines a `WITH [NO] DATA` clause; this is not currently implemented by HAWQ. The behavior provided by HAWQ is equivalent to the standard's `WITH DATA` case. `WITH NO DATA` can be simulated by appending `LIMIT 0` to the query.
-   HAWQ handles temporary tables differently from the standard; see `CREATE TABLE` for details.
-   The `WITH` clause is a HAWQ extension; neither storage parameters nor `OIDs` are in the standard.
-   The HAWQ concept of tablespaces is not part of the standard. The `TABLESPACE` clause is an extension.

## <a id="topic1__section8"></a>See Also

[CREATE EXTERNAL TABLE](CREATE-EXTERNAL-TABLE.html), [EXECUTE](EXECUTE.html), [SELECT](SELECT.html), [SELECT INTO](SELECT-INTO.html)
