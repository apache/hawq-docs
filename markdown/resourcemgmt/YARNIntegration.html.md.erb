---
title: Integrating YARN with HAWQ
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

HAWQ supports integration with YARN for global resource management. In a YARN managed environment, HAWQ can request resources \(containers\) dynamically from YARN, and return resources when HAWQ's workload is not heavy. This feature makes HAWQ a native citizen of the whole Hadoop eco-system.

To integrate YARN with HAWQ, use the following high-level steps.

1.  Install YARN, if you have not already done so.

    **Note:** If you are using HDP 2.3, you must set `yarn.resourcemanager.system-metrics-publisher.enabled` to `false`. See the Release Notes for additional YARN workaround configurations.

2.  Configure YARN using CapacityScheduler and reserve one application queue exclusively for HAWQ. See [Configuring YARN for HAWQ](#hawqinputformatexample) and [Setting HAWQ Segment Resource Capacity in YARN](#topic_pzf_kqn_c5).
3.  If desired, enable high availability in YARN. See your Ambari or Hadoop documentation for details.
3.  Enable YARN mode within HAWQ. See [Enabling YARN Mode in HAWQ](#topic_rtd_cjh_15).
4.  After you integrate YARN with HAWQ, adjust HAWQ's resource usage as needed by doing any of the following:
    -   Change the capacity of the corresponding YARN resource queue for HAWQ. For example, see the properties described for CapacityScheduler configuration. You can then refresh the YARN queues without having to restart or reload HAWQ. See See [Configuring YARN for HAWQ](#hawqinputformatexample) and [Setting HAWQ Segment Resource Capacity in YARN](#topic_pzf_kqn_c5).
    -   Change resource consumption within HAWQ on a finer grained level by altering HAWQ's resource queues. See [Working with Hierarchical Resource Queues](ResourceQueues.html).
    -   \(Optional\) Tune HAWQ and YARN resource negotiations. For example, you can set a minimum number of YARN containers per segment or modify the idle timeout for YARN resources in HAWQ. See [Tune HAWQ Resource Negotiations with YARN](#topic_wp3_4bx_15).

## <a id="hawqinputformatexample"></a>Configuring YARN for HAWQ 

This topic describes how to configure YARN to manage HAWQ's resources.

When HAWQ has queries that require resources to execute, the HAWQ resource manager negotiates with YARN's resource scheduler to allocate resources. Then, when HAWQ is not busy, HAWQ's resource manager returns resources to YARN's resource scheduler.

To integrate YARN with HAWQ, you must define one YARN application resource queue exclusively for HAWQ. YARN resource queues are configured for a specific YARN resource scheduler. The YARN resource scheduler uses resource queue configuration to allocate resources to applications. There are several available YARN resource schedulers; however, HAWQ currently only supports using CapacityScheduler to manage YARN resources.

### <a id="capacity_scheduler"></a>Using CapacityScheduler for YARN Resource Scheduling 

The following example demonstrates how to configure CapacityScheduler as the YARN resource scheduler. In `yarn-site.xml`, use the following configuration to enable CapacityScheduler.

``` xml
<property>
   <name>yarn.resourcemanager.scheduler.class</name>
   <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler</value>
</property>
```

Then, define the queues in CapacityScheduler's configuration. In `capacity-scheduler.xml`, you could define the queues as follows:

``` xml
<property>
   <name>yarn.scheduler.capacity.root.queues</name>
   <value>mrque1,mrque2,hawqque</value>
</property>

```

In the above example configuration, CapacityScheduler has two MapReduce queues \(`mrque1` and `mrque2`\) and one HAWQ queue \(`hawqque`\) configured under the root queue. Only `hawqque` is defined for HAWQ usage, and it coexists with the other two MapReduce queues. These three queues share the resources of the entire cluster.

In the following configuration within `capacity-scheduler.xml,` we configure the additional properties for the queues to control the capacity of each queue. The HAWQ resource queue can utilize 20% to a maximum of 80% resources of the whole cluster.

``` xml
<property>
   <name>yarn.scheduler.capacity.hawqque.maximum-applications</name>
   <value>1</value>
</property>

<property>
  <name>yarn.scheduler.capacity.hawqque.capacity</name>
  <value>20</value>
</property>

<property>
  <name>yarn.scheduler.capacity.hawqque.maximum-capacity</name>
  <value>80</value>
</property>

<property>
  <name>yarn.scheduler.capacity.hawqque.user-limit-factor</name>
  <value>2</value>
</property>

<property>
  <name>yarn.scheduler.capacity.mrque1.capacity</name>
  <value>30</value>
</property>

<property>
  <name>yarn.scheduler.capacity.mrque1.maximum-capacity</name>
  <value>50</value>
</property>

<property>
  <name>yarn.scheduler.capacity.mrque2.capacity</name>
  <value>50</value>
</property>

<property>
  <name>yarn.scheduler.capacity.mrque2.maximum-capacity</name>
  <value>50</value>
</property>
```

|Item|Description|
|----|-----------|
|yarn.scheduler.capacity.*\<queue\_name\>*.maximum-applications|Maximum number of HAWQ applications in the system that can be concurrently active \(both running and pending.\) The current recommendation is to let one HAWQ instance exclusively use one resource queue.|
|yarn.scheduler.capacity.*\<queue\_name\>*.capacity|Queue capacity in percentage \(%\) as a float \(e.g. 12.5\). The sum of capacities for all queues, at each level, must equal 100. Applications in the queue may consume more resources than the queue's capacity if there are free resources, which provides elasticity.|
|yarn.scheduler.capacity.*\<queue\_name\>*.maximum-capacity|Maximum queue capacity in percentage \(%\) as a float. This limits the elasticity for applications in the queue. Defaults to -1 which disables it.|
|yarn.scheduler.capacity.*\<queue\_name\>*.user-limit-factor|Multiple of the queue capacity, which can be configured to allow a single user to acquire more resources. By default this is set to 1, which ensures that a single user can never take more than the queue's configured capacity irrespective of how idle the cluster is. Value is specified as a float.<br/><br/>Setting this to a value higher than 1 allows the overcommittment of resources at the application level. For example, in terms of HAWQ configuration, if we want twice the maximum capacity for the HAWQ's application, we can set this as 2.|

## <a id="topic_pzf_kqn_c5"></a>Setting HAWQ Segment Resource Capacity in YARN 

Similar to how you can set segment resource capacity in HAWQ's standalone mode, you can do the same for HAWQ segments managed by YARN.

In HAWQ standalone mode, you can configure the resource capacity of individual segments as described in [Configuring Segment Resource Capacity](ConfigureResourceManagement.html). If you are using YARN to manage HAWQ resources, then you configure the resource capacity of segments by configuring YARN. We recommend that you configure all segments with identical resource capacity. In `yarn-site.xml`, set the following properties:

``` xml
<property>
  <name>yarn.nodemanager.resource.memory-mb</name>
  <value>4GB</value>
</property>
<property>
  <name>yarn.nodemanager.resource.cpu-vcores</name>
  <value>1</value>
</property>
```

We recommend that in your memory to core ratio that memory is a multiple of 1GB, such as 1GB per core, 2GB per core or 4 GB per core. 

After you set limits on the segments, you can use resource queues to configure additional resource management rules in HAWQ.

### <a id="avoid_fragmentation"></a>Avoiding Resource Fragmentation with YARN Managed Resources 

To reduce the likelihood of resource fragmentation in deployments where resources are managed by YARN, ensure that you have configured the following:

-   Segment resource capacity configured in `yarn.nodemanager.resource.memory-mb` must be a multiple of the virtual segment resource quotas that you configure in your resource queues
-   CPU to memory ratio must be a multiple of the amount configured for `yarn.scheduler.minimum-allocation-mb`

For example, if you have the following properties set in YARN:

-   `yarn.scheduler.minimum-allocation-mb=1gb`

    **Note:** This is the default value set by Ambari in some cases.

-   `yarn.nodemanager.resource.memory-mb=48gb`
-   `yarn.nodemanager.resource.cpu-vcores=16`

Then the CPU to memory ratio calculated by HAWQ equals 3GB \(48 divided by 16\). Since `yarn.scheduler.minimum-allocation-mb` is set to 1GB, each YARN container will be 1GB. Since 3GB is a multiple of 1GB, you should not encounter fragmentation.

However, if you had set `yarn.scheduler.minimum-allocation-mb` to 4GB, then it would leave 1GB of fragmented space \(4GB minus 3GB.\) To prevent fragmentation in this scenario, you could reconfigure `yarn.nodemanager.resource.memory-mb=64gb` \(or you could set `yarn.scheduler.minimum-allocation-mb=1gb`.\)

**Note:** If you are specifying 1GB or under for `yarn.scheduler.minimum-allocation-mb` in `yarn-site.xml`, then make sure that the property is an equal subdivision of 1GB. For example, 1024, 512.

See [Handling Segment Resource Fragmentation](../troubleshooting/Troubleshooting.html) for general information on resource fragmentation.

## <a id="topic_rtd_cjh_15"></a>Enabling YARN Mode in HAWQ 

After you have properly configured YARN, you can enable YARN as HAWQ's global resource manager.

To configure YARN as the global resource manager in a HAWQ cluster, add the following property configuration to your `hawq-site.xml` file:

``` xml
<property>
      <name>hawq_global_rm_type</name>
      <value>yarn</value>
</property>
```

When enabled, the HAWQ resource manager only uses resources allocated from YARN.

### Configuring HAWQ in YARN Environments

If you set the global resource manager to YARN, you must also configure the following properties in `hawq-site.xml`:

``` xml
<property>
      <name>hawq_rm_yarn_address</name>
      <value>localhost:8032</value>
</property>
<property>
      <name>hawq_rm_yarn_scheduler_address</name>
      <value>localhost:8030</value>
</property>
<property>
      <name>hawq_rm_yarn_queue_name</name>
      <value>hawqque</value></property>
<property>
      <name>hawq_rm_yarn_app_name</name>
      <value>hawq</value>
</property>
```
**Note:** If you have enabled high availability for your YARN resource managers, then you must configure `yarn.resourcemanager.ha` and `yarn.resourcemanager.scheduler.ha` in `yarn-client.xml` located in `$GPHOME/etc` instead. The values specified for `hawq_rm_yarn_address` and `hawq_rm_yarn_scheduler_address` are ignored. See [Configuring HAWQ in High Availablity-Enabled YARN Environments](#highlyavailableyarn)

#### <a id="id_uvp_3pm_q5"></a>hawq\_rm\_yarn\_address 

Server address \(host and port\) of the YARN resource manager server \(the value of `yarn.resourcemanager.address`\). User must define this if `hawq_global_rm_type` is set to `yarn`. For example, `localhost:8032`.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
|valid hostname and port| none set |master|

#### <a id="id_ocq_jpm_q5"></a>hawq\_rm\_yarn\_scheduler\_address 

Server address \(host and port\) of the YARN resource manager scheduler \(the value of `yarn.resourcemanager.scheduler.address`\). User must define this if `hawq_global_rm_type` is set to `yarn`. For example, `localhost:8030`.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
|valid hostname and port| none set |master|

#### <a id="id_y23_kpm_q5"></a>hawq\_rm\_yarn\_queue\_name 

The name of the YARN resource queue to register with HAWQ's resource manager.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
|string|default|master|

#### <a id="id_h1c_lpm_q5"></a>hawq\_rm\_yarn\_app\_name 

The name of the YARN application registered with HAWQ's resource manager. For example, `hawq`.

|Value Range|Default|Set Classifications|
|-----------|-------|-------------------|
|string|hawq|master|

### <a id="highlyavailableyarn"></a>Configuring HAWQ in High Availablity-Enabled YARN Environments 

If you have enabled high-availability for your YARN resource managers, then specify the following parameters in `yarn-client.xml` located in `$GPHOME/etc` instead. 

**Note:** When you use high availability in YARN, HAWQ ignores the values specified for `hawq_rm_yarn_address` and `hawq_rm_yarn_scheduler_address` in `hawq-site.xml` and uses the values specified in `yarn-client.xml` instead.

``` xml
    <property>
      <name>yarn.resourcemanager.ha</name>
      <value>{0}:8032,{1}:8032</value>
    </property>
    
    <property>
      <name>yarn.resourcemanager.scheduler.ha</name>
      <value>{0}:8030,{1}:8030</value>
    </property>
```

where {0} and {1} are substituted with the fully qualified hostnames of the YARN resource manager host machines.

To reduce connection time between HAWQ and YARN, be sure to specify the YARN master hostname first in the `yarn.resourcemanager.*` property lists, and the YARN standby resource manager hostname second in the lists.

## <a id="topic_wp3_4bx_15"></a>Tune HAWQ Resource Negotiations with YARN 

To ensure efficient management of resources and highest performance, you can configure some aspects of how HAWQ's resource manager negotiate resources from YARN.

### <a id="min_yarn_containers"></a>Minimum Number of YARN Containers Per Segment 

When HAWQ is integrated with YARN and has no workload, HAWQ does not acquire any resources right away. HAWQ's 's resource manager only requests resource from YARN when HAWQ receives its first query request. In order to guarantee optimal resource allocation for subsequent queries and to avoid frequent YARN resource negotiation, you can adjust `hawq_rm_min_resource_perseg` so HAWQ receives at least some number of YARN containers per segment regardless of the size of the initial query. The default value is 2, which means HAWQ's resource manager acquires at least 2 YARN containers for each segment even if the first query's resource request is small.

This configuration property cannot exceed the capacity of HAWQ’s YARN queue. For example, if HAWQ's queue capacity in YARN is no more than 50% of the whole cluster, and each YARN node has a maximum of 64GB memory and 16 vcores, then `hawq_rm_min_resource_perseg` in HAWQ cannot be set to more than 8 since HAWQ's resource manager acquires YARN containers by vcore. In the case above, the HAWQ resource manager acquires a YARN container quota of 4GB memory and 1 vcore.

### <a id="set_yarn_timeout"></a>Setting a Timeout for YARN Resources 

If the level of HAWQ’s workload is lowered, then HAWQ's resource manager may have some idle YARN resources. You can adjust `hawq_rm_resource_idle_timeout` to let the HAWQ resource manager return idle resources more quickly or more slowly.

For example, when HAWQ's resource manager has to reacquire resources, it can cause latency for query resource requests. To let HAWQ resource manager retain resources longer in anticipation of an upcoming workload, increase the value of `hawq_rm_resource_idle_timeout`. The default value of `hawq_rm_resource_idle_timeout` is 300 seconds.
