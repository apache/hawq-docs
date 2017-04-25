---
title: About Database Statistics
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

## <a id="overview"></a>Overview

Statistics are metadata that describe the data stored in the database. The query optimizer needs up-to-date statistics to choose the best execution plan for a query. For example, if a query joins two tables and one of them must be broadcast to all segments, the optimizer can choose the smaller of the two tables to minimize network traffic.

The statistics used by the optimizer are calculated and saved in the system catalog by the `ANALYZE` command. There are three ways to initiate an analyze operation:

-   You can run the `ANALYZE` command directly.
-   You can run the `analyzedb` management utility outside of the database, at the command line.
-   An automatic analyze operation can be triggered when DML operations are performed on tables that have no statistics or when a DML operation modifies a number of rows greater than a specified threshold.

These methods are described in the following sections.

Calculating statistics consumes time and resources, so HAWQ produces estimates by calculating statistics on samples of large tables. In most cases, the default settings provide the information needed to generate correct execution plans for queries. If the statistics produced are not producing optimal query execution plans, the administrator can tune configuration parameters to produce more accurate stastistics by increasing the sample size or the granularity of statistics saved in the system catalog. Producing more accurate statistics has CPU and storage costs and may not produce better plans, so it is important to view explain plans and test query performance to ensure that the additional statistics-related costs result in better query performance.

## <a id="topic_oq3_qxj_3s"></a>System Statistics

### <a id="tablesize"></a>Table Size

The query planner seeks to minimize the disk I/O and network traffic required to execute a query, using estimates of the number of rows that must be processed and the number of disk pages the query must access. The data from which these estimates are derived are the `pg_class` system table columns `reltuples` and `relpages`, which contain the number of rows and pages at the time a `VACUUM` or `ANALYZE` command was last run. As rows are added, the numbers become less accurate. However, an accurate count of disk pages is always available from the operating system, so as long as the ratio of `reltuples` to `relpages` does not change significantly, the optimizer can produce an estimate of the number of rows that is sufficiently accurate to choose the correct query execution plan.

In append-optimized tables, the number of tuples is kept up-to-date in the system catalogs, so the `reltuples` statistic is not an estimate. Non-visible tuples in the table are subtracted from the total. The `relpages` value is estimated from the append-optimized block sizes.

When the `reltuples` column differs significantly from the row count returned by `SELECT COUNT(*)`, an analyze should be performed to update the statistics.

### <a id="views"></a>The pg\_statistic System Table and pg\_stats View

The `pg_statistic` system table holds the results of the last `ANALYZE` operation on each database table. There is a row for each column of every table. It has the following columns:

starelid  
The object ID of the table or index the column belongs to.

staatnum  
The number of the described column, beginning with 1.

stanullfrac  
The fraction of the column's entries that are null.

stawidth  
The average stored width, in bytes, of non-null entries.

stadistinct  
The number of distinct nonnull data values in the column.

stakind*N*  
A code number indicating the kind of statistics stored in the *N*th slot of the `pg_statistic` row.

staop*N*  
An operator used to derive the statistics stored in the *N*th slot.

stanumbers*N*  
Numerical statistics of the appropriate kind for the *N*th slot, or NULL if the slot kind does not involve numerical values.

stavalues*N*  
Column data values of the appropriate kind for the *N*th slot, or NULL if the slot kind does not store any data values.

