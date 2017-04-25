---
title: CREATE TABLE
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

Defines a new table.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE <table_name> (
[ { <column_name> <data_type> [ DEFAULT <default_expr> ]
   [<column_constraint> [ ... ]
[ ENCODING ( <storage_directive> [,...] ) ]
]
   | <table_constraint>
   | LIKE <other_table> [{INCLUDING | EXCLUDING}
                      {DEFAULTS | CONSTRAINTS}] ...} ]
   [, ... ] ]
   [<column_reference_storage_directive> [, …] ]
   )
   [ INHERITS ( <parent_table> [, ... ] ) ]
   [ WITH ( <storage_parameter>=<value> [, ... ] )
   [ ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP} ]
   [ TABLESPACE <tablespace> ]
   [ DISTRIBUTED BY (<column>, [ ... ] ) | DISTRIBUTED RANDOMLY ]
   [ PARTITION BY <partition_type> (<column>)
       [ SUBPARTITION BY <partition_type> (<column>) ]
          [ SUBPARTITION TEMPLATE ( <template_spec> ) ]
       [...]
    ( <partition_spec> )
        | [ SUBPARTITION BY partition_type (<column>) ]
          [...]
    ( <partition_spec>
      [ ( <subpartition_spec>
           [(...)]
         ) ]
    )
```

where \<column\_constraint\> is:

``` pre
   [CONSTRAINT <constraint_name>]
   NOT NULL | NULL
   | CHECK ( <expression> )
```

where \<storage\_directive\> for a column is:

``` pre
   COMPRESSTYPE={ZLIB | SNAPPY | GZIP | NONE}
 | COMPRESSLEVEL={0-9}
 | BLOCKSIZE={8192-2097152}
```

where \<storage\_parameter\> for a table is:

``` pre
   APPENDONLY={TRUE}
   BLOCKSIZE={8192-2097152}
   bucketnum={<x>}
   ORIENTATION={ROW | PARQUET}
   COMPRESSTYPE={ZLIB | SNAPPY | GZIP | NONE}
   COMPRESSLEVEL={0-9}
   FILLFACTOR={10-100}
   OIDS=[TRUE|FALSE]
   PAGESIZE={1024-1073741823}
   ROWGROUPSIZE={1024-1073741823}
```

and \<table\_constraint\> is:

``` pre
   [CONSTRAINT <constraint_name>]
   | CHECK ( <expression> )
```

where \<partition\_type\> is:

``` pre
    LIST  | RANGE
```

where \<partition\_specification\> is:

``` pre
            <partition_element> [, ...]
```

and \<partition\_element\> is:

``` pre
   DEFAULT PARTITION <name>
  | [PARTITION <name>] VALUES (<list_value> [,...] )
  | [PARTITION <name>]
     START ([<datatype>] '<start_value>') [INCLUSIVE | EXCLUSIVE]
     [ END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ([<datatype>] [<number> | INTERVAL] '<interval_value>') ]
  | [PARTITION <name>]
     END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ([<datatype>] [<number> | INTERVAL] '<interval_value>') ]
[ WITH ( <partition_storage_parameter>=<value> [, ... ] ) ]
[<column_reference_storage_directive> [, …] ]
[ TABLESPACE <tablespace> ]
```

where \<subpartition\_spec\> or \<template\_spec\> is:

``` pre
            <subpartition_element> [, ...]
```

and \<subpartition\_element\> is:

``` pre
   DEFAULT SUBPARTITION <name>
  | [SUBPARTITION <name>] VALUES (<list_value> [,...] )
  | [SUBPARTITION <name>]
     START ([<datatype>] '<start_value>') [INCLUSIVE | EXCLUSIVE]
     [ END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ([<datatype>] [<number> | INTERVAL] '<interval_value>') ]
  | [SUBPARTITION <name>]
     END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ([<datatype>] [<number> | INTERVAL] '<interval_value>') ]
