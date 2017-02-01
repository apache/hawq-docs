---
title: Starting and Stopping HAWQ
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

In a HAWQ DBMS, the database server instances \(the master and all segments\) are started or stopped across all of the hosts in the system in such a way that they can work together as a unified DBMS.

Because a HAWQ system is distributed across many machines, the process for starting and stopping a HAWQ system is different than the process for starting and stopping a regular PostgreSQL DBMS.

Use the `hawq start `*`object`* and `hawq stop `*`object`* commands to start and stop HAWQ, respectively. These management tools are located in the `$GPHOME/bin` directory on your HAWQ master host. 

Initializing a HAWQ system also starts the system.

**Important:**

Do not issue a `KILL` command to end any Postgres process. Instead, use the database command `pg_cancel_backend()`.

For information about [hawq start](../reference/cli/admin_utilities/hawqstart.html) and [hawq stop](../reference/cli/admin_utilities/hawqstop.html), see the appropriate pages in the HAWQ Management Utility Reference or enter `hawq start -h` or `hawq stop -h` on the command line.


## <a id="task_hkd_gzv_fp"></a>Starting HAWQ 

When a HAWQ system is first initialized, it is also started. For more information about initializing HAWQ, see [hawq init](../reference/cli/admin_utilities/hawqinit.html). 

To start a stopped HAWQ system that was previously initialized, run the `hawq start` command on the master instance.

You can also use the `hawq start master` command to start only the HAWQ master, without segment nodes, then add these later, using `hawq start segment`. If you want HAWQ to ignore hosts that fail ssh validation, use the hawq start `--ignore-bad-hosts` option. 

Use the `hawq start cluster` command to start a HAWQ system that has already been initialized by the `hawq init cluster` command, but has been stopped by the `hawq stop cluster` command. The `hawq start cluster` command starts a HAWQ system on the master host and starts all its segments. The command orchestrates this process and performs the process in parallel.


## <a id="task_gpdb_restart"></a>Restarting HAWQ 

Stop the HAWQ system and then restart it.

The `hawq restart` command with the appropriate `cluster` or node-type option will stop and then restart HAWQ after the shutdown completes. If the master or segments are already stopped, restart will have no effect.

-   To restart a HAWQ cluster, enter the following command on the master host:

    ```shell
    $ hawq restart cluster
    ```


## <a id="task_upload_config"></a>Reloading Configuration File Changes Only 

Reload changes to the HAWQ configuration files without interrupting the system.

The `hawq stop` command can reload changes to the `pg_hba.conf `configuration file and to *runtime* parameters in the `hawq-site.xml` and `pg_hba.conf` files without service interruption. Active sessions pick up changes when they reconnect to the database. Many server configuration parameters require a full system restart \(`hawq restart cluster`\) to activate. For information about server configuration parameters, see the [Server Configuration Parameter Reference](../reference/guc/guc_config.html).

-   Reload configuration file changes without shutting down the system using the `hawq stop` command:

    ```shell
    $ hawq stop cluster --reload
    ```
    
    Or:

    ```shell
    $ hawq stop cluster -u
    ```
    

## <a id="task_maint_mode"></a>Starting the Master in Maintenance Mode 

Start only the master to perform maintenance or administrative tasks without affecting data on the segments.

Maintenance mode is a superuser-only mode that should only be used when required for a particular maintenance task. For example, you can connect to a database only on the master instance in maintenance mode and edit system catalog settings.

1.  Run `hawq start` on the `master` using the `-m` option:

    ```shell
    $ hawq start master -m
    ```

2.  Connect to the master in maintenance mode to do catalog maintenance. For example:

    ```shell
    $ PGOPTIONS='-c gp_session_role=utility' psql template1
    ```
3.  After completing your administrative tasks, restart the master in production mode. 

    ```shell
    $ hawq restart master 
    ```

    **Warning:**

    Incorrect use of maintenance mode connections can result in an inconsistent HAWQ system state. Only expert users should perform this operation.


## <a id="task_gpdb_stop"></a>Stopping HAWQ 

The `hawq stop cluster` command stops or restarts your HAWQ system and always runs on the master host. When activated, `hawq stop cluster` stops all `postgres` processes in the system, including the master and all segment instances. The `hawq stop cluster` command uses a default of up to 64 parallel worker threads to bring down the segments that make up the HAWQ cluster. The system waits for any active transactions to finish before shutting down. To stop HAWQ immediately, use fast mode. The commands `hawq stop master`, `hawq stop segment`, `hawq stop standby`, or `hawq stop allsegments` can be used to stop the master, the local segment node, standby, or all segments in the cluster. Stopping the master will stop only the master segment, and will not shut down a cluster.

-   To stop HAWQ:

    ```shell
    $ hawq stop cluster
    ```

-   To stop HAWQ in fast mode:

    ```shell
    $ hawq stop cluster -M fast
    ```


## <a id="task_tx4_bl3_h5"></a>Best Practices to Start/Stop HAWQ Cluster Members 

For best results in using `hawq start` and `hawq stop` to manage your HAWQ system, the following best practices are recommended.

-   Issue the `CHECKPOINT` command to update and flush all data files to disk and update the log file before stopping the cluster. A checkpoint ensures that, in the event of a crash, files can be restored from the checkpoint snapshot.

-   Stop the entire HAWQ system by stopping the cluster on the master host. 

    ```shell
    $ hawq stop cluster
    ```

-   To stop segments and kill any running queries without causing data loss or inconsistency issues, use `fast` or `immediate` mode on the cluster:

    ```shell
    $ hawq stop cluster -M fast
    $ hawq stop cluster -M immediate
    ```

-   Use `hawq stop master` to stop the master only. If you cannot stop the master due to running transactions, try using `fast` shutdown. If `fast` shutdown does not work, use `immediate` shutdown. Use `immediate` shutdown with caution, as it will result in a crash-recovery run when the system is restarted.

	```shell
    $ hawq stop master -M fast
    $ hawq stop master -M immediate
    ```
-   If you have changed or want to reload server parameter settings on a HAWQ database where there are active connections, use the command:


	```shell
    $ hawq stop master -u -M fast 
    ```   

-   When stopping a segment or all segments, use `smart` mode, which is the default. Using `fast` or `immediate` mode on segments will have no effect since segments are stateless.

    ```shell
    $ hawq stop segment
    $ hawq stop allsegments
    ```
-	You should typically always use `hawq start cluster` or `hawq restart cluster` to start the cluster. If you do end up starting nodes individually with `hawq start standby|master|segment`, make sure to always start the standby *before* the active master. Otherwise, the standby can become unsynchronized with the active master.
