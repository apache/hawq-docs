---
title: Best Practices for Querying Data
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

To obtain the best results when querying data in HAWQ, review the best practices described in this topic.

## <a id="virtual_seg_performance"></a>Factors Impacting Query Performance

The number of virtual segments used for a query directly impacts the query's performance. The following factors can impact the degree of parallelism of a query:

-   **Cost of the query**. Small queries use fewer segments and larger queries use more segments. Some techniques used in defining resource queues can influence the number of both virtual segments and general resources allocated to queries. For more information, see [Best Practices for Using Resource Queues](managing_resources_bestpractices.html#topic_hvd_pls_wv).
-   **Available resources at query time**. If more resources are available in the resource queue, those resources will be used.
-   **Hash table and bucket number**. If the query involves only hash-distributed tables, the query's parallelism is fixed (equal to the hash table bucket number) under the following conditions: 
 
  	- The bucket number (bucketnum) configured for all the hash tables is the same for all tables 
   - The table size for random tables is no more than 1.5 times the size allotted for the hash tables. 

  Otherwise, the number of virtual segments depends on the query's cost: hash-distributed table queries behave like queries on randomly-distributed tables.
  
-   **Query Type**: It can be difficult to calculate  resource costs for queries with some user-defined functions or for queries to external tables. With these queries,  the number of virtual segments is controlled by the  `hawq_rm_nvseg_perquery_limit `and `hawq_rm_nvseg_perquery_perseg_limit` parameters, as well as by the ON clause and the location list of external tables. If the query has a hash result table (e.g. `INSERT into hash_table`), the number of virtual segments must be equal to the bucket number of the resulting hash table. If the query is performed in utility mode, such as for `COPY` and `ANALYZE` operations, the virtual segment number is calculated by different policies.

  ***Note:*** PXF external tables use the `default_hash_table_bucket_number` parameter, not the `hawq_rm_nvseg_perquery_perseg_limit` parameter, to control the number of virtual segments.

See [Query Performance](../query/query-performance.html#topic38) for more details.

## <a id="id_xtk_jmq_1v"></a>Examining Query Plans to Solve Problems

If a query performs poorly, examine its query plan and ask the following questions:

-   **Do operations in the plan take an exceptionally long time?** Look for an operation that consumes the majority of query processing time. For example, if a scan on a hash table takes longer than expected, the data locality may be low; reloading the data can increase the data locality and speed up the query. Or, adjust `enable_<operator>` parameters to see if you can force the legacy query optimizer (planner) to choose a different plan by disabling a particular query plan operator for that query.
-   **Are the optimizer's estimates close to reality?** Run `EXPLAIN             ANALYZE` and see if the number of rows the optimizer estimates is close to the number of rows the query operation actually returns. If there is a large discrepancy, collect more statistics on the relevant columns.
-   **Are selective predicates applied early in the plan?** Apply the most selective filters early in the plan so fewer rows move up the plan tree. If the query plan does not correctly estimate query predicate selectivity, collect more statistics on the relevant columns. You can also try reordering the `WHERE` clause of your SQL statement.
-   **Does the optimizer choose the best join order?** When you have a query that joins multiple tables, make sure that the optimizer chooses the most selective join order. Joins that eliminate the largest number of rows should be done earlier in the plan so fewer rows move up the plan tree.

    If the plan is not choosing the optimal join order, set `join_collapse_limit=1` and use explicit `JOIN` syntax in your SQL statement to force the legacy query optimizer (planner) to the specified join order. You can also collect more statistics on the relevant join columns.

-   **Does the optimizer selectively scan partitioned tables?** If you use table partitioning, is the optimizer selectively scanning only the child tables required to satisfy the query predicates? Scans of the parent tables should return 0 rows since the parent tables do not contain any data. See [Verifying Your Partition Strategy](../ddl/ddl-partition.html#topic74) for an example of a query plan that shows a selective partition scan.
-   **Does the optimizer choose hash aggregate and hash join operations where applicable?** Hash operations are typically much faster than other types of joins or aggregations. Row comparison and sorting is done in memory rather than reading/writing from disk. To enable the query optimizer to choose hash operations, there must be sufficient memory available to hold the estimated number of rows. Run an `EXPLAIN  ANALYZE` for the query to show which plan operations spilled to disk, how much work memory they used, and how much memory was required to avoid spilling to disk. For example:

    `Work_mem used: 23430K bytes avg, 23430K bytes max (seg0). Work_mem wanted: 33649K bytes avg, 33649K bytes max (seg0) to lessen workfile I/O affecting 2               workers.`

  **Note:** The "bytes wanted" (*work\_mem* property) is based on the amount of data written to work files and is not exact. This property is not configurable. Use resource queues to manage memory use. For more information on resource queues, see [Configuring Resource Management](../resourcemgmt/ConfigureResourceManagement.html) and [Working with Hierarchical Resource Queues](../resourcemgmt/ResourceQueues.html).

