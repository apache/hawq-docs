---
title: Managing HAWQ Using Ambari
---

Ambari provides an easy interface to perform some of the most common HAWQ and PXF Administration Tasks.

## Performing a Rolling Restart<a id="amb-restart"></a>
Ambari provides the ability to restart a HAWQ cluster by restarting one or more segments at a time until all segments (or all segments with stale configurations) restart. You can specify a delay between restarting segments, and Ambari can stop the process if a specified number of segments fail to restart. Performing a rolling restart in this manner can help ensure that some HAWQ segments are available to service client requests.

**Note** If you do not need to preserve client connections, you can instead perform an full restart of the entire HAWQ cluster using **Service Actions > Restart All**.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Restart HAWQ Segments**.
4. In the Restart HAWQ Segments page:
   * Specify the number of segments that you want Ambari to restart at a time.
   * Specify the number of seconds Ambari should wait before restarting the next batch of HAWQ segments.
   * Specify the number of restart failures that may occur before Ambari stops the rolling restart process.
   * Select **Only restart HAWQ Segments with stale configs** if you want to limit the restart process to those hosts.
   * Select **Turn On Maintenance Mode for HAWQ** to enable maintenance mode before starting the rolling restart process. This suppresses alerts that are normally generated when a segment goes offline.
5. Click **Trigger Rolling Restart** to begin the restart process.

    Ambari displays the **Rolling Restart of HAWQ segments** task in the list of background operations, and indicates the current batch of segments that it is restarting. Click the name of the task to view the log messages generated during the restart. If any segment fails to restart, Ambari displays a red warning icon next to the task.

## Adding a HAWQ Standby Master<a id="amb-add-standby"></a>

A HAWQ Standby Master serves as a backup of the HAWQ Master host, and is an important part of providing high availability for the HAWQ cluster. When your cluster uses a standby master, you can activate the standby if the active HAWQ Master host fails or becomes unreachable.

### When to Perform
* Execute this procedure during a scheduled maintenance period, because it requires a restart of the HAWQ service.
* Adding a HAWQ standby master is recommended as a best practice for all new clusters to provide high availability.
* Add a new standby master after you activate an existing standby master.

### Procedure

1.  Select an existing host in the HAWQ cluster to run the HAWQ standby master. You cannot run the standby master on the same host that runs the HAWQ master.
1. Login to the HAWQ host that you chose to run the standby master and determine if there is an existing HAWQ master directory (for example, /data/hawq/master) on the machine. If the directory exists, rename the directory. For example:
     ```
     $ mv /data/hawq/master /data/hawq/master-old
     ```

     **Note:**  If a HAWQ master directory exists on the host when you configure the HAWQ standby master, then the standby master may be initialized with stale data. Rename any existing master directory before you proceed.
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Add HAWQ Standby Master** to start the Add HAWQ Standby Master Wizard.
4.  Read the Get Started page for information about HAWQ the standby master and to acknowledge that the procedure requires a service restart. Click **Next** to display the Select Host page.
5.  Use the HAWQ Standby Master menu to select a host to use for the standby service. Click **Next** to display the Review page.

    **Note:**
    * The Current HAWQ Master host is shown only for reference. You cannot change the HAWQ Master host when you configure a standby master.
    * You cannot place the standby master on the same host as the HAWQ master.
6. Review the information to verify the host on which the HAWQ Standby Master will be installed. Click **Back** to change your selection or **Next** to continue.
7. Confirm that you have renamed any existing HAWQ master data directory on the selected host machine, as described earlier in this procedure. If an existing master data directory exists, the new HAWQ Standby Master may be initialized with stale data and can place the cluster in an inconsistent state. Click **Confirm** to continue.

     Ambari displays a list of tasks that are performed to install the standby master server and reconfigure the cluster. Click on any of the tasks to view progress or to view the actual log messages that are generated while performing the task.
7. Click **Complete** after the Wizard finishes all tasks.


## Activating a HAWQ Standby Master<a id="amb-activate-standby"></a>
Activating the HAWQ Standby Master promotes the standby host as the new HAWQ Master host. The previous HAWQ Master configuration is automatically removed from the cluster.

### When to Perform
* Execute this procedure immediately if the HAWQ Master fails or becomes unreachable.
* If you want to take the current HAWQ Master host offline for maintenance, execute this procedure during a scheduled maintenance period. This procedure requires a restart of the HAWQ service.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Activate HAWQ Standby Master** to start the Activate HAWQ Standby Master Wizard.
4.  Read the description of the Wizard and click **Next** to review the tasks that will be performed.
5.  Ambari displays the host name of the current HAWQ Master that will be removed from the cluster, as well as the HAWQ Standby Master host that will be activated. The information is provided only for review and cannot be edited on this page. Click **Next** to confirm the operation.
6. Click **OK** to confirm that you want to perform the procedure, as it is not possible to roll back the operation using Ambari.

     Ambari displays a list of tasks that are performed to activate the standby server and remove the previous HAWQ Master host. Click on any of the tasks to view progress or to view the actual log messages that are generated while performing the task.
