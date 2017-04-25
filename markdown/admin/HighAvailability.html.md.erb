---
title: High Availability in HAWQ
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

A HAWQ cluster can be made highly available by providing fault-tolerant hardware, by enabling HAWQ or HDFS high-availability features, and by performing regular monitoring and maintenance procedures to ensure the health of all system components.

Hardware components eventually fail either due to normal wear or to unexpected circumstances. Loss of power can lead to temporarily unavailable components. You can make a system highly available by providing redundant standbys for components that can fail so services can continue uninterrupted when a failure does occur. In some cases, the cost of redundancy is higher than a user’s tolerance for interruption in service. When this is the case, the goal is to ensure that full service is able to be restored, and can be restored within an expected timeframe.

With HAWQ, fault tolerance and data availability is achieved with:

* [Hardware Level Redundancy (RAID and JBOD)](#ha_raid)
* [Master Mirroring](#ha_master_mirroring)
* [Dual Clusters](#ha_dual_clusters)

## <a id="ha_raid"></a>Hardware Level Redundancy (RAID and JBOD) 

As a best practice, HAWQ deployments should use RAID for master nodes and JBOD for segment nodes. Using these hardware-level systems provides high performance redundancy for single disk failure without having to go into database level fault tolerance. RAID and JBOD provide a lower level of redundancy at the disk level.

## <a id="ha_master_mirroring"></a>Master Mirroring 

There are two masters in a highly available cluster, a primary and a standby. As with segments, the master and standby should be deployed on different hosts so that the cluster can tolerate a single host failure. Clients connect to the primary master and queries can be executed only on the primary master. The secondary master is kept up-to-date by replicating the write-ahead log (WAL) from the primary to the secondary.

## <a id="ha_dual_clusters"></a>Dual Clusters 

You can add another level of redundancy to your deployment by maintaining two HAWQ clusters, both storing the same data.

The two main methods for keeping data synchronized on dual clusters are "dual ETL" and "backup/restore."

Dual ETL provides a complete standby cluster with the same data as the primary cluster. ETL (extract, transform, and load) refers to the process of cleansing, transforming, validating, and loading incoming data into a data warehouse. With dual ETL, this process is executed twice in parallel, once on each cluster, and is validated each time. It also allows data to be queried on both clusters, doubling the query throughput.

Applications can take advantage of both clusters and also ensure that the ETL is successful and validated on both clusters.

To maintain a dual cluster with the backup/restore method, create backups of the primary cluster and restore them on the secondary cluster. This method takes longer to synchronize data on the secondary cluster than the dual ETL strategy, but requires less application logic to be developed. Populating a second cluster with backups is ideal in use cases where data modifications and ETL are performed daily or less frequently.

See [Backing Up and Restoring HAWQ](BackingUpandRestoringHAWQDatabases.html) for instructions on how to backup and restore HAWQ.


