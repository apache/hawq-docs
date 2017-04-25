---
title: Troubleshooting
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

This chapter describes how to resolve common problems and errors that occur in a HAWQ system.



## <a id="topic_dwd_rnx_15"></a>Query Performance Issues

**Problem:** Query performance is slow.

**Cause:** There can be multiple reasons why a query might be performing slowly. For example, the locality of data distribution, the number of virtual segments, or the number of hosts used to execute the query can all affect its performance. The following procedure describes how to investigate query performance issues.

### <a id="task_ayl_pbw_c5"></a>How to Investigate Query Performance Issues

A query is not executing as quickly as you would expect. Here is how to investigate possible causes of slowdown:

1.  Check the health of the cluster.
    1.  Are any DataNodes, segments or nodes down?
    2.  Are there many failed disks?

2.  Check table statistics. Have the tables involved in the query been analyzed?
3.  Check the plan of the query and run [`EXPLAIN ANALYZE`](../reference/sql/EXPLAIN.html) to determine the bottleneck. 
    Sometimes, there is not enough memory for some operators, such as Hash Join, or spill files are used. If an operator cannot perform all of its work in the memory allocated to it, it caches data on disk in *spill files*. Compared with no spill files, a query will run much slower.

4.  Check data locality statistics using [`EXPLAIN ANALYZE`](../reference/sql/EXPLAIN.html). Alternately you can check the logs. Data locality result for every query could also be found in the log of HAWQ. See [Data Locality Statistics](../query/query-performance.html#topic_amk_drc_d5) for information on the statistics.
5.  Check resource queue status. You can query view `pg_resqueue_status` to check if the target queue has already dispatched some resource to the queries, or if the target queue is lacking resources. See [Checking Existing Resource Queues](../resourcemgmt/ResourceQueues.html#topic_lqy_gls_zt).
6.  Analyze a dump of the resource manager's status to see more resource queue status. See [Analyzing Resource Manager Status](../resourcemgmt/ResourceQueues.html#topic_zrh_pkc_f5).

## <a id="topic_vm5_znx_15"></a>Rejection of Query Resource Requests

**Problem:** HAWQ resource manager is rejecting query resource allocation requests.

**Cause:** The HAWQ resource manager will reject resource query allocation requests under the following conditions:

-   **Too many physical segments are unavailable.**

    HAWQ resource manager expects that the physical segments listed in file `$GPHOME/etc/slaves` are already registered and can be queried from table `gp_segment_configuration`.

    If the resource manager determines that the number of unregistered or unavailable HAWQ physical segments is greater than [hawq\_rm\_rejectrequest\_nseg\_limit](../reference/guc/parameter_definitions.html#hawq_rm_rejectrequest_nseg_limit), then the resource manager rejects query resource requests directly. The purpose of rejecting the query is to guarantee that queries are run in a full size cluster. This makes diagnosing query performance problems easier. The default value of `hawq_rm_rejectrequest_nseg_limit` is 0.25, which means that if more than 0.25 \* the number segments listed in `$GPHOME/etc/slaves` are found to be unavailable or unregistered, then the resource manager rejects the query's request for resources. For example, if there are 15 segments listed in the slaves file, the resource manager calculates that no more than 4 segments (0.25 \* 15) can be unavailable

    In most cases, you do not need to modify this default value.

-   **There are unused physical segments with virtual segments allocated for the query.**

    The limit defined in [hawq\_rm\_tolerate\_nseg\_limit](../reference/guc/parameter_definitions.html#hawq_rm_tolerate_nseg_limit) has been exceeded.

-   **Virtual segments have been dispatched too unevenly across physical segments.**

    To ensure best query performance, HAWQ resource manager tries to allocate virtual segments for query execution as evenly as possible across physical segments. However, there can be variance in allocations. HAWQ will reject query resource allocation requests that have a variance greater than the value set in [hawq\_rm\_nvseg\_variance\_amon\_seg\_limit](../reference/guc/parameter_definitions.html#hawq_rm_nvseg_variance_amon_seg_limit)

    For example, one query execution causes nine (9) virtual segments to be dispatched to two (2) physical segments. Assume that one segment has been allocated seven (7) virtual segments and another one has allocated two (2) virtual segments. Then the variance between the segments is five (5). If `hawq_rm_nvseg_variance_amon_seg_limit` is set to the default of one (1), then the allocation of resources for this query is rejected and will be reallocated later. However, if a physical segment has five virtual segments and the other physical segment has four (4), then this resource allocation is accepted.

**Solution:** Check on the status of the nodes in the cluster. Restart existing nodes, if necessary, or add new nodes. Modify the [hawq\_rm\_nvseg\_variance\_amon\_seg\_limit](../reference/guc/parameter_definitions.html#hawq_rm_nvseg_variance_amon_seg_limit) (although note that this can affect query performance.)

## <a id="topic_qq4_rkl_wv"></a>Queries Cancelled Due to High VMEM Usage

**Problem:** Certain queries are cancelled due to high virtual memory usage. Example error message:

``` pre
ERROR: Canceling query because of high VMEM usage. Used: 1748MB, available 480MB, red zone: 9216MB (runaway_cleaner.c:135) (seg74 bcn-w3:5532 pid=33619) (dispatcher.c:1681)
```

**Cause:** This error occurs when the virtual memory usage on a segment exceeds the virtual memory threshold, which is can configured as a percentage through the [runaway\_detector\_activation\_percent](../reference/guc/parameter_definitions.html#runaway_detector_activation_percent).

If the amount of virtual memory utilized by a physical segment exceeds the calculated threshold, then HAWQ begins terminating queries based on memory usage, starting with the query that is consuming the largest amount of memory. Queries are terminated until the percentage of utilized virtual memory is below the specified percentage.

**Solution:** Try temporarily increasing the value of `hawq_re_memory_overcommit_max` to allow specific queries to run without error.

Check `pg_log` files for more memory usage details on session and QE processes. HAWQ logs terminated query information such as memory allocation history and context information as well as query plan operator memory usage information. This information is sent to the master and segment instance log files.

## <a id="topic_hlj_zxx_15"></a>Segments Do Not Appear in gp\_segment\_configuration

**Problem:** Segments have successfully started, but cannot be found in table `gp_segment_configuration`.

**Cause:** Your segments may have been assigned identical IP addresses.

Some software and projects have virtualized network interfaces that use auto-configured IP addresses. This may cause some HAWQ segments to obtain identical IP addresses. The resource manager's fault tolerance service component will only recognize one of the segments with an identical IP address.

**Solution:** Change your network's configuration to disallow identical IP addresses before starting up the HAWQ cluster.

## <a id="investigatedownsegment"></a>Investigating Segments Marked As Down 

**Problem:** The [HAWQ fault tolerance service (FTS)](../admin/FaultTolerance.html) has marked a segment as down in the [gp_segment_configuration](../reference/catalog/gp_segment_configuration.html) catalog table.

**Cause:**  FTS marks a segment as down when a segment encounters a critical error. For example, a temporary directory on the segment fails due to a hardware error. Other causes might include network or communication errors, resource manager errors, or simply a heartbeat timeout. The segment reports critical failures to the HAWQ master through a heartbeat report.

**Solution:** The actions required for recovering a segment varies depending upon the reason. In some cases, the segment is only marked as down temporarily until the heartbeat interval can recheck the segment's status. To investigate the reason why the segment was marked down, check the gp_configuration_history catalog table for a corresponding reason. See [Viewing the Current Status of a Segment](../admin/FaultTolerance.html#view_segment_status) for a description of various reasons that the fault tolerance service may mark a segment as down.

## <a id="topic_mdz_q2y_15"></a>Handling Segment Resource Fragmentation

Different HAWQ resource queues can have different virtual segment resource quotas, which can result in resource fragmentation. For example, a HAWQ cluster has 4GB memory available for a currently queued query, but the resource queues are configured to split four 512MB memory blocks in 4 different segments. It is impossible to allocate two 1GB memory virtual segments.

In standalone mode, the segment resources are all exclusively occupied by HAWQ. Resource fragmentation can occur when segment capacity is not a multiple of a virtual segment resource quota. For example, a segment has 15GB memory capacity, but the virtual segment resource quota is set to 2GB. The maximum possible memory consumption in a segment is 14GB. Therefore, you should configure segment resource capacity as a multiple of all virtual segment resource quotas.

In YARN mode, resources are allocated from the YARN resource manager. The HAWQ resource manager acquires a YARN container by 1 vcore. For example, if YARN reports that a segment having 64GB memory and 16 vcore is configured for YARN applications, HAWQ requests YARN containers by 4GB memory and 1 vcore. In this manner, HAWQ resource manager acquires YARN containers on demand. If the capacity of the YARN container is not a multiple of the virtual segment resource quota, resource fragmentation may occur. For example, if the YARN container resource capacity is 3GB memory 1 vcore, one segment may have 1 or 3 YARN containers for HAWQ query execution. In this situation, if the virtual segment resource quota is 2GB memory, then HAWQ will always have 1 GB memory that cannot be utilized. Therefore, it is recommended to configure YARN node resource capacity carefully to make YARN container resource quota as a multiple of all virtual segment resource quotas. In addition, make sure your CPU to memory ratio is a multiple of the amount configured for `yarn.scheduler.minimum-allocation-mb`. See [Setting HAWQ Segment Resource Capacity in YARN](../resourcemgmt/YARNIntegration.html#topic_pzf_kqn_c5) for more information.

If resource fragmentation occurs, queued requests are not processed until either some running queries return resources or the global resource manager provides more resources. If you encounter resource fragmentation, you should double check the configured capacities of the resource queues for any errors. For example, an error might be that the global resource manager container's memory to core ratio is not a multiple of virtual segment resource quota.


