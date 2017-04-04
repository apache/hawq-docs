---
title: Working with Hierarchical Resource Queues
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

This section describes how administrators can define and work with resource queues in order to allocate resource usage within HAWQ. By designing hierarchical resource queues, system administrators can balance system resources to queries as needed.

## <a id="resource_queues"></a>HAWQ Resource Queues 

Resource queues are the main tool for managing the degree of concurrency in a HAWQ system. Resource queues are database objects that you create with the CREATE RESOURCE QUEUE SQL statement. You can use them to manage the number of active queries that may execute concurrently, and the maximum amount of memory and CPU usage each type of query is allocated. Resource queues can also guard against queries that would consume too many resources and degrade overall system performance.

Internally, HAWQ manages its resources dynamically based on a system of hierarchical resource queues. HAWQ uses resource queues to allocate resources efficiently to concurrently running queries. Resource queues are organized as a n-ary tree, as depicted in the diagram below.

![](../images/svg/hawq_resource_queues.svg)

When HAWQ is initialized, there is always one queue named `pg_root` at the root of the tree and one queue named `pg_default`. If YARN is configured, HAWQ's resource manager automatically fetches the capacity of this root queue from the global resource manager. When you create a new resource queue, you must specify a parent queue. This forces all resource queues to organize into a tree.

When a query comes in, after query parsing and semantic analysis, the optimizer coordinates with HAWQ resource manager on the resource usage for the query and get an optimized plan given the resources available for the query. The resource allocation for each query is sent with the plan together to the segments. Consequently, each query executor \(QE\) knows the resource quota for the current query and enforces the resource consumption during the whole execution. When query execution finishes or is cancelled. the resource is returned to the HAWQ resource manager.

**About Branch Queues and Leaf Queues**

In this hierarchical resource queue tree depicted in the diagram, there are branch queues \(rectangles outlined in dashed lines\) and leaf queues \(rectangles drawn with solid lines\). Only leaf queues can be associated with roles and accept queries.

**Query Resource Allocation Policy**

The HAWQ resource manager follows several principles when allocating resources to queries:

-   Resources are allocated only to queues that have running or queued queries.
-   When multiple queues are busy, the resource manager balances resources among queues based on resource queue capacities.
-   In one resource queue, when multiple queries are waiting for resources, resources are distributed evenly to each query in a best effort manner.

**Enforcing Limits on Resources**

You can configure HAWQ to enforce limits on resource usage by setting memory and CPU usage limits on both segments and resource queues. See [Configuring Segment Resource Capacity](ConfigureResourceManagement.html) and [Creating Resource Queues](ResourceQueues.html). For some best practices on designing and using resource queues in HAWQ, see [Best Practices for Managing Resources](../bestpractices/managing_resources_bestpractices.html).

For a high-level overview of how resource management works in HAWQ, see [Managing Resources](HAWQResourceManagement.html).

## <a id="topic_dyy_pfp_15"></a>Setting the Maximum Number of Resource Queues 

You can configure the maximum number of resource queues allowed in your HAWQ cluster.

By default, the maximum number of resource queues that you can create in HAWQ is 128.

You can configure this property in `hawq-site.xml`. The new maximum takes effect when HAWQ restarts. For example, the configuration below sets this value to 50.

``` xml
<property>
   <name>hawq_rm_nresqueue_limit</name>
   <value>50</value>
</property>
```

The minimum value that can be configured is 3, and the maximum is 1024.

To check the currently configured limit, you can execute the following command:

``` sql
postgres=# SHOW hawq_rm_nresqueue_limit;
```

``` pre
 hawq_rm_nresqueue_limit
----------------------------------------------
128
(1 row)
```

## <a id="topic_p4l_dls_zt"></a>Creating Resource Queues 

Use CREATE RESOURCE QUEUE to create a new resource queue. Only a superuser can run this DDL statement.

Creating a resource queue involves giving it a name, a parent, setting the CPU and memory limits for the queue, and optionally a limit to the number of active statements on the resource queue. See [CREATE RESOURCE QUEUE](../reference/sql/CREATE-RESOURCE-QUEUE.html).

**Note:** You can only associate roles and queries with leaf-level resource queues. Leaf-level resource queues are resource queues that do not have any children.

### Examples

Create a resource queue as a child of `pg_root` with an active query limit of 20 and memory and core limits of 50%:

``` sql
CREATE RESOURCE QUEUE myqueue WITH (PARENT='pg_root', ACTIVE_STATEMENTS=20,
MEMORY_LIMIT_CLUSTER=50%, CORE_LIMIT_CLUSTER=50%);
```

Create a resource queue as a child of pg\_root with memory and CPU limits and a resource overcommit factor:

``` sql
CREATE RESOURCE QUEUE test_queue_1 WITH (PARENT='pg_root',
MEMORY_LIMIT_CLUSTER=50%, CORE_LIMIT_CLUSTER=50%, RESOURCE_OVERCOMMIT_FACTOR=2);
```

## <a id="topic_e1b_2ls_zt"></a>Altering Resource Queues 

Use ALTER RESOURCE QUEUE to modify an existing resource queue. Only a superuser can run this DDL statement.

The ALTER RESOURCE QUEUE statement allows you to modify resource limits and the number of active statements allowed in the queue. You cannot change the parent queue of an existing resource queue, and you are subject to the same constraints that apply to the creation of resource queues.

