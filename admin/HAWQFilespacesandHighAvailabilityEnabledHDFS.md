---
title: HAWQ Filespaces and High Availability Enabled HDFS
---

If you initialized HAWQ without the HDFS High Availability \(HA\) feature, you can enable it by using the following procedure.

## Enabling the HDFS NameNode HA Feature <a id="enablingthehdfsnamenodehafeature"></a>

To enable the HDFS NameNode HA feature for use with HAWQ, you need to perform the following tasks:

1. Enable high availability in your HDFS cluster
1. Collect information about the target filespace
1. Stop the HAWQ cluster and backup the catalog
1. Move the filespace location using the command line tool
1. Configure $\{GPHOME\}/etc/hdfs-client.xml
1. Resynchronize the standby master after moving the filespace


### Step 1: Enable High Availability in Your HDFS Cluster <a id="enablehahdfs"></a>

Enable high availability for NameNodes on your HDFS cluster.


### Step 2: Collect Information about the Target Filespace <a id="collectinginformationaboutthetargetfilespace"></a>

A default filespace named dfs\_system exists in the pg\_filespace catalog and the parameter, pg\_filespace\_entry, contains detailed information for each filespace. 

To move the filespace location to a HA-enabled HDFS location, you must move the data to a new path on your HA-enabled HDFS cluster. 

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
		  fsname | fsedbid | fselocation
	--------------+---------+-------------------------------------------------
	cdbfast_fs_c | 0       | hdfs://hdfs-cluster/hawq//cdbfast_fs_c
	cdbfast_fs_b | 0       | hdfs://hdfs-cluster/hawq//cdbfast_fs_b
	cdbfast_fs_a | 0       | hdfs://hdfs-cluster/hawq//cdbfast_fs_a
	dfs_system   | 0       | hdfs://test5:9000/hawq/hawq-1459499690
	(4 rows)
    ```

    The output contains the following:
    - HDFS paths that share the same prefix 
    - Current filespace location
    
    **Note:** If you see `{replica=3}` in the filespace location, ignore this part of the prefix. This is a known issue.
        
2.  To enable HA HDFS, you need the filespace name and the common prefix of your HDFS paths. The filespace location is formatted like a URL. 

	If the previous filespace location is 'hdfs://test5:9000/hawq/hawq-1459499690' and the HA HDFS common prefix is 'hdfs://hdfs-cluster', then the new filespace location should be 'hdfs://hdfs-cluster/hawq/hawq-1459499690'.

    ```
    Filespace Name: dfs_system
    Old location: hdfs://test5:9000/hawq/hawq-1459499690
    New location: hdfs://hdfs-cluster/hawq/hawq-1459499690
    ```

### Step 3: Stop the HAWQ Cluster and Back Up the Catalog <a id="stoppinghawqclusterandbackupcatalog"></a>

To enable HA HDFS,  you are changing the HAWQ catalog and persistent tables. You cannot perform transactions while persistent tables are being updated. Therefore, before you move the filespace location, back up the catalog. This is to ensure that you do not lose data due to a hardware failure or during an operation \(such as killing the HAWQ process\). 

1.  Disconnect all workload connections. Check the active connection with:

    ```
    psql -p <custom port> -c "select * from pg_catalog.pg_stat_activity" -d template1
    ```
    where \<custom port\> corresponds to the port number you optionally customized for HAWQ master.

2.  Issue a checkpoint: 

    ```
    psql -p <custom port> -c "checkpoint" -d template1
    ```

3.  Shut down the HAWQ cluster: 

    ```
    hawq stop cluster -a -M fast
    ```

4.  Copy the master data directory:

    ```
    $cp -r MASTER_DATA_DIRECTORY /catalog/backup/location
    ```
	The master data directory contains the catalog. Fatal errors can occur due to hardware failure or if you fail to kill a HAWQ process before attempting a filespace location change. Make sure you back this directory up.

### Step 4: Move the Filespace Location <a id="movingthefilespacelocation"></a>

HAWQ provides the command line tool, `hawq filespace`, to move the location of the filespace.

1. If you defined a custom port for HAWQ master, export the PGPORT environment variable.

	```
	export PGPORT=9000
	```
1. Run the following command to move a file space location:

	```
	hawq filespace --movefilespace default --location=hdfs://hdfs-cluster/hawq_new_filespace
	```

	If the target original filespace is not the default filespace, replace `default` in command line with the actual filespace name. Replace `hdfs://hdfs-cluster/hawq_new_filespace` with new filespace location.

**Important:** Errors while moving the location of the filespace:

Non-fatal error can occur if you provide invalid input or if you have not stopped HAWQ before attempting a filespace location change. Check that you have followed the instructions from the beginning, or correct the input error before you re-run `hawq filespace`.

Fatal errors can occur due to hardware failure or if you fail to kill a HAWQ process before attempting a filespace location change. When a fatal error occurs, you will see the message, "PLEASE RESTORE MASTER DATA DIRECTORY" in the output. If this occurs, shut down the database and restore the `$MASTER_DATA_DIRECTORY` that you backed up in Step 3.

### Step 5: Configure $\{GPHOME\}/etc/hdfs-client.xml <a id="configuregphomeetchdfsclientxml"></a>

Configure the hdfs-client.xml file.

### Step 6: Restart the HAWQ Cluster and Resynchronize the Standby Master <a id="reinitializethestandbymaster"></a>

1. Restart the HAWQ cluster:

	```
	$ hawq start cluster -a
	```
	
1. Moving the filespace to a new location renders the standby master catalog invalid. To update the standby, reinitialize and resync the standby master.  On the active master, run the following command to ensure that the standby master's catalog is resynced with the active master.

	```
	$ hawq init standby -n

	```