---
title: Partitioning Large Tables
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

Table partitioning enables supporting very large tables, such as fact tables, by logically dividing them into smaller, more manageable pieces. Partitioned tables can improve query performance by allowing the HAWQ query optimizer to scan only the data needed to satisfy a given query instead of scanning all the contents of a large table.

Partitioning does not change the physical distribution of table data across the segments. Table distribution is physical: HAWQ physically divides partitioned tables and non-partitioned tables across segments to enable parallel query processing. Table *partitioning* is logical: HAWQ logically divides big tables to improve query performance and facilitate data warehouse maintenance tasks, such as rolling old data out of the data warehouse.

HAWQ supports:

-   *range partitioning*: division of data based on a numerical range, such as date or price.
-   *list partitioning*: division of data based on a list of values, such as sales territory or product line.
-   A combination of both types.
<a id="im207241"></a>

![](../images/partitions.jpg "Example Multi-level Partition Design")

## <a id="topic64"></a>Table Partitioning in HAWQ 

HAWQ divides tables into parts \(also known as partitions\) to enable massively parallel processing. Tables are partitioned during `CREATE TABLE` using the `PARTITION BY` \(and optionally the `SUBPARTITION BY`\) clause. Partitioning creates a top-level \(or parent\) table with one or more levels of sub-tables \(or child tables\). Internally, HAWQ creates an inheritance relationship between the top-level table and its underlying partitions, similar to the functionality of the `INHERITS` clause of PostgreSQL.

HAWQ uses the partition criteria defined during table creation to create each partition with a distinct `CHECK` constraint, which limits the data that table can contain. The query optimizer uses `CHECK` constraints to determine which table partitions to scan to satisfy a given query predicate.

The HAWQ system catalog stores partition hierarchy information so that rows inserted into the top-level parent table propagate correctly to the child table partitions. To change the partition design or table structure, alter the parent table using `ALTER TABLE` with the `PARTITION` clause.

To insert data into a partitioned table, you specify the root partitioned table, the table created with the `CREATE TABLE` command. You also can specify a leaf child table of the partitioned table in an `INSERT` command. An error is returned if the data is not valid for the specified leaf child table. Specifying a child table that is not a leaf child table in the `INSERT` command is not supported.

## <a id="topic65"></a>Deciding on a Table Partitioning Strategy 

Not all tables are good candidates for partitioning. If the answer is *yes* to all or most of the following questions, table partitioning is a viable database design strategy for improving query performance. If the answer is *no* to most of the following questions, table partitioning is not the right solution for that table. Test your design strategy to ensure that query performance improves as expected.

-   **Is the table large enough?** Large fact tables are good candidates for table partitioning. If you have millions or billions of records in a table, you may see performance benefits from logically breaking that data up into smaller chunks. For smaller tables with only a few thousand rows or less, the administrative overhead of maintaining the partitions will outweigh any performance benefits you might see.
-   **Are you experiencing unsatisfactory performance?** As with any performance tuning initiative, a table should be partitioned only if queries against that table are producing slower response times than desired.
-   **Do your query predicates have identifiable access patterns?** Examine the `WHERE` clauses of your query workload and look for table columns that are consistently used to access data. For example, if most of your queries tend to look up records by date, then a monthly or weekly date-partitioning design might be beneficial. Or if you tend to access records by region, consider a list-partitioning design to divide the table by region.
-   **Does your data warehouse maintain a window of historical data?** Another consideration for partition design is your organization's business requirements for maintaining historical data. For example, your data warehouse may require that you keep data for the past twelve months. If the data is partitioned by month, you can easily drop the oldest monthly partition from the warehouse and load current data into the most recent monthly partition.
-   **Can the data be divided into somewhat equal parts based on some defining criteria?** Choose partitioning criteria that will divide your data as evenly as possible. If the partitions contain a relatively equal number of records, query performance improves based on the number of partitions created. For example, by dividing a large table into 10 partitions, a query will execute 10 times faster than it would against the unpartitioned table, provided that the partitions are designed to support the query's criteria.

Do not create more partitions than are needed. Creating too many partitions can slow down management and maintenance jobs, such as vacuuming, recovering segments, expanding the cluster, checking disk usage, and others.

