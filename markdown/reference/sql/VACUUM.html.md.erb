---
title: VACUUM
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

Garbage-collects and optionally analyzes a database. 

**Note**: HAWQ `VACUUM` support is provided only for system catalog tables.  `VACUUM`ing a HAWQ user table has no effect.

## <a id="topic1__section2"></a>Synopsis

``` pre
VACUUM [FULL] [FREEZE] [VERBOSE] <table>
VACUUM [FULL] [FREEZE] [VERBOSE] ANALYZE
              [<table> [(<column> [, ...] )]]
```

## <a id="topic1__section3"></a>Description

`VACUUM` reclaims storage occupied by deleted tuples. In normal HAWQ operation, tuples that are deleted or obsoleted by an update are not physically removed from their table; they remain present on disk until a `VACUUM` is done. Therefore it is necessary to do `VACUUM` periodically, especially on frequently-updated catalog tables. (`VACUUM` has no effect on a normal HAWQ table, since the delete or update operations are not supported on normal HAWQ table.)

With no parameter, `VACUUM` processes every table in the current database. With a parameter, `VACUUM` processes only that table. `VACUUM ANALYZE` performs a `VACUUM` and then an `ANALYZE` for each selected table. This is a handy combination form for routine maintenance scripts. See [ANALYZE](ANALYZE.html) for more details about its processing.

Plain `VACUUM` (without `FULL`) simply reclaims space and makes it available for re-use. This form of the command can operate in parallel with normal reading and writing of the table, as an exclusive lock is not obtained. `VACUUM FULL` does more extensive processing, including moving of tuples across blocks to try to compact the table to the minimum number of disk blocks. This form is much slower and requires an exclusive lock on each table while it is being processed.  

**Note:** `VACUUM FULL` is not recommended in HAWQ.

**Outputs**

When `VERBOSE` is specified, `VACUUM` emits progress messages to indicate which table is currently being processed. Various statistics about the tables are printed as well.

## <a id="topic1__section5"></a>Parameters

<dt>FULL  </dt>
<dd>Selects a full vacuum, which may reclaim more space but takes much longer and exclusively locks the table.

**Note:** A VACUUM FULL is not recommended in HAWQ. See [Notes](#topic1__section6).</dd>

<dt>FREEZE  </dt>
<dd>Specifying `FREEZE` is equivalent to performing `VACUUM` with the `vacuum_freeze_min_age` server configuration parameter set to zero. The `FREEZE` option is deprecated and will be removed in a future release.</dd>

<dt>VERBOSE  </dt>
<dd>Prints a detailed vacuum activity report for each table.</dd>

<dt>ANALYZE  </dt>
<dd>Updates statistics used by the planner to determine the most efficient way to execute a query.</dd>

<dt> \<table\>   </dt>
<dd>The name (optionally schema-qualified) of a specific table to vacuum. Defaults to all tables in the current database.</dd>

<dt> \<column\>   </dt>
<dd>The name of a specific column to analyze. Defaults to all columns.</dd>

## <a id="topic1__section6"></a>Notes

`VACUUM` cannot be executed inside a transaction block.

A recommended practice is to vacuum active production databases frequently (at least nightly), in order to remove expired rows. After adding or deleting a large number of rows, it may be a good idea to issue a `VACUUM ANALYZE` command for the affected table. This will update the system catalogs with the results of all recent changes, and allow the HAWQ query planner to make better choices in planning queries.

`VACUUM` causes a substantial increase in I/O traffic, which can cause poor performance for other active sessions. Therefore, it is advisable to vacuum the database at low usage times. The `auto vacuum` daemon feature, that automates the execution of `VACUUM` and `ANALYZE` commands is currently disabled in HAWQ.

Expired rows are held in what is called the *free space map*. The free space map must be sized large enough to cover the dead rows of all tables in your database. If not sized large enough, space occupied by dead rows that overflow the free space map cannot be reclaimed by a regular `VACUUM` command.

`VACUUM FULL` will reclaim all expired row space, but is a very expensive operation and may take an unacceptably long time to finish on large, distributed HAWQ tables. If you do get into a situation where the free space map has overflowed, it may be more timely to recreate the table with a `CREATE TABLE AS` statement and drop the old table.

`VACUUM FULL` is not recommended in HAWQ. It is best to size the free space map appropriately. The free space map is configured with the following server configuration parameters:

-   `max_fsm_pages`
-   `max_fsm_relations`

## <a id="topic1__section7"></a>Examples

Vacuum all tables in the current database:

``` sql
VACUUM;
```

Vacuum a specific table only:

``` sql
VACUUM mytable;
```

Vacuum all tables in the current database and collect statistics for the query planner:

``` sql
VACUUM ANALYZE;
```

## <a id="topic1__section8"></a>Compatibility

There is no `VACUUM` statement in the SQL standard.

## <a id="topic1__section9"></a>See Also

[ANALYZE](ANALYZE.html)
