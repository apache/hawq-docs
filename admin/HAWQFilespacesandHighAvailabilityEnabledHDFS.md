---
title: HAWQ Filespaces and High Availability Enabled HDFS
---

In previous versions of HAWQ, you may have initialized HAWQ on HDFS without the High Availability \(HA\) feature. Using the current version, you can now use the HDFS NameNode HA feature.

This topic contains the following sections:

-   [Enabling the HDFS NameNode HA feature](#enablingthehdfsnamenodehafeature)
    -   [Collecting Information about the Target Filespace](#collectinginformationaboutthetargetfilespace)
    -   [Stopping HAWQ Cluster and Backup Catalog](#stoppinghawqclusterandbackupcatalog)
    -   [Moving the Filespace Location ](#movingthefilespacelocation)
    -   [Configure $\{GPHOME\}/etc/hdfs-client.xml ](#configuregphomeetchdfsclientxml)
    -   [Reinitialize the Standby Master](#reinitializethestandbymaster)

## Enabling the HDFS NameNode HA feature <a name="enablingthehdfsnamenodehafeature"></a>

To enable the HDFS NameNode HA feature, you need to perform the following tasks:

-   Collect information about the target filespace
-   Stop the HAWQ Cluster and backup catalog
-   Move the filespace location using the command line tool
-   Configure $\{GPHOME\}/etc/hdfs-client.xml
-   Reinitialize the standby master after moving the filespace

### Collecting Information about the Target Filespace <a name="collectinginformationaboutthetargetfilespace"></a>

A default filespace named dfs\_system exists in the pg\_filespace catalog and the parameter, pg\_filespace\_entry, contains detailed information for each filespace. 

1.  Use the following SQL query to gather information about the filespace located on HDFS:

    ```
    SELECT
        fsname, fsedbid, fselocation
    FROM
        pg_filespace as sp, pg_filespace_entry as entry, pg_filesystem as fs
    WHERE
        sp.fsfsys = fs.oid and fs.fsysname = 'hdfs' and sp.oid = entry.fsefsoid
    ORDER BY
        entry.fsedbid;
    ```

    The sample output is as follows:

    ```
    fsname   | fsedbid |             fselocation
    ------------+---------+--------------------------------------
     dfs_system |       1 | /data/hawq-kerberos/dfs/gpseg-1
     dfs_system |       2 | hdfs://mdw:9000/hawq-security/gpseg0
     dfs_system |       3 | hdfs://mdw:9000/hawq-security/gpseg1
     dfs_system |       4 | hdfs://mdw:9000/hawq-security/gpseg2
     dfs_system |       5 | hdfs://mdw:9000/hawq-security/gpseg3
     dfs_system |       6 | hdfs://mdw:9000/hawq-security/gpseg4
     dfs_system |       7 | hdfs://mdw:9000/hawq-security/gpseg5
    (7 rows)
    ```

    The output can contain the following:
    -   Master instance path information.
    -   Standby master instance path information, if the standby master is configured \(not in this example\).
    -   HDFS paths that share the same prefix for segment instances.
2.  To enable HA HDFS, you need the segment location comprising the filespace name and the common prefix of segment HDFS paths. The segment location is formatted like a URL. The sample output displays the segment location, hdfs://mdw:9000/hawq-security.  mdw:9000 is the NameNode host and RPC port, you must replace it with your HA HDFS cluster service ID to get the new segment location. For example hdfs://phdcluster/hawq-security.

    ```
    Filespace Name: dfs_system
    New segment location: hdfs://phdcluster/hawq-security
    ```

    **Note:** To move the filespace location to a segment location that is different from the old segment location, you must move the data to new path on HDFS.

    For example, you can do this by moving the filespace from hdfs://phdcluster/hawq-security to hdfs://phdcluster/hawq/another/path.


### Stopping the HAWQ Cluster and Backing Up the Catalog <a name="stoppinghawqclusterandbackupcatalog"></a>

To enable HA HDFS,  you are changing the HAWQ catalog and persistent tables. You cannot preform transactions while persistent tables are being updated. Therefore, before you move the filespace location, back up the catalog. This is to ensure that you do not lose data due to a hardware failure or during an operation \(such as killing the HAWQ process\). 

1.  Disconnect all workload connections. Check the active connection with:

    ```
    psql -c "select * from pg_catalog.pg_stat_activity"
    ```

2.  Issue a checkpoint: 

    ```
    psql -c "checkpoint"
    ```

3.  Shut down the HAWQ cluster: 

    ```
    hawq stop -a -M fast
    ```

4.  Copy the master data directory:

    ```
    $cp -r MASTER_DATA_DIRECTORY /catalog/backup/location
    ```


### Moving the Filespace Location <a name="movingthefilespacelocation"></a>

HAWQ provides the command line tool, `hawq filespace`, to move the location of the filespace.

Define `$MASTER_DATA_DIRECTORY` to point to the MASTER\_DATA\_DIRECTORY path. For example:

```
export MASTER_DATA_DIRECTORY=/data1/hawq_path/masterdd/
```

**Note:** The path in this example may not reflect your actual MASTER\_DATA\_DIRECTORY path.

Run the following command to move a file space location:

```
hawq filespace --movefilespace default --location=hdfs://phdcluster/hawq-security
```

**Note:**

1.  If the target filespace is not default filespace, replace default in command line with the actual filespace name.
2.  Replace `hdfs://phdcluster/hawq-security` with new segment location.

>**Important:** Errors while moving the location of the filespace:
>Non-fatal error can occur if you provide invalid input or if you have not stopped HAWQ before attempting a filespace location change. Check that you have followed the instructions from the beginning, or correct the input error before you re-run `hawq filespace`.
>
>Fatal errors can occur due to hardware failure or if you fail to kill a HAWQ process before attempting a filespace location change. When a fatal error occurs, you will see the message, "PLEASE RESTORE MASTER DATA DIRECTORY" in the output. If this occurs, shut down the database and restore the `$MASTER_DATA_DIRECTORY`.

### Configure $\{GPHOME\}/etc/hdfs-client.xml <a name="configuregphomeetchdfsclientxml"></a>

Configure the hdfs-client.xml file.

### Reinitialize the Standby Master <a name="reinitializethestandbymaster"></a>

The standby master catalog is rendered invalid during the move, and needs to be reinitialized. If you did not have a standby master configured, you can skip this task.

```
hawq start -a                              #start HAWQ cluster
hawq restart standby                                #shutdown and restart standby
hawq init standby <standby host name>               #initialize a standby master
```
