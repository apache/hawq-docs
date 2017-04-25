---
title: ALTER TABLE
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

Changes the definition of a table.

## <a id="altertable__section2"></a>Synopsis

```pre
ALTER TABLE [ONLY] <name> RENAME [COLUMN] <column> TO <new_column>

ALTER TABLE <name> RENAME TO <new_name>

ALTER TABLE <name> SET SCHEMA <new_schema>

ALTER TABLE [ONLY] <name> SET 
     DISTRIBUTED BY (<column>, [ ... ] ) 
   | DISTRIBUTED RANDOMLY 
   | WITH (REORGANIZE=true|false)
 
ALTER TABLE [ONLY] <name>
            <action> [, ... ]

ALTER TABLE <name>
   [ ALTER PARTITION { <partition_name> | FOR (RANK(<number>)) 
   | FOR (<value>) } <partition_action> [...] ] 
   <partition_action>        
```

where \<action\> is one of:

```pre
   ADD [COLUMN] <column_name> <type>
      [ ENCODING ( <storage_directive> [,...] ) ]
      [<column_constraint> [ ... ]]
  DROP [COLUMN] <column> [RESTRICT | CASCADE]
  ALTER [COLUMN] <column> TYPE <type> [USING <expression>]
  ALTER [COLUMN] <column> SET DEFAULT <expression>
  ALTER [COLUMN] <column> DROP DEFAULT
  ALTER [COLUMN] <column> { SET | DROP } NOT NULL
  ALTER [COLUMN] <column> SET STATISTICS <integer>
  ADD <table_constraint>
  DROP CONSTRAINT <constraint_name> [RESTRICT | CASCADE]
  SET WITHOUT OIDS
  INHERIT <parent_table>
  NO INHERIT <parent_table>
  OWNER TO <new_owner>
         
```

where \<partition\_action\> is one of:

```pre
  ALTER DEFAULT PARTITION
  DROP DEFAULT PARTITION [IF EXISTS]
  DROP PARTITION [IF EXISTS] { <partition_name> | 
    FOR (RANK(<number>)) | FOR (<value>) } [CASCADE]
  TRUNCATE DEFAULT PARTITION
  TRUNCATE PARTITION { <partition_name> | FOR (RANK(<number>)) | 
    FOR (<value>) }
  RENAME DEFAULT PARTITION TO <new_partition_name>
  RENAME PARTITION { <partition_name> | FOR (RANK(<number>)) | 
        FOR (<value>) } TO <new_partition_name>
  ADD DEFAULT PARTITION <name> [ ( <subpartition_spec> ) ]
  ADD PARTITION <name>
            <partition_element>
      [ ( <subpartition_spec> ) ]
  EXCHANGE DEFAULT PARTITION WITH TABLE <table_name>
        [ WITH | WITHOUT VALIDATION ]
  EXCHANGE PARTITION { <partition_name> | FOR (RANK(<number>)) | 
        FOR (<value>) } WITH TABLE <table_name>
        [ WITH | WITHOUT VALIDATION ]
  SET SUBPARTITION TEMPLATE (<subpartition_spec>)
  SPLIT DEFAULT PARTITION
     { AT (<list_value>)
     | START([<datatype>] <range_value>) [INCLUSIVE | EXCLUSIVE] 
        END([<datatype>] <range_value>) [INCLUSIVE | EXCLUSIVE] }
    [ INTO ( PARTITION <new_partition_name>, 
             PARTITION <default_partition_name> ) ]
  SPLIT PARTITION { <partition_name> | FOR (RANK(<number>)) | 
    FOR (<value>) } AT (<value>) 
    [ INTO (PARTITION <partition_name>, PARTITION <partition_name>)]
```

where \<partition\_element\> is:

```pre
    VALUES (<list_value> [,...] )
  | START ([<datatype>] '<start_value>') [INCLUSIVE | EXCLUSIVE]
    [ END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE] ]
  | END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE]
[ WITH ( <partition_storage_parameter>=<value> [, ... ] ) ]
[ TABLESPACE <tablespace> ]
```

