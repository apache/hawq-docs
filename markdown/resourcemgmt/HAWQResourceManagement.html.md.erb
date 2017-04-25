---
title: How HAWQ Manages Resources
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

HAWQ manages resources (CPU, memory, I/O and file handles) using a variety of mechanisms including global resource management, resource queues and the enforcement of limits on resource usage.

## <a id="global-env"></a>Globally Managed Environments

In Hadoop clusters, resources are frequently managed globally by YARN. YARN provides resources to MapReduce jobs and any other applications that are configured to work with YARN. In this type of environment, resources are allocated in units called containers. In a HAWQ environment, segments and node managers control the consumption of resources and enforce resource limits on each node.

The following diagram depicts the layout of a HAWQ cluster in a YARN-managed Hadoop environment:

![](../images/hawq_high_level_architecture.png)

When you run HAWQ natively in a Hadoop cluster, you can configure HAWQ to register as an application in YARN. After configuration, HAWQ's resource manager communicates with YARN to acquire resources \(when needed to execute queries\) and return resources \(when no longer needed\) back to YARN.

Resources obtained from YARN are then managed in a distributed fashion by HAWQ's resource manager, which is hosted on the HAWQ master.

## <a id="section_w4f_vx4_15"></a>HAWQ Resource Queues 

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

## Enforcing Limits on Resources

You can configure HAWQ to enforce limits on resource usage by setting memory and CPU usage limits on both segments and resource queues. See [Configuring Segment Resource Capacity](ConfigureResourceManagement.html) and [Creating Resource Queues](ResourceQueues.html).

**Cluster Memory to Core Ratio**

The HAWQ resource manager chooses a cluster memory to core ratio when most segments have registered and when the resource manager has received a cluster report from YARN \(if the resource manager is running in YARN mode.\) The HAWQ resource manager selects the ratio based on the amount of memory available in the cluster and the number of cores available on registered segments. The resource manager selects the smallest ratio possible in order to minimize the waste of resources.

HAWQ trims each segment's resource capacity automatically to match the selected ratio. For example, if the resource manager chooses 1GB per core as the ratio, then a segment with 5GB of memory and 8 cores will have 3 cores cut. These cores will not be used by HAWQ. If a segment has 12GB and 10 cores, then 2GB of memory will be cut by HAWQ.

After the HAWQ resource manager has selected its ratio, then the ratio will not change until you restart the HAWQ master node. Therefore, memory and core resources for any segments added dynamically to the cluster are automtaically cut based on the fixed ratio.

To find out the cluster memory to core ratio selected by the resource manager, check the HAWQ master database logs for messages similar to the following:

```
Resource manager chooses ratio 1024 MB per core as cluster level memory to core ratio, there are 3072 MB memory 0 CORE resource unable to be utilized.
```

You can also check the master logs to see how resources are being cut from individual segments due to the cluster memory to core ratio. For example:

```
Resource manager adjusts segment localhost original resource capacity from (8192 MB, 5 CORE) to (5120 MB, 5 CORE)

Resource manager adjusts segment localhost original global resource manager resource capacity from (8192 MB, 5 CORE) to (5120 MB, 5 CORE)
```

See [HAWQ Database Server Log Files](../admin/logfiles.html#topic28) for more information on working with HAWQ database server log files.
