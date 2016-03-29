---
title: Expanding a Cluster
---

Apache HAWQ supports dynamic node expansion. You can add segment nodes while HAWQ is running without having to suspend or terminate cluster operations.

## Guidelines for Cluster Expansion <a name="topic_kkc_tgb_h5"></a>

This topic provides some guidelines around expanding your HAWQ cluster.

There are several recommendations to keep in mind when modifying the size of your running HAWQ cluster:

-   When you add a new node, install both a DataNode and a physical segment on the new node.
-   After adding a new node, you should always rebalance HDFS data to maintain cluster performance.
-   Adding or removing a node also necessitates an update to the HDFS metadata cache. This update will happen eventually, but can take some time. To speed the update of the metadata cache, execute **`select gp_metadata_cache_clear();`**.
-   Note that for hash distributed tables, expanding the cluster will not immediately improve performance since hash distributed tables use a fixed number of virtual segments. In order to obtain better performance with hash distributed tables, you must redistribute the table to the updated cluster by either the [ALTER TABLE](/200/hawq/reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](/200/hawq/reference/sql/CREATE-TABLE-AS.html) command.
-   If you are using hash tables, consider updating the `default_hash_table_bucket_number` server configuration parameter to a larger value after expanding the cluster but before redistributing the hash tables.

## Adding a New Node to an Existing HAWQ Cluster <a name="task_hawq_expand"></a>

The following procedure describes the steps required to add a node to an existing HAWQ cluster.

For example purposes in this procedure, we are adding a new node named `sdw4`.

1.  Prepare the target machine by checking operating system configurations and passwordless ssh. HAWQ requires passwordless ssh access to all cluster nodes. To set up passwordless ssh on the new node, perform the following steps:
    1.  Login to the master HAWQ node as gpadmin. If you are logged in as a different user, switch to the gpadmin user and source the `greenplum_path.sh` file.

        ```
        $ su - gpadmin
        $ source /usr/local/hawq/greenplum_path.sh
        ```

    2.  On the HAWQ master node, change directories to /usr/local/hawq/etc. In this location, create a file called `new_hosts` and add the hostname\(s\) of the node\(s\) you wish to add to the existing HAWQ cluster, one per line. For example:

        ```
        sdw4
        ```

    3.  Login to the master HAWQ node as root and source the `greenplum_path.sh` file.

        ```
        $ su - root
        $ source /usr/local/hawq/greenplum_path.sh
        ```

    4.  Execute the following hawq command to set up passwordless ssh for root on the new host machine:

        ```
        $ hawq ssh-exkeys -e hawq_hosts -x new_hosts
        ```

    5.  Create the gpadmin user on the new host\(s\).

        ```
        $ hawq ssh -f new_hosts -e '/usr/sbin/useradd gpadmin’
        $ hawq ssh –f new_hosts -e 'echo -e "changeme\changeme" | passwd gpadmin'
        ```

    6.  Switch to the gpadmin user and source the `greenplum_path.sh` file again.

        ```
        $ su - gpadmin
        $ source /usr/local/hawq/greenplum_path.sh
        ```

    7.  Execute the following hawq command a second time to set up passwordless ssh for the gpadmin user:

        ```
        $ hawq ssh-exkeys -e hawq_hosts -x new_hosts
        ```

    8.  After setting up passwordless ssh, you can execute the following hawq command to check the target machine's configuration.

        ```
        $ hawq check -f new_hosts
        ```

        Configure operating system parameters as needed on the host machine. See the HAWQ installation documentation for a list of specific operating system parameters to configure.

2.  Login to the target host machine `sdw4` as the root user. If you are logged in as a different user, switch to the root account:

    ```
    $ su - root
    ```

