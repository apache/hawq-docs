---
title: HAWQ Best Practices
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

This topic addresses general best practices for users who are new to HAWQ.

When using HAWQ, adhere to the following guidelines for best results:

-   **Use a consistent `hawq-site.xml` file to configure your entire cluster**:

    Configuration guc/parameters are located in `$GPHOME/etc/hawq-site.xml`. This configuration file resides on all HAWQ instances and can be modified by using the `hawq config` utility. You can use the same configuration file cluster-wide across both master and segments.
    
    If you install and manage HAWQ using Ambari, do not use `hawq config` to set or change HAWQ configuration properties. Use the Ambari interface for all configuration changes. Configuration changes to `hawq-site.xml` made outside the Ambari interface will be overwritten when you restart or reconfigure  HAWQ using Ambari.

    **Note:** While `postgresql.conf` still exists in HAWQ, any parameters defined in `hawq-site.xml` will overwrite configurations in `postgresql.conf`. For this reason, we recommend that you only use `hawq-site.xml` to configure your HAWQ cluster.

-   **Keep in mind the factors that impact the number of virtual segments used for queries. The number of virtual segments used directly impacts the query's performance.** The degree of parallelism achieved by a query is determined by multiple factors, including the following:
    -   **Cost of the query**. Small queries use fewer segments and larger queries use more segments. Note that there are some techniques you can use when defining resource queues to influence the number of virtual segments and general resources that are allocated to queries. See [Best Practices for Using Resource Queues](managing_resources_bestpractices.html#topic_hvd_pls_wv).
    -   **Available resources**. Resources available at query time. If more resources are available in the resource queue, the resources will be used.
    -   **Hash table and bucket number**. If the query involves only hash-distributed tables, and the bucket number (bucketnum) configured for all the hash tables is either the same bucket number for all tables or the table size for random tables is no more than 1.5 times larger than the size of hash tables for the hash tables, then the query's parallelism is fixed (equal to the hash table bucket number). Otherwise, the number of virtual segments depends on the query's cost and hash-distributed table queries will behave like queries on randomly distributed tables.
    -   **Query Type**: For queries with some user-defined functions or for external tables where calculating resource costs is difficult , then the number of virtual segments is controlled by `hawq_rm_nvseg_perquery_limit `and `hawq_rm_nvseg_perquery_perseg_limit` parameters, as well as by the ON clause and the location list of external tables. If the query has a hash result table (e.g. `INSERT into hash_table`) then the number of virtual segment number must be equal to the bucket number of the resulting hash table, If the query is performed in utility mode, such as for `COPY` and `ANALYZE` operations, the virtual segment number is calculated by different policies, which will be explained later in this section.
    -   **PXF**: PXF external tables use the `default_hash_table_bucket_number` parameter, not the `hawq_rm_nvseg_perquery_perseg_limit` parameter, to control the number of virtual segments. 

    See [Query Performance](../query/query-performance.html#topic38) for more details.


