---
title: Query Performance
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

<span class="shortdesc">HAWQ dynamically allocates resources to queries. Query performance depends on several factors such as data locality, number of virtual segments used for the query and general cluster health.</span>

-   Dynamic Partition Elimination

    In HAWQ, values available only when a query runs are used to dynamically prune partitions, which improves query processing speed. Enable or disable dynamic partition elimination by setting the server configuration parameter `gp_dynamic_partition_pruning` to `ON` or `OFF`; it is `ON` by default.

-   Memory Optimizations

    HAWQ allocates memory optimally for different operators in a query and frees and re-allocates memory during the stages of processing a query.

-   Runaway Query Termination

    HAWQ can automatically terminate the most memory-intensive queries based on a memory usage threshold. The threshold is set as a configurable percentage ([runaway\_detector\_activation\_percent](../reference/guc/parameter_definitions.html#runaway_detector_activation_percent)) of the resource quota for the segment, which is calculated by HAWQ's resource manager.

    If the amount of virtual memory utilized by a physical segment exceeds the calculated threshold, then HAWQ begins terminating queries based on memory usage, starting with the query that is consuming the largest amount of memory. Queries are terminated until the percentage of utilized virtual memory is below the specified percentage.

    To calculate the memory usage threshold for runaway queries, HAWQ uses the following formula:

    *vmem threshold* = (*virtual memory quota calculated by resource manager* + [hawq\_re\_memory\_overcommit\_max](../reference/guc/parameter_definitions.html#hawq_re_memory_overcommit_max)) \* [runaway\_detector\_activation\_percent](../reference/guc/parameter_definitions.html#runaway_detector_activation_percent).

    For example, if HAWQ resource manager calculates a virtual memory quota of 9GB,`             hawq_re_memory_overcommit_max` is set to 1GB and the value of `runaway_detector_activation_percent` is 95 (95%), then HAWQ starts terminating queries when the utilized virtual memory exceeds 9.5 GB.

    To disable automatic query detection and termination, set the value of `runaway_detector_activation_percent` to 100.

## <a id="id_xkg_znj_f5"></a>How to Investigate Query Performance Issues

A query is not executing as quickly as you would expect. Here is how to investigate possible causes of slowdown:

1.  Check the health of the cluster.
    1.  Are any DataNodes, segments or nodes down?
    2.  Are there many failed disks?

2.  Check table statistics. Have the tables involved in the query been analyzed?
3.  Check the plan of the query and run /3/4 to determine the bottleneck. 
    Sometimes, there is not enough memory for some operators, such as Hash Join, or spill files are used. If an operator cannot perform all of its work in the memory allocated to it, it caches data on disk in *spill files*. Compared with no spill files, a query will run much slower.

4.  Check data locality statistics using /3/4. Alternately you can check the logs. Data locality result for every query could also be found in the log of HAWQ. See [Data Locality Statistics](query-performance.html#topic_amk_drc_d5) for information on the statistics.
5.  Check resource queue status. You can query view `pg_resqueue_status` to check if the target queue has already dispatched some resource to the queries, or if the target queue is lacking resources. See [Checking Existing Resource Queues](../resourcemgmt/ResourceQueues.html#topic_lqy_gls_zt).
6.  Analyze a dump of the resource manager's status to see more resource queue status. See [Analyzing Resource Manager Status](../resourcemgmt/ResourceQueues.html#topic_zrh_pkc_f5).

## <a id="topic_amk_drc_d5"></a>Data Locality Statistics

For visibility into query performance, use the EXPLAIN ANALYZE to obtain data locality statistics. For example:

``` sql
postgres=# CREATE TABLE test (i int);
postgres=# INSERT INTO test VALUES(2);
postgres=# EXPLAIN ANALYZE SELECT * FROM test;
```
```
QUERY PLAN
.......
Data locality statistics:
data locality ratio: 1.000; virtual segment number: 1; different host number: 1;
virtual segment number per host(avg/min/max): (1/1/1);
segment size(avg/min/max): (32.000 B/32 B/32 B);
segment size with penalty(avg/min/max): (32.000 B/32 B/32 B);
continuity(avg/min/max): (1.000/1.000/1.000); DFS metadatacache: 7.816 ms;
resource allocation: 0.615 ms; datalocality calculation: 0.136 ms.
```

The following table describes the metrics related to data locality. Use these metrics to examine issues behind a query's performance.

<a id="topic_amk_drc_d5__table_q4p_25c_d5"></a>

<table>
<caption><span class="tablecap">Table 1. Data Locality Statistics</span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Statistic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>data locality ratio</td>
<td><p>Indicates the total local read ratio of a query. The lower the ratio, the more remote read happens. Since remote read on HDFS needs network IO, the execution time of a query may increase.</p>
<p>For hash distributed tables, all the blocks of a file will be processed by one segment, so if data on HDFS is redistributed, such as by the HDFS Balancer, the data locality ratio will be decreased. In this case, you can redistribute the hash distributed table manually by using CREATE TABLE AS SELECT.</p></td>
</tr>
<tr class="even">
<td>number of virtual segments</td>
<td>Typically, the more virtual segments are used, the faster the query will be executed. If the virtual segment number is too small, you can check whether <code class="ph codeph">default_hash_table_bucket_number</code>, <code class="ph codeph">hawq_rm_nvseg_perquery_limit</code>, or the bucket number of a hash distributed table is small. See <a href="#topic_wv3_gzc_d5">Number of Virtual Segments</a>.</td>
</tr>
<tr class="odd">
<td>different host number</td>
<td>Indicates how many hosts are used to run this query. All the hosts should be used when the virtual segment number is bigger than the total number of hosts according to the resource allocation strategy of HAWQ. As a result, if this metric is smaller than the total number of hosts for a big query, it often indicates that some hosts are down. In this case, use “select gp_segment_configuration” to check the node states first.</td>
</tr>
<tr class="even">
<td>segment size and segment size with penalty</td>
<td>“segment size” indicates the (avg/min/max) data size which is processed by a virtual segment. “segment size with penalty” is the segment size when remote read is calculated as “net_disk_ratio” * block size. The virtual segment that contains remote read should process less data than the virtual segment that contains only local read. “net_disk_ratio” can be tuned to measure how much slower the remote read is than local read for different network environments, while considering the workload balance between the nodes. The default value of “net_disk_ratio” is 1.01.</td>
</tr>
<tr class="odd">
<td>continuity</td>
<td>reading a HDFS file discontinuously will introduce additional seek, which will slow the table scan of a query. A low value of continuity indicates that the blocks of a file are not continuously distributed on a DataNode.</td>
</tr>
<tr class="even">
<td>DFS metadatacache</td>
<td>Indicates the metadatacache time cost for a query. In HAWQ, HDFS block information is cached in a metadatacache process. If cache miss happens, time cost of metadatacache may increase.</td>
</tr>
<tr class="odd">
<td>resource allocation</td>
<td>Indicates the time cost of acquiring resources from the resource manager.</td>
</tr>
<tr class="even">
<td>datalocality calculation</td>
<td>Indicates the time to run the algorithm that assigns HDFS blocks to virtual segments and calculates the data locality ratio.</td>
</tr>
</tbody>
</table>

## <a id="topic_wv3_gzc_d5"></a>Number of Virtual Segments

To obtain the best results when querying data in HAWQ, review the best practices described in this topic.

### <a id="virtual_seg_performance"></a>Factors Impacting Query Performance

The number of virtual segments used for a query directly impacts the query's performance. The following factors can impact the degree of parallelism of a query:

-   **Cost of the query**. Small queries use fewer segments and larger queries use more segments. Some techniques used in defining resource queues can influence the number of both virtual segments and general resources allocated to queries.
-   **Available resources at query time**. If more resources are available in the resource queue, those resources will be used.
-   **Hash table and bucket number**. If the query involves only hash-distributed tables, the query's parallelism is fixed (equal to the hash table bucket number) under the following conditions:

   - The bucket number (bucketnum) configured for all the hash tables is the same bucket number
   - The table size for random tables is no more than 1.5 times the size allotted for the hash tables.

  Otherwise, the number of virtual segments depends on the query's cost: hash-distributed table queries behave like queries on randomly-distributed tables.

-   **Query Type**: It can be difficult to calculate  resource costs for queries with some user-defined functions or for queries to external tables. With these queries,  the number of virtual segments is controlled by the  `hawq_rm_nvseg_perquery_limit `and `hawq_rm_nvseg_perquery_perseg_limit` parameters, as well as by the ON clause and the location list of external tables. If the query has a hash result table (e.g. `INSERT into hash_table`), the number of virtual segments must be equal to the bucket number of the resulting hash table. If the query is performed in utility mode, such as for `COPY` and `ANALYZE` operations, the virtual segment number is calculated by different policies.

###General Guidelines

The following guidelines expand on the numbers of virtual segments to use, provided there are sufficient resources available.

-   **Random tables exist in the select list:** \#vseg (number of virtual segments) depends on the size of the table.
-   **Hash tables exist in the select list:** \#vseg depends on the bucket number of the table.
-   **Random and hash tables both exist in the select list:** \#vseg depends on the bucket number of the table, if the table size of random tables is no more than 1.5 times the size of hash tables. Otherwise, \#vseg depends on the size of the random table.
-   **User-defined functions exist:** \#vseg depends on the `hawq_rm_nvseg_perquery_limit` and `hawq_rm_nvseg_perquery_perseg_limit` parameters.
-   **PXF external tables exist:** \#vseg depends on the `default_hash_table_bucket_number` parameter.
-   **gpfdist external tables exist:** \#vseg is at least the number of locations in the location list.
-   **The command for CREATE EXTERNAL TABLE is used:** \#vseg must reflect the value in the command and use the `ON` clause in the command.
-   **Hash tables are copied to or from files:** \#vseg depends on the bucket number of the hash table.
-   **Random tables are copied to files:** \#vseg depends on the size of the random table.
-   **Random tables are copied from files:** \#vseg is a fixed value. \#vseg is 6, when there are sufficient resources.
-   **ANALYZE table:** Analyzing a nonpartitioned table will use more virtual segments than a partitioned table.
-   **Relationship between hash distribution results:** \#vseg must be the same as the bucket number for the hash table.


