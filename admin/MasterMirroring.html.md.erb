---
title: Using Master Mirroring
---

There are two masters in a HAWQ cluster-- a primary master and a standby master. Clients connect to the primary master and queries can be executed only on the primary master.

You deploy a backup or mirror of the master instance on a separate host machine from the primary master so that the cluster can tolerate a single host failure. A backup master or standby master serves as a warm standby if the primary master becomes non-operational. You create a standby master from the primary master while the primary is online.

The primary master continues to provide services to users while HAWQ takes a transactional snapshot of the primary master instance. While HAWQ takes transactional snapshot and deploys it to the standby master, HAWQ also records changes to the primary master. After HAWQ deploys the snapshot to the standby master, HAWQ deploys the updates to synchronize the standby master with the primary master.

After the primary master and standby master are synchronized, HAWQ keeps the standby master up to date by walsender and walreceiver, which are write-ahead log (WAL)-based replication processes. The walreceiver is a standby master process. The walsender process is a primary master process. The two processes use WAL-based streaming replication to keep the primary and standby masters synchronized.

Since the master does not house user data, only system catalog tables are synchronized between the primary and standby masters. When these tables are updated, changes are automatically copied to the standby master to keep it current with the primary.

*Figure 1: Master Mirroring in HAWQ*

![](../mdimages/standby_master.jpg)


If the primary master fails, the replication process stops, and an administrator can activate the standby master. Upon activation of the standby master, the replicated logs reconstruct the state of the primary master at the time of the last successfully committed transaction. The activated standby then functions as the HAWQ master, accepting connections on the port specified when standby master was initialized.

If the master fails, the administrator runs the hawq activate standby utility or uses Ambari to have the standby master take over as the new primary master. 

**Tip:** You can configure a virtual IP address for the master and standby so that client programs do not have to switch to a different network address when the ‘active’ master changes. If the master host fails, the virtual IP address can be swapped to the actual acting master.

##Configuring Master Mirroring <a id="standby_master_configure"></a>

You can configure a new HAWQ system with a standby master during HAWQ’s installation process or you can add a standby master later using the hawq init standby command line utility. This topic assumes you are adding a standby master to an existing system.

###To add a standby master to an existing system

1. Ensure the host machine for the standby master has been installed with HAWQ and configured accordingly.
    * gpadmin system user created
    * HAWQ binaries are installed
    * environment variables set
    * SSH keys exchanged
    * Data directory created
1. Run the `hawq init standby` utility on the host of the currently active primary master to add a standby master host to your HAWQ system. For example:

	```shell
	$ hawq init standby -s new_standby_master_hostname
	```

	where `-s` specifies the hostname of the standby master.

1. Then, check on the status of master mirroring by querying the `gp_master_mirroring system` view. See Checking on the State of Master Mirroring for instructions.

1. To activate or failover to the standby master, see [Failing Over to a Standby Master](#standby_failover).

##Failing Over to a Standby Master<a id="standby_failover"></a>

If the primary master fails, log replication stops. Use `hawq activate standby` to activate the standby master.

Upon activation of the standby master, HAWQ reconstructs the state of the master at the time of the last successfully committed transaction.

###To activate the standby master

1. Ensure that a standby master host has been configured for the system. 

1. Run the hawq activate standby utility from the standby master host you are activating. For example:

	```shell
	$ hawq activate standby
 	```
 	
1. After you activate the standby master, it becomes the active or primary master for the HAWQ cluster.
1. (Optional, but recommended.) Configure a new standby master. Run the following command:

	```shell
	$ hawq init standby -s new_standby_master_hostname
	```
	where `-s` specifies the hostname of the standby master.
	
1. Run hawq state to check the status of the cluster:

	```shell
	$ hawq state
	```
	
	The newly activated master's status should be **Active**. 
	
1. If you configured a new standby master, its status is **Passive**. When a standby master is not configured, the command displays `-No entries found` and the message indicates that a standby master instance is not configured.

1. Query the `gp_segment_configuration` table to verify that segments have registered themselves to the new master.

	$ psql dbname -c 'SELECT * FROM gp_segment_configuration;'
	
1. Then, check on the status of master mirroring by querying the `gp_master_mirroring` system view. See [Checking on the State of Master Mirroring](#standby_check) for instructions.


##Checking on the State of Master Mirroring <a id="standby_check"></a>

To check on the status of master mirroring, query the `gp_master_mirroring` system view. The view provides information about the walsender process used for HAWQ master mirroring. 

```shell
$ psql dbname -c 'SELECT * FROM gp_master_mirroring;'
```

If a standby master has not been set up for the cluster, you will see the following output:

```
 summary_state  | detail_state | log_time | error_message
----------------+--------------+----------+---------------
 Not Configured |              |          | 
(1 row)
```

If the standby is configured and in sync with the master, then you will see something similar to the following output:

```
 summary_state | detail_state | log_time               | error_message
---------------+--------------+------------------------+---------------
 Synchronized  |              | 2016-01-22 21:53:47+00 |
(1 row)
```

##Resynchronizing Standby with the Master <a id="resync_master"></a>


If the the log synchronization process between the master and standby has stopped or has fallen behind, then the standby can become out-of-date. If this occurs, you will see something similar to the following output after querying the `gp_master_mirroring` view.

```
   summary_state  | detail_state | log_time               | error_message
------------------+--------------+------------------------+---------------
 Not Synchronized |              |                        |
(1 row)
```

To resynchronize the standby with the master, execute the following command on the master.

```shell
$ hawq init standby -n
```

This command stops and restarts the master and then synchronizes the standby.
