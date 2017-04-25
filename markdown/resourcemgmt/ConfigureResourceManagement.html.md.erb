---
title: Configuring Resource Management
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

This topic provides configuration information for system administrators and database superusers responsible for managing resources in a HAWQ system.

To configure resource management in HAWQ, follow these high-level steps:

1.  Decide which kind of resource management you need in your HAWQ deployment. HAWQ supports two modes of global resource management:
    -   Standalone mode, or no global resource management. When configured to run in standalone mode, HAWQ consumes cluster node resources without considering the resource requirements of co-existing applications, and the HAWQ resource manager assumes it can use all the resources from registered segments, unless configured otherwise. See [Using Standalone Mode](#topic_url_pls_zt).
    -   External global resource manager mode. Currently HAWQ supports YARN as a global resource manager. When you configure YARN as the global resource manager in a HAWQ cluster, HAWQ becomes an unmanaged YARN application. HAWQ negotiates resources with the YARN resource manager to consume YARN cluster resources.
2.  If you are using standalone mode for HAWQ resource management, decide on whether to limit the amount of memory and CPU usage allocated per HAWQ segment. See [Configuring Segment Resource Capacity](#topic_htk_fxh_15).
3.  If you are using YARN as your global resource manager, configure the resource queue in YARN where HAWQ will register itself as a YARN application. Then configure HAWQ with the location and configuration requirements for communicating with YARN's resource manager. See [Integrating YARN with HAWQ](YARNIntegration.html) for details.
4.  In HAWQ, create and define resource queues. See [Working with Hierarchical Resource Queues](ResourceQueues.html).

## <a id="topic_url_pls_zt"></a>Using Standalone Mode 

Standalone mode means that the HAWQ resource manager assumes it can use all resources from registered segments unless configured otherwise.

To configure HAWQ to run without a global resource manager, add the following property configuration to your `hawq-site.xml` file:

``` xml
<property>
      <name>hawq_global_rm_type</name>
      <value>none</value>
</property>
```

### <a id="id_wgb_44m_q5"></a>hawq\_global\_rm\_type 

HAWQ global resource manager type. Valid values are `yarn` and `none`. Setting this parameter to `none` indicates that the HAWQ resource manager will manages its own resources. Setting the value to `yarn` means that HAWQ will negotiate with YARN for resources.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
|yarn or none|none|master<br/><br/>system<br/><br/>restart|

## <a id="topic_htk_fxh_15"></a>Configuring Segment Resource Capacity 

When you run the HAWQ resource manager in standalone mode \(`hawq_global_rm_type=none`\), then you can set limits on the resources used by each HAWQ cluster segment.

In `hawq-site.xml`, add the following parameters:

``` xml
<property>
   <name>hawq_rm_memory_limit_perseg</name>
   <value>8GB</value>
</property>
<property>
   <name>hawq_rm_nvcore_limit_perseg</name>
   <value>4</value>
</property>
```

**Note:** Due to XML configuration validation, you must set these properties for either mode even though they do not apply if you are using YARN mode.

You must configure all segments with identical resource capacities. Memory should be set as a multiple of 1GB, such as 1GB per core, 2GB per core or 4GB per core. For example, if you want to use the ratio of 4GB per core, then you must configure all segments to use a 4GB per core resource capacity.

After you set limits on the segments, you can then use resource queues to configure additional resource management rules in HAWQ.

**Note:** To reduce the likelihood of resource fragmentation, you should make sure that the segment resource capacity configured for HAWQ \(`hawq_rm_memory_limit_perseg`\) is a multiple of the resource quotas for all virtual segments.

### <a id="id_qqq_s4m_q5"></a>hawq\_rm\_memory\_limit\_perseg 

Limit of memory usage by a HAWQ segment when `hawq_global_rm_type` is set to `none`. For example, `8GB`.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
| no specific lower or upper limit | 64GB |session<br/><br/>reload|

### <a id="id_xpv_t4m_q5"></a>hawq\_rm\_nvcore\_limit\_perseg 

Maximum number of virtual cores that can be used for query execution in a HAWQ segment when `hawq_global_rm_type` is set to `none`. For example, `2.0`.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
|1.0 to maximum integer|1.0|master<br/><br/>session<br/><br/>reload|

## <a id="topic_g2p_zdq_15"></a>Configuring Resource Quotas for Query Statements 

In some cases, you may want to specify additional resource quotas on the query statement level.

The following configuration properties allow a user to control resource quotas without altering corresponding resource queues.

-   [hawq\_rm\_stmt\_nvseg](../reference/guc/parameter_definitions.html)
-   [hawq\_rm\_stmt\_vseg\_memory](../reference/guc/parameter_definitions.html)

However, the changed resource quota for the virtual segment cannot exceed the resource queue’s maximum capacity in HAWQ.

***Note:*** The value of `hawq_rm_stmt_vseg_memory` depends on `hawq_rm_stmt_nvseg`, which defines the number of virtual segments used for the query. You must set `hawq_rm_stmt_nvseg` to a value greater than 0 before setting the memory quota for each segment with  `hawq_rm_stmt_vseg_memory`. After running a query or completing the session, reset the value of `hawq_rm_stmt_nvseg` to 0 to disable the statement level resource quota.

In the following example, when executing the next query statement, the HAWQ resource manager will attempt to allocate 10 virtual segments and each segment has a 256MB memory quota.


``` sql
postgres=# SET hawq_rm_stmt_nvseg=10;
SET
postgres=# SET hawq_rm_stmt_vseg_memory='256mb';
SET
postgres=# SELECT <x> FROM <from_item> WHERE <condition>;
postgres=# SET hawq_rm_stmt_nvseg=0;
SET

```

Note that given the dynamic nature of resource allocation in HAWQ, you cannot expect that each segment has reserved resources for every query. The HAWQ resource manager will only attempt to allocate those resources. In addition, the number of virtual segments allocated for the query statement cannot amount to a value larger than the value set in global configuration parameter `hawq_rm_nvseg_perquery_limit` and `hawq_rm_nvseg_perquery_perseg_limit`.

## <a id="topic_tl5_wq1_f5"></a>Configuring the Maximum Number of Virtual Segments 

You can limit the number of virtual segments used during statement execution on a cluster-wide level.

Limiting the number of virtual segments used during statement execution is useful for preventing resource bottlenecks during data load and the overconsumption of resources without performance benefits. The number of files that can be opened concurrently for write on both NameNode and DataNode are limited. Consider the following scenario:

-   You need to load data into a table with P partitions
-   There are N nodes in the cluster and V virtual segments per node started for the load query

Then there will be P \* V files opened per DataNode and at least P \* V threads started in the DataNode. If the number of partitions and the number of virtual segments per node is very high, the DataNode becomes a bottleneck. On the NameNode side, there will be V \* N connections. If the number of nodes is very high, then NameNode can become a bottleneck.

To alleviate the load on NameNode, you can limit V, the number of virtual segments started per node. Use the following server configuration parameters:

-   `hawq_rm_nvseg_perquery_limit` limits the maximum number of virtual segments that can be used for one statement execution on a cluster-wide level.  The hash buckets defined in `default_hash_table_bucket_number` cannot exceed this number. The default value is 512.
-   `default_hash_table_bucket_number` defines the number of buckets used by default when you create a hash table. When you query a hash table, the query's virtual segment resources are fixed and allocated based on the bucket number defined for the table. A best practice is to tune this configuration parameter after you expand the cluster.

You can also limit the number of virtual segments used by queries when configuring your resource queues. \(See [CREATE RESOURCE QUEUE](../reference/sql/CREATE-RESOURCE-QUEUE.html).\) The global configuration parameters are a hard limit, however, and any limits set on the resource queue or on the statement-level cannot be larger than these limits set on the cluster-wide level.
