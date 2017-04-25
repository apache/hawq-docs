---
title: Managing HAWQ Using Ambari
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

Ambari provides an easy interface to perform some of the most common HAWQ and PXF Administration Tasks.

## <a id="amb-yarn"></a>Integrating YARN for Resource Management

HAWQ supports integration with YARN for global resource management. In a YARN managed environment, HAWQ can request resources (containers) dynamically from YARN, and return resources when HAWQ’s workload is not heavy.

See also [Integrating YARN with HAWQ](../resourcemgmt/YARNIntegration.html) for command-line instructions and additional details about using HAWQ with YARN.

### When to Perform

Follow this procedure if you have already installed YARN and HAWQ, but you are currently using the HAWQ Standalone mode (not YARN) for resource management. This procedure helps you configure YARN and HAWQ so that HAWQ uses YARN for resource management. This procedure assumes that you will use the default YARN queue for managing HAWQ.

### Procedure

1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Select **HAWQ** from the list of installed services.
3.  Select the **Configs** tab, then the **Settings** tab.
4.  Use the **Resource Manager** menu to change select the **YARN** option.
5.  Click **Save**.<br/><br/>HAWQ will use the default YARN queue, and Ambari automatically configures settings for `hawq_rm_yarn_address`, `hawq_rm_yarn_app_name`, and `hawq_rm_yarn_scheduler_address` in the `hawq-site.xml` file.<br/><br/>If YARN HA was enabled, Ambari also automatically configures the `yarn.resourcemanager.ha` and `yarn.resourcemanager.scheduler.ha` properties in `yarn-site.xml`.
6.  If you are using HDP 2.3, follow these additional instructions:
    1. Select **YARN** from the list of installed services.
    2. Select the **Configs** tab, then the **Advanced** tab.
    3. Expand the **Advanced yarn-site** section.
    4. Locate the `yarn.resourcemanager.system-metrics-publisher.enabled` property and change its value to `false`.
    5. Click **Save**.
6.  (Optional.)  When HAWQ is integrated with YARN and has no workload, HAWQ does not acquire any resources right away. HAWQ’s resource manager only requests resources from YARN when HAWQ receives its first query request. In order to guarantee optimal resource allocation for subsequent queries and to avoid frequent YARN resource negotiation, you can adjust `hawq_rm_min_resource_perseg` so HAWQ receives at least some number of YARN containers per segment regardless of the size of the initial query. The default value is 2, which means HAWQ’s resource manager acquires at least 2 YARN containers for each segment even if the first query’s resource request is small.<br/><br/>This configuration property cannot exceed the capacity of HAWQ’s YARN queue. For example, if HAWQ’s queue capacity in YARN is no more than 50% of the whole cluster, and each YARN node has a maximum of 64GB memory and 16 vcores, then `hawq_rm_min_resource_perseg` in HAWQ cannot be set to more than 8 since HAWQ’s resource manager acquires YARN containers by vcore. In the case above, the HAWQ resource manager acquires a YARN container quota of 4GB memory and 1 vcore.<br/><br/>To change this parameter, expand **Custom hawq-site** and click **Add Property ...** Then specify `hawq_rm_min_resource_perseg` as the key and enter the desired Value. Click **Add** to add the property definition.
7.  (Optional.)  If the level of HAWQ’s workload is lowered, then HAWQ's resource manager may have some idle YARN resources. You can adjust `hawq_rm_resource_idle_timeout` to let the HAWQ resource manager return idle resources more quickly or more slowly.<br/><br/>For example, when HAWQ's resource manager has to reacquire resources, it can cause latency for query resource requests. To let HAWQ resource manager retain resources longer in anticipation of an upcoming workload, increase the value of `hawq_rm_resource_idle_timeout`. The default value of `hawq_rm_resource_idle_timeout` is 300 seconds.<br/><br/>To change this parameter, expand **Custom hawq-site** and click **Add Property ...** Then specify `hawq_rm_resource_idle_timeout` as the key and enter the desired Value. Click **Add** to add the property definition.
8.  Click **Save** to save your configuration changes.