Partitioning does not improve query performance unless the query optimizer can eliminate partitions based on the query predicates. Queries that scan every partition run slower than if the table were not partitioned, so avoid partitioning if few of your queries achieve partition elimination. Check the explain plan for queries to make sure that partitions are eliminated. See [Query Profiling](../query/query-profiling.html) for more about partition elimination.

Be very careful with multi-level partitioning because the number of partition files can grow very quickly. For example, if a table is partitioned by both day and city, and there are 1,000 days of data and 1,000 cities, the total number of partitions is one million. Column-oriented tables store each column in a physical table, so if this table has 100 columns, the system would be required to manage 100 million files for the table.

Before settling on a multi-level partitioning strategy, consider a single level partition with bitmap indexes. Indexes slow down data loads, so consider performance testing with your data and schema to decide on the best strategy.

## <a id="topic66"></a>Creating Partitioned Tables 

You partition tables when you create them with `CREATE TABLE`. This topic provides examples of SQL syntax for creating a table with various partition designs.

To partition a table:

1.  Decide on the partition design: date range, numeric range, or list of values.
2.  Choose the column\(s\) on which to partition the table.
3.  Decide how many levels of partitions you want. For example, you can create a date range partition table by month and then subpartition the monthly partitions by sales region.

-   [Defining Date Range Table Partitions](#topic67)
-   [Defining Numeric Range Table Partitions](#topic68)
-   [Defining List Table Partitions](#topic69)
-   [Defining Multi-level Partitions](#topic70)
-   [Partitioning an Existing Table](#topic71)

### <a id="topic67"></a>Defining Date Range Table Partitions 

A date range partitioned table uses a single `date` or `timestamp` column as the partition key column. You can use the same partition key column to create subpartitions if necessary, for example, to partition by month and then subpartition by day. Consider partitioning by the most granular level. For example, for a table partitioned by date, you can partition by day and have 365 daily partitions, rather than partition by year then subpartition by month then subpartition by day. A multi-level design can reduce query planning time, but a flat partition design runs faster.

You can have HAWQ automatically generate partitions by giving a `START` value, an `END` value, and an `EVERY` clause that defines the partition increment value. By default, `START` values are always inclusive and `END` values are always exclusive. For example:

``` sql
CREATE TABLE sales (id int, date date, amt decimal(10,2))
DISTRIBUTED BY (id)
PARTITION BY RANGE (date)
( START (date '2008-01-01') INCLUSIVE
   END (date '2009-01-01') EXCLUSIVE
   EVERY (INTERVAL '1 day') );
```

You can also declare and name each partition individually. For example:

``` sql
CREATE TABLE sales (id int, date date, amt decimal(10,2))
DISTRIBUTED BY (id)
PARTITION BY RANGE (date)
( PARTITION Jan08 START (date '2008-01-01') INCLUSIVE ,
  PARTITION Feb08 START (date '2008-02-01') INCLUSIVE ,
  PARTITION Mar08 START (date '2008-03-01') INCLUSIVE ,
  PARTITION Apr08 START (date '2008-04-01') INCLUSIVE ,
  PARTITION May08 START (date '2008-05-01') INCLUSIVE ,
  PARTITION Jun08 START (date '2008-06-01') INCLUSIVE ,
  PARTITION Jul08 START (date '2008-07-01') INCLUSIVE ,
  PARTITION Aug08 START (date '2008-08-01') INCLUSIVE ,
  PARTITION Sep08 START (date '2008-09-01') INCLUSIVE ,
  PARTITION Oct08 START (date '2008-10-01') INCLUSIVE ,
  PARTITION Nov08 START (date '2008-11-01') INCLUSIVE ,
  PARTITION Dec08 START (date '2008-12-01') INCLUSIVE
                  END (date '2009-01-01') EXCLUSIVE );
```

You do not have to declare an `END` value for each partition, only the last one. In this example, `Jan08` ends where `Feb08` starts.

### <a id="topic68"></a>Defining Numeric Range Table Partitions 

A numeric range partitioned table uses a single numeric data type column as the partition key column. For example:

``` sql
CREATE TABLE rank (id int, rank int, year int, gender
char(1), count int)
DISTRIBUTED BY (id)
PARTITION BY RANGE (year)
( START (2001) END (2008) EVERY (1),
  DEFAULT PARTITION extra );
```

For more information about default partitions, see [Adding a Default Partition](#topic80).

### <a id="topic69"></a>Defining List Table Partitions 

A list partitioned table can use any data type column that allows equality comparisons as its partition key column. A list partition can also have a multi-column \(composite\) partition key, whereas a range partition only allows a single column as the partition key. For list partitions, you must declare a partition specification for every partition \(list value\) you want to create. For example:

``` sql
CREATE TABLE rank (id int, rank int, year int, gender
char(1), count int )
DISTRIBUTED BY (id)
PARTITION BY LIST (gender)
( PARTITION girls VALUES ('F'),
  PARTITION boys VALUES ('M'),
  DEFAULT PARTITION other );
```

**Note:** The HAWQ legacy optimizer allows list partitions with multi-column \(composite\) partition keys. A range partition only allows a single column as the partition key. GPORCA does not support composite keys.

For more information about default partitions, see [Adding a Default Partition](#topic80).

### <a id="topic70"></a>Defining Multi-level Partitions 

You can create a multi-level partition design with subpartitions of partitions. Using a *subpartition template* ensures that every partition has the same subpartition design, including partitions that you add later. For example, the following SQL creates the two-level partition design shown in [Figure 1](#im207241):

``` sql
CREATE TABLE sales (trans_id int, date date, amount
decimal(9,2), region text)
DISTRIBUTED BY (trans_id)
PARTITION BY RANGE (date)
SUBPARTITION BY LIST (region)
SUBPARTITION TEMPLATE
( SUBPARTITION usa VALUES ('usa'),
  SUBPARTITION asia VALUES ('asia'),
  SUBPARTITION europe VALUES ('europe'),
  DEFAULT SUBPARTITION other_regions)
  (START (date '2011-01-01') INCLUSIVE
   END (date '2012-01-01') EXCLUSIVE
   EVERY (INTERVAL '1 month'),
   DEFAULT PARTITION outlying_dates );
```

The following example shows a three-level partition design where the `sales` table is partitioned by `year`, then `month`, then `region`. The `SUBPARTITION TEMPLATE` clauses ensure that each yearly partition has the same subpartition structure. The example declares a `DEFAULT` partition at each level of the hierarchy.

``` sql
CREATE TABLE p3_sales (id int, year int, month int, day int,
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
               DEFAULT SUBPARTITION other_regions )
( START (2002) END (2012) EVERY (1),
  DEFAULT PARTITION outlying_years );
```

**CAUTION**:

When you create multi-level partitions on ranges, it is easy to create a large number of subpartitions, some containing little or no data. This can add many entries to the system tables, which increases the time and memory required to optimize and execute queries. Increase the range interval or choose a different partitioning strategy to reduce the number of subpartitions created.

### <a id="topic71"></a>Partitioning an Existing Table 

Tables can be partitioned only at creation. If you have a table that you want to partition, you must create a partitioned table, load the data from the original table into the new table, drop the original table, and rename the partitioned table with the original table's name. You must also re-grant any table permissions. For example:

``` sql
CREATE TABLE sales2 (LIKE sales)
PARTITION BY RANGE (date)
( START (date '2008-01-01') INCLUSIVE
   END (date '2009-01-01') EXCLUSIVE
   EVERY (INTERVAL '1 month') );
INSERT INTO sales2 SELECT * FROM sales;
DROP TABLE sales;
ALTER TABLE sales2 RENAME TO sales;
GRANT ALL PRIVILEGES ON sales TO admin;
GRANT SELECT ON sales TO guest;
```

## <a id="topic73"></a>Loading Partitioned Tables 

After you create the partitioned table structure, top-level parent tables are empty. Data is routed to the bottom-level child table partitions. In a multi-level partition design, only the subpartitions at the bottom of the hierarchy can contain data.

Rows that cannot be mapped to a child table partition are rejected and the load fails. To avoid unmapped rows being rejected at load time, define your partition hierarchy with a `DEFAULT` partition. Any rows that do not match a partition's `CHECK` constraints load into the `DEFAULT` partition. See [Adding a Default Partition](#topic80).

At runtime, the query optimizer scans the entire table inheritance hierarchy and uses the `CHECK` table constraints to determine which of the child table partitions to scan to satisfy the query's conditions. The `DEFAULT` partition \(if your hierarchy has one\) is always scanned. `DEFAULT` partitions that contain data slow down the overall scan time.

When you use `COPY` or `INSERT` to load data into a parent table, the data is automatically rerouted to the correct partition, just like a regular table.

Best practice for loading data into partitioned tables is to create an intermediate staging table, load it, and then exchange it into your partition design. See [Exchanging a Partition](#topic83).

## <a id="topic74"></a>Verifying Your Partition Strategy 

When a table is partitioned based on the query predicate, you can use `EXPLAIN` to verify that the query optimizer scans only the relevant data to examine the query plan.

For example, suppose a *sales* table is date-range partitioned by month and subpartitioned by region as shown in [Figure 1](#im207241). For the following query:

``` sql
EXPLAIN SELECT * FROM sales WHERE date='01-07-12' AND
region='usa';
```

The query plan for this query should show a table scan of only the following tables:

-   the default partition returning 0-1 rows \(if your partition design has one\)
-   the January 2012 partition \(*sales\_1\_prt\_1*\) returning 0-1 rows
-   the USA region subpartition \(*sales\_1\_2\_prt\_usa*\) returning *some number* of rows.

The following example shows the relevant portion of the query plan.

``` pre
->  `Seq Scan on``sales_1_prt_1` sales (cost=0.00..0.00 `rows=0`
     width=0)
Filter: "date"=01-07-08::date AND region='USA'::text
->  `Seq Scan on``sales_1_2_prt_usa` sales (cost=0.00..9.87
`rows=20`
      width=40)
```

Ensure that the query optimizer does not scan unnecessary partitions or subpartitions \(for example, scans of months or regions not specified in the query predicate\), and that scans of the top-level tables return 0-1 rows.

### <a id="topic75"></a>Troubleshooting Selective Partition Scanning 

The following limitations can result in a query plan that shows a non-selective scan of your partition hierarchy.

-   The query optimizer can selectively scan partitioned tables only when the query contains a direct and simple restriction of the table using immutable operators such as:

    =, < , <= , \>,  \>= , and <\>

-   Selective scanning recognizes `STABLE` and `IMMUTABLE` functions, but does not recognize `VOLATILE` functions within a query. For example, `WHERE` clauses such as `date > CURRENT_DATE` cause the query optimizer to selectively scan partitioned tables, but `time > TIMEOFDAY` does not.

## <a id="topic76"></a>Viewing Your Partition Design 

You can look up information about your partition design using the *pg\_partitions* view. For example, to see the partition design of the *sales* table:

``` sql
SELECT partitionboundary, partitiontablename, partitionname,
partitionlevel, partitionrank
FROM pg_partitions
WHERE tablename='sales';
```

The following table and views show information about partitioned tables.

-   *pg\_partition* - Tracks partitioned tables and their inheritance level relationships.
-   *pg\_partition\_templates* - Shows the subpartitions created using a subpartition template.
-   *pg\_partition\_columns* - Shows the partition key columns used in a partition design.

## <a id="topic77"></a>Maintaining Partitioned Tables 

To maintain a partitioned table, use the `ALTER TABLE` command against the top-level parent table. The most common scenario is to drop old partitions and add new ones to maintain a rolling window of data in a range partition design. If you have a default partition in your partition design, you add a partition by *splitting* the default partition.

-   [Adding a Partition](#topic78)
-   [Renaming a Partition](#topic79)
-   [Adding a Default Partition](#topic80)
-   [Dropping a Partition](#topic81)
-   [Truncating a Partition](#topic82)
-   [Exchanging a Partition](#topic83)
-   [Splitting a Partition](#topic84)
-   [Modifying a Subpartition Template](#topic85)

**Note:** When using multi-level partition designs, the following operations are not supported with ALTER TABLE:

-   ADD DEFAULT PARTITION
-   ADD PARTITION
-   DROP DEFAULT PARTITION
-   DROP PARTITION
-   SPLIT PARTITION
-   All operations that involve modifying subpartitions.

**Important:** When defining and altering partition designs, use the given partition name, not the table object name. Although you can query and load any table \(including partitioned tables\) directly using SQL commands, you can only modify the structure of a partitioned table using the `ALTER TABLE...PARTITION` clauses.

Partitions are not required to have names. If a partition does not have a name, use one of the following expressions to specify a part: `PARTITION FOR (value)` or \)`PARTITION FOR(RANK(number)`.

### <a id="topic78"></a>Adding a Partition 

You can add a partition to a partition design with the `ALTER TABLE` command. If the original partition design included subpartitions defined by a *subpartition template*, the newly added partition is subpartitioned according to that template. For example:

``` sql
ALTER TABLE sales ADD PARTITION
    START (date '2009-02-01') INCLUSIVE
    END (date '2009-03-01') EXCLUSIVE;
```

If you did not use a subpartition template when you created the table, you define subpartitions when adding a partition:

``` sql
ALTER TABLE sales ADD PARTITION
    START (date '2009-02-01') INCLUSIVE
    END (date '2009-03-01') EXCLUSIVE
     ( SUBPARTITION usa VALUES ('usa'),
       SUBPARTITION asia VALUES ('asia'),
       SUBPARTITION europe VALUES ('europe') );
```

When you add a subpartition to an existing partition, you can specify the partition to alter. For example:

``` sql
ALTER TABLE sales ALTER PARTITION FOR (RANK(12))
      ADD PARTITION africa VALUES ('africa');
```

**Note:** You cannot add a partition to a partition design that has a default partition. You must split the default partition to add a partition. See [Splitting a Partition](#topic84).

### <a id="topic79"></a>Renaming a Partition 

Partitioned tables use the following naming convention. Partitioned subtable names are subject to uniqueness requirements and length limitations.

<pre><code><i>&lt;parentname&gt;</i>_<i>&lt;level&gt;</i>_prt_<i>&lt;partition_name&gt;</i></code></pre>

For example:

```
sales_1_prt_jan08
```

For auto-generated range partitions, where a number is assigned when no name is given\):

```
sales_1_prt_1
```

To rename a partitioned child table, rename the top-level parent table. The *&lt;parentname&gt;* changes in the table names of all associated child table partitions. For example, the following command:

``` sql
ALTER TABLE sales RENAME TO globalsales;
```

Changes the associated table names:

```
globalsales_1_prt_1
```

You can change the name of a partition to make it easier to identify. For example:

``` sql
ALTER TABLE sales RENAME PARTITION FOR ('2008-01-01') TO jan08;
```

Changes the associated table name as follows:

```
sales_1_prt_jan08
```

When altering partitioned tables with the `ALTER TABLE` command, always refer to the tables by their partition name \(*jan08*\) and not their full table name \(*sales\_1\_prt\_jan08*\).

**Note:** The table name cannot be a partition name in an `ALTER TABLE` statement. For example, `ALTER TABLE sales...` is correct, `ALTER TABLE sales_1_part_jan08...` is not allowed.

### <a id="topic80"></a>Adding a Default Partition 

You can add a default partition to a partition design with the `ALTER TABLE` command.

``` sql
ALTER TABLE sales ADD DEFAULT PARTITION other;
```

If incoming data does not match a partition's `CHECK` constraint and there is no default partition, the data is rejected. Default partitions ensure that incoming data that does not match a partition is inserted into the default partition.

### <a id="topic81"></a>Dropping a Partition 

You can drop a partition from your partition design using the `ALTER TABLE` command. When you drop a partition that has subpartitions, the subpartitions \(and all data in them\) are automatically dropped as well. For range partitions, it is common to drop the older partitions from the range as old data is rolled out of the data warehouse. For example:

``` sql
ALTER TABLE sales DROP PARTITION FOR (RANK(1));
```

### <a id="topic_enm_vrk_kv"></a>Sorting AORO Partitioned Tables 

HDFS read access for large numbers of append-only, row-oriented \(AORO\) tables with large numbers of partitions can be tuned by using the `optimizer_parts_to_force_sort_on_insert` parameter to control how HDFS opens files. This parameter controls the way the optimizer sorts tuples during INSERT operations, to maximize HDFS performance.

The user-tunable parameter `optimizer_parts_to_force_sort_on_insert` can force the GPORCA query optimizer to generate a plan for sorting tuples during insertion into an append-only, row-oriented \(AORO\) partitioned tables. Sorting the insert tuples reduces the number of partition switches, thus improving the overall INSERT performance. For a given AORO table, if its number of leaf-partitioned tables is greater than or equal to the number specified in `optimizer_parts_to_force_sort_on_insert`, the plan generated by the GPORCA will sort inserts by their partition IDs before performing the INSERT operation. Otherwise, the inserts are not sorted. The default value for `optimizer_parts_to_force_sort_on_insert` is 160.

### <a id="topic82"></a>Truncating a Partition 

You can truncate a partition using the `ALTER TABLE` command. When you truncate a partition that has subpartitions, the subpartitions are automatically truncated as well.

``` sql
ALTER TABLE sales TRUNCATE PARTITION FOR (RANK(1));
```

### <a id="topic83"></a>Exchanging a Partition 

You can exchange a partition using the `ALTER TABLE` command. Exchanging a partition swaps one table in place of an existing partition. You can exchange partitions only at the lowest level of your partition hierarchy \(only partitions that contain data can be exchanged\).

Partition exchange can be useful for data loading. For example, load a staging table and swap the loaded table into your partition design. You can use partition exchange to change the storage type of older partitions to append-only tables. For example:

``` sql
CREATE TABLE jan12 (LIKE sales) WITH (appendonly=true);
INSERT INTO jan12 SELECT * FROM sales_1_prt_1 ;
ALTER TABLE sales EXCHANGE PARTITION FOR (DATE '2012-01-01')
WITH TABLE jan12;
```

**Note:** This example refers to the single-level definition of the table `sales`, before partitions were added and altered in the previous examples.

### <a id="topic84"></a>Splitting a Partition 

Splitting a partition divides a partition into two partitions. You can split a partition using the `ALTER TABLE` command. You can split partitions only at the lowest level of your partition hierarchy: only partitions that contain data can be split. The split value you specify goes into the *latter* partition.

For example, to split a monthly partition into two with the first partition containing dates January 1-15 and the second partition containing dates January 16-31:

``` sql
ALTER TABLE sales SPLIT PARTITION FOR ('2008-01-01')
AT ('2008-01-16')
INTO (PARTITION jan081to15, PARTITION jan0816to31);
```

If your partition design has a default partition, you must split the default partition to add a partition.

When using the `INTO` clause, specify the current default partition as the second partition name. For example, to split a default range partition to add a new monthly partition for January 2009:

``` sql
ALTER TABLE sales SPLIT DEFAULT PARTITION
START ('2009-01-01') INCLUSIVE
END ('2009-02-01') EXCLUSIVE
INTO (PARTITION jan09, default partition);
```

### <a id="topic85"></a>Modifying a Subpartition Template 

Use `ALTER TABLE` SET SUBPARTITION TEMPLATE to modify the subpartition template of a partitioned table. Partitions added after you set a new subpartition template have the new partition design. Existing partitions are not modified.

The following example alters the subpartition template of this partitioned table:

``` sql
CREATE TABLE sales (trans_id int, date date, amount decimal(9,2), region text)
  DISTRIBUTED BY (trans_id)
  PARTITION BY RANGE (date)
  SUBPARTITION BY LIST (region)
  SUBPARTITION TEMPLATE
    ( SUBPARTITION usa VALUES ('usa'),
      SUBPARTITION asia VALUES ('asia'),
      SUBPARTITION europe VALUES ('europe'),
      DEFAULT SUBPARTITION other_regions )
  ( START (date '2014-01-01') INCLUSIVE
    END (date '2014-04-01') EXCLUSIVE
    EVERY (INTERVAL '1 month') );
```

This `ALTER TABLE` command, modifies the subpartition template.

``` sql
ALTER TABLE sales SET SUBPARTITION TEMPLATE
( SUBPARTITION usa VALUES ('usa'),
  SUBPARTITION asia VALUES ('asia'),
  SUBPARTITION europe VALUES ('europe'),
  SUBPARTITION africa VALUES ('africa'),
  DEFAULT SUBPARTITION regions );
```

When you add a date-range partition of the table sales, it includes the new regional list subpartition for Africa. For example, the following command creates the subpartitions `usa`, `asia`, `europe`, `africa`, and a default partition named `other`:

``` sql
ALTER TABLE sales ADD PARTITION "4"
  START ('2014-04-01') INCLUSIVE
  END ('2014-05-01') EXCLUSIVE ;
```

To view the tables created for the partitioned table `sales`, you can use the command `\dt sales*` from the psql command line.

To remove a subpartition template, use `SET SUBPARTITION TEMPLATE` with empty parentheses. For example, to clear the sales table subpartition template:

``` sql
ALTER TABLE sales SET SUBPARTITION TEMPLATE ();
```