3.  If not already installed, install the target machine \(`sdw4`\) as an HDFS DataNode.
4.  Download and install HAWQ on the target machine \(`sdw4`\) as described in the [software build instructions](https://cwiki.apache.org/confluence/display/HAWQ/Build+and+Install) or in the distribution installation documentation.
5.  On the HAWQ master node, check current cluster and host information using `psql`.

    ```
    #psql -d postgres
    postgres=#select * from gp_segment_configuration;
     registration_order | role | status | port  | hostname |    address    
    --------------------+------+--------+-------+----------+---------------
                     -1 | s    | u      |  5432 | sdw1     | 192.168.2.202
                      0 | m    | u      |  5432 | mdw      | rhel64-1
                      1 | p    | u      | 40000 | sdw3     | 192.168.2.204
                      2 | p    | u      | 40000 | sdw2     | 192.168.2.203
    (4 rows)
    ```

    At this point the new node does not appear in the cluster.

6.  Execute the following command to confirm that HAWQ was installed on the new host:

    ```
    $ hawq ssh -f new_hosts -e "ls -l $GPHOME"
    ```

7.  On the master node, use a text editor to add hostname `sdw4` into the `hawq_hosts` file you created during HAWQ installation. \(If you do not already have this file, then you create it first and list all the nodes in your cluster.\)

    ```
    mdw
    smdw
    sdw1
    sdw2
    sdw3
    sdw4
    ```

8.  On the master node, use a text editor to add hostname `sdw4` to the `$GPHOME/etc/slaves` file. This file lists all the segment host names for your cluster. For example:

    ```
    sdw1
    sdw2
    sdw3
    sdw4
    ```

9.  Sync the `hawq-site.xml` and `slaves` configuration files to all nodes in the cluster \(as listed in hawq\_hosts\).

    ```
    $ hawq scp -f hawq_hosts hawq-site.xml slaves =:$GPHOME/etc/
    ```

10. Make sure that the HDFS DataNode service has started on the new node.
11. On `sdw4`, create directories based on the values assigned to the following properties in `hawq-site.xml`. These new directories must be owned by the same database user \(for example, `gpadmin`\) who will execute the `hawq init segment` command in the next step.
    -   `hawq_segment_directory`
    -   `hawq_segment_temp_directory`
    **Note:** The `hawq_segment_directory` must be empty.

12. On `sdw4`, switch to the database user \(for example, `gpadmin`\), and initalize the segment.

    ```
    $ su - gpadmin
    $ hawq init segment
    ```

13. On the master node, check current cluster and host information using `psql` to verify that the new `sdw4` node has initialized successfully.

    ```
    #psql -d postgres
    postgres=# select * from gp_segment_configuration ;
     registration_order | role | status | port  | hostname |    address    
    --------------------+------+--------+-------+----------+---------------
                     -1 | s    | u      |  5432 | sdw1     | 192.168.2.202
                      0 | m    | u      |  5432 | mdw      | rhel64-1
                      1 | p    | u      | 40000 | sdw3     | 192.168.2.204
                      2 | p    | u      | 40000 | sdw2     | 192.168.2.203
                      3 | p    | u      | 40000 | sdw4     | 192.168.2.205
    (5 rows)
    ```

14. To maintain optimal cluster performance, rebalance HDFS data by running the following command:
    <pre><code>$ sudo -u hdfs hdfs balancer -threshold <i>threshhold_value</i>
    </code></pre>

    where *threshhold\_value* represents how much a DataNode's disk usage, in percentage, can differ from overall disk usage in the cluster. Adjust the threshold value according to the needs of your production data and disk. The smaller the value, the longer the rebalance time.
>
    **Note:** If you do not specify a threshold, then a default value of 20 is used. If the balancer detects that a DataNode is using less than a 20% difference of the cluster's overall disk usage, then data on that node will not be rebalanced. For example, if disk usage across all DataNodes in the cluster is 40% of the cluster's total disk-storage capacity, then the balancer script ensures that a DataNode's disk usage is between 20% and 60% of that DataNode's disk-storage capacity. DataNodes whose disk usage falls within that percentage range will not be rebalanced.

    Rebalance time is also affected by network bandwidth. You can adjust network bandwidth used by the balancer by using the following command:
    <pre><code>$ sudo -u hdfs hdfs dfsadmin -setBalancerBandwidth <i>network_bandwith</i></code></pre>
    The default value is 1MB/s. Adjust the value according to your network.

15. Speed up the clearing of the metadata cache by using the following command:

    ```
    #psql -d postgres
    postgres=#select gp_metadata_cache_clear();
    ```

16. If you are using hash tables, adjust the `default_hash_table_bucket_number` server configuration property to reflect the cluster's new size. Update this configuration's value by multiplying the new number of nodes in the cluster by 6.
    -   `default_hash_table_bucket_number` = \(new number of nodes\) \* 6
17. Redistribute the data in all hash-distributed tables by using either the [ALTER TABLE](/200/hawq/reference/sql/ALTER-TABLE.html) or [CREATE TABLE AS](/200/hawq/reference/sql/CREATE-TABLE-AS.html) command.
