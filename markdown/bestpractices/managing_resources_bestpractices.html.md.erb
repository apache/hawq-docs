---
title: Best Practices for Managing Resources
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

This topic describes best practices for managing resources in HAWQ.

## <a id="topic_ikz_ndx_15"></a>Best Practices for Configuring Resource Management

When configuring resource management, you can apply certain best practices to ensure that resources are managed both efficiently and for best system performance.

The following is a list of high-level best practices for optimal resource management:

-   Make sure segments do not have identical IP addresses. See [Segments Do Not Appear in gp\_segment\_configuration](../troubleshooting/Troubleshooting.html#topic_hlj_zxx_15) for an explanation of this problem.
-   Configure all segments to have the same resource capacity. See [Configuring Segment Resource Capacity](../resourcemgmt/ConfigureResourceManagement.html#topic_htk_fxh_15).
-   To prevent resource fragmentation, ensure that your deployment's segment resource capacity (standalone mode) or YARN node resource capacity (YARN mode) is a multiple of all virtual segment resource quotas. See [Configuring Segment Resource Capacity](../resourcemgmt/ConfigureResourceManagement.html#topic_htk_fxh_15) (HAWQ standalone mode) and [Setting HAWQ Segment Resource Capacity in YARN](../resourcemgmt/YARNIntegration.html#topic_pzf_kqn_c5).
-   Ensure that enough registered segments are available and usable for query resource requests. If the number of unavailable or unregistered segments is higher than a set limit, then query resource requests are rejected. Also ensure that the variance of dispatched virtual segments across physical segments is not greater than the configured limit. See [Rejection of Query Resource Requests](../troubleshooting/Troubleshooting.html#topic_vm5_znx_15).
-   Use multiple master and segment temporary directories on separate, large disks (2TB or greater) to load balance writes to temporary files (for example, `/disk1/tmp             /disk2/tmp`). For a given query, HAWQ will use a separate temp directory (if available) for each virtual segment to store spill files. Multiple HAWQ sessions will also use separate temp directories where available to avoid disk contention. If you configure too few temp directories, or you place multiple temp directories on the same disk, you increase the risk of disk contention or running out of disk space when multiple virtual segments target the same disk.
-   Configure minimum resource levels in YARN, and tune the timeout of when idle resources are returned to YARN. See [Tune HAWQ Resource Negotiations with YARN](../resourcemgmt/YARNIntegration.html#topic_wp3_4bx_15).
-   Make sure that the property `yarn.scheduler.minimum-allocation-mb` in `yarn-site.xml` is an equal subdivision of 1GB. For example, 1024, 512.

## <a id="topic_hvd_pls_wv"></a>Best Practices for Using Resource Queues

Design and configure your resource queues depending on the operational needs of your deployment. This topic describes the best practices for creating and modifying resource queues within the context of different operational scenarios.

### Modifying Resource Queues for Overloaded HDFS

A high number of concurrent HAWQ queries can cause HDFS to overload, especially when querying partitioned tables. Use the `ACTIVE_STATEMENTS` attribute to restrict statement concurrency in a resource queue. For example, if an external application is executing more than 100 concurrent queries, then limiting the number of active statements in your resource queues will instruct the HAWQ resource manager to restrict actual statement concurrency within HAWQ. You might want to modify an existing resource queue as follows:

```sql
ALTER RESOURCE QUEUE sampleque1 WITH (ACTIVE_STATEMENTS=20);
```

In this case, when this DDL is applied to queue `sampleque1`, the roles using this queue will have to wait until no more than 20 statements are running to execute their queries. Therefore, 80 queries will be waiting in the queue for later execution. Restricting the number of active query statements helps limit the usage of HDFS resources and protects HDFS. You can alter concurrency even when the resource queue is busy. For example, if a queue already has 40 concurrent statements running, and you apply a DDL statement that specifies `ACTIVE_STATEMENTS=20`, then the resource queue pauses the allocation of resources to queries until more than 20 statements have returned their resources.

### Isolating and Protecting Production Workloads

Another best practice is using resource queues to isolate your workloads. Workload isolation prevents your production workload from being starved of resources. To create this isolation, divide your workload by creating roles for specific purposes. For example, you could create one role for production online verification and another role for the regular running of production processes.

In this scenario, let us assign `role1` for the production workload and `role2` for production software verification. We can define the following resource queues under the same parent queue `dept1que`, which is the resource queue defined for the entire department.

```sql
CREATE RESOURCE QUEUE dept1product
   WITH (PARENT='dept1que', MEMORY_LIMIT_CLUSTER=90%, CORE_LIMIT_CLUSTER=90%, RESOURCE_OVERCOMMIT_FACTOR=2);

CREATE RESOURCE QUEUE dept1verification 
   WITH (PARENT='dept1que', MEMORY_LIMIT_CLUSTER=10%, CORE_LIMIT_CLUSTER=10%, RESOURCE_OVERCOMMIT_FACTOR=10);

ALTER ROLE role1 RESOURCE QUEUE dept1product;

ALTER ROLE role2 RESOURCE QUEUE dept1verification;
```

With these resource queues defined, workload is spread across the resource queues as follows:

-   When both `role1` and `role2` have workloads, the test verification workload gets only 10% of the total available `dept1que` resources, leaving 90% of the `dept1que` resources available for running the production workload.
-   When `role1` has a workload but `role2` is idle, then 100% of all `dept1que` resources can be consumed by the production workload.
-   When only `role2` has a workload (for example, during a scheduled testing window), then 100% of all `dept1que` resources can also be utilized for testing.

Even when the resource queues are busy, you can alter the resource queue's memory and core limits to change resource allocation policies before switching workloads.

In addition, you can use resource queues to isolate workloads for different departments or different applications. For example, we can use the following DDL statements to define 3 departments, and an administrator can arbitrarily redistribute resource allocations among the departments according to usage requirements.

```sql
ALTER RESOURCE QUEUE pg_default 
   WITH (MEMORY_LIMIT_CLUSTER=10%, CORE_LIMIT_CLUSTER=10%);

CREATE RESOURCE QUEUE dept1 
   WITH (PARENT='pg_root', MEMORY_LIMIT_CLUSTER=30%, CORE_LIMIT_CLUSTER=30%);

CREATE RESOURCE QUEUE dept2 
   WITH (PARENT='pg_root', MEMORY_LIMIT_CLUSTER=30%, CORE_LIMIT_CLUSTER=30%);

CREATE RESOURCE QUEUE dept3 
   WITH (PARENT='pg_root', MEMORY_LIMIT_CLUSTER=30%, CORE_LIMIT_CLUSTER=30%);

CREATE RESOURCE QUEUE dept11
   WITH (PARENT='dept1', MEMORY_LIMIT_CLUSTER=50%,CORE_LIMIT_CLUSTER=50%);

CREATE RESOURCE QUEUE dept12
   WITH (PARENT='dept1', MEMORY_LIMIT_CLUSTER=50%, CORE_LIMIT_CLUSTER=50%);
```

### Querying Parquet Tables with Large Table Size

You can use resource queues to improve query performance on Parquet tables with a large page size. This type of query requires a large memory quota for virtual segments. Therefore, if one role mostly queries Parquet tables with a large page size, alter the resource queue associated with the role to increase its virtual segment resource quota. For example:

```sql
ALTER RESOURCE queue1 WITH (VSEG_RESOURCE_QUOTA='mem:2gb');
```

If there are only occasional queries on Parquet tables with a large page size, use a statement level specification instead of altering the resource queue. For example:

```sql
postgres=# SET hawq_rm_stmt_nvseg=10;
postgres=# SET hawq_rm_stmt_vseg_memory='2gb';
postgres=# query1;
postgres=# SET hawq_rm_stmt_nvseg=0;
SET
```
***Note:*** To set the parameters at the statement level, you must set `hawq_rm_stmt_nvseg` to a value greater than 0 before setting `hawq_rm_stmt_vseg_memory`. After running a query or completing the session, the value of `hawq_rm_stmt_nvseg` should be reset to 0,  as shown in the example above.


### Restricting Resource Consumption for Specific Queries

In general, the HAWQ resource manager attempts to provide as much resources as possible to the current query to achieve high query performance. When a query is complex and large, however, the associated resource queue can use up many virtual segments causing other resource queues (and queries) to starve. Under these circumstances,you should enable nvseg limits on the resource queue associated with the large query. For example, you can specify that all queries can use no more than 200 virtual segments. To achieve this limit, alter the resource queue as follows

``` sql
ALTER RESOURCE QUEUE queue1 WITH (NVSEG_UPPER_LIMIT=200);
```

If we hope to make this limit vary according to the dynamic cluster size, we can use the following statement.

```sql
ALTER RESOURCE QUEUE queue1 WITH (NVSEG_UPPER_LIMIT_PERSEG=10);
```

After setting the limit in the above example, the actual limit will be 100 if you have a 10-node cluster. If the cluster is expanded to 20 nodes, then the limit increases automatically to 200.

### Guaranteeing Resource Allocations for Individual Statements

In general, the minimum number of virtual segments allocated to a statement is decided by the resource queue's actual capacity and its concurrency setting. For example, if there are 10 nodes in a cluster and the total resource capacity of the cluster is 640GB and 160 cores, then a resource queue having 20% capacity has a capacity of 128GB (640GB \* .20) and 32 cores (160 \*.20). If the virtual segment quota is set to 256MB, then this queue has 512 virtual segments allocated (128GB/256MB=512). If the `ACTIVE_STATEMENTS` concurrency setting for the resource queue is 20, then the minimum number of allocated virtual segments for each query is **25** (*trunc*(512/20)=25). However, this minimum number of virtual segments is a soft restriction. If a query statement requires only 5 virtual segments, then this minimum number of 25 is ignored since it is not necessary to allocate 25 for this statement.

In order to raise the minimum number of virtual segments available for a query statement, there are two options.

-   *Option 1*: Alter the resource queue to reduce concurrency. This is the recommended way to achieve the goal. For example:

    ```sql
    ALTER RESOURCE QUEUE queue1 WITH (ACTIVE_STATEMENTS=10);
    ```

    If the original concurrency setting is 20, then the minimum number of virtual segments is doubled.

-   *Option 2*: Alter the nvseg limits of the resource queue. For example:

    ```sql
    ALTER RESOURCE QUEUE queue1 WITH (NVSEG_LOWER_LIMIT=50);
    ```

    or, alternately:

    ```sql
    ALTER RESOURCE QUEUE queue1 WITH (NVSEG_LOWER_LIMIT_PERSEG=5);
    ```

    In the second DDL, if there are 10 nodes in the cluster, the actual minimum number of virtual segments is 50 (5 \* 10 = 50).



