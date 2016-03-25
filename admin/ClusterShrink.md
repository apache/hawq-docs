---
title: Removing a Node
---

This topic outlines the proper procedure for removing a node from a HAWQ cluster.

In general, you should not need to remove nodes manually from running HAWQ clusters. HAWQ isolates any nodes that HAWQ detects as failing due to hardware or other types of errors.

## Guidelines for Removing a Node <a name="topic_p53_ct3_kv"></a>

If you do need to remove a node from a HAWQ cluster, keep in mind the following guidelines around removing nodes:

-   Never remove more than two nodes at a time since the risk of data loss is high.
-   Only remove nodes during system maintenance windows when the cluster is not busy or running queries.

## Removing a Node from a Running HAWQ Cluster <a name="task_oy5_ct3_kv"></a>

The following is a typical procedure to remove a node from a running HAWQ cluster:

1.  Login as gpadmin to the node that you wish to remove and source `greenplum_path.sh`.

    ```
    $ su - gpadmin
    $ source /usr/local/hawq/greenplum_path.sh
    ```

2.  Make sure that there are no running QEs on the segment. Execute the following command to check for running QE processes:

    ```
    $ ps -ef | grep postres
    ```

    In the output, look for processes that contain SQL commands such as INSERT or SELECT. For example:

    ```
    [gpadmin@rhel64-3 ~]$ ps -ef | grep postgres
    gpadmin 3000 2999 0 Mar21 ? 00:00:08 postgres: port 40000, logger process
    gpadmin 3003 2999 0 Mar21 ? 00:00:03 postgres: port 40000, stats collector process
    gpadmin 3004 2999 0 Mar21 ? 00:00:50 postgres: port 40000, writer process
    gpadmin 3005 2999 0 Mar21 ? 00:00:06 postgres: port 40000, checkpoint process
    gpadmin 3006 2999 0 Mar21 ? 00:01:25 postgres: port 40000, segment resource manager
    gpadmin 7880 2999 0 02:08 ? 00:00:00 postgres: port 40000, gpadmin postgres 192.168.2.201(33874) con11 seg0 cmd18 MPPEXEC INSERT
    ```

3.  Stop hawq on this segment by executing the following command:

    ```
    $ hawq stop segment
    ```

4.  On HAWQ master, remove the hostname of the segment from the `slaves` file. Then sync the `slaves` file to all nodes in the cluster by executing the following command:

    ```
    $ hawq scp -f hostfile slaves =:  $GPHOME/etc/slaves
    ```