[ WITH ( <partition_storage_parameter>=<value> [, ... ] ) ]
[<column_reference_storage_directive> [, …] ]
[ TABLESPACE <tablespace> ]
```

where \<storage\_directive\> is:

``` pre
   COMPRESSTYPE={ZLIB | SNAPPY | GZIP | NONE}
 | COMPRESSLEVEL={0-9}
 | BLOCKSIZE={8192-2097152}
```

where \<column\_reference\_storage\_directive\> is:

``` pre
   COLUMN column_name ENCODING (<storage_directive> [, ... ] ), ...
 |
   DEFAULT COLUMN ENCODING (<storage_directive> [, ... ] )
```

where \<storage\_parameter\> for a partition is:

``` pre
   APPENDONLY={TRUE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={ROW | PARQUET}
   COMPRESSTYPE={ZLIB | SNAPPY | GZIP | NONE}
   COMPRESSLEVEL={0-9}
   FILLFACTOR={10-100}
   OIDS=[TRUE|FALSE]
   PAGESIZE={1024-1073741823}
   ROWGROUPSIZE={1024-1073741823}
```

## <a id="topic1__section3"></a>Description

`CREATE TABLE` creates a new, initially empty table in the current database. The table is owned by the user issuing the command. If a schema name is given then the table is created in the specified schema. Otherwise it is created in the current schema. Temporary tables exist in a special schema, so a schema name may not be given when creating a temporary table. The name of the table must be distinct from the name of any other table, external table, sequence, or view in the same schema.

The optional constraint clauses specify conditions that new rows must satisfy for an insert operation to succeed. A constraint is an SQL object that helps define the set of valid values in the table in various ways. Constraints apply to tables, not to partitions. You cannot add a constraint to a partition or subpartition.

There are two ways to define constraints: table constraints and column constraints. A column constraint is defined as part of a column definition. A table constraint definition is not tied to a particular column, and it can encompass more than one column. Every column constraint can also be written as a table constraint; a column constraint is only a notational convenience for use when the constraint only affects one column.

When creating a table, there is an additional clause to declare the HAWQ distribution policy. If a `DISTRIBUTED BY` clause is not supplied, HAWQ assigns a `RANDOM` distribution policy to the table, where the rows are distributed based on a round-robin or random distribution. You can also choose to distribute data with a hash-based policy, where the `bucketnum` attribute sets the number of hash buckets used by a hash-distributed table. Columns of geometric or user-defined data types are not eligible as HAWQ distribution key columns. The number of buckets affects how many virtual segments will be used in processing.

By default, a HASH distributed table is created with the number of hash buckets specified by the parameter \<default\_hash\_table\_bucket\_number\>. This can be changed in session level or in the create table DDL with `bucketnum` storage parameter.

**Note:** Column-oriented tables are no longer supported. Use Parquet tables for HAWQ internal tables.

The `PARTITION BY` clause allows you to divide the table into multiple sub-tables (or parts) that, taken together, make up the parent table and share its schema. Though the sub-tables exist as independent tables, HAWQ restricts their use in important ways. Internally, partitioning is implemented as a special form of inheritance. Each child table partition is created with a distinct `CHECK` constraint which limits the data the table can contain, based on some defining criteria. The `CHECK` constraints are also used by the query planner to determine which table partitions to scan in order to satisfy a given query predicate. These partition constraints are managed automatically by HAWQ.

## <a id="topic1__section4"></a>Parameters

<dt>GLOBAL | LOCAL  </dt>
<dd>These keywords are present for SQL standard compatibility, but have no effect in HAWQ.</dd>

<dt>TEMPORARY | TEMP  </dt>
<dd>If specified, the table is created as a temporary table. Temporary tables are automatically dropped at the end of a session, or optionally at the end of the current transaction (see `ON COMMIT`). Existing permanent tables with the same name are not visible to the current session while the temporary table exists, unless they are referenced with schema-qualified names. Any indexes created on a temporary table are automatically temporary as well.</dd>

<dt> \<table\_name\>  </dt>
<dd>The name (optionally schema-qualified) of the table to be created.</dd>

<dt> \<column\_name\>  </dt>
<dd>The name of a column to be created in the new table.</dd>

<dt> \<data\_type\>  </dt>
<dd>The data type of the column. This may include array specifiers.</dd>

<dt>DEFAULT \<default\_expr\>  </dt>
<dd>The `DEFAULT` clause assigns a default data value for the column whose column definition it appears within. The value is any variable-free expression (subqueries and cross-references to other columns in the current table are not allowed). The data type of the default expression must match the data type of the column. The default expression will be used in any insert operation that does not specify a value for the column. If there is no default for a column, then the default is null.</dd>

<dt>INHERITS  </dt>
<dd>The optional `INHERITS` clause specifies a list of tables from which the new table automatically inherits all columns. Use of `INHERITS` creates a persistent relationship between the new child table and its parent table(s). Schema modifications to the parent(s) normally propagate to children as well, and by default the data of the child table is included in scans of the parent(s).

In HAWQ, the `INHERITS` clause is not used when creating partitioned tables. Although the concept of inheritance is used in partition hierarchies, the inheritance structure of a partitioned table is created using the PARTITION BY clause.

If the same column name exists in more than one parent table, an error is reported unless the data types of the columns match in each of the parent tables. If there is no conflict, then the duplicate columns are merged to form a single column in the new table. If the column name list of the new table contains a column name that is also inherited, the data type must likewise match the inherited column(s), and the column definitions are merged into one. However, inherited and new column declarations of the same name need not specify identical constraints: all constraints provided from any declaration are merged together and all are applied to the new table. If the new table explicitly specifies a default value for the column, this default overrides any defaults from inherited declarations of the column. Otherwise, any parents that specify default values for the column must all specify the same default, or an error will be reported.</dd>

<dt>LIKE \<other\_table\> \[{INCLUDING | EXCLUDING} {DEFAULTS | CONSTRAINTS}\]  </dt>
<dd>The `LIKE` clause specifies a table from which the new table automatically copies all column names, data types, not-null constraints, and distribution policy. Storage properties like append-only or partition structure are not copied. Unlike `INHERITS`, the new table and original table are completely decoupled after creation is complete.

Default expressions for the copied column definitions will only be copied if `INCLUDING DEFAULTS` is specified. The default behavior is to exclude default expressions, resulting in the copied columns in the new table having null defaults.

Not-null constraints are always copied to the new table. `CHECK` constraints will only be copied if `INCLUDING CONSTRAINTS` is specified; other types of constraints will *never* be copied. Also, no distinction is made between column constraints and table constraints — when constraints are requested, all check constraints are copied.

Note also that unlike `INHERITS`, copied columns and constraints are not merged with similarly named columns and constraints. If the same name is specified explicitly or in another `LIKE` clause an error is signalled.</dd>

<dt>NULL | NOT NULL  </dt>
<dd>Specifies if the column is or is not allowed to contain null values. `NULL` is the default.</dd>

<dt>CHECK ( \<expression\> )  </dt>
<dd>The `CHECK` clause specifies an expression producing a Boolean result which new rows must satisfy for an insert operation to succeed. Expressions evaluating to `TRUE` or `UNKNOWN` succeed. Should any row of an insert operation produce a `FALSE` result an error exception is raised and the insert does not alter the database. A check constraint specified as a column constraint should reference that column's value only, while an expression appearing in a table constraint may reference multiple columns. `CHECK` expressions cannot contain subqueries nor refer to variables other than columns of the current row.</dd>

<dt>WITH ( \<storage\_option\>=\<value\> )  </dt>
<dd>The `WITH` clause can be used to set storage options for the table or its indexes. Note that you can also set storage parameters on a particular partition or subpartition by declaring the `WITH` clause in the partition specification.

Note: You cannot create a table with both column encodings and compression parameters in a WITH clause.

The following storage options are available:

**APPENDONLY** — Set to `TRUE` to create the table as an append-only table. If `FALSE` is specified, an error message displays stating that heap tables are not supported.

**BLOCKSIZE** — Set to the size, in bytes for each block in a table. The `BLOCKSIZE` must be between 8192 and 2097152 bytes, and be a multiple of 8192. The default is 32768.

**bucketnum** — Set to the number of hash buckets to be used in creating a hash-distributed table, specified as an integer greater than 0 and no more than the value of `default_hash_table_bucket_number`. The default when the table is created is 6 times the segment count. However, explicitly setting the bucket number when creating a hash table is recommended.

**ORIENTATION** — Set to `row` (the default) for row-oriented storage, or parquet. The parquet column-oriented format can be more efficient for large-scale queries. This option is only valid if `APPENDONLY=TRUE`. 

**COMPRESSTYPE** — Set to `ZLIB`, `SNAPPY`, or `GZIP` to specify the type of compression used. `ZLIB` provides more compact compression ratios at lower speeds. Parquet tables support `SNAPPY` and `GZIP` compression. Append-only tables support `SNAPPY` and `ZLIB` compression.  This option is valid only if `APPENDONLY=TRUE`.

**COMPRESSLEVEL** — Set to an integer value from 1 (fastest compression) to 9 (highest compression ratio). If not specified, the default is 1. This option is valid only if `APPENDONLY=TRUE` and `COMPRESSTYPE=[ZLIB|GZIP]`.

**OIDS** — Set to `OIDS=FALSE` (the default) so that rows do not have object identifiers assigned to them. Do not enable OIDS when creating a table. On large tables, such as those in a typical HAWQ system, using OIDs for table rows can cause wrap-around of the 32-bit OID counter. Once the counter wraps around, OIDs can no longer be assumed to be unique, which not only makes them useless to user applications, but can also cause problems in the HAWQ system catalog tables. In addition, excluding OIDs from a table reduces the space required to store the table on disk by 4 bytes per row, slightly improving performance. OIDS are not allowed on partitioned tables.</dd>

<dt>ON COMMIT  </dt>
<dd>The behavior of temporary tables at the end of a transaction block can be controlled using `ON COMMIT`. The three options are:

**PRESERVE ROWS** - No special action is taken at the ends of transactions for temporary tables. This is the default behavior.

**DELETE ROWS** - All rows in the temporary table will be deleted at the end of each transaction block. Essentially, an automatic `TRUNCATE` is done at each commit.

**DROP** - The temporary table will be dropped at the end of the current transaction block.</dd>

<dt>TABLESPACE \<tablespace\>  </dt>
<dd>The name of the tablespace in which the new table is to be created. If not specified, the database's default tablespace dfs\_default is used. Creating table on tablespace `pg_default` is not allowed.</dd>

<dt>DISTRIBUTED BY (\<column\>, \[ ... \] )  
DISTRIBUTED RANDOMLY  </dt>
<dd>Used to declare the HAWQ distribution policy for the table. The default is RANDOM distribution. `DISTIBUTED BY` can use hash distribution with one or more columns declared as the distribution key. If hash distribution is desired, it must be specified using the first eligible column of the table as the distribution key.</dd>

<dt>PARTITION BY  </dt>
<dd>Declares one or more columns by which to partition the table.</dd>

<dt> \<partition\_type\>  </dt>
<dd>Declares partition type: `LIST` (list of values) or `RANGE` (a numeric or date range).</dd>

<dt> \<partition\_specification\>  </dt>
<dd>Declares the individual partitions to create. Each partition can be defined individually or, for range partitions, you can use the `EVERY` clause (with a `START` and optional `END` clause) to define an increment pattern to use to create the individual partitions.

**`DEFAULT PARTITION \<name\>                      `** — Declares a default partition. When data does not match to an existing partition, it is inserted into the default partition. Partition designs that do not have a default partition will reject incoming rows that do not match to an existing partition.

**`PARTITION \<name\>  `** — Declares a name to use for the partition. Partitions are created using the following naming convention: `                      parentname_level#_prt_givenname                   `.

**`VALUES`** — For list partitions, defines the value(s) that the partition will contain.

**`START`** — For range partitions, defines the starting range value for the partition. By default, start values are `INCLUSIVE`. For example, if you declared a start date of '`2008-01-01`', then the partition would contain all dates greater than or equal to '`2008-01-01`'. Typically the data type of the `START` expression is the same type as the partition key column. If that is not the case, then you must explicitly cast to the intended data type.

**`END`** — For range partitions, defines the ending range value for the partition. By default, end values are `EXCLUSIVE`. For example, if you declared an end date of '`2008-02-01`', then the partition would contain all dates less than but not equal to '`2008-02-01`'. Typically the data type of the `END` expression is the same type as the partition key column. If that is not the case, then you must explicitly cast to the intended data type.

**`EVERY`** — For range partitions, defines how to increment the values from `START` to `END` to create individual partitions. Typically the data type of the `EVERY` expression is the same type as the partition key column. If that is not the case, then you must explicitly cast to the intended data type.

**`WITH`** — Sets the table storage options for a partition. For example, you may want older partitions to be append-only tables and newer partitions to be regular heap tables.

**`TABLESPACE`** — The name of the tablespace in which the partition is to be created.</dd>

<dt>SUBPARTITION BY  </dt>
<dd>Declares one or more columns by which to subpartition the first-level partitions of the table. The format of the subpartition specification is similar to that of a partition specification described above.</dd>

<dt>SUBPARTITION TEMPLATE  </dt>
<dd>Instead of declaring each subpartition definition individually for each partition, you can optionally declare a subpartition template to be used to create the subpartitions. This subpartition specification would then apply to all parent partitions.</dd>

## <a id="topic1__section5"></a>Notes

Using OIDs in new applications is not recommended. Avoid assuming that OIDs are unique across tables; if you need a database-wide unique identifier, use the combination of table OID and row OID for the purpose.

Primary key and foreign key constraints are not supported in HAWQ. For inherited tables, table privileges *are not* inherited in the current implementation.

HAWQ also supports the parquet columnar storage format. Parquet tables can be more efficient for increasing performance on large queries.

## <a id="parquetset"></a>Setting Parameters for Parquet Tables

You can set three kinds of parameters for a parquet table.

1.  Set the parquet orientation parameter:

    ``` pre
    with (appendonly=true, orientation=parquet);
    ```

2.  Set the compression type parameter. Parquet tables can be compressed using either `SNAPPY` or `GZIP`. `GZIP` supports compression level values between 1 and 9. `SNAPPY` does not support compression level; providing a compression level when using `SNAPPY` will cause the create table operation to fail. Specifying a compression level but no compression type when creating a parquet table will default to `GZIP` compression.

    **Note:**  For best performance with parquet storage, use `SNAPPY` compression. 

3.  Set the data storage parameter: By default, the two parameters, `PAGESIZE` and `ROWGROUPSIZE` are set to 1MB/8MB for common and partitioned tables.

    **Note:** The page size should be less than the rowgroup size. This is because rowgroup includes the metadata information of a single page even for a single column table. The parameters `PAGESIZE` and `ROWGROUPSIZE` are valid for parquet tables, while `BLOCKSIZE` is valid for append-only tables

## <a id="aboutparquet"></a>About Parquet Storage

DDL and DML: Most DDL and DML operations are valid for a parquet table. The usage for DDL and DML operations is similar to append-only tables. Valid operations on parquet tables include:

-   Parquet table creation (with/without partition, with/without compression type)
-   Insert and Select

**Compression type and level**: You can only set the compression type at the table level. HAWQ does not support setting column level compression. The specified compression type is propagated to the columns. All the columns must have the same compress type and level.

Using `SNAPPY` compression with parquet files is recommended for best performance.

**Data type**: HAWQ supports all data types except arrays and user defined types.

**Alter table**: HAWQ does not support adding a new column to an existing parquet table or dropping a column. You can use `ALTER TABLE` for a partition operation.

**FillFactor/OIDS/Checksum**: HAWQ does not support these operations when creating parquet tables. The default value for checksum for a parquet table is false. You cannot set this value or specify fillfactor and oids.

**Memory occupation**: When inserting or loading data to a parquet table, the whole rowgroup is stored in physical memory until the size exceeds the threshold or the end of the `INSERT` operation. Once either occurs, the entire rowgroup is flushed to disk. Also, at the beginning of the `INSERT` operation, each column is pre-allocated a page buffer. The column pre-allocated page buffer size should be `min(pageSizeLimit,                rowgroupSizeLimit/estimatedColumnWidth/estimatedRecordWidth)` for the first rowgroup. For the following rowgroup, it should be `min(pageSizeLimit,                actualColumnChunkSize in last rowgroup * 1.05)`, of which 1.05 is the estimated scaling factor. When reading data from a parquet table, the requested columns of the row group are loaded into memory. Memory is allocated 8 MB by default. Ensure that memory occupation does not exceed physical memory when setting `ROWGROUPSIZE` or `PAGESIZE`, otherwise you may encounter an out of memory error. 

**Bulk vs. trickle loads**
Only bulk loads are recommended for use with parquet tables. Trickle loads can result in bloated footers and larger data files.

## <a id="parquetexamples"></a>Parquet Examples

**Parquet Example 1**

Create an append-only table using the parquet format:

``` pre
CREATE TABLE customer ( id integer, fname text, lname text,
    address text, city text, state text, zip text )
WITH (APPENDONLY=true, ORIENTATION=parquet, OIDS=FALSE)
DISTRIBUTED BY (id);
```

**Parquet Example 2**

Create a parquet table with twelve monthly partitions:

``` pre
CREATE TABLE sales (id int, date date, amt decimal(10,2))
WITH (APPENDONLY=true, ORIENTATION=parquet, OIDS=FALSE)
DISTRIBUTED BY (id)
PARTITION BY RANGE (date)
  ( START (date '2016-01-01') INCLUSIVE
    END   (date '2017-01-01') EXCLUSIVE
    EVERY (INTERVAL '1 month')
  );
```

**Parquet Example 3**

Add a new partition to the sales table:

``` pre
ALTER TABLE sales ADD PARTITION
    START (date '2017-01-01') INCLUSIVE
    END (date '2017-02-01') EXCLUSIVE;
```

## <a id="aoexamples"></a>AO Examples

Append-only tables support `ZLIB` and `SNAPPY` compression types.

**AO Example 1**: Create a table named rank in the schema named baby and distribute the data using the columns rank, gender, and year:

``` pre
CREATE TABLE baby.rank ( id int, rank int, year smallint, gender char(1), count int )
DISTRIBUTED BY (rank, gender, year);
```

**AO Example 2**: Create table films and table distributors. The first column will be used as the HAWQ distribution key by default:

``` pre
CREATE TABLE films (
    code char(5), title varchar(40) NOT NULL, did integer NOT NULL,
    date_prod date, kind varchar(10), len interval hour to minute
);

CREATE TABLE distributors (
    did integer,
    name varchar(40) NOT NULL CHECK (name <> '')
);
```

**AO Example 3**: Create a snappy-compressed, append-only table:

``` pre
CREATE TABLE sales (txn_id int, qty int, date date)
WITH (appendonly=true, compresstype=snappy)
DISTRIBUTED BY (txn_id);
```

**AO Example 4**: Create a three level partitioned table using subpartition templates and default partitions at each level:

``` pre
CREATE TABLE sales (id int, year int, month int, day int,
region text)
DISTRIBUTED BY (id)
PARTITION BY RANGE (year)
SUBPARTITION BY RANGE (month)
SUBPARTITION TEMPLATE (
START (1) END (13) EVERY (1),
DEFAULT SUBPARTITION other_months )
SUBPARTITION BY LIST (region)
SUBPARTITION TEMPLATE (
SUBPARTITION usa VALUES ('usa'),
SUBPARTITION europe VALUES ('europe'),
SUBPARTITION asia VALUES ('asia'),
DEFAULT SUBPARTITION other_regions)
( START (2002) END (2010) EVERY (1),
DEFAULT PARTITION outlying_years);
```

**AO Example 5** Create a hash-distributed table named “sales” with 100 buckets.

``` pre
CREATE TABLE sales(id int, profit float)
WITH (bucketnum=100)
DISTRIBUTED BY (id);
```

## <a id="topic1__section7"></a>Compatibility

The `CREATE TABLE` command conforms to the SQL standard, with the following exceptions:

-   **Temporary Tables** — In the SQL standard, temporary tables are defined just once and automatically exist (starting with empty contents) in every session that needs them. HAWQ instead requires each session to issue its own `CREATE TEMPORARY                   TABLE` command for each temporary table to be used. This allows different sessions to use the same temporary table name for different purposes, whereas the standard's approach constrains all instances of a given temporary table name to have the same table structure.

    The standard's distinction between global and local temporary tables is not in HAWQ. HAWQ will accept the `GLOBAL` and `LOCAL` keywords in a temporary table declaration, but they have no effect.

    If the `ON COMMIT` clause is omitted, the SQL standard specifies that the default behavior as `ON COMMIT DELETE ROWS`. However, the default behavior in HAWQ is `ON COMMIT PRESERVE ROWS`. The `ON COMMIT DROP` option does not exist in the SQL standard.

-   **Column Check Constraints** — The SQL standard says that `CHECK` column constraints may only refer to the column they apply to; only `CHECK` table constraints may refer to multiple columns. HAWQ does not enforce this restriction; it treats column and table check constraints alike.
-   **NULL Constraint** — The `NULL` constraint is a HAWQ extension to the SQL standard that is included for compatibility with some other database systems (and for symmetry with the `NOT NULL` constraint). Since it is the default for any column, its presence is not required.
-   **Inheritance** — Multiple inheritance via the `INHERITS` clause is a HAWQ language extension. SQL:1999 and later define single inheritance using a different syntax and different semantics. SQL:1999-style inheritance is not yet supported by HAWQ.
-   **Partitioning** — Table partitioning via the `PARTITION BY` clause is a HAWQ language extension.
-   **Zero-column tables** — HAWQ allows a table of no columns to be created (for example, `CREATE TABLE foo();`). This is an extension from the SQL standard, which does not allow zero-column tables. Zero-column tables are not in themselves very useful, but disallowing them creates odd special cases for `ALTER TABLE DROP COLUMN`, so this spec restriction is ignored.
-   **WITH clause** — The `WITH` clause is an extension; neither storage parameters nor OIDs are in the standard.
-   **Tablespaces** — The HAWQ concept of tablespaces is not part of the SQL standard. The clauses `TABLESPACE` and `USING INDEX TABLESPACE` are extensions.
-   **Data Distribution** — The HAWQ concept of a parallel or distributed database is not part of the SQL standard. The `DISTRIBUTED` clauses are extensions.

## <a id="topic1__section8"></a>See Also

[ALTER TABLE](ALTER-TABLE.html), [DROP TABLE](DROP-TABLE.html), [CREATE EXTERNAL TABLE](CREATE-EXTERNAL-TABLE.html), [CREATE TABLE AS](CREATE-TABLE-AS.html)
