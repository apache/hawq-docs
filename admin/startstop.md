---
title: Starting and Stopping HAWQ
---

In a HAWQ DBMS, the database server instances \(the master and all segments\) are started or stopped across all of the hosts in the system in such a way that they can work together as a unified DBMS.

Because a HAWQ system is distributed across many machines, the process for starting and stopping a HAWQ system is different than the process for starting and stopping a regular PostgreSQL DBMS.

Use the `hawq start *object*` and `hawq stop` commands to start and stop HAWQ, respectively. These management tools are located in the $GPHOME/bin directory on your HAWQ master host. Initializing a HAWQ system also starts it.

**Important:**

Do not issue a `KILL` command to end any Postgres process. Instead, use the database command `pg_cancel_backend()`.

For information about [hawq start](/200/reference/cli/admin_utilities/hawqstart.html) and [hawq stop](/200/reference/cli/admin_utilities/hawqstop.html), see the appropriate pages in the HAWQ Management Utility Reference or enter `hawq start -h` or `hawq stop -h` on the command line.

## Initialize HAWQ <a name="task_g1y_xtm_s5"></a>

Initialize and start the HAWQ system using configuration parameters defined in `$GPHOME/etc/hawq-site.xml`.

The `hawq init` command with the appropriate cluster or node command initializes and starts a HAWQ cluster. The master or segment nodes can be individually initialized by using `hawq init master` and `hawq init segment` commands, respectively. Format options can also be specified at this time.

The `hawq init <object>` utility will create a HAWQ instance using configuration parameters defined in `$GPHOME/etc/hawq-site.xml` A single node cluster can be started without any user-defined changes to the default `hawq-site.xml` file. Use the template-hawq-site.xml file to specify the configuration for larger clusters.

When using the template for initializing a new cluster configuration, replace the items contained within the % markers, for example in: *`value`*`%master.host%`*`value`*, `%master.host%` would be replaced with the master host name. After modification, rename the file to the name of the default configuration file: `hawq-site.xml`.

-   Before initializing HAWQ, set the `$GPHOME` environment variable to point to the location of your HAWQ installation on the master host and exchange SSH keys between all host addresses in the array, using `hawq ssh-exkeys`.
-   To initialize and start a HAWQ cluster, enter the following command on the master host:

    ```
    $ hawq init cluster
    ```


## Starting HAWQ <a name="task_hkd_gzv_fp"></a>

Start an initialized HAWQ system by running the `hawq start` command on the master instance.

Use the `hawq start cluster` command to start a HAWQ system that has already been initialized by the `hawq init cluster` command, but has been stopped by the `hawq stop cluster` command. The `hawq start cluster` command starts HAWQ by starting all the Postgres database instances on the HAWQ cluster. `hawq start cluster` orchestrates this process and performs the process in parallel.

You can also use the `hawq start master` command to start only the HAWQ master, without segment nodes, then add these later, using `hawq start segment`.

-   Run `hawq start cluster` on the master host to start a HAWQ system:

    ```
    $ hawq start cluster
    ```

    **Note:**

    When the HAWQ system is first initialized with the `hawq init` command, it is automatically started.


## Restarting HAWQ <a name="task_gpdb_restart"></a>

Stop the HAWQ system and then restart it.

The `hawq restart` command with the appropriate cluster or node command can stop and then restart HAWQ after the shutdown completes. If the master or segments are already stopped, restart will have no effect.

-   To restart a HAWQ cluster, enter the following command on the master host:

    ```
    $ hawq restart cluster
    ```


## Reloading Configuration File Changes Only <a name="task_upload_config"></a>

Reload changes to the HAWQ configuration files without interrupting the system.

The `hawq stop` command can reload changes to the pg\_hba.conf configuration file and to *runtime* parameters in the hawq-site.xml file and pg\_hba.conf file without service interruption. Active sessions pick up changes when they reconnect to the database. Many server configuration parameters require a full system restart \(`hawq restart cluster`\) to activate. For information about server configuration parameters, see the [Server Configuration Parameter Reference](/200/reference/guc/guc_config.html).

-   Reload configuration file changes without shutting down the system using the `hawq stop` command:

    ```
    $ hawq stop --reload
    ```


## Starting the Master in Maintenance Mode <a name="task_maint_mode"></a>

Start only the master to perform maintenance or administrative tasks without affecting data on the segments.

Maintenance mode should only be used when required for a particular maintenance task. For example, you can connect to a database only on the master instance in maintenance mode and edit system catalog settings.

1.  Run `hawq start` using the master -m option:

    ```
    $ hawq start master -m
    ```

2.  Connect to the master in maintenance mode to do catalog maintenance. For example:

    ```
    $ PGOPTIONS='-c gp_session_role=utility' psql template1
    ```
3.  After completing your administrative tasks, restart the master in maintenance mode. Maintenance mode is a special utility mode.

    ```
    $ hawq restart master --special-mode maintenance
    ```

    **Warning:**

    Incorrect use of maintenance mode connections can result in an inconsistent system state. Only expert users should perform this operation.


## Stopping HAWQ <a name="task_gpdb_stop"></a>

The `hawq stop cluster` command stops or restarts your HAWQ system and always runs on the master host. When activated, `hawq stop cluster` stops all `postgres` processes in the system, including the master and all segment instances. The `hawq stop cluster` command uses a default of up to 64 parallel worker threads to bring down the Postgres instances that make up the HAWQ cluster. The system waits for any active transactions to finish before shutting down. To stop HAWQ immediately, use fast mode. The commands `hawq stop master`, `hawq stop segment`, `hawq stop standby`, or `hawq stop allsegments` can be used to stop the master, the local segment node, standby, or all segments in the cluster. Stopping the master will stop only the master segment, and will not shut down a cluster.

-   To stop HAWQ:

    ```
    $ hawq stop cluster
    ```

-   To stop HAWQ in fast mode:

    ```
    $ hawq stop cluster -M fast
    ```


## Best Practices to Start/Stop HAWQ Cluster Members <a name="task_tx4_bl3_h5"></a>

For best results in using `hawq start` and `hawq stop` to manage your HAWQ system, the following best practices are recommended.

-   Stop the entire HAWQ system by stopping the cluster on the master host:

    ```
    $ hawq stop cluster
    ```

-   To stop segments and kill any running queries without causing data loss or inconstency issues, use `fast` or `immediate` mode on the master or segments:

    ```
    $ hawq stop cluster -M fast
    ```

-   Use `hawq stop master` to stop the master only. If, due to running transactions, you cannot stop the master, try using fast shutdown. If fast shutdown does not work, use immediate shutdown. Use immediate shutdown with caution, as it will result in a crash-recovery run when the system is restarted.
-   When stopping a segment, you can use the default mode, smart mode. Using fast or immediate mode on segments will have no effect, as the segment is stateless.

    ```
    $ hawq stop allsegments
    ```
