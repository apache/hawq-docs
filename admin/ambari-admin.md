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

### Procedure
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