where \<subpartition\_spec\> is:

```pre
            <subpartition_element> [, ...]
```

and \<subpartition\_element\> is:

```pre
  DEFAULT SUBPARTITION <subpartition_name>
  | [SUBPARTITION <subpartition_name>] VALUES (<list_value> [,...] )
  | [SUBPARTITION <subpartition_name>] 
     START ([<datatype>] '<start_value>') [INCLUSIVE | EXCLUSIVE]
     [ END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ( [<number> | <datatype>] '<interval_value>') ]
  | [SUBPARTITION <subpartition_name>] 
     END ([<datatype>] '<end_value>') [INCLUSIVE | EXCLUSIVE]
    [ EVERY ( [<number> | <datatype>] '<interval_value>') ]
[ WITH ( <partition_storage_parameter>=<value> [, ... ] ) ]
[ TABLESPACE <tablespace> ]
```

where \<storage\_parameter\> is:

```pre
   APPENDONLY={TRUE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={ROW | PARQUET}
   COMPRESSTYPE={ZLIB|SNAPPY|GZIP|NONE}
   COMPRESSLEVEL={0-9}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```

where \<storage\_directive\> is:

```pre
   COMPRESSTYPE={ZLIB|SNAPPY|GZIP|NONE} 
 | COMPRESSLEVEL={0-9} 
 | BLOCKSIZE={8192-2097152}
```

where \<column\_reference\_storage\_directive\> is:

```pre
   COLUMN <column_name> ENCODING ( <storage_directive> [, ... ] ), ... 
 | DEFAULT COLUMN ENCODING ( <storage_directive> [, ... ] )
```

**Note:**
When using multi-level partition designs, the following operations are not supported with ALTER TABLE:

-   ADD DEFAULT PARTITION
-   ADD PARTITION
-   DROP DEFAULT PARTITION
-   DROP PARTITION
-   SPLIT PARTITION
-   All operations that involve modifying subpartitions.

## <a id="limitations"></a>Limitations

HAWQ does not support using `ALTER TABLE` to `ADD` or `DROP` a column in an existing Parquet table.

## <a id="altertable__section4"></a>Parameters


<dt>ONLY  </dt>
<dd>Only perform the operation on the table name specified. If the `ONLY` keyword is not used, the operation       will be performed on the named table and any child table partitions associated with that table.</dd>

<dt>\<name\>  </dt>
<dd>The name (possibly schema-qualified) of an existing table to alter. If `ONLY` is specified, only that table is altered. If `ONLY` is not specified, the table and all its descendant tables (if any) are updated.

*Note:* Constraints can only be added to an entire table, not to a partition. Because of that restriction, the \<name\> parameter can only contain a table name, not a partition name.</dd>

<dt> \<column\>   </dt>
<dd>Name of a new or existing column. Note that HAWQ distribution key columns must be treated with special care. Altering or dropping these columns can change the distribution policy for the table.</dd>

<dt> \<new\_column\>   </dt>
<dd>New name for an existing column.</dd>

<dt> \<new\_name\>   </dt>
<dd>New name for the table.</dd>

<dt> \<type\>   </dt>
<dd>Data type of the new column, or new data type for an existing column. If changing the data type of a HAWQ distribution key column, you are only allowed to change it to a compatible type (for example, `text` to `varchar` is OK, but `text` to `int` is not).</dd>

<dt> \<table\_constraint\>   </dt>
<dd>New table constraint for the table. Note that foreign key constraints are currently not supported in HAWQ. Also a table is only allowed one unique constraint and the uniqueness must be within the HAWQ distribution key.</dd>

<dt> \<constraint\_name\>   </dt>
<dd>Name of an existing constraint to drop.</dd>

<dt>CASCADE  </dt>
<dd>Automatically drop objects that depend on the dropped column or constraint (for example, views referencing the column).</dd>

<dt>RESTRICT  </dt>
<dd>Refuse to drop the column or constraint if there are any dependent objects. This is the default behavior.</dd>

