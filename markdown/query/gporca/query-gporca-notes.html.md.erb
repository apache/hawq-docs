---
title: Considerations when Using GPORCA
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

<span class="shortdesc"> To execute queries optimally with GPORCA, consider certain criteria for the query. </span>

Ensure the following criteria are met:

-   The table does not contain multi-column partition keys.
-   The table does not contain multi-level partitioning.
-   The query does not run against master only tables such as the system table *pg\_attribute*.
-   Statistics have been collected on the root partition of a partitioned table.

If the partitioned table contains more than 20,000 partitions, consider a redesign of the table schema.

GPORCA generates minidumps to describe the optimization context for a given query. Use the minidump files to analyze HAWQ issues. The minidump file is located under the master data directory and uses the following naming format:

`Minidump_date_time.mdp`

For information about the minidump file, see the server configuration parameter `optimizer_minidump`.

When the `EXPLAIN ANALYZE` command uses GPORCA, the `EXPLAIN` plan shows only the number of partitions that are being eliminated. The scanned partitions are not shown. To show name of the scanned partitions in the segment logs set the server configuration parameter `gp_log_dynamic_partition_pruning` to `on`. This example `SET` command enables the parameter.

``` sql
SET gp_log_dynamic_partition_pruning = on;
```