The statistics collected for a column vary for different data types, so the `pg_statistic` table stores statistics that are appropriate for the data type in four *slots*, consisting of four columns per slot. For example, the first slot, which normally contains the most common values for a column, consists of the columns `stakind1`, `staop1`, `stanumbers1`, and `stavalues1`. Also see [pg\_statistic](../reference/catalog/pg_statistic.html#topic1).

The `stakindN` columns each contain a numeric code to describe the type of statistics stored in their slot. The `stakind` code numbers from 1 to 99 are reserved for core PostgreSQL data types. HAWQ uses code numbers 1, 2, and 3. A value of 0 means the slot is unused. The following table describes the kinds of statistics stored for the three codes.

<a id="topic_oq3_qxj_3s__table_upf_1yc_nt"></a>

<table>
<caption><span class="tablecap">Table 1. Contents of pg_statistic &quot;slots&quot;</span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>stakind Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><em>Most CommonValues (MCV) Slot</em>
<ul>
<li><code class="ph codeph">staop</code> contains the object ID of the &quot;=&quot; operator, used to decide whether values are the same or not.</li>
<li><code class="ph codeph">stavalues</code> contains an array of the <em>K</em> most common non-null values appearing in the column.</li>
<li><code class="ph codeph">stanumbers</code> contains the frequencies (fractions of total row count) of the values in the <code class="ph codeph">stavalues</code> array.</li>
</ul>
The values are ordered in decreasing frequency. Since the arrays are variable-size, <em>K</em> can be chosen by the statistics collector. Values must occur more than once to be added to the <code class="ph codeph">stavalues</code> array; a unique column has no MCV slot.</td>
</tr>
<tr class="even">
<td>2</td>
<td><em>Histogram Slot</em> – describes the distribution of scalar data.
<ul>
<li><code class="ph codeph">staop</code> is the object ID of the &quot;&lt;&quot; operator, which describes the sort ordering.</li>
<li><code class="ph codeph">stavalues</code> contains <em>M</em> (where <em>M</em>&gt;=2) non-null values that divide the non-null column data values into <em>M</em>-1 bins of approximately equal population. The first <code class="ph codeph">stavalues</code> item is the minimum value and the last is the maximum value.</li>
<li><code class="ph codeph">stanumbers</code> is not used and should be null.</li>
</ul>
<p>If a Most Common Values slot is also provided, then the histogram describes the data distribution after removing the values listed in the MCV array. (It is a <em>compressed histogram</em> in the technical parlance). This allows a more accurate representation of the distribution of a column with some very common values. In a column with only a few distinct values, it is possible that the MCV list describes the entire data population; in this case the histogram reduces to empty and should be omitted.</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td><em>Correlation Slot</em> – describes the correlation between the physical order of table tuples and the ordering of data values of this column.
<ul>
<li><code class="ph codeph">staop</code> is the object ID of the &quot;&lt;&quot; operator. As with the histogram, more than one entry could theoretically appear.</li>
<li><code class="ph codeph">stavalues</code> is not used and should be NULL.</li>
<li><code class="ph codeph">stanumbers</code> contains a single entry, the correlation coefficient between the sequence of data values and the sequence of their actual tuple positions. The coefficient ranges from +1 to -1.</li>
</ul></td>
</tr>
</tbody>
</table>

The `pg_stats` view presents the contents of `pg_statistic` in a friendlier format. For more information, see [pg\_stats](../reference/catalog/pg_stats.html#topic1).

Newly created tables and indexes have no statistics.

### <a id="topic_oq3_qxj_3s__section_wsy_1rv_mt"></a>Sampling

When calculating statistics for large tables, HAWQ creates a smaller table by sampling the base table. If the table is partitioned, samples are taken from all partitions.

If a sample table is created, the number of rows in the sample is calculated to provide a maximum acceptable relative error. The amount of acceptable error is specified with the `gp_analyze_relative_error` system configuration parameter, which is set to .25 (25%) by default. This is usually sufficiently accurate to generate correct query plans. If `ANALYZE` is not producing good estimates for a table column, you can increase the sample size by setting the `gp_analyze_relative_error` configuration parameter to a lower value. Beware that setting this parameter to a low value can lead to a very large sample size and dramatically increase analyze time.

### <a id="topic_oq3_qxj_3s__section_u5p_brv_mt"></a>Updating Statistics

Running `ANALYZE` with no arguments updates statistics for all tables in the database. This could take a very long time, so it is better to analyze tables selectively after data has changed. You can also analyze a subset of the columns in a table, for example columns used in joins, `WHERE` clauses, `SORT` clauses, `GROUP BY` clauses, or `HAVING` clauses.

See the SQL Command Reference for details of running the `ANALYZE` command.

Refer to the Management Utility Reference for details of running the `analyzedb` command.

### <a id="topic_oq3_qxj_3s__section_cv2_crv_mt"></a>Analyzing Partitioned and Append-Optimized Tables

When the `ANALYZE` command is run on a partitioned table, it analyzes each leaf-level subpartition, one at a time. You can run `ANALYZE` on just new or changed partition files to avoid analyzing partitions that have not changed. If a table is partitioned, you can analyze just new or changed partitions.

The `analyzedb` command-line utility skips unchanged partitions automatically. It also runs concurrent sessions so it can analyze several partitions concurrently. It runs five sessions by default, but the number of sessions can be set from 1 to 10 with the `-p` command-line option. Each time `analyzedb` runs, it saves state information for append-optimized tables and partitions in the `db_analyze` directory in the master data directory. The next time it runs, `analyzedb` compares the current state of each table with the saved state and skips analyzing a table or partition if it is unchanged. Heap tables are always analyzed.

If the Pivotal Query Optimizer is enabled, you also need to run `ANALYZE             ROOTPARTITION` to refresh the root partition statistics. The Pivotal Query Optimizer requires statistics at the root level for partitioned tables. The legacy optimizer does not use these statistics. Enable the Pivotal Query Optimizer by setting both the `optimizer` and `optimizer_analyze_root_partition` system configuration parameters to on. The root level statistics are then updated when you run `ANALYZE` or `ANALYZE ROOTPARTITION`. The time to run `ANALYZE ROOTPARTITION` is similar to the time to analyze a single partition since `ANALYZE ROOTPARTITION`. The `analyzedb` utility updates root partition statistics by default .

## <a id="topic_gyb_qrd_2t"></a>Configuring Statistics

There are several options for configuring HAWQ statistics collection.

### <a id="statstarget"></a>Statistics Target

The statistics target is the size of the `most_common_vals`, `most_common_freqs`, and `histogram_bounds` arrays for an individual column. By default, the target is 25. The default target can be changed by setting a server configuration parameter and the target can be set for any column using the `ALTER TABLE` command. Larger values increase the time needed to do `ANALYZE`, but may improve the quality of the legacy query optimizer (planner) estimates.

Set the system default statistics target to a different value by setting the `default_statistics_target` server configuration parameter. The default value is usually sufficient, and you should only raise or lower it if your tests demonstrate that query plans improve with the new target. 

You will perform different procedures to set server configuration parameters for your whole HAWQ cluster depending upon whether you manage your cluster from the command line or use Ambari. If you use Ambari to manage your HAWQ cluster, you must ensure that you update server configuration parameters via the Ambari Web UI only. If you manage your HAWQ cluster from the command line, you will use the `hawq config` command line utility to set server configuration parameters.

The following examples show how to raise the default statistics target from 25 to 50.

If you use Ambari to manage your HAWQ cluster:

1. Set the `default_statistics_target` configuration property to `50` via the HAWQ service **Configs > Advanced > Custom hawq-site** drop down.
2. Select **Service Actions > Restart All** to load the updated configuration.

If you manage your HAWQ cluster from the command line:

1.  Log in to the HAWQ master host as a HAWQ administrator and source the file `/usr/local/hawq/greenplum_path.sh`.

    ``` shell
    $ source /usr/local/hawq/greenplum_path.sh
    ```

1. Use the `hawq config` utility to set `default_statistics_target`:

    ``` shell
    $ hawq config -c default_statistics_target -v 50
    ```
2. Reload the HAWQ configuration:

    ``` shell
    $ hawq stop cluster -u
    ```

The statististics target for individual columns can be set with the `ALTER             TABLE` command. For example, some queries can be improved by increasing the target for certain columns, especially columns that have irregular distributions. You can set the target to zero for columns that never contribute to query optimization. When the target is 0, `ANALYZE` ignores the column. For example, the following `ALTER TABLE` command sets the statistics target for the `notes` column in the `emp` table to zero:

``` sql
ALTER TABLE emp ALTER COLUMN notes SET STATISTICS 0;
```

The statistics target can be set in the range 0 to 1000, or set it to -1 to revert to using the system default statistics target.

Setting the statistics target on a parent partition table affects the child partitions. If you set statistics to 0 on some columns on the parent table, the statistics for the same columns are set to 0 for all children partitions. However, if you later add or exchange another child partition, the new child partition will use either the default statistics target or, in the case of an exchange, the previous statistics target. Therefore, if you add or exchange child partitions, you should set the statistics targets on the new child table.

### <a id="topic_gyb_qrd_2t__section_j3p_drv_mt"></a>Automatic Statistics Collection

HAWQ can be set to automatically run `ANALYZE` on a table that either has no statistics or has changed significantly when certain operations are performed on the table. For partitioned tables, automatic statistics collection is only triggered when the operation is run directly on a leaf table, and then only the leaf table is analyzed.

Automatic statistics collection has three modes:

-   `none` disables automatic statistics collection.
-   `on_no_stats` triggers an analyze operation for a table with no existing statistics when any of the commands `CREATE TABLE AS SELECT`, `INSERT`, or `COPY` are executed on the table.
-   `on_change` triggers an analyze operation when any of the commands `CREATE TABLE AS SELECT`, `INSERT`, or `COPY` are executed on the table and the number of rows affected exceeds the threshold defined by the `gp_autostats_on_change_threshold` configuration parameter.

The automatic statistics collection mode is set separately for commands that occur within a procedural language function and commands that execute outside of a function:

-   The `gp_autostats_mode` configuration parameter controls automatic statistics collection behavior outside of functions and is set to `on_no_stats` by default.

With the `on_change` mode, `ANALYZE` is triggered only if the number of rows affected exceeds the threshold defined by the `gp_autostats_on_change_threshold` configuration parameter. The default value for this parameter is a very high value, 2147483647, which effectively disables automatic statistics collection; you must set the threshold to a lower number to enable it. The `on_change` mode could trigger large, unexpected analyze operations that could disrupt the system, so it is not recommended to set it globally. It could be useful in a session, for example to automatically analyze a table following a load.

To disable automatic statistics collection outside of functions, set the `gp_autostats_mode` parameter to `none`. For a command-line-managed HAWQ cluster:

``` shell
$ hawq configure -c gp_autostats_mode -v none
```

For an Ambari-managed cluster, set `gp_autostats_mode` via the Ambari Web UI.

Set the `log_autostats` system configuration parameter to `on` if you want to log automatic statistics collection operations.
