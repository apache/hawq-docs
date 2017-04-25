---
title: High Availability, Redundancy and Fault Tolerance
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

HAWQ ensures high availability for its clusters through system redundancy. HAWQ deployments utilize platform hardware redundancy, such as RAID for the master catalog, JBOD for segments and network redundancy for its interconnect layer. On the software level, HAWQ provides redundancy via master mirroring and dual cluster maintenance. In addition, HAWQ supports high availability NameNode configuration within HDFS.

To maintain cluster health, HAWQ uses a fault tolerance service based on heartbeats and on-demand probe protocols. It can identify newly added nodes dynamically and remove nodes from the cluster when it becomes unusable.

## <a id="abouthighavailability"></a>About High Availability 

HAWQ employs several mechanisms for ensuring high availability. The foremost mechanisms are specific to HAWQ and include the following:

* Master mirroring. Clusters have a standby master in the event of failure of the primary master.
* Dual clusters. Administrators can create a secondary cluster and synchronizes its data with the primary cluster either through dual ETL or backup and restore mechanisms.

In addition to high availability managed on the HAWQ level, you can enable high availability in HDFS for HAWQ by implementing the high availability feature for NameNodes. See [HAWQ Filespaces and High Availability Enabled HDFS](../admin/HAWQFilespacesandHighAvailabilityEnabledHDFS.html).


## <a id="aboutsegmentfailover"></a>About Segment Fault Tolerance 

In HAWQ, the segments are stateless. This ensures faster recovery and better availability.

When a segment fails, the segment is removed from the resource pool. Queries are no longer dispatched to the segment. When the segment is operational again, the Fault Tolerance Service verifies its state and adds the segment back to the resource pool.

## <a id="aboutinterconnectredundancy"></a>About Interconnect Redundancy 

The *interconnect* refers to the inter-process communication between the segments and the network infrastructure on which this communication relies. You can achieve a highly available interconnect by deploying dual Gigabit Ethernet switches on your network and deploying redundant Gigabit connections to the HAWQ host \(master and segment\) servers.

In order to use multiple NICs in HAWQ, NIC bounding is required.