## <a id="move_yarn_rm"></a>Moving a YARN Resource Manager

If you are using YARN to manage HAWQ resources and need to move a YARN resource manager, then you must update your HAWQ configuration.

### When to Perform

Use one of the following procedures to move YARN resource manager component from one node to another when HAWQ is configured to use YARN as the global resource manager (`hawq_global_rm_type` is `yarn`). The exact procedure you should use depends on whether you have enabled high availability in YARN.

**Note:** In a Kerberos-secured environment, you must update <code>hadoop.proxyuser.yarn.hosts</code> property in HDFS <code>core-site.xml</code> before running a service check. The values should be set to the current YARN Resource Managers.</p>

### Procedure (Single YARN Resource Manager)

1. Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
1. Click **YARN** in the list of installed services.
1. Select **Move ResourceManager**, and complete the steps in the Ambari wizard to move the Resource Manager to a new host.
1. After moving the Resource Manager successfully in YARN, click **HAWQ** in the list of installed services.
1. On the HAWQ **Configs** page, select the **Advanced** tab.
1. Under Advanced hawq-site section, update the following HAWQ properties:
   - `hawq_rm_yarn_address`. Enter the same value defined in the `yarn.resourcemanager.address` property of `yarn-site.xml`.
   - `hawq_rm_yarn_scheduler_address`. Enter the same value in the `yarn.resourcemanager.scheduler.address` property of `yarn-site.xml`.