7. Click **Complete** after the Wizard finishes all tasks.

   **Important:** After the Wizard completes, your HAWQ cluster no longer includes a HAWQ Standby Master host. As a best practice, follow the instructions in [Adding a HAWQ Standby Master](#amb-add-standby) to configure a new one.

## Removing a HAWQ Standby Master<a id="amb-remove-standby"></a>

If you need to perform maintenance on the HAWQ Standby Master host, first remove the standby master from the HAWQ cluster configuration.

### When to Perform
* Execute this procedure if the HAWQ Standby Master fails or requires maintenance.
* Execute this procedure during a scheduled maintenance period, because it requires a restart of the HAWQ service.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Remove HAWQ Standby Master** to start the Remove HAWQ Standby Master Wizard.
4.  Read the Get Started page for information about the procedure and to acknowledge that the procedure requires a service restart. Click **Next** to display the Review page.
5.  Ambari displays the HAWQ Standby Master host that will be removed from the cluster configuration. Click **Next** to continue, then click **OK** to confirm.

     Ambari displays a list of tasks that are performed to remove the standby master host from the cluster configuration. Click on any of the tasks to view progress or to view the actual log messages that are generated while performing the task.

7. Click **Complete** after the Wizard finishes all tasks.

      **Important:** After the Wizard completes, your HAWQ cluster no longer includes a HAWQ Standby Master host. As a best practice, follow the instructions in [Adding a HAWQ Standby Master](#amb-add-standby) to configure a new one.


## Expanding the HAWQ Cluster<a id="amb-expand"></a>

Apache HAWQ supports dynamic node expansion. You can add segment nodes while HAWQ is running without having to suspend or terminate cluster operations.

### Guidelines for Cluster Expansion

This topic provides some guidelines around expanding your HAWQ cluster.

There are several recommendations to keep in mind when modifying the size of your running HAWQ cluster:

-   When you add a new node, install both a DataNode and a physical segment on the new node.
-   After adding a new node, you should always rebalance HDFS data to maintain cluster performance.
-   Adding or removing a node also necessitates an update to the HDFS metadata cache. This update will happen eventually, but can take some time. To speed the update of the metadata cache, execute **`select gp_metadata_cache_clear();`** (for CLI users) or the **Service Actions > Clear HAWQ's HDFS Metadata Cache** option in Ambari.
-   Note that for hash distributed tables, expanding the cluster will not immediately improve performance since hash distributed tables use a fixed number of virtual segments. In order to obtain better performance with hash distributed tables, you must redistribute the table to the updated cluster by either the [ALTER TABLE](/200/hawq/reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](/200/hawq/reference/sql/CREATE-TABLE-AS.html) command.
-   If you are using hash tables, consider updating the `default_hash_table_bucket_number` server configuration parameter to a larger value after expanding the cluster but before redistributing the hash tables.

### Procedure
1.  If you have any user-defined function (UDF) libraries installed in your existing HAWQ cluster, install them on the new node(s) that you want to add to the HAWQ cluster.
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Select the **Hosts** tab at the top of the screen to display the Hosts summary.
3.  If the host(s) that you want to add are not currently listed in the Host summary, follow these steps:
   1. Select **Actions > Add New Hosts** to start the Add Host Wizard.
   2. Follow the initial steps of the Add Host Wizard to identify the new host, specify SSH keys or manually register the host, and confirm the new host(s) to add.

         See [Set Up Password-less SSH](http://docs.hortonworks.com/HDPDocuments/Ambari-2.2.1.1/bk_Installing_HDP_AMB/content/_set_up_password-less_ssh.html) in the HDP documentation if you need more information about performing these tasks.
    3. When you reach the Assign Slaves and Clients page, ensure that the **DataNode**, **HAWQ Segment**, and **PXF** components are selected. Select additional components as necessary for your cluster.
   4. Complete the wizard to add the new host and install the selected components.
4. If the host(s) that you want to add already appear in the Hosts summary, follow these steps:
   1. Click the hostname that you want to add to the HAWQ cluster from the list of hosts.
   2. In the Components summary, ensure that the host already runs the DataNode component. If it does not, select **Add > DataNode** and then click **Confirm Add**.  Click **OK** when the task completes.
   2. In the Components summary, select **Add > HAWQ Segment**.
   3. Click **Confirm Add** to acknowledge the component to add. Click **OK** when the task completes.
   2. In the Components summary, select **Add > PXF**.
   3. Click **Confirm Add** to acknowledge the component to add. Click **OK** when the task completes.
17. (Optional) If you are using hash tables, adjust the **Default buckets for Hash Distributed tables** setting (`default_hash_table_bucket_number`) on the HAWQ service's **Configs > Settings** tab. Update this setting's value by multiplying the new number of nodes in the cluster by the appropriate amount indicated below.

	|Number of Nodes After Expansion|Suggested default\_hash\_table\_bucket\_number value|
	|---------------|------------------------------------------|
	|<= 85|6 \* \#nodes|
	|\> 85 and <= 102|5 \* \#nodes|
	|\> 102 and <= 128|4 \* \#nodes|
	|\> 128 and <= 170|3 \* \#nodes|
	|\> 170 and <= 256|2 \* \#nodes|
	|\> 256 and <= 512|1 \* \#nodes|
	|\> 512|512|
6.  **Note:** Ambari requires the HAWQ service to be restarted in order to apply the configuration changes. If you need to apply the configuration *without* restarting HAWQ (for dynamic cluster expansion), then you can use the HAWQ CLI commands described in [Manually Updating the HAWQ Configuration](#manual-config-steps) *instead* of following this step.
    <br/><br/>Stop and then start the HAWQ service to apply your configuration changes via Ambari. Select **Service Actions > Stop**, followed by **Service Actions > Start** to ensure that the HAWQ Master starts before the newly-added segment. During the HAWQ startup, Ambari exchanges ssh keys for the `gpadmin` user, updates the `hawq_hosts` and `slaves` files in `$GPHOME/etc/`, and applies the new configuration.
>**Note:** Do not use the **Restart All** service action to complete this step.
6.  **Note** Consider the impact of rebalancing HDFS to other components, such as HBase, before you complete this step.
    <br/><br/>Rebalance your HDFS data by selecting the **HDFS** service and then choosing **Service Actions > Rebalance HDFS**. Follow the Ambari instructions to complete the rebalance action.
6.  Speed up the clearing of the metadata cache by first selecting the **HAWQ** service and then selecting **Service Actions > Clear HAWQ's HDFS Metadata Cache**.
5.  If you are using hash distributed tables and wish to take advantage of the performance benefits of using a larger cluster, redistribute the data in all hash-distributed tables by using either the [ALTER TABLE](/200/hawq/reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](/200/hawq/reference/sql/CREATE-TABLE-AS.html) command. You should redistribute the table data if you modified the `default_hash_table_bucket_number` configuration parameter.

   	**Note:** The redistribution of table data can take a significant amount of time.

#### Manually Updating the HAWQ Configuration<a id="manual-config-steps"></a>
If you need to expand your HAWQ cluster without restarting the HAWQ service, follow these steps to manually apply the new HAWQ configuration. (Use these steps *instead* of following Step 7 in the above procedure.):

1.  Update your configuration to use the new `default_hash_table_bucket_number` value that you calculated:

      1. SSH into the HAWQ master host as the `gpadmin` user:

         ```
         $ ssh gpadmin@<HAWQ_MASTER_HOST>
         ```
      2. Source the `greenplum_path.sh` file to update the shell environment:

         ```
         $ source /usr/local/hawq/greenplum_path.sh
         ```
      3. Verify the current value of `default_hash_table_bucket_number`:

         ```
         $ hawq config -s default_hash_table_bucket_number
         ```
      4. Update `default_hash_table_bucket_number` to the new value that you calculated:

         ```
         $ config -c default_hash_table_bucket_number -v <new_value>
         ```
      5. Reload the configuration without restarting the cluster:

         ```
         $ hawq stop cluster -u
         ```
      6. Verify that the `default_hash_table_bucket_number` value was updated:

         ```
         $ hawq config -s default_hash_table_bucket_number
         ```
2.  Edit the `/usr/local/hawq/etc/slaves` file and add the new HAWQ hostname(s) to the end of the file. Separate multiple hosts with new lines. For example, after adding host4 and host5 to a cluster already contains hosts 1-3, the updated file contents would be:

    ```
    host1
    host2
    host3
    host4
    host5
    ```
3.  Continue with Step 8 in the previous procedure, [Expanding the HAWQ Cluster](#amb-expand).  When the HAWQ service is ready to be restarted via Ambari, Ambari will refresh the new configurations.

## Performing a Configuration check<a id="amb-config-check"></a>

A configuration check determines if operating system parameters on a HAWQ host machines match their recommended settings. You can also perform this procedure from the command line using the `hawq check` command.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3. (Optional) Perform this step if you want to view or modify the host configuration parameters that are evaluated during the HAWQ config check:
   1. Select the **Configs** tab, then select the **Advanced** tab in the settings.
   1. Expand **Advanced Hawq Check** to view or change the list of parameters that are checked with a `hawq check` command or with the Ambari HAWQ Config check.

         **Note:** All parameter entries are stored in the `/usr/local/hawq/hawq_check.cnf` file. Click the **Set Recommended** button if you want to restore the file to its original contents.
4. Select **Service Actions > Run HAWQ Config Check**, then click **OK** to perform the configuration check.

    Ambari displays the **Run HAWQ Config Check** task in the list of background operations. If any parameter does not meet the specification defined in `/usr/local/hawq/hawq_check.cnf`, then Ambari displays a red error icon next to the task.  
5. Click the **Run HAWQ Config Check** task to view the actual log messages that are generated while performing the task. Address any configuration errors on the indicated host machines.

6. Click **OK** to dismiss the log messages or list of background tasks.


## Performing a HAWQ Service Check<a id="amb-service-check"></a>

A HAWQ Service check uses the `hawq state` command to display the configuration and status of segment hosts in a HAWQ Cluster. It also performs tests to ensure that HAWQ can write to and read from tables, and to ensure that PXF can write to and read from HDFS external tables.

### When to Perform
* Execute this procedure immediately after a new install to validate the basic functioning of the HAWQ cluster.
* Execute this procedure after expanding or removing HAWQ nodes to validate the new HAWQ cluster configuration.
* Execute this procedure as a first step in troubleshooting problems in accessing HDFS data.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
4. Select **Service Actions > Run Service Check**, then click **OK** to perform the service check.

    Ambari displays the **HAWQ Service Check** task in the list of background operations. If any test fails, then Ambari displays a red error icon next to the task.  
5. Click the **HAWQ Service Check** task to view the actual log messages that are generated while performing the task. The log messages display the basic configuration and status of HAWQ segments, as well as the results of the HAWQ and PXF tests.

6. Click **OK** to dismiss the log messages or list of background tasks.

## Upgrading the HDP Stack<a id="hdp-upgrade"></a>

If you install HAWQ using Ambari 2.2.2 with the HDP 2.3 stack, before you attempt to upgrade to HDP 2.4 you must use Ambari to change the `dfs.allow.truncate` property to `false`. Ambari will display a configuration warning with this setting, but it is required in order to complete the upgrade; choose **Proceed Anyway** when Ambari warns you about the configured value of `dfs.allow.truncate`. After you complete the upgrade to HDP 2.4, change the value of `dfs.allow.truncate` back to `true` to ensure that HAWQ can operate as intended.

## Changing the HAWQ gpadmin Password<a id="gpadmin-password-change"></a>

### Prerequisites
HAWQ service on the cluster must be already installed and managed through Ambari.

### Changing the gpadmin Password

The all of the listed steps are mandatory. This ensures that HAWQ service remains fully functional.
1.  Use the reference script to manually change the password for the gpadmin user on all HAWQ hosts \(all Master and Slave component hosts\) by updating the `hawq_hosts` file with its contents. 
Each line of the `hawq_hosts` file represents the hostname of a host on which a HAWQ component has been installed. To execute this script, you must have ssh access to all host machines as the gpadmin user.
2.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\) The perform the following steps: 
    1. Click **HAWQ** in the list of installed services. 
    1. On the HAWQ Server Configs page, go to the **Advanced** tab and update the **HAWQ System User Password** to the new password specified in the script. Click **Save** to save the updated configuration.
3.  Restart HAWQ service to propagate the configuration change to all Ambari agents. 

###Reference Script

Change the contents of this file to reflect your old and new gpadmin passwords.

        ```
        #!/bin/bash

        # Read Password (old and new) from the User
        echo -n "Enter old password:":
        read -s oldPassword
        echo-n "Enter new password:":
        read -s newPassword

        # Change Password on all Hosts
        for host in $(cat hawq_hosts: do
        echo "Changing password for gpadmin user on "$host;
        ssh gpadmin@$host "passwd <<EOF
        oldPassword
        newPassword
        newPassword
        EOF";
        done
        ```

###What if the HAWQ System User Password on Ambari Is Not Updated?

Not updating the Ambari system user password causes Ambari to behave as if the gpadmin password was never changed \(it keeps the old password\). The password issued by the Ambari web console is used for the `hawq ssh-exkeys` utility, which is run during the start phase of HAWQMASTER. 
If passwordless ssh has already been set up \(a key has been exchanged earlier and the host has it stored in `~/.ssh/authorized_keys`\), the `hawq ssh-exkeys` utility will not exchange the key. 
If passwordless ssh has not been set up, `hawq ssh-exkeys` attempts to exchange the key by using the password provided by the Ambari web console. If the password on the host machine differs from the HAWQ System User password recognized on Ambari, exchanging the key with the HAWQMASTER fails. Components without passwordless ssh might not be registered with the HAWQ cluster. 

###What if the Password Expires on the Host Machines?

Use the procedure above to create a new password on the host machines, then update the HAWQ **System User Password** on the Ambari Web Console. This will synchronize the password on the host machines with the password recognized by Ambari. 
