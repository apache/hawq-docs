---
title: GPORCA Limitations
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

<span class="shortdesc">There are limitations in HAWQ when GPORCA is enabled. GPORCA and the legacy query optimizer currently coexist in HAWQ because GPORCA does not support all HAWQ features. </span>


## <a id="topic_kgn_vxl_vp"></a>Unsupported SQL Query Features

These HAWQ features are unsupported when GPORCA is enabled:

-   Indexed expressions
-   `PERCENTILE` window function
-   External parameters
-   SortMergeJoin (SMJ)
-   Ordered aggregations
-   These analytics extensions:
    -   CUBE
    -   Multiple grouping sets
-   These scalar operators:
    -   `ROW`
    -   `ROWCOMPARE`
    -   `FIELDSELECT`
-   Multiple `DISTINCT` qualified aggregate functions
-   Inverse distribution functions

## <a id="topic_u4t_vxl_vp"></a>Performance Regressions

When GPORCA is enabled in HAWQ, the following features are known performance regressions:

-   Short running queries - For GPORCA, short running queries might encounter additional overhead due to GPORCA enhancements for determining an optimal query execution plan.
-   `ANALYZE` - For GPORCA, the `ANALYZE` command generates root partition statistics for partitioned tables. For the legacy optimizer, these statistics are not generated.
-   DML operations - For GPORCA, DML enhancements including the support of updates on partition and distribution keys might require additional overhead.

Also, enhanced functionality of the features from previous versions could result in additional time required when GPORCA executes SQL statements with the features.


