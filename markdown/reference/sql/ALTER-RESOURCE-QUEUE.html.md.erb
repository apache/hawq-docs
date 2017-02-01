---
title: ALTER RESOURCE QUEUE
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

Modify an existing resource queue.

## <a id="topic1__section2"></a>Synopsis

```pre
ALTER RESOURCE QUEUE <name> WITH (<queue_attribute>=<value> [, ... ])
```

where \<queue\_attribute\> is:

```pre
   [MEMORY_LIMIT_CLUSTER=<percentage>]
   [CORE_LIMIT_CLUSTER=<percentage>]
   [ACTIVE_STATEMENTS=<integer>]
   [ALLOCATION_POLICY='even']
   [VSEG_RESOURCE_QUOTA='mem:<memory_units>']
   [RESOURCE_OVERCOMMIT_FACTOR=<double>]
   [NVSEG_UPPER_LIMIT=<integer>]
   [NVSEG_LOWER_LIMIT=<integer>]
   [NVSEG_UPPER_LIMIT_PERSEG=<double>]
   [NVSEG_LOWER_LIMIT_PERSEG=<double>]
```
```
   <memory_units> ::= {128mb|256mb|512mb|1024mb|2048mb|4096mb|
                       8192mb|16384mb|1gb|2gb|4gb|8gb|16gb}
   <percentage> ::= <integer>%
```

## <a id="topic1__section3"></a>Description

Changes attributes for an existing resource queue in HAWQ. You cannot change the parent of an existing resource queue, and you cannot change a resource queue while it is active. Only a superuser can modify a resource queue.

Resource queues with an `ACTIVE_STATEMENTS` threshold set a maximum limit on the number parallel active query statements that can be executed by roles assigned to the leaf queue. It controls the number of active queries that are allowed to run at the same time. The value for `ACTIVE_STATEMENTS` should be an integer greater than 0. If not specified, the default value is 20.

When modifying the resource queue, use the MEMORY\_LIMIT\_CLUSTER and CORE\_LIMIT\_CLUSTER to tune the allowed resource usage of the resource queue. MEMORY\_LIMIT\_CLUSTER and CORE\_LIMIT\_CLUSTER must be equal for the same resource queue. In addition the sum of the percentages of MEMORY\_LIMIT\_CLUSTER (and CORE\_LIMIT\_CLUSTER) for resource queues that share the same parent cannot exceed 100%.

To modify the role associated with the resource queue, use the [ALTER ROLE](ALTER-ROLE.html) or [CREATE ROLE](CREATE-ROLE.html) command. You can only assign roles to the leaf-level resource queues (resource queues that do not have any children.)

