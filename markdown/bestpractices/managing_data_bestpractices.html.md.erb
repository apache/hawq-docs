---
title: Best Practices for Managing Data
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

This topic describes best practices for creating databases, loading data, partioning data, and recovering data in HAWQ.

## <a id="topic_xhy_v2j_1v"></a>Best Practices for Loading Data

Loading data into HDFS is challenging due to the limit on the number of files that can be opened concurrently for write on both NameNodes and DataNodes.

To obtain the best performance during data loading, observe the following best practices:

-   Typically the number of concurrent connections to a NameNode should not exceed 50,000, and the number of open files per DataNode should not exceed 10,000. If you exceed these limits, NameNode and DataNode may become overloaded and slow.
-   If the number of partitions in a table is large, the recommended way to load data into the partitioned table is to load the data partition by partition. For example, you can use query such as the following to load data into only one partition:

    ```sql
    INSERT INTO target_partitioned_table_part1 SELECT * FROM source_table WHERE filter
    ```

    where *filter* selects only the data in the target partition.

-   To alleviate the load on NameNode, you can reduce the number of virtual segment used per node. You can do this on the statement-level or on the resource queue level. See [Configuring the Maximum Number of Virtual Segments](../resourcemgmt/ConfigureResourceManagement.html#topic_tl5_wq1_f5) for more information.
-   Use resource queues to limit load query and read query concurrency.

The best practice for loading data into partitioned tables is to create an intermediate staging table, load it, and then exchange it into your partition design. See [Exchanging a Partition](../ddl/ddl-partition.html#topic83).

## <a id="topic_s23_52j_1v"></a>Best Practices for Partitioning Data

### <a id="topic65"></a>Deciding on a Table Partitioning Strategy

Not all tables are good candidates for partitioning. If the answer is *yes* to all or most of the following questions, table partitioning is a viable database design strategy for improving query performance. If the answer is *no* to most of the following questions, table partitioning is not the right solution for that table. Test your design strategy to ensure that query performance improves as expected.

-   **Is the table large enough?** Large fact tables are good candidates for table partitioning. If you have millions or billions of records in a table, you may see performance benefits from logically breaking that data up into smaller chunks. For smaller tables with only a few thousand rows or less, the administrative overhead of maintaining the partitions will outweigh any performance benefits you might see.
-   **Are you experiencing unsatisfactory performance?** As with any performance tuning initiative, a table should be partitioned only if queries against that table are producing slower response times than desired.
-   **Do your query predicates have identifiable access patterns?** Examine the `WHERE` clauses of your query workload and look for table columns that are consistently used to access data. For example, if most of your queries tend to look up records by date, then a monthly or weekly date-partitioning design might be beneficial. Or if you tend to access records by region, consider a list-partitioning design to divide the table by region.
-   **Does your data warehouse maintain a window of historical data?** Another consideration for partition design is your organization's business requirements for maintaining historical data. For example, your data warehouse may require that you keep data for the past twelve months. If the data is partitioned by month, you can easily drop the oldest monthly partition from the warehouse and load current data into the most recent monthly partition.
-   **Can the data be divided into somewhat equal parts based on some defining criteria?** Choose partitioning criteria that will divide your data as evenly as possible. If the partitions contain a relatively equal number of records, query performance improves based on the number of partitions created. For example, by dividing a large table into 10 partitions, a query will execute 10 times faster than it would against the unpartitioned table, provided that the partitions are designed to support the query's criteria.

Do not create more partitions than are needed. Creating too many partitions can slow down management and maintenance jobs, such as vacuuming, recovering segments, expanding the cluster, checking disk usage, and others.

Partitioning does not improve query performance unless the query optimizer can eliminate partitions based on the query predicates. Queries that scan every partition run slower than if the table were not partitioned, so avoid partitioning if few of your queries achieve partition elimination. Check the explain plan for queries to make sure that partitions are eliminated. See [Query Profiling](../query/query-profiling.html#topic39) for more about partition elimination.

Be very careful with multi-level partitioning because the number of partition files can grow very quickly. For example, if a table is partitioned by both day and city, and there are 1,000 days of data and 1,000 cities, the total number of partitions is one million. Column-oriented tables store each column in a physical table, so if this table has 100 columns, the system would be required to manage 100 million files for the table.

Before settling on a multi-level partitioning strategy, consider a single level partition with bitmap indexes. Indexes slow down data loads, so consider performance testing with your data and schema to decide on the best strategy.


