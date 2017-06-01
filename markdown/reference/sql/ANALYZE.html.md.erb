---
title: ANALYZE
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

Collects statistics about a database.

## <a id="synopsis"></a>Synopsis

``` pre
ANALYZE [VERBOSE] [ROOTPARTITION] <table> [ (<column> [, ...] ) ]]
```

## <a id="desc"></a>Description

`ANALYZE` collects statistics about the contents of tables in the database, and stores the results in the system table `pg_statistic`. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries.

With no parameter, `ANALYZE` examines every table in the current database. With a parameter, `ANALYZE` examines only that table. It is further possible to give a list of column names, in which case only the statistics for those columns are collected.

## <a id="params"></a>Parameters

<dt>VERBOSE  </dt>
<dd>Enables display of progress messages. When specified, `ANALYZE` emits progress messages to indicate which table is currently being processed. Various statistics about the tables are printed as well.</dd>

<dt>ROOTPARTITION  </dt>
<dd>For partitioned tables, `ANALYZE` on the parent (the root in multi-level partitioning) table without this option will collect statistics on each individual leaf partition as well as the global partition table, both of which are needed for query planning. In scenarios when all the individual child partitions have up-to-date statistics (for example, after loading and analyzing a daily partition), the `ROOTPARTITION` option can be used to collect only the global stats on the partition table. This could save the time of re-analyzing each individual leaf partition.

If you use `ROOTPARTITION` on a non-root or non-partitioned table, `ANALYZE` will skip the option and issue a warning. You can also analyze all root partition tables in the database by using `ROOTPARTITION ALL`

**Note:** Use `ROOTPARTITION ALL` to analyze all root partition tables in the database.</dd>

<dt> \<table\>   </dt>
<dd>The name (possibly schema-qualified) of a specific table to analyze. Defaults to all tables in the current database.</dd>

<dt> \<column\>   </dt>
<dd>The name of a specific column to analyze. Defaults to all columns.</dd>

## <a id="notes"></a>Notes

It is a good idea to run `ANALYZE` periodically, or just after making major changes in the contents of a table. Accurate statistics will help the query planner to choose the most appropriate query plan, and thereby improve the speed of query processing. A common strategy is to run `VACUUM` and `ANALYZE` once a day during a low-usage time of day.

`ANALYZE` requires only a read lock on the target table, so it can run in parallel with other activity on the table.

`ANALYZE` skips tables if the user is not the table owner or database owner.

The statistics collected by `ANALYZE` usually include a list of some of the most common values in each column and a histogram showing the approximate data distribution in each column. One or both of these may be omitted if `ANALYZE` deems them uninteresting (for example, in a unique-key column, there are no common values) or if the column data type does not support the appropriate operators.

For large tables, `ANALYZE` takes a random sample of the table contents, rather than examining every row. This allows even very large tables to be analyzed in a small amount of time. Note, however, that the statistics are only approximate, and will change slightly each time `ANALYZE` is run, even if the actual table contents did not change. This may result in small changes in the planner’s estimated costs shown by `EXPLAIN`. In rare situations, this non-determinism will cause the query optimizer to choose a different query plan between runs of `ANALYZE`. To avoid this, raise the amount of statistics collected by `ANALYZE` by adjusting the `default_statistics_target` configuration parameter, or on a column-by-column basis by setting the per-column statistics target with `ALTER                TABLE ... ALTER COLUMN ... SET STATISTICS` (see `ALTER             TABLE`). The target value sets the maximum number of entries in the most-common-value list and the maximum number of bins in the histogram. The default target value is 10, but this can be adjusted up or down to trade off accuracy of planner estimates against the time taken for `ANALYZE` and the amount of space occupied in `pg_statistic`. In particular, setting the statistics target to zero disables collection of statistics for that column. It may be useful to do that for columns that are never used as part of the `WHERE`, `GROUP                BY`, or `ORDER BY` clauses of queries, since the planner will have no use for statistics on such columns.

The largest statistics target among the columns being analyzed determines the number of table rows sampled to prepare the statistics. Increasing the target causes a proportional increase in the time and space needed to do `ANALYZE`.

The `pxf_enable_stat_collection` server configuration parameter determines if `ANALYZE` calculates statistics for PXF readable external tables. When `pxf_enable_stat_collection` is true, the default setting, `ANALYZE` estimates the number of tuples in the table from the total size of the table, the size of the first fragment, and the number of tuples in the first fragment. Then it builds a sample table and calculates statistics for the PXF table by running statistics queries on the sample table, the same as it does with native tables. A sample table is always created to calculate PXF table statistics, even when the table has a small number of rows.

The `pxf_stat_max_fragments` configuration parameter, default 100, sets the maximum number of fragments that are sampled to build the sample table. Setting `pxf_stat_max_fragments` to a higher value provides a more uniform sample, but decreases `ANALYZE` performance. Setting it to a lower value increases performance, but the statistics are calculated on a less uniform sample.

When `pxf_stat_max_fragments` is false, `ANALYZE` outputs a message to warn that it is skipping the analyze operation on the PXF table because `pxf_stat_max_fragments` is turned off.

There may be situations where the remote statistics retrieval could fail to perform a task on a PXF table. For example, if a PXF Java component is down, the remote statistics retrieval might not occur, and the database transaction would not succeed. In these cases, the statistics remain with the default external table values.

**Note**: The `ANALYZE` command is not supported on PXF external tables created with the `HBase` or `Json` profiles.

## <a id="examples"></a>Examples

Collect statistics for the table `mytable`:

``` pre
ANALYZE mytable;
```

## <a id="compat"></a>Compatibility

There is no ANALYZE statement in the SQL standard.

## <a id="see"></a>See Also

[ALTER TABLE](ALTER-TABLE.html), [EXPLAIN](EXPLAIN.html), [VACUUM](VACUUM.html)