The default memory allotment can be overridden on a per-query basis by using `hawq_rm_stmt_vseg_memory` and` hawq_rm_stmt_nvseg` configuration parameters. See [Configuring Resource Quotas for Query Statements](../../resourcemgmt/ConfigureResourceManagement.html#topic_g2p_zdq_15).

To see the status of a resource queue, see [Checking Existing Resource Queues](../../resourcemgmt/ResourceQueues.html#topic_lqy_gls_zt).

See also [Best Practices for Using Resource Queues](../../bestpractices/managing_resources_bestpractices.html#topic_hvd_pls_wv).

## <a id="topic1__section4"></a>Parameters

<dt> \<name\>   </dt>
<dd>Required. The name of the resource queue you wish to modify.</dd>

<!-- -->

<dt>MEMORY\_LIMIT\_CLUSTER=\<percentage\> </dt>
<dd>Required. Defines how much memory a resource queue can consume from its parent resource queue and consequently dispatch to the execution of parallel statements. The valid values are 1% to 100%. The value of MEMORY\_ LIMIT\_CLUSTER must be identical to the value of CORE\_LIMIT\_CLUSTER. The sum of values for MEMORY\_LIMIT\_CLUSTER of this queue plus other queues that share the same parent cannot exceed 100%. The HAWQ resource manager periodically validates this restriction.

**Note:** If you want to increase the percentage, you may need to decrease the percentage of any resource queue(s) that share the same parent resource queue first. The total cannot exceed 100%.</dd>

<dt>CORE\_LIMIT\_CLUSTER=\<percentage\> </dt>
<dd>Required. The percentage of consumable CPU (virtual core) resources that the resource queue can take from its parent resource queue. The valid values are 1% to 100%. The value of CORE\_ LIMIT\_CLUSTER must be identical to the value of MEMORY\_LIMIT\_CLUSTER. The sum of values for CORE\_LIMIT\_CLUSTER of this queue and queues that share the same parent cannot exceed 100%.

**Note:** If you want to increase the percentage, you may need to decrease the percentage of any resource queue(s) that share the same parent resource queue first. The total cannot exceed 100%.</dd>

<dt>ACTIVE\_STATEMENTS=\<integer\> </dt>
<dd>Optional. Defines the limit of the number of parallel active statements in one leaf queue. The maximum number of connections cannot exceed this limit. If this limit is reached, the HAWQ resource manager queues more query allocation requests. Note that a single session can have several concurrent statement executions that occupy multiple connection resources. The value for `ACTIVE_STATEMENTS` should be an integer greater than 0. The default value is 20.</dd>

<dt>ALLOCATION\_POLICY=\<string\> </dt>
<dd>Optional. Defines the resource allocation policy for parallel statement execution. The default value is `even`.

**Note:** This release only supports an `even` allocation policy. Even if you do not specify this attribute, the resource queue still applies an `even` allocation policy. Future releases will support alternative allocation policies.

Setting the allocation policy to `even` means resources are always evenly dispatched based on current concurrency. When multiple query resource allocation requests are queued, the resource queue tries to evenly dispatch resources to queued requests until one of the following conditions are encountered:

-   There are no more allocated resources in this queue to dispatch, or
-   The ACTIVE\_STATEMENTS limit has been reached

For each query resource allocation request, the HAWQ resource mananger determines the minimum and maximum size of a virtual segment based on multiple factors including query cost, user configuration, table properties, and so on. For example, a hash distributed table requires fixed size of virtual segments. With an even allocation policy, the HAWQ resource manager uses the minimum virtual segment size requirement and evenly dispatches resources to each query resource allocation request in the resource queue.</dd>

<dt>VSEG\_RESOURCE\_QUOTA='mem:{128mb | 256mb | 512mb | 1024mb | 2048mb | 4096mb | 8192mb | 16384mb | 1gb | 2gb | 4gb | 8gb | 16gb}'</dt>
<dd>Optional. This quota defines how resources are split across multiple virtual segments. For example, when the HAWQ resource manager determines that 256GB memory and 128 vcores should be allocated to the current resource queue, there are multiple solutions on how to divide the resources across virtual segments. For example, you could use a) 2GB/1 vcore \* 128 virtual segments or b) 1GB/0.5 vcore \* 256 virtual segments. Therefore, you can use this attribute to make the HAWQ resource manager calculate the number of virtual segments based on how to divide the memory. For example, if `VSEG_RESOURCE_QUOTA``='mem:512mb'`, then the resource queue will use 512MB/0.25 vcore \* 512 virtual segments. The default value is '`mem:256mb`'.

**Note:** To avoid resource fragmentation, make sure that the segment resource capacity configured for HAWQ (in HAWQ Standalone mode: `hawq_rm_memory_limit_perseg`; in YARN mode: `yarn.nodemanager.resource.memory-mb` must be a multiple of the resource quotas for all virtual segments and CPU to memory ratio must be a multiple of the amount configured for `yarn.scheduler.minimum-allocation-mb`.</dd>

<dt>RESOURCE\_OVERCOMMIT\_FACTOR=\<double\> </dt>
<dd>Optional. This factor defines how much a resource can be overcommitted. The default value is `2.0`. For example, if RESOURCE\_OVERCOMMIT\_FACTOR is set to 3.0 and MEMORY\_LIMIT\_CLUSTER is set to 30%, then the maximum possible resource allocation in this queue is 90% (30% x 3.0). If the resulting maximum is bigger than 100%, then 100% is adopted. The minimum value that this attribute can be set to is `1.0`.</dd>

<dt>NVSEG\_UPPER\_LIMIT=\<integer\> / NVSEG\_UPPER\_LIMIT\_PERSEG=\<double\>  </dt>
<dd>Optional. These limits restrict the range of number of virtual segments allocated in this resource queue for executing one query statement. NVSEG\_UPPER\_LIMIT defines an upper limit of virtual segments for one statement execution regardless of actual cluster size, while NVSEG\_UPPER\_LIMIT\_PERSEG defines the same limit by using the average number of virtual segments in one physical segment. Therefore, the limit defined by NVSEG\_UPPER\_LIMIT\_PERSEG varies dynamically according to the changing size of the HAWQ cluster.

For example, if you set `NVSEG_UPPER_LIMIT=10` all query resource requests are strictly allocated no more than 10 virtual segments. If you set NVSEG\_UPPER\_LIMIT\_PERSEG=2 and assume that currently there are 5 available HAWQ segments in the cluster, query resource requests are allocated 10 virtual segments at the most.

NVSEG\_UPPER\_LIMIT cannot be set to a lower value than NVSEG\_LOWER\_LIMIT if both limits are enabled. In addition, the upper limit cannot be set to a value larger than the value set in global configuration parameter `hawq_rm_nvseg_perquery_limit` and `hawq_rm_nvseg_perquery_perseg_limit`.

By default, both limits are set to **-1**, which means the limits are disabled. `NVSEG_UPPER_LIMIT` has higher priority than `NVSEG_UPPER_LIMIT_PERSEG`. If both limits are set, then `NVSEG_UPPER_LIMIT_PERSEG` is ignored. If you have enabled resource quotas for the query statement, then these limits are ignored.

**Note:** If the actual lower limit of the number of virtual segments becomes greater than the upper limit, then the lower limit is automatically reduced to be equal to the upper limit. This situation is possible when user sets both `NVSEG_UPPER_LIMIT `and `NVSEG_LOWER_LIMIT_PERSEG`. After expanding the cluster, the dynamic lower limit may become greater than the value set for the fixed upper limit.</dd>

<dt>NVSEG\_LOWER\_LIMIT=\<integer\> / NVSEG\_LOWER\_LIMIT\_PERSEG=\<double\>   </dt>
<dd>Optional. These limits specify the minimum number of virtual segments allocated for one statement execution in order to guarantee query performance. NVSEG\_LOWER\_LIMIT defines the lower limit of virtual segments for one statement execution regardless the actual cluster size, while NVSEG\_LOWER\_LIMIT\_PERSEG defines the same limit by the average virtual segment number in one segment. Therefore, the limit defined by NVSEG\_LOWER\_LIMIT\_PERSEG varies dynamically along with the size of HAWQ cluster.

NVSEG\_UPPER\_LIMIT\_PERSEG cannot be less than NVSEG\_LOWER\_LIMIT\_PERSEG if both limits are set enabled.

For example, if you set NVSEG\_LOWER\_LIMIT=10, and one statement execution potentially needs no fewer than 10 virtual segments, then this request has at least 10 virtual segments allocated. If you set NVSEG\_UPPER\_LIMIT\_PERSEG=2, assuming there are currently 5 available HAWQ segments in the cluster, and one statement execution potentially needs no fewer than 10 virtual segments, then the query resource request will be allocated at least 10 virtual segments. If one statement execution needs at most 4 virtual segments, the resource manager will allocate at most 4 virtual segments instead of 10 since this resource request does not need more than 9 virtual segments.

By default, both limits are set to **-1**, which means the limits are disabled. `NVSEG_LOWER_LIMIT` has higher priority than `NVSEG_LOWER_LIMIT_PERSEG`. If both limits are set, then `NVSEG_LOWER_LIMIT_PERSEG` is ignored. If you have enabled resource quotas for the query statement, then these limits are ignored.

**Note:** If the actual lower limit of the number of virtual segments becomes greater than the upper limit, then the lower limit is automatically reduced to be equal to the upper limit. This situation is possible when user sets both `NVSEG_UPPER_LIMIT `and `NVSEG_LOWER_LIMIT_PERSEG`. After expanding the cluster, the dynamic lower limit may become greater than the value set for the fixed upper limit. </dd>

## <a id="topic1__section6"></a>Examples

Change the memory and core limit of a resource queue:

```pre
ALTER RESOURCE QUEUE test_queue_1 WITH (MEMORY_LIMIT_CLUSTER=40%,
CORE_LIMIT_CLUSTER=40%);
```

Change the active statements maximum for the resource queue:

```pre
ALTER RESOURCE QUEUE test_queue_1 WITH (ACTIVE_STATEMENTS=50);
```

## <a id="topic1__section7"></a>Compatibility

`ALTER RESOURCE QUEUE` is a HAWQ extension. There is no provision for resource queues or workload management in the SQL standard.

## <a id="topic1__section8"></a>See Also

[ALTER ROLE](ALTER-ROLE.html), [CREATE RESOURCE QUEUE](CREATE-RESOURCE-QUEUE.html), [CREATE ROLE](CREATE-ROLE.html), [DROP RESOURCE QUEUE](DROP-RESOURCE-QUEUE.html)
