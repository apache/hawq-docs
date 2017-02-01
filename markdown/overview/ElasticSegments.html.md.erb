---
title: Elastic Query Execution Runtime
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

HAWQ uses dynamically allocated virtual segments to provide resources for query execution.

In HAWQ 1.x, the number of segments \(compute resource carrier\) used to run a query is fixed, no matter whether the underlying query is big query requiring many resources or a small query requiring little resources. This architecture is simple, however it uses resources inefficiently.

To address this issue, HAWQ now uses the elastic query execution runtime feature, which is based on virtual segments. HAWQ allocates virtual segments on demand based on the costs of queries. In other words, for big queries, HAWQ starts a large number of virtual segments, while for small queries HAWQ starts fewer virtual segments.

## Storage

In HAWQ, the number of invoked segments varies based on cost of query. In order to simplify table data management, all data of one relation are saved under one HDFS folder.

For all the HAWQ table storage formats, AO \(Append-Only\) and Parquet, the data files are splittable, so that HAWQ can assign multiple virtual segments to consume one data file concurrently to increase the parallelism of a query.

## Physical Segments and Virtual Segments

In HAWQ, only one physical segment needs to be installed on one host, in which multiple virtual segments can be started to run queries. HAWQ allocates multiple virtual segments distributed across different hosts on demand to run one query. Virtual segments are carriers \(containers\) for resources such as memory and CPU. Queries are executed by query executors in virtual segments.

**Note:** In this documentation, when we refer to segment by itself, we mean a *physical segment*.

## Virtual Segment Allocation Policy

Different number of virtual segments are allocated based on virtual segment allocation policies. The following factors determine the number of virtual segments that are used for a query:

-   Resources available at the query running time
-   The cost of the query
-   The distribution of the table; in other words, randomly distributed tables and hash distributed tables
-   Whether the query involves UDFs and external tables
-   Specific server configuration parameters, such as `default_hash_table_bucket_number` for hash table queries and `hawq_rm_nvseg_perquery_limit`
