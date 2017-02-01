---
title: The hawq_toolkit Administrative Schema
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

This section provides a reference on the `hawq_toolkit` administrative schema.

HAWQ provides an administrative schema called `hawq_toolkit` that you can use to query the system catalogs, log files, and operating environment for system status information. The `hawq_toolkit` schema contains a number of views that you can access using SQL commands. The `hawq_toolkit` schema is accessible to all database users, although some objects may require superuser permissions.

This documentation describes the most useful views in `hawq_toolkit`. You may notice other objects (views, functions, and external tables) within the `hawq_toolkit` schema that are not described in this documentation (these are supporting objects to the views described in this section).

**Warning:** Do not change database objects in the `hawq_toolkit` schema. Do not create database objects in the schema. Changes to objects in the schema might affect the accuracy of administrative information returned by schema objects.

## <a id="topic2"></a>Checking for Tables that Need Routine Maintenance

The following views can help identify tables that need routine table maintenance (`VACUUM` and/or `ANALYZE`).

-   [hawq\_stats\_missing](#topic4)

The `VACUUM` command is applicable only to system catalog tables. The `VACUUM` command reclaims disk space occupied by deleted or obsolete rows. Because of the MVCC transaction concurrency model used in HAWQ, data rows that are deleted or updated still occupy physical space on disk even though they are not visible to any new transactions. Expired rows increase table size on disk and eventually slow down scans of the table.

**Note:** VACUUM FULL is not recommended in HAWQ. See [VACUUM](../sql/VACUUM.html#topic1).

The `ANALYZE` command collects column-level statistics needed by the query optimizer. HAWQ uses a cost-based query optimizer that relies on database statistics. Accurate statistics allow the query optimizer to better estimate selectivity and the number of rows retrieved by a query operation in order to choose the most efficient query plan.

### <a id="topic4"></a>hawq\_stats\_missing

This view shows tables that do not have statistics and therefore may require an `ANALYZE` be run on the table.

<a id="topic4__ie194266"></a>

<span class="tablecap">Table 1. hawq\_stats\_missing view</span>

| Column    | Description                                                                                                                                                                                                                                                                                                                                                                |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| smischema | Schema name.                                                                                                                                                                                                                                                                                                                                                               |
| smitable  | Table name.                                                                                                                                                                                                                                                                                                                                                                |
| smisize   | Does this table have statistics? False if the table does not have row count and row sizing statistics recorded in the system catalog, which may indicate that the table needs to be analyzed. This will also be false if the table does not contain any rows. For example, the parent tables of partitioned tables are always empty and will always return a false result. |
| smicols   | Number of columns in the table.                                                                                                                                                                                                                                                                                                                                            |
| smirecs   | Number of rows in the table.                                                                                                                                                                                                                                                                                                                                               |


## <a id="topic16"></a>Viewing HAWQ Server Log Files

Each component of a HAWQ system (master, standby master, and segments) keeps its own server log files. The `hawq_log_*` family of views allows you to issue SQL queries against the server log files to find particular entries of interest. The use of these views requires superuser permissions.

-   [hawq\_log\_command\_timings](#topic17)
-   [hawq\_log\_master\_concise](#topic19)

### <a id="topic17"></a>hawq\_log\_command\_timings

This view uses an external table to read the log files on the master and report the execution time of SQL commands executed in a database session. The use of this view requires superuser permissions.

<a id="topic17__ie176169"></a>

<span class="tablecap">Table 2. hawq\_log\_command\_timings view</span>

| Column      | Description                                                |
|-------------|------------------------------------------------------------|
| logsession  | The session identifier (prefixed with "con").              |
| logcmdcount | The command number within a session (prefixed with "cmd"). |
| logdatabase | The name of the database.                                  |
| loguser     | The name of the database user.                             |
| logpid      | The process id (prefixed with "p").                        |
| logtimemin  | The time of the first log message for this command.        |
| logtimemax  | The time of the last log message for this command.         |
| logduration | Statement duration from start to end time.                 |


### <a id="topic19"></a>hawq\_log\_master\_concise

This view uses an external table to read a subset of the log fields from the master log file. The use of this view requires superuser permissions.

<a id="topic19__ie177543"></a>

<span class="tablecap">Table 3. hawq\_log\_master\_concise view</span>

| Column      | Description                                                |
|-------------|------------------------------------------------------------|
| logtime     | The timestamp of the log message.                          |
| logdatabase | The name of the database.                                  |
| logsession  | The session identifier (prefixed with "con").              |
| logcmdcount | The command number within a session (prefixed with "cmd"). |
| logseverity | The severity level for the record.                         |
| logmessage  | Log or error message text.                                 |


## <a id="topic38"></a>Checking Database Object Sizes and Disk Space

The `hawq_size_*` family of views can be used to determine the disk space usage for a distributed HAWQ, schema, table, or index. The following views calculate the total size of an object across all segments.

-   [hawq\_size\_of\_all\_table\_indexes](#topic39)
-   [hawq\_size\_of\_database](#topic40)
-   [hawq\_size\_of\_index](#topic41)
-   [hawq\_size\_of\_partition\_and\_indexes\_disk](#topic42)
-   [hawq\_size\_of\_schema\_disk](#topic43)
-   [hawq\_size\_of\_table\_and\_indexes\_disk](#topic44)
-   [hawq\_size\_of\_table\_and\_indexes\_licensing](#topic45)
-   [hawq\_size\_of\_table\_disk](#topic46)
-   [hawq\_size\_of\_table\_uncompressed](#topic47)

The table and index sizing views list the relation by object ID (not by name). To check the size of a table or index by name, you must look up the relation name (`relname`) in the `pg_class` table. For example:

``` pre
SELECT relname AS name, sotdsize AS size, sotdtoastsize AS 
toast, sotdadditionalsize AS other 
FROM hawq_size_of_table_disk AS sotd, pg_class 
WHERE sotd.sotdoid=pg_class.oid ORDER BY relname;
```

### <a id="topic39"></a>hawq\_size\_of\_all\_table\_indexes

This view shows the total size of all indexes for a table. This view is accessible to all users, however non-superusers will only be able to see relations that they have permission to access.

<a id="topic39__ie181657"></a>

<span class="tablecap">Table 4. hawq\_size\_of\_all\_table\_indexes view</span>

| Column          | Description                                  |
|-----------------|----------------------------------------------|
| soatioid        | The object ID of the table                   |
| soatisize       | The total size of all table indexes in bytes |
| soatischemaname | The schema name                              |
| soatitablename  | The table name                               |


### <a id="topic40"></a>hawq\_size\_of\_database

This view shows the total size of a database. This view is accessible to all users, however non-superusers will only be able to see databases that they have permission to access.

<a id="topic40__ie181758"></a>

<span class="tablecap">Table 5. hawq\_size\_of\_database view</span>

| Column      | Description                       |
|-------------|-----------------------------------|
| sodddatname | The name of the database          |
| sodddatsize | The size of the database in bytes |


### <a id="topic41"></a>hawq\_size\_of\_index

This view shows the total size of an index. This view is accessible to all users, however non-superusers will only be able to see relations that they have permission to access.

<a id="topic41__ie181709"></a>

<span class="tablecap">Table 6. hawq\_size\_of\_index view</span>

| Column             | Description                                           |
|--------------------|-------------------------------------------------------|
| soioid             | The object ID of the index                            |
| soitableoid        | The object ID of the table to which the index belongs |
| soisize            | The size of the index in bytes                        |
| soiindexschemaname | The name of the index schema                          |
| soiindexname       | The name of the index                                 |
| soitableschemaname | The name of the table schema                          |
| soitablename       | The name of the table                                 |


### <a id="topic42"></a>hawq\_size\_of\_partition\_and\_indexes\_disk

This view shows the size on disk of partitioned child tables and their indexes. This view is accessible to all users, however non-superusers will only be able to see relations that they have permission to access.

<a id="topic42__ie181803"></a>

<span class="tablecap">Table 7. hawq\_size\_of\_partition\_and\_indexes\_disk view</span>

| Column                     | Description                                     |
|----------------------------|-------------------------------------------------|
| sopaidparentoid            | The object ID of the parent table               |
| sopaidpartitionoid         | The object ID of the partition table            |
| sopaidpartitiontablesize   | The partition table size in bytes               |
| sopaidpartitionindexessize | The total size of all indexes on this partition |
| Sopaidparentschemaname     | The name of the parent schema                   |
| Sopaidparenttablename      | The name of the parent table                    |
| Sopaidpartitionschemaname  | The name of the partition schema                |
| sopaidpartitiontablename   | The name of the partition table                 |


### <a id="topic43"></a>hawq\_size\_of\_schema\_disk

This view shows schema sizes for the public schema and the user-created schemas in the current database. This view is accessible to all users, however non-superusers will be able to see only the schemas that they have permission to access.

<a id="topic43__ie183105"></a>

<span class="tablecap">Table 8. hawq\_size\_of\_schema\_disk view</span>

| Column              | Description                                      |
|---------------------|--------------------------------------------------|
| sosdnsp             | The name of the schema                           |
| sosdschematablesize | The total size of tables in the schema in bytes  |
| sosdschemaidxsize   | The total size of indexes in the schema in bytes |


### <a id="topic44"></a>hawq\_size\_of\_table\_and\_indexes\_disk

This view shows the size on disk of tables and their indexes. This view is accessible to all users, however non-superusers will only be able to see relations that they have permission to access.

<a id="topic44__ie183128"></a>

<span class="tablecap">Table 9. hawq\_size\_of\_table\_and\_indexes\_disk view</span>

| Column           | Description                                |
|------------------|--------------------------------------------|
| sotaidoid        | The object ID of the parent table          |
| sotaidtablesize  | The disk size of the table                 |
| sotaididxsize    | The total size of all indexes on the table |
| sotaidschemaname | The name of the schema                     |
| sotaidtablename  | The name of the table                      |


### <a id="topic45"></a>hawq\_size\_of\_table\_and\_indexes\_licensing

This view shows the total size of tables and their indexes for licensing purposes. The use of this view requires superuser permissions.

<a id="topic45__ie181949"></a>

<span class="tablecap">Table 10. hawq\_size\_of\_table\_and\_indexes\_licensing view</span>

| Column                      | Description                                                                                 |
|-----------------------------|---------------------------------------------------------------------------------------------|
| sotailoid                   | The object ID of the table                                                                  |
| sotailtablesizedisk         | The total disk size of the table                                                            |
| sotailtablesizeuncompressed | If the table is a compressed append-only table, shows the uncompressed table size in bytes. |
| sotailindexessize           | The total size of all indexes in the table                                                  |
| sotailschemaname            | The schema name                                                                             |
| sotailtablename             | The table name                                                                              |


### <a id="topic46"></a>hawq\_size\_of\_table\_disk

This view shows the size of a table on disk. This view is accessible to all users, however non-superusers will only be able to see tables that they have permission to access

<a id="topic46__ie183408"></a>

<span class="tablecap">Table 11. hawq\_size\_of\_table\_disk view</span>

| Column             | Description                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sotdoid            | The object ID of the table                                                                                                                                                                           |
| sotdsize           | The size of the table in bytes. The size is only the main table size. The size does not include auxiliary objects such as oversized (toast) attributes, or additional storage objects for AO tables. |
| sotdtoastsize      | The size of the TOAST table (oversized attribute storage), if there is one.                                                                                                                          |
| sotdadditionalsize | Reflects the segment and block directory table sizes for append-only (AO) tables.                                                                                                                    |
| sotdschemaname     | The schema name                                                                                                                                                                                      |
| sotdtablename      | The table name                                                                                                                                                                                       |


### <a id="topic47"></a>hawq\_size\_of\_table\_uncompressed

This view shows the uncompressed table size for append-only (AO) tables. Otherwise, the table size on disk is shown. The use of this view requires superuser permissions.

<a id="topic47__ie183582"></a>

<span class="tablecap">Table 12. hawq\_size\_of\_table\_uncompressed view</span>

| Column         | Description                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------------|
| sotuoid        | The object ID of the table                                                                                    |
| sotusize       | The uncomressed size of the table in bytes if it is a compressed AO table. Otherwise, the table size on disk. |
| sotuschemaname | The schema name                                                                                               |
| sotutablename  | The table name                                                                                                |