You can modify an existing resource queue even when it is active or when one of its descendents is active. All queued resource requsts are adjusted based on the modifications to the resource queue.

However, when you alter a resource queue, queued resource requests may encounter some conflicts. For example, a resource deadlock can occur or some requests cannot be satisfied based on the newly modified resource queue capacity.

To prevent conflicts, HAWQ cancels by default all resource requests that are in conflict with the new resource queue definition. This behavior is controlled by the `hawq_rm_force_alterqueue_cancel_queued_request` server configuration parameter, which is by default set to true \(`on`\). If you set the server configuration parameter `hawq_rm_force_alterqueue_cancel_queued_request` to false, the actions specified in ALTER RESOURCE QUEUE are canceled if the resource manager finds at least one resource request that is in conflict with the new resource definitions supplied in the altering command.

For more information, see [ALTER RESOURCE QUEUE](../reference/sql/ALTER-RESOURCE-QUEUE.html).

**Note:** To change the roles \(users\) assigned to a resource queue, use the ALTER ROLE command.

### Examples

Change the memory and core limit of a resource queue:

``` sql
ALTER RESOURCE QUEUE test_queue_1 WITH (MEMORY_LIMIT_CLUSTER=40%,
CORE_LIMIT_CLUSTER=40%);
```

Change the active statements maximum for the resource queue:

``` sql
ALTER RESOURCE QUEUE test_queue_1 WITH (ACTIVE_STATEMENTS=50);
```

## <a id="topic_hbp_fls_zt"></a>Dropping Resource Queues 

Use DROP RESOURCE QUEUE to remove an existing resource queue.

DROP RESOURCE QUEUE drops an existing resource queue. Only a superuser can run this DDL statement when the queue is not busy. You cannot drop a resource queue that has at least one child resource queue or a role assigned to it.

The default resource queues `pg_root` and `pg_default` cannot be dropped.

### Examples

Remove a role from a resource queue \(and move the role to the default resource queue, `pg_default`\):

``` sql
ALTER ROLE bob RESOURCE QUEUE NONE;
```

Remove the resource queue named `adhoc`:

``` sql
DROP RESOURCE QUEUE adhoc;
```

## <a id="topic_lqy_gls_zt"></a>Checking Existing Resource Queues 

The HAWQ catalog table `pg_resqueue` saves all existing resource queues.

The following example shows the data selected from `pg_resqueue`.

``` sql
postgres=# SELECT rsqname,parentoid,activestats,memorylimit,corelimit,resovercommit,
allocpolicy,vsegresourcequota,nvsegupperlimit,nvseglowerlimit,nvsegupperlimitperseg,nvseglowerlimitperseg
FROM pg_resqueue WHERE rsqname='test_queue_1';
```

``` pre
   rsqname    | parentoid | activestats | memorylimit | corelimit | resovercommit | allocpolicy | vsegresourcequota | nvsegupperlimit | nvseglowerlimit |nvsegupperlimitperseg  | nvseglowerlimitperseg
--------------+-----------+-------------+-------------+-----------+---------------+-------------+-------------------+-----------------+-----------------+-----------------------+-----------------------
 test_queue_1 |      9800 |         100 | 50%         | 50%       |             2 | even        | mem:128mb         | 0               | 0               | 0                     |1
```

The query displays all the attributes and their values of the selected resource queue. See [CREATE RESOURCE QUEUE](../reference/sql/CREATE-RESOURCE-QUEUE.html) for a description of these attributes.

You can also check the runtime status of existing resource queues by querying the `pg_resqueue_status` view:

``` sql
postgres=# SELECT * FROM pg_resqueue_status;
```


``` pre
  rsqname   | segmem | segcore  | segsize | segsizemax | inusemem | inusecore | rsqholders | rsqwaiters | paused
------------+--------+----------+---------+------------+----------+-----------+------------+------------+--------
 pg_root    | 128    | 0.125000 | 64      | 64         | 0        | 0.000000  | 0          | 0          | F
 pg_default | 128    | 0.125000 | 32      | 64         | 0        | 0.000000  | 0          | 0          | F(2 rows)
```

The query returns the following pieces of data about the resource queue's runtime status:

|Resource Queue Runtime|Description|
|----------------------|-----------|
|rsqname|HAWQ resource queue name|
|segmem|Virtual segment memory quota in MB|
|segcore|Virtual segment vcore quota|
|segsize|Number of virtual segments the resource queue can dispatch for query execution|
|segsizemax|Maximum number of virtual segments the resource queue can dispatch for query execution when overcommit the other queues’ resource quota|
|inusemem|Accumulated memory in use in MB by current running statements|
|inusecore|Accumulated vcore in use by current running statements|
|rsqholders|The total number of concurrent running statements|
|rsqwaiters|Total number of queuing statements|
|paused|Indicates whether the resource queue is temporarily paused due to no resource status changes. ‘F’ means false, ‘T’ means true, ‘R’ means maybe the resource queue has encountered a resource fragmentation problem|

## <a id="topic_scr_3ls_zt"></a>Assigning Roles to Resource Queues 

By default, a role is assigned to `pg_default` resource queue. Assigning a role to a branch queue is not allowed.

The following are some examples of creating and assigning a role to a resource queue:

``` sql
CREATE ROLE rmtest1 WITH LOGIN RESOURCE QUEUE pg_default;

ALTER ROLE rmtest1 RESOURCE QUEUE test_queue_1;
```

