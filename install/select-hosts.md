---
title: Select HAWQ Host Machines
---

Before you begin to install HAWQ, follow these steps to select and prepare the host machines.

Complete this procedure for all HAWQ deployments:

1.  Choose the host machines that will host a HAWQ segment. Keep in mind these restrictions and requirements:
    -   Each host must meet the system requirements for the version of HAWQ you are installing.
    -   Hosts that run other PostgreSQL instances cannot be used to run a default HAWQ master or standby service configuration. The default PostgreSQL port \(5432\) conflicts with the default port assignment of those services. You must either change the default port configuration of the running PostgreSQL instance or change the HAWQ master port setting during the HAWQ service installation to avoid port conflicts.

        **Note:** The Ambari server node uses PostgreSQL as the default metadata database. The Hive Metastore uses MySQL as the default metadata database.
    -   Each HAWQ segment must be co-located on a host that runs an HDFS data node.
    -   The HAWQ master segment and standby master segment must be hosted on separate machines.
2.  Choose the host machines that will run PXF:
    -   PXF must be installed on the HDFS NameNode *and* on all HDFS data nodes.
    -   If you have configured Hadoop with high availability, PXF must also be installed on all HDFS nodes including all NameNode services.
    -   If you want to use PXF with HBase or Hive, you must first install the HBase client \(hbase-client\) and/or Hive client \(hive-client\) on each machine where you intend to install PXF. See the [HDP installation documentation](http://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.3.4/index.html) for more information.
