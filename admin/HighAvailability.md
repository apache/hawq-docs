---
title: High Availability in HAWQ
---

A HAWQ cluster can be made highly available by providing fault-tolerant hardware, by enabling HAWQ or HDFS high-availability features, and by performing regular monitoring and maintenance procedures to ensure the health of all system components.

Hardware components eventually fail either due to normal wear or to unexpected circumstances. Loss of power can lead to temporarily unavailable components. You can make a system highly available by providing redundant standbys for components that can fail so services can continue uninterrupted when a failure does occur. In some cases, the cost of redundancy is higher than a user’s tolerance for interruption in service. When this is the case, the goal is to ensure that full service is able to be restored, and can be restored within an expected timeframe.

With HAWQ, fault tolerance and data availability is achieved with:

* [Hardware Level RAID](#ha_raid)
* [Master Mirroring](#ha_master_mirroring)
* [Dual Clusters](#ha_dual_clusters)

## Hardware Level RAID <a id="ha_raid"></a>

As a best practice, HAWQ deployments use hardware level RAID to provide high performance redundancy for single disk failure without having to go into the database level fault tolerance. This provides a lower level of redundancy at the disk level.

## Master Mirroring <a id="ha_master_mirroring"></a>

There are two masters in a highly available cluster, a primary and a standby. As with segments, the master and standby should be deployed on different hosts so that the cluster can tolerate a single host failure. Clients connect to the primary master and queries can be executed only on the primary master. The secondary master is kept up-to-date by replicating the write-ahead log (WAL) from the primary to the secondary.

## Dual Clusters <a id="ha_dual_clusters"></a>

You can add another level of redundancy to your deployment by maintaining two HAWQ clusters, both storing the same data.

The main two methods for keeping data synchronized on dual clusters are "dual ETL" and "backup/restore."

Dual ETL provides a complete standby cluster with the same data as the primary cluster. ETL (extract, transform, and load) refers to the process of cleansing, transforming, validating, and loading incoming data into a data warehouse. With dual ETL, this process is executed twice in parallel, once on each cluster, and is validated each time. It also allows data to be queried on both clusters, doubling the query throughput.

Applications can take advantage of both clusters and also ensure that the ETL is successful and validated on both clusters.

To maintain a dual cluster with the backup/restore method, create backups of the primary cluster and restore them on the secondary cluster. This method takes longer to synchronize data on the secondary cluster than the dual ETL strategy, but requires less application logic to be developed. Populating a second cluster with backups is ideal in use cases where data modifications and ETL are performed daily or less frequently.

See [Backing Up and Restoring HAWQ](BackingUpandRestoringHAWQDatabases.html) for instructions on how to backup and restore HAWQ.