1. Restart all HAWQ components so that the configurations get updated on all HAWQ hosts.
1. Run HAWQ Service Check, as described in [Performing a HAWQ Service Check](#amb-service-check), to ensure that HAWQ is operating properly.

### Procedure (Highly Available YARN Resource Managers)

1. Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
1. Click **YARN** in the list of installed services.
1. Select **Move ResourceManager**, and complete the steps in the Ambari wizard to move the Resource Manager to a new host.
1. After moving the Resource Manager successfully in YARN, click **HAWQ** in the list of installed services.
1. On the HAWQ **Configs** page, select the **Advanced** tab.
1. Under `Custom yarn-client` section, update the HAWQ properties `yarn.resourcemanager.ha` and `yarn.resourcemanager.scheduler.ha`. These parameter values should be updated to match the corresponding parameters for the YARN service. Check the values under **ResourceManager hosts** in the **Resource Manager** section of the **Advanced** configurations for the YARN service.
1. Restart all HAWQ components so that the configuration change is updated on all HAWQ hosts. You can ignore the warning about the values of `hawq_rm_yarn_address` and `hawq_rm_yarn_scheduler_address` in `hawq-site.xml` not matching the values in `yarn-site.xml`, and click **Proceed Anyway**.
1. Run HAWQ Service Check, as described in [Performing a HAWQ Service Check](#amb-service-check), to ensure that HAWQ is operating properly.


## <a id="amb-service-check"></a>Performing a HAWQ Service Check

A HAWQ Service check uses the `hawq state` command to display the configuration and status of segment hosts in a HAWQ Cluster. It also performs tests to ensure that HAWQ can write to and read from tables, and to ensure that HAWQ can write to and read from HDFS external tables using PXF.

### When to Perform
* Execute this procedure immediately after any common maintenance operations, such as adding, activating, or removing the HAWQ Master Standby.
* Execute this procedure as a first step in troubleshooting problems in accessing HDFS data.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
4. Select **Service Actions > Run Service Check**, then click **OK** to perform the service check.

    Ambari displays the **HAWQ Service Check** task in the list of background operations. If any test fails, then Ambari displays a red error icon next to the task.  
5. Click the **HAWQ Service Check** task to view the actual log messages that are generated while performing the task. The log messages display the basic configuration and status of HAWQ segments, as well as the results of the HAWQ and PXF tests (if PXF is installed).

6. Click **OK** to dismiss the log messages or list of background tasks.

## <a id="amb-config-check"></a>Performing a Configuration Check

A configuration check determines if operating system parameters on the HAWQ host machines match their recommended settings. You can also perform this procedure from the command line using the `hawq check` command. The `hawq check` command is run against all HAWQ hosts.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3. (Optional) Perform this step if you want to view or modify the host configuration parameters that are evaluated during the HAWQ config check:
   1. Select the **Configs** tab, then select the **Advanced** tab in the settings.
   1. Expand **Advanced Hawq Check** to view or change the list of parameters that are checked with a `hawq check` command or with the Ambari HAWQ Config check.

         **Note:** All parameter entries are stored in the `/usr/local/hawq/etc/hawq_check.cnf` file. Click the **Set Recommended** button if you want to restore the file to its original contents.
4. Select **Service Actions > Run HAWQ Config Check**, then click **OK** to perform the configuration check.

    Ambari displays the **Run HAWQ Config Check** task in the list of background operations. If any parameter does not meet the specification defined in `/usr/local/hawq/etc/hawq_check.cnf`, then Ambari displays a red error icon next to the task.  
5. Click the **Run HAWQ Config Check** task to view the actual log messages that are generated while performing the task. Address any configuration errors on the indicated host machines.

6. Click **OK** to dismiss the log messages or list of background tasks.

## <a id="amb-restart"></a>Performing a Rolling Restart
Ambari provides the ability to restart a HAWQ cluster by restarting one or more segments at a time until all segments (or all segments with stale configurations) restart. You can specify a delay between restarting segments, and Ambari can stop the process if a specified number of segments fail to restart. Performing a rolling restart in this manner can help ensure that some HAWQ segments are available to service client requests.

**Note:** If you do not need to preserve client connections, you can instead perform an full restart of the entire HAWQ cluster using **Service Actions > Restart All**.

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

## <a id="bulk-lifecycle"></a>Performing Host-Level Actions on HAWQ Segment and PXF Hosts

Ambari host-level actions enable you to perform actions on one or more hosts in the cluster at once. With HAWQ clusters, you can apply the **Start**, **Stop**, or **Restart** actions to one or more HAWQ segment hosts or PXF hosts. Using the host-level actions saves you the trouble of accessing individual hosts in Ambari and applying service actions one-by-one.

### When to Perform
*  Use the Ambari host-level actions when you have a large number of hosts in your cluster and you want to start, stop, or restart all HAWQ segment hosts or all PXF hosts as part of regularly-scheduled maintenance.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Select the **Hosts** tab at the top of the screen to display a list of all hosts in the cluster.
3.  To apply a host-level action to all HAWQ segment hosts or PXF hosts, select an action using the applicable menu:
    *  **Actions > Filtered Hosts > HAWQ Segments >** [ **Start** | **Stop** |  **Restart** ]
    *  **Actions > Filtered Hosts > PXF Hosts >** [ **Start** | **Stop** |  **Restart** ]
4.  To apply a host level action to a subset of HAWQ segments or PXF hosts:
    1.  Filter the list of available hosts using one of the filter options:
        *  **Filter > HAWQ Segments**
        *  **Filter > PXF Hosts**
    2.  Use the check boxes to select the hosts to which you want to apply the action.
    3.  Select **Actions > Selected Hosts >** [ **Start** | **Stop** |  **Restart** ] to apply the action to your selected hosts.


## <a id="amb-expand"></a>Expanding the HAWQ Cluster

Apache HAWQ supports dynamic node expansion. You can add segment nodes while HAWQ is running without having to suspend or terminate cluster operations.

### Guidelines for Cluster Expansion

This topic provides some guidelines around expanding your HAWQ cluster.

There are several recommendations to keep in mind when modifying the size of your running HAWQ cluster:

-  When you add a new node, install both a DataNode and a HAWQ segment on the new node.  If you are using YARN to manage HAWQ resources, you must also configure a YARN NodeManager on the new node.
-  After adding a new node, you should always rebalance HDFS data to maintain cluster performance.
-  Adding or removing a node also necessitates an update to the HDFS metadata cache. This update will happen eventually, but can take some time. To speed the update of the metadata cache, select the **Service Actions > Clear HAWQ's HDFS Metadata Cache** option in Ambari.
-  Note that for hash distributed tables, expanding the cluster will not immediately improve performance since hash distributed tables use a fixed number of virtual segments. In order to obtain better performance with hash distributed tables, you must redistribute the table to the updated cluster by either the [ALTER TABLE](../reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](../reference/sql/CREATE-TABLE-AS.html) command.
-  If you are using hash tables, consider updating the `default_hash_table_bucket_number` server configuration parameter to a larger value after expanding the cluster but before redistributing the hash tables.

### Procedure
First ensure that the new node(s) has been configured per the instructions found in [Apache HAWQ System Requirements](../requirements/system-requirements.html) and [Select HAWQ Host Machines](../install/select-hosts.html).

1.  If you have any user-defined function (UDF) libraries installed in your existing HAWQ cluster, install them on the new node(s) that you want to add to the HAWQ cluster.
2.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
3.  Click **HAWQ** in the list of installed services.
4.  Select the **Configs** tab, then select the **Advanced** tab in the settings.
5.  Expand the **General** section, and ensure that the **Exchange SSH Keys** property (`hawq_ssh_keys`) is set to `true`.  Change this property to `true` if needed, and click **Save** to continue. Ambari must be able to exchange SSH keys with any hosts that you add to the cluster in the following steps.
6.  Select the **Hosts** tab at the top of the screen to display the Hosts summary.
7.  If the host(s) that you want to add are not currently listed in the Hosts summary page, follow these steps:
    1. Select **Actions > Add New Hosts** to start the Add Host Wizard.
    2. Follow the initial steps of the Add Host Wizard to identify the new host, specify SSH keys or manually register the host, and confirm the new host(s) to add.

         See [Set Up Password-less SSH](http://docs.hortonworks.com/HDPDocuments/Ambari-2.2.1.1/bk_Installing_HDP_AMB/content/_set_up_password-less_ssh.html) in the HDP documentation if you need more information about performing these tasks.
    3. When you reach the Assign Slaves and Clients page, ensure that the **DataNode**, **HAWQ Segment**, and **PXF** (if the PXF service is installed) components are selected. Select additional components as necessary for your cluster.
    4. Complete the wizard to add the new host and install the selected components.
8. If the host(s) that you want to add already appear in the Hosts summary, follow these steps:
   1. Click the hostname that you want to add to the HAWQ cluster from the list of hosts.
   2. In the Components summary, ensure that the host already runs the DataNode component. If it does not, select **Add > DataNode** and then click **Confirm Add**.  Click **OK** when the task completes.
   3. In the Components summary, select **Add > HAWQ Segment**.
   4. Click **Confirm Add** to acknowledge the component to add. Click **OK** when the task completes.
   5. In the Components summary, select **Add > PXF**.
   6. Click **Confirm Add** to acknowledge the component to add. Click **OK** when the task completes.
17. (Optional) If you are using hash tables, adjust the **Default buckets for Hash Distributed tables** setting (`default_hash_table_bucket_number`).

    1. Open the HAWQ service's **Configs > Settings** tab. Update the `default_hash_table_bucket_number` property's value by multiplying the new number of nodes in the cluster by the appropriate number indicated below.

        |Number of Nodes After Expansion|Suggested default\_hash\_table\_bucket\_number value|
        |---------------|------------------------------------------|
        |<= 85|6 \* \#nodes|
        |\> 85 and <= 102|5 \* \#nodes|
        |\> 102 and <= 128|4 \* \#nodes|
        |\> 128 and <= 170|3 \* \#nodes|
        |\> 170 and <= 256|2 \* \#nodes|
        |\> 256 and <= 512|1 \* \#nodes|
        |\> 512|512|
    18.  Ambari requires you to restart the HAWQ service in order to apply the configuration changes. If you need to apply the configuration *without* restarting HAWQ (for dynamic cluster expansion), then use the procedure described in [Workaround for Dynamic Cluster Expansion](#manual-config-steps) *instead* of following this step.
        <br/><br/>Stop and then start the HAWQ service to apply your configuration changes via Ambari. Select **Service Actions > Stop**, followed by **Service Actions > Start** to ensure that the HAWQ Master starts before the newly-added segment. During the HAWQ startup, Ambari exchanges ssh keys for the `gpadmin` user, and applies the new configuration.
        **Note:** Do *not* use the **Restart All** service action to complete this step.
<a id="step-10"></a>
19.  Consider the impact of rebalancing HDFS to other components, such as HBase, before you complete this step.
    <br/><br/>Rebalance your HDFS data by selecting the **HDFS** service and then choosing **Service Actions > Rebalance HDFS**. Follow the Ambari instructions to complete the rebalance action.
20.  Speed up the clearing of the metadata cache by first selecting the **HAWQ** service and then selecting **Service Actions > Clear HAWQ's HDFS Metadata Cache**.
21.  If you are using hash distributed tables and wish to take advantage of the performance benefits of using a larger cluster, redistribute the data in all hash-distributed tables by using either the [ALTER TABLE](../reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](../reference/sql/CREATE-TABLE-AS.html) command. You should redistribute the table data if you modified the `default_hash_table_bucket_number` configuration parameter.

    **Note:** The redistribution of table data can take a significant amount of time.
22.  (Optional.) If you changed the **Exchange SSH Keys** property value before adding the host(s), change the value back to `false` after Ambari exchanges keys with the new hosts. This prevents Ambari from exchanging keys with all hosts every time the HAWQ master is started or restarted.

23.  (Optional.) If you enabled temporary password-based authentication while preparing/configuring your HAWQ host systems, turn off password-based authentication as described in [Apache HAWQ System Requirements](../requirements/system-requirements.html#topic_pwdlessssh).

#### <a id="manual-config-steps"></a>Workaround for Dynamic Cluster Expansion 
If you need to expand your HAWQ cluster without restarting the HAWQ service, follow this procedure to manually apply the HAWQ configuration changes required for this operation. (Perform these steps *instead of* following Step 9b in the above procedure.)

1. Log in to the HAWQ master host as a HAWQ administrator and source greenplum_path.sh:

    ``` shell
    $ ssh gpadmin@<master>
    gpadmin@master$ source /usr/local/hawq/greenplum_path.sh
    ```

2. Set the configuration parameter to the new value:

    ``` shell
    gpadmin@master$ hawq config -c default_hash_table_bucket_number -v <new_value>
    ```
        
3. Reload the HAWQ configuration; this operation does not restart the cluster:

    ``` shell
    gpadmin@master$ hawq stop cluster --reload
    ```
    
4. Verify that the parameter was updated:

    ```shell
    gpadmin@master$ hawq config -s default_hash_table_bucket_number
    ```


5.  Edit the `/usr/local/hawq/etc/slaves` file and add the new HAWQ hostname(s) to the end of the file. Identify each host on a separate line. For example, after adding host4 and host5 to a cluster already containing hosts 1-3, the `slaves` file would appear similar to the following:

     ```
     host1
     host2
     host3
     host4
     host5
     ```
 
6.  Continue with [Step 10](#step-10) in the previous procedure, [Expanding the HAWQ Cluster](#amb-expand).  When the HAWQ service is ready to be restarted via Ambari, Ambari will refresh the new configurations.

## <a id="amb-activate-standby"></a>Activating the HAWQ Standby Master
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

## <a id="amb-add-standby"></a>Adding a HAWQ Standby Master

The HAWQ Standby Master serves as a backup of the HAWQ Master host, and is an important part of providing high availability for the HAWQ cluster. When your cluster uses a standby master, you can activate the standby if the active HAWQ Master host fails or becomes unreachable.

### When to Perform
* Execute this procedure during a scheduled maintenance period, because it requires a restart of the HAWQ service.
* Adding a HAWQ standby master is recommended as a best practice for all new clusters to provide high availability.
* Add a new standby master soon after you activate an existing standby master to ensure that the cluster has a backup master service.

### Procedure

1.  Select an existing host in the cluster to run the HAWQ standby master. You cannot run the standby master on the same host that runs the HAWQ master. Also, do not run a standby master on the node where you deployed the Ambari server; if the Ambari postgres instance is running on the same port as the HAWQ master posgres instance, initialization fails and will leave the cluster in an inconsistent state.
1. Login to the HAWQ host that you chose to run the standby master and determine if there is an existing HAWQ master directory (for example, `/data/hawq/master`) on the machine. If the directory exists, rename the directory. For example:

    ```shell
    $ mv /data/hawq/master /data/hawq/master-old
    ```

   **Note:**  If a HAWQ master directory exists on the host when you configure the HAWQ standby master, then the standby master may be initialized with stale data. Rename any existing master directory before you proceed.
   
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Add HAWQ Standby Master** to start the Add HAWQ Standby Master Wizard.
4.  Read the Get Started page for information about HAWQ the standby master and to acknowledge that the procedure requires a service restart. Click **Next** to display the Select Host page.
5.  Use the dropdown menu to select a host to use for the HAWQ Standby Master. Click **Next** to display the Review page.

    **Note:**
    * The Current HAWQ Master host is shown only for reference. You cannot change the HAWQ Master host when you configure a standby master.
    * You cannot place the standby master on the same host as the HAWQ master.
6. Review the information to verify the host on which the HAWQ Standby Master will be installed. Click **Back** to change your selection or **Next** to continue.
7. Confirm that you have renamed any existing HAWQ master data directory on the selected host machine, as described earlier in this procedure. If an existing master data directory exists, the new HAWQ Standby Master may be initialized with stale data and can place the cluster in an inconsistent state. Click **Confirm** to continue.

     Ambari displays a list of tasks that are performed to install the standby master server and reconfigure the cluster. Click on any of the tasks to view progress or to view the actual log messages that are generated while performing the task.
7. Click **Complete** after the Wizard finishes all tasks.

## <a id="amb-remove-standby"></a>Removing the HAWQ Standby Master

This service action enables you to remove the HAWQ Standby Master component in situations where you may need to reinstall the component.

### When to Perform
* Execute this procedure if you need to decommission or replace theHAWQ Standby Master host.
* Execute this procedure as a first step when [Resynchronizing the Standby with the Master](MasterMirroring.html#resync_master).
* Execute this procedure during a scheduled maintenance period, because it requires a restart of the HAWQ service.

### Procedure
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Remove HAWQ Standby Master** to start the Remove HAWQ Standby Master Wizard.
4.  Read the Get Started page for information about the procedure and to acknowledge that the procedure requires a service restart. Click **Next** to display the Review page.
5.  Ambari displays the HAWQ Standby Master host that will be removed from the cluster configuration. Click **Next** to continue, then click **OK** to confirm.

     Ambari displays a list of tasks that are performed to remove the standby master from the cluster. Click on any of the tasks to view progress or to view the actual log messages that are generated while performing the task.

7. Click **Complete** after the Wizard finishes all tasks.

      **Important:** After the Wizard completes, your HAWQ cluster no longer includes a HAWQ Standby Master host. As a best practice, follow the instructions in [Adding a HAWQ Standby Master](#amb-add-standby) to configure a new one.

## <a id="hdp-upgrade"></a>Upgrading the HDP Stack

If you install HAWQ using Ambari 2.2.2 with the HDP 2.3 stack, before you attempt to upgrade to HDP 2.4 you must use Ambari to change the `dfs.allow.truncate` property to `false`. Ambari will display a configuration warning with this setting, but it is required in order to complete the upgrade; choose **Proceed Anyway** when Ambari warns you about the configured value of `dfs.allow.truncate`.

After you complete the upgrade to HDP 2.4, change the value of `dfs.allow.truncate` back to `true` to ensure that HAWQ can operate as intended.

## <a id="gpadmin-password-change"></a>Changing the HAWQ gpadmin Password
The password issued by the Ambari web console is used for the `hawq ssh-exkeys` utility, which is run during the start phase of the HAWQ Master.
Ambari stores and uses its own copy of the gpadmin password, independently of the host system. Passwords on the master and slave nodes are not automatically updated and synchronized with Ambari. Not updating the Ambari system user password causes Ambari to behave as if the gpadmin password was never changed \(it keeps using the old password\).

If passwordless ssh has not been set up, `hawq ssh-exkeys` attempts to exchange the key by using the password provided by the Ambari web console. If the password on the host machine differs from the HAWQ System User password recognized on Ambari, exchanging the key with the HAWQ Master fails. Components without passwordless ssh might not be registered with the HAWQ cluster.

### When to Perform
You should change the gpadmin password when:

* The gpadmin password on the host machines has expired.
* You want to change passwords as part of normal system security procedures.
When updating the gpadmin password, it must be kept in synch with the gpadmin user on the HAWQ hosts. This requires manually changing the password on the Master and Slave hosts, then updating the Ambari password.

###Procedure
All of the listed steps are mandatory. This ensures that HAWQ service remains fully functional.

1.  Use a script to manually change the password for the gpadmin user on all HAWQ hosts \(all Master and Slave component hosts\). To manually update the password, you must have ssh access to all host machines as the gpadmin user. Generate a hosts file to use with the `hawq ssh` command to reset the password on all hosts. Use a text editor to create a file that lists the hostname of the master node, the standby master node, and each segment node used in the cluster. Specify one hostname per line, for example:

    ```
    mdw
    smdw
    sdw1
    sdw2
    sdw3
    ```

    You can then use a command similar to the following to change the password on all hosts that are listed in the file:

    ```shell
    $ hawq ssh -f hawq_hosts 'echo "gpadmin:newpassword" | /usr/sbin/chpasswd'
    ```    

    **Note:** Be sure to make appropriate user and password system administrative changes in order to prevent operational disruption. For example, you may need to disable the password expiration policy for the `gpadmin` account.
2.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\) Then perform the following steps:
    1. Click **HAWQ** in the list of installed services.
    2. On the HAWQ Server Configs page, go to the **Advanced** tab and update the **HAWQ System User Password** to the new password specified in the script.
    3. Click **Save** to save the updated configuration.
    4. Restart HAWQ service to propagate the configuration change to all Ambari agents.

    This will synchronize the password on the host machines with the password that you specified in Ambari.
    
## <a id="manual-cfg-norestart"></a>Updating HAWQ Configuration Without Cluster Restart
There may be circumstances, such as during dynamic cluster expansion, when you must update HAWQ configuration parameters but cannot tolerate cluster downtime in your Ambari-managed cluster. In these situations, perform the following workaround to update and reload HAWQ configuration changes without a complete cluster restart.

**Note**: Use this procedure for setting or updating only those HAWQ server configuration parameters with a set classification of `reload`.

1.  Use the Ambari console UI to set and save the desired HAWQ configuration parameter(s) via the **HAWQ** service **Settings**, **Configs >Settings**, and/or **Configs >Advanced** tabs. Make sure to note the configuration parameter names and new values. You may need to hover the mouse over the configuration field to identify the HAWQ parameter name.
    
    **Note**: After updating the configuration parameters, do *not* restart the HAWQ service. 

1.  Use HAWQ command line utilities to update the same HAWQ configuration parameters:
    1. Log in to the HAWQ master host as a HAWQ administrator and source greenplum_path.sh:

        ``` shell
        $ ssh gpadmin@<master>
        gpadmin@master$ source /usr/local/hawq/greenplum_path.sh
        ```
        
    2. Identify the current value of the HAWQ configuration parameter:

        ``` shell
        gpadmin@master$ hawq config -s <parameter_name>
        ```
        
    3. Set the configuration parameter to the new value:

        ``` shell
        gpadmin@master$ hawq config -c <parameter_name> -v <new_value>
        ```
        
        Perform Steps b and c for each configuration parameter you set or updated via Ambari.
        
3. Reload the HAWQ configuration; this operation does not restart the cluster:

    ``` shell
    gpadmin@master$ hawq stop cluster --reload
    ```
    
4. Verify that each parameter was updated:

    ```shell
    gpadmin@master$ hawq config -s <parameter_name>
    ```

## <a id="gpadmin-setup-alert"></a>Setting Up Alerts
 
Alerts advise you of when a HAWQ process is down or not responding, or when certain conditions requiring attention occur.
Alerts can be created for the Master, Standby Master, Segments, and PXF components. You can also set up custom alert groups to monitor these conditions and send email notifications when they occur.

### When to Perform
Alerts are enabled by default. You might want to disable alert functions when performing system operations in maintenance mode and then re-enable them after returning to normal operation.

You can configure alerts to display messages for all system status changes or only for conditions of interest, such as warnings or critical conditions. Alerts can advise you if there are communication issues between the HAWQ Master and HAWQ segments, or if the HAWQ Master, Standby Master, a segment, or the PXF service is down or not responding. 

You can configure Ambari to check for alerts at specified intervals, on a particular service or host, and what level of criticality you want to trigger an alert (OK, WARNING, or CRITICAL).

### Procedure
Ambari can show Alerts and also configure certain status conditions. 

#### Viewing Alerts
To view the current alert information for HAWQ, click the **Groups** button at the top left of the Alerts page, then select **HAWQ Default** in the drop-down menu, then click on the **Alert** button at the top of the Ambari console. Ambari will display a list of all available alert functions and their current status. 

To check PXF alerts, click the **Groups** dropdown button at the top left of the Alerts page. Select **PXF Default** in the dropdown menu. Alerts are displayed on the PXF Status page.

To view the current Alert settings, click on the name of the alert.

The Alerts you can view are as follows:

* HAWQ Master Process:
This alert is triggered when the HAWQ Master process is down or not responding. 

* HAWQ Segment Process:
This alert is triggered when a HAWQ Segment on a node is down or not responding.  

* HAWQ Standby Master Process:
This alert is triggered when the HAWQ Standby Master process is down or not responding. If no standby is present, the Alert shows as **NONE**. 

* HAWQ Standby Master Sync Status:
This alert is triggered when the HAWQ Standby Master is not synchronized with the HAWQ Master. Using this Alert eliminates the need to check the gp\_master\_mirroring catalog table to determine if the Standby Master is fully synchronized. 
If no standby Master is present, the status will show as **UNKNOWN**.
   If this Alert is triggered, go to the HAWQ **Services** tab and click on the **Service Action** button to re-sync the HAWQ Standby Master with the HAWQ Master.
   
* HAWQ Segment Registration Status:
This alert is triggered when any of the HAWQ Segments fail to register with the HAWQ Master. This indicates that the HAWQ segments having an up status in the gp\_segment\_configuration table do not match the HAWQ Segments listed in the /usr/local/hawq/etc/slaves file on the HAWQ Master. 

* Percent HAWQ Segment Status Available:
This Alert monitors the percentage of HAWQ segments available versus total segments. 
   Alerts for **WARN**, and **CRITICAL** are displayed when the number of unresponsive HAWQ segments in the cluster is greater than the specified threshold. Otherwise, the status will show as **OK**.

* PXF Process Alerts:
PXF Process alerts are triggered when a PXF process on a node is down or not responding on the network. If PXF Alerts are enabled, the Alert status is shown on the PXF Status page.

#### Setting the Monitoring Inteval
You can customize how often you wish the system to check for certain conditions. The default interval for checking the HAWQ system is 1 minute. 

To customize the interval, perform the following steps:

1.  Click on the name of the Alert you want to edit. 
2.  When the Configuration screen appears, click **Edit**. 
3.  Enter a number for how often to check status for the selected Alert, then click **Save**. The interval must be specified in whole minutes.


#### Setting the Available HAWQ Segment Threshold
HAWQ monitors the percentage of available HAWQ segments and can send an alert when a specified percent of unresponsive segments is reached. 

To set the threshold for the unresponsive segments that will trigger an alert:

   1.  Click on **Percent HAWQ Segments Available**. 
   2.  Click **Edit**. Enter the percentage of total segments to create a **Warning** alert (default is 10 percent of the total segments) or **Critical** alert (default is 25 percent of total segments).
   3.  Click **Save** when done.
   Alerts for **WARN**, and **CRITICAL** will be displayed when the number of unresponsive HAWQ segments in the cluster is greater than the specified percentage. 

## <a id="ambari-rest-api"></a>Using the Ambari REST API
You can perform certain HAWQ cluster management activities from the command line using Ambari REST APIs. Refer to [Using the Ambari REST API](ambari-rest-api.html) for additional information.
