---
title: Enabling GPORCA
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

<span class="shortdesc">Precompiled versions of HAWQ that include the GPORCA query optimizer enable it by default, no additional configuration is required. To use the GPORCA query optimizer in a HAWQ built from source, your build must include GPORCA. You must also enable specific HAWQ server configuration parameters at or after install time: </span>

-   [Set the <code class="ph codeph">optimizer\_analyze\_root\_partition</code> parameter to <code class="ph codeph">on</code>](#topic_r5d_hv1_kr) to enable statistics collection for the root partition of a partitioned table.
-   Set the `optimizer` parameter to `on` to enable GPORCA. You can set the parameter at these levels:
    -   [A HAWQ system](#topic_byp_lqk_br)
    -   [A specific HAWQ database](#topic_pzr_3db_3r)
    -   [A session or query](#topic_lx4_vqk_br)

**Important:** If you intend to execute queries on partitioned tables with GPORCA enabled, you must collect statistics on the partitioned table root partition with the `ANALYZE ROOTPARTITION` command. The command `ANALYZE         ROOTPARTITION` collects statistics on the root partition of a partitioned table without collecting statistics on the leaf partitions. If you specify a list of column names for a partitioned table, the statistics for the columns and the root partition are collected. For information on the `ANALYZE` command, see [ANALYZE](../../reference/sql/ANALYZE.html).

You can also use the HAWQ utility `analyzedb` to update table statistics. The HAWQ utility `analyzedb` can update statistics for multiple tables in parallel. The utility can also check table statistics and update statistics only if the statistics are not current or do not exist. For information about the `analyzedb` utility, see [analyzedb](../../reference/cli/admin_utilities/analyzedb.html#topic1).

As part of routine database maintenance, you should refresh statistics on the root partition when there are significant changes to child leaf partition data.

## <a id="topic_r5d_hv1_kr"></a>Setting the optimizer\_analyze\_root\_partition Parameter

When the configuration parameter `optimizer_analyze_root_partition` is set to `on`, root partition statistics will be collected when `ANALYZE` is run on a partitioned table. Root partition statistics are required by GPORCA.

You will perform different procedures to set optimizer configuration parameters for your whole HAWQ cluster depending upon whether you manage your cluster from the command line or use Ambari. If you use Ambari to manage your HAWQ cluster, you must ensure that you update server configuration parameters only via the Ambari Web UI. If you manage your HAWQ cluster from the command line, you will use the `hawq config` command line utility to set optimizer server configuration parameters.

If you use Ambari to manage your HAWQ cluster:

1. Set the `optimizer_analyze_root_partition` configuration property to `on` via the HAWQ service **Configs > Advanced > Custom hawq-site** drop down. 
2. Select **Service Actions > Restart All** to load the updated configuration.

If you manage your HAWQ cluster from the command line:

1.  Log in to the HAWQ master host as a HAWQ administrator and source the file `/usr/local/hawq/greenplum_path.sh`.

    ``` shell
    $ source /usr/local/hawq/greenplum_path.sh
    ```

1. Use the `hawq config` utility to set `optimizer_analyze_root_partition`:

    ``` shell
    $ hawq config -c optimizer_analyze_root_partition -v on
    ```
2. Reload the HAWQ configuration:

    ``` shell
    $ hawq stop cluster -u
    ```

## <a id="topic_byp_lqk_br"></a>Enabling GPORCA for a System

Set the server configuration parameter `optimizer` for the HAWQ system.

If you use Ambari to manage your HAWQ cluster:

1. Set the `optimizer` configuration property to `on` via the HAWQ service **Configs > Advanced > Custom hawq-site** drop down. 
2. Select **Service Actions > Restart All** to load the updated configuration.

If you manage your HAWQ cluster from the command line:

1.  Log in to the HAWQ master host as a HAWQ administrator and source the file `/usr/local/hawq/greenplum_path.sh`.

    ``` shell
    $ source /usr/local/hawq/greenplum_path.sh
    ```

1. Use the `hawq config` utility to set `optimizer`:

    ``` shell
    $ hawq config -c optimizer -v on
    ```
2. Reload the HAWQ configuration:

    ``` shell
    $ hawq stop cluster -u
    ```

## <a id="topic_pzr_3db_3r"></a>Enabling GPORCA for a Database

Set the server configuration parameter `optimizer` for individual HAWQ databases with the `ALTER DATABASE` command. For example, this command enables GPORCA for the database *test\_db*.

``` sql
=> ALTER DATABASE test_db SET optimizer = ON ;
```

## <a id="topic_lx4_vqk_br"></a>Enabling GPORCA for a Session or a Query

You can use the `SET` command to set `optimizer` server configuration parameter for a session. For example, after you use the `psql` utility to connect to HAWQ, this `SET` command enables GPORCA:

``` sql
=> SET optimizer = on ;
```

To set the parameter for a specific query, include the `SET` command prior to running the query.