<dt>ALL  </dt>
<dd>Disable or enable all triggers belonging to the table including constraint related triggers. This requires superuser privilege.</dd>

<dt>USER  </dt>
<dd>Disable or enable all user-created triggers belonging to the table.</dd>

<dt>DISTRIBUTED RANDOMLY | DISTRIBUTED BY (\<column\>)  </dt>
<dd>Specifies the distribution policy for a table. The default is RANDOM distribution. Changing a distribution policy will cause the table data to be physically redistributed on disk, which can be resource intensive. If you declare the same distribution policy or change from random to hash distribution, data will not be redistributed unless you declare `SET WITH (REORGANIZE=true)`.</dd>

<dt>REORGANIZE=true|false  </dt>
<dd>Use `REORGANIZE=true` when the distribution policy has not changed or when you have changed from a random to a hash distribution, and you want to redistribute the data anyways.</dd>

<dt> \<parent\_table\>   </dt>
<dd>A parent table to associate or de-associate with this table.</dd>

<dt> \<new\_owner\>   </dt>
<dd>The role name of the new owner of the table.</dd>

<dt> \<new\_tablespace\>   </dt>
<dd>The name of the tablespace to which the table will be moved.</dd>

<dt> \<new\_schema\>   </dt>
<dd>The name of the schema to which the table will be moved.</dd>

<dt> \<parent\_table\_name\>   </dt>
<dd>When altering a partitioned table, the name of the top-level parent table.</dd>

<dt>ALTER \[DEFAULT\] PARTITION  </dt>
<dd>If altering a partition deeper than the first level of partitions, the `ALTER PARTITION` clause is used to specify which subpartition in the hierarchy you want to alter.</dd>

<dt>DROP \[DEFAULT\] PARTITION  </dt>
<dd>**Note:** Cannot be used with multi-level partitions.

Drops the specified partition. If the partition has subpartitions, the subpartitions are automatically dropped as well.</dd>

<dt>TRUNCATE \[DEFAULT\] PARTITION  </dt>
<dd>Truncates the specified partition. If the partition has subpartitions, the subpartitions are automatically truncated as well.</dd>

<dt>RENAME \[DEFAULT\] PARTITION  </dt>
<dd>Changes the partition name of a partition (not the relation name). Partitioned tables are created using the naming convention: \<*parentname*\>\_\<*level*\>\_prt\_\<*partition\_name*\>.</dd>

<dt>ADD DEFAULT PARTITION  </dt>
<dd>**Note:** Cannot be used with multi-level partitions.

Adds a default partition to an existing partition design. When data does not match to an existing partition, it is inserted into the default partition. Partition designs that do not have a default partition will reject incoming rows that do not match to an existing partition. Default partitions must be given a name.</dd>

<dt>ADD PARTITION  </dt>
<dd>**Note:** Cannot be used with multi-level partitions.

\<partition\_element\> - Using the existing partition type of the table (range or list), defines the boundaries of new partition you are adding.

\<name\> - A name for this new partition.

**VALUES** - For list partitions, defines the value(s) that the partition will contain.

**START** - For range partitions, defines the starting range value for the partition. By default, start values are `INCLUSIVE`. For example, if you declared a start date of `'2008-01-01'`, then the partition would contain all dates greater than or equal to `'2008-01-01'`. Typically the data type of the `START` expression is the same type as the partition key column. If that is not the case, then you must explicitly cast to the intended data type.

**END** - For range partitions, defines the ending range value for the partition. By default, end values are `EXCLUSIVE`. For example, if you declared an end date of `'2008-02-01'`, then the partition would contain all dates less than but not equal to `'2008-02-01'`. Typically the data type of the `END` expression is the same type as the partition key column. If that is not the case, then you must explicitly cast to the intended data type.

**WITH** - Sets the table storage options for a partition. For example, you may want older partitions to be append-only tables and newer partitions to be regular heap tables. See `CREATE TABLE` for a description of the storage options.

**TABLESPACE** - The name of the tablespace in which the partition is to be created.

