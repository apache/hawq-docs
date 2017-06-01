---
title: Using Master Mirroring
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

There are two masters in a HAWQ cluster-- a primary master and a standby master. Clients connect to the primary master and queries can be executed only on the primary master.

You deploy a backup or mirror of the master instance on a separate host machine from the primary master so that the cluster can tolerate a single host failure. A backup master or standby master serves as a warm standby if the primary master becomes non-operational. You create a standby master from the primary master while the primary is online.

The primary master continues to provide services to users while HAWQ takes a transactional snapshot of the primary master instance. In addition to taking a transactional snapshot and deploying it to the standby master, HAWQ also records changes to the primary master. After HAWQ deploys the snapshot to the standby master, HAWQ deploys the updates to synchronize the standby master with the primary master.

After the primary master and standby master are synchronized, HAWQ keeps the standby master up to date using walsender and walreceiver, write-ahead log (WAL)-based replication processes. The walreceiver is a standby master process. The walsender process is a primary master process. The two processes use WAL-based streaming replication to keep the primary and standby masters synchronized.

Since the master does not house user data, only system catalog tables are synchronized between the primary and standby masters. When these tables are updated, changes are automatically copied to the standby master to keep it current with the primary.

*Figure 1: Master Mirroring in HAWQ*

![](../images/standby_master.jpg)


If the primary master fails, the replication process stops, and an administrator can activate the standby master. Upon activation of the standby master, the replicated logs reconstruct the state of the primary master at the time of the last successfully committed transaction. The activated standby then functions as the HAWQ master, accepting connections on the port specified when the standby master was initialized.

If the master fails, the administrator uses command line tools or Ambari to instruct the standby master to take over as the new primary master. 

**Tip:** You can configure a virtual IP address for the master and standby so that client programs do not have to switch to a different network address when the ‘active’ master changes. If the master host fails, the virtual IP address can be swapped to the actual acting master.

##Configuring Master Mirroring <a id="standby_master_configure"></a>

You can configure a new HAWQ system with a standby master during HAWQ’s installation process, or you can add a standby master later. This topic assumes you are adding a standby master to an existing node in your HAWQ cluster.

###Add a standby master to an existing system

1. Ensure the host machine for the standby master has been installed with HAWQ and configured accordingly:
    * The gpadmin system user has been created.
    * HAWQ binaries are installed.
    * HAWQ environment variables are set.
    * SSH keys have been exchanged.
    * HAWQ Master Data directory has been created.

2. Initialize the HAWQ master standby:

    a. If you use Ambari to manage your cluster, follow the instructions in [Adding a HAWQ Standby Master](ambari-admin.html#amb-add-standby).

    b. If you do not use Ambari, log in to the HAWQ master and re-initialize the HAWQ master standby node:
 
    ``` shell
    $ ssh gpadmin@<hawq_master>
    hawq_master$ . /usr/local/hawq/greenplum_path.sh
    hawq_master$ hawq init standby -s <new_standby_master>
    ```

    where \<new\_standby\_master\> identifies the hostname of the standby master.

3. Check the status of master mirroring by querying the `gp_master_mirroring system` view. See [Checking on the State of Master Mirroring](#standby_check) for instructions.

4. To activate or failover to the standby master, see [Failing Over to a Standby Master](#standby_failover).

##Failing Over to a Standby Master<a id="standby_failover"></a>

If the primary master fails, log replication stops. You must explicitly activate the standby master in this circumstance.

Upon activation of the standby master, HAWQ reconstructs the state of the master at the time of the last successfully committed transaction.

###To activate the standby master

1. Ensure that a standby master host has been configured for the system.

2. Activate the standby master:

    a. If you use Ambari to manage your cluster, follow the instructions in [Activating the HAWQ Standby Master](ambari-admin.html#amb-activate-standby).

    b. If you do not use Ambari, log in to the HAWQ master and activate the HAWQ master standby node:

	``` shell
	hawq_master$ hawq activate standby
 	```
   After you activate the standby master, it becomes the active or primary master for the HAWQ cluster.

4. (Optional, but recommended.) Configure a new standby master. See [Add a standby master to an existing system](#standby_master_configure) for instructions.
	
5. Check the status of the HAWQ cluster by executing the following command on the master:

	```shell
	hawq_master$ hawq state
	```
	
	The newly-activated master's status should be **Active**. If you configured a new standby master, its status is **Passive**. When a standby master is not configured, the command displays `-No entries found`, the message indicating that no standby master instance is configured.
	
6. If you have enabled HAWQ Ranger Authentication in high availability mode in your cluster, you must manually update the Ranger HAWQ service definition to identify the new master node. Refer to [Failover to HAWQ Standby Master](../ranger/ranger-ha.html#rps_ha_cfg_masterfailover) in the HAWQ Ranger documentation for additional information.

6. Query the `gp_segment_configuration` table to verify that segments have registered themselves to the new master:

    ``` shell
    hawq_master$ psql dbname -c 'SELECT * FROM gp_segment_configuration;'
    ```
	
7. Finally, check the status of master mirroring by querying the `gp_master_mirroring` system view. See [Checking on the State of Master Mirroring](#standby_check) for instructions.


##Checking on the State of Master Mirroring <a id="standby_check"></a>

To check on the status of master mirroring, query the `gp_master_mirroring` system view. This view provides information about the walsender process used for HAWQ master mirroring. 

```shell
hawq_master$ psql dbname -c 'SELECT * FROM gp_master_mirroring;'
```

If a standby master has not been set up for the cluster, you will see the following output:

```
 summary_state  | detail_state | log_time | error_message
----------------+--------------+----------+---------------
 Not Configured |              |          | 
(1 row)
```

If the standby is configured and in sync with the master, you will see output similar to the following:

```
 summary_state | detail_state | log_time               | error_message
---------------+--------------+------------------------+---------------
 Synchronized  |              | 2016-01-22 21:53:47+00 |
(1 row)
```

##Resynchronizing Standby with the Master <a id="resync_master"></a>

The standby can become out-of-date if the log synchronization process between the master and standby has stopped or has fallen behind. If this occurs, you will observe output similar to the following after querying the `gp_master_mirroring` view:

```
   summary_state  | detail_state | log_time               | error_message
------------------+--------------+------------------------+---------------
 Not Synchronized |              |                        |
(1 row)
```

To resynchronize the standby with the master:

1. If you use Ambari to manage your cluster:

    1. Follow the instructions in [Removing the HAWQ Standby Master](ambari-admin.html#amb-remove-standby) to remove the HAWQ Standby Master node.
    2. Follow the instructions in [Adding a HAWQ Standby Master](ambari-admin.html#amb-add-standby) to re-add the Standby Master.

2. If you do not use Ambari, execute the following command on the HAWQ master:

    ```shell
    hawq_master$ hawq init standby -n
    ```

    This command stops and restarts the master and then synchronizes the standby.