\<subpartition\_spec\> - Only allowed on partition designs that were created without a subpartition template. Declares a subpartition specification for the new partition you are adding. If the partitioned table was originally defined using a subpartition template, then the template will be used to generate the subpartitions automatically.</dd>

<dt>EXCHANGE \[DEFAULT\] PARTITION  </dt>
<dd>Exchanges another table into the partition hierarchy into the place of an existing partition. In a multi-level partition design, you can only exchange the lowest level partitions (those that contain data).

**WITH TABLE** \<table\_name\> - The name of the table you are swapping in to the partition design.

**WITH** | **WITHOUT VALIDATION** - Validates that the data in the table matches the `CHECK` constraint of the partition you are exchanging. The default is to validate the data against the `CHECK` constraint.</dd>

<dt>SET SUBPARTITION TEMPLATE  </dt>
<dd>Modifies the subpartition template for an existing partition. After a new subpartition template is set, all new partitions added will have the new subpartition design (existing partitions are not modified).</dd>

<dt>SPLIT DEFAULT PARTITION  </dt>
<dd>**Note:** Cannot be used with multi-level partitions.

Splits a default partition. In a multi-level partition design, you can only split the lowest level default partitions (those that contain data). Splitting a default partition creates a new partition containing the values specified and leaves the default partition containing any values that do not match to an existing partition.

**AT** - For list partitioned tables, specifies a single list value that should be used as the criteria for the split.

**START** - For range partitioned tables, specifies a starting value for the new partition.

**END** - For range partitioned tables, specifies an ending value for the new partition.

**INTO** - Allows you to specify a name for the new partition. When using the `INTO` clause to split a default partition, the second partition name specified should always be that of the existing default partition. If you do not know the name of the default partition, you can look it up using the `pg_partitions` view.</dd>

<dt>SPLIT PARTITION  </dt>
<dd>**Note:** Cannot be used with multi-level partitions.

Splits an existing partition into two partitions. In a multi-level partition design, you can only split the lowest level partitions (those that contain data).

**AT** - Specifies a single value that should be used as the criteria for the split. The partition will be divided into two new partitions with the split value specified being the starting range for the *latter* partition.

**INTO** - Allows you to specify names for the two new partitions created by the split.</dd>

<dt> \<partition\_name\>   </dt>
<dd>The given name of a partition.</dd>

<dt>FOR (RANK(\<number\>))  </dt>
<dd>For range partitions, the rank of the partition in the range.</dd>

<dt>FOR ('\<value\>')  </dt>
<dd>Specifies a partition by declaring a value that falls within the partition boundary specification. If the value declared with `FOR` matches to both a partition and one of its subpartitions (for example, if the value is a date and the table is partitioned by month and then by day), then `FOR` will operate on the first level where a match is found (for example, the monthly partition). If your intent is to operate on a subpartition, you must declare so as follows:

``` pre
ALTER TABLE name ALTER PARTITION FOR ('2008-10-01') DROP PARTITION FOR ('2008-10-01');
```
</dd>

## <a id="notes"></a>Notes

Take special care when altering or dropping columns that are part of the HAWQ distribution key as this can change the distribution policy for the table. HAWQ does not currently support foreign key constraints.

**Note:** Note: The table name specified in the `ALTER TABLE` command cannot be the name of a partition within a table.

Adding a `CHECK` or `NOT NULL` constraint requires scanning the table to verify that existing rows meet the constraint.

When a column is added with `ADD COLUMN`, all existing rows in the table are initialized with the column’s default value (`NULL` if no `DEFAULT` clause is specified). Adding a column with a non-null default or changing the type of an existing column will require the entire table to be rewritten. This may take a significant amount of time for a large table; and it will temporarily require double the disk space.

You can specify multiple changes in a single `ALTER TABLE` command, which will be done in a single pass over the table.

The `DROP COLUMN` form does not physically remove the column, but simply makes it invisible to SQL operations. Subsequent insert operations in the table will store a null value for the column. Thus, dropping a column is quick but it will not immediately reduce the on-disk size of your table, as the space occupied by the dropped column is not reclaimed.

The fact that `ALTER TYPE` requires rewriting the whole table is sometimes an advantage, because the rewriting process eliminates any dead space in the table. For example, to reclaim the space occupied by a dropped column immediately, the fastest way is: `ALTER TABLE <table> ALTER COLUMN <anycol> TYPE <sametype>;` Where \<anycol\> is any remaining table column and \<sametype\> is the same type that column already has. This results in no semantically-visible change in the table, but the command forces rewriting, which gets rid of no-longer-useful data.

If a table is partitioned or has any descendant tables, it is not permitted to add, rename, or change the type of a column in the parent table without doing the same to the descendants. This ensures that the descendants always have columns matching the parent.

A recursive `DROP COLUMN` operation will remove a descendant table’s column only if the descendant does not inherit that column from any other parents and never had an independent definition of the column. A nonrecursive `DROP COLUMN` (`ALTER TABLE ONLY ... DROP COLUMN`) never removes any descendant columns, but instead marks them as independently defined rather than inherited.

The `OWNER` action never recurse to descendant tables; that is, they always act as though `ONLY` were specified. Adding a constraint can recurse only for `CHECK` constraints.

Changing any part of a system catalog table is not permitted.

## <a id="examples"></a>Examples

Add a column to a table:

``` pre
ALTER TABLE distributors ADD COLUMN address varchar(30);
```

Rename an existing column:

``` pre
ALTER TABLE distributors RENAME COLUMN address TO city;
```

Rename an existing table:

``` pre
ALTER TABLE distributors RENAME TO suppliers;
```

Add a not-null constraint to a column:

``` pre
ALTER TABLE distributors ALTER COLUMN street SET NOT NULL;
```

Add a check constraint to a table:

``` pre
ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK (char_length(zipcode) = 5);
```

Move a table to a different schema:

``` pre
ALTER TABLE myschema.distributors SET SCHEMA yourschema;
```

Add a new partition to a partitioned table:

``` pre
ALTER TABLE sales ADD PARTITION
        START (date '2009-02-01') INCLUSIVE 
        END (date '2009-03-01') EXCLUSIVE; 
```

Add a default partition to an existing partition design:

``` pre
ALTER TABLE sales ADD DEFAULT PARTITION other;
```

Rename a partition:

``` pre
ALTER TABLE sales RENAME PARTITION FOR ('2008-01-01') TO jan08;
```

Drop the first (oldest) partition in a range sequence:

``` pre
ALTER TABLE sales DROP PARTITION FOR (RANK(1));
```

Exchange a table into your partition design:

``` pre
ALTER TABLE sales EXCHANGE PARTITION FOR ('2008-01-01') WITH TABLE jan08;
```

Split the default partition (where the existing default partition’s name is `other`) to add a new monthly partition for January 2009:

``` pre
ALTER TABLE sales SPLIT DEFAULT PARTITION
    START ('2009-01-01') INCLUSIVE
    END ('2009-02-01') EXCLUSIVE
    INTO (PARTITION jan09, PARTITION other);
```

Split a monthly partition into two with the first partition containing dates January 1-15 and the second partition containing dates January 16-31:

``` pre
ALTER TABLE sales SPLIT PARTITION FOR ('2008-01-01')
    AT ('2008-01-16')
    INTO (PARTITION jan081to15, PARTITION jan0816to31);
```

## <a id="compat"></a>Compatibility

The `ADD`, `DROP`, and `SET DEFAULT` forms conform with the SQL standard. The other forms are HAWQ extensions of the SQL standard. Also, the ability to specify more than one manipulation in a single `ALTER                TABLE` command is an extension. `ALTER TABLE DROP COLUMN` can be used to drop the only column of a table, leaving a zero-column table. This is an extension of SQL, which disallows zero-column tables.

## <a id="altertable__section8"></a>See Also

[CREATE TABLE](CREATE-TABLE.html), [DROP TABLE](DROP-TABLE.html)
