---
title: HAWQ Filespaces and High Availability Enabled HDFS
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

If you initialized HAWQ without the HDFS High Availability \(HA\) feature, you can enable it by using the following procedure.

## <a id="enablingthehdfsnamenodehafeature"></a>Enabling the HDFS NameNode HA Feature 

To enable the HDFS NameNode HA feature for use with HAWQ, you need to perform the following tasks:

1. Enable high availability in your HDFS cluster.
1. Collect information about the target filespace.
1. Stop the HAWQ cluster and backup the catalog (**Note:** Ambari users must perform this manual step.)
1. Move the filespace location using the command line tool (**Note:** Ambari users must perform this manual step.)
1. Reconfigure `${GPHOME}/etc/hdfs-client.xml` and `${GPHOME}/etc/hawq-site.xml` files. Then, synchronize updated configuration files to all HAWQ nodes.
1. Start the HAWQ cluster and resynchronize the standby master after moving the filespace.


### <a id="enablehahdfs"></a>Step 1: Enable High Availability in Your HDFS Cluster 

Enable high availability for NameNodes in your HDFS cluster. See the documentation for your Hadoop distribution for instructions on how to do this. 

**Note:** If you're using Ambari to manage your HDFS cluster, you can use the Enable NameNode HA Wizard. For example, [this Hortonworks HDP procedure](https://docs.hortonworks.com/HDPDocuments/Ambari-2.4.1.0/bk_ambari-user-guide/content/how_to_configure_namenode_high_availability.html) outlines how to do this in Ambari for HDP.

### <a id="collectinginformationaboutthetargetfilespace"></a>Step 2: Collect Information about the Target Filespace 

A default filespace named dfs\_system exists in the pg\_filespace catalog and the parameter, pg\_filespace\_entry, contains detailed information for each filespace. 

To move the filespace location to a HA-enabled HDFS location, you must move the data to a new path on your HA-enabled HDFS cluster.

1.  Use the following SQL query to gather information about the filespace located on HDFS:

    ```sql
    SELECT
        fsname, fsedbid, fselocation
    FROM
        pg_filespace AS sp, pg_filespace_entry AS entry, pg_filesystem AS fs
    WHERE
        sp.fsfsys = fs.oid AND fs.fsysname = 'hdfs' AND sp.oid = entry.fsefsoid
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

### <a id="stoppinghawqclusterandbackupcatalog"></a>Step 3: Stop the HAWQ Cluster and Back Up the Catalog 

**Note:** Ambari users must perform this manual step.

When you enable HA HDFS, you are changing the HAWQ catalog and persistent tables. You cannot perform transactions while persistent tables are being updated. Therefore, before you move the filespace location, back up the catalog. This is to ensure that you do not lose data due to a hardware failure or during an operation \(such as killing the HAWQ process\). 


1. If you defined a custom port for HAWQ master, export the `PGPORT` environment variable. For example:

	```shell
	export PGPORT=9000
	```

1. Save the HAWQ master data directory, found in the `hawq_master_directory` property value from `hawq-site.xml` to an environment variable.
 
	```bash
	export MDATA_DIR=/path/to/hawq_master_directory
	```

1.  Disconnect all workload connections. Check the active connection with:

    ```shell
    $ psql -p ${PGPORT} -c "SELECT * FROM pg_catalog.pg_stat_activity" -d template1
    ```
    where `${PGPORT}` corresponds to the port number you optionally customized for HAWQ master. 
    

2.  Issue a checkpoint: 

    ```shell
    $ psql -p ${PGPORT} -c "CHECKPOINT" -d template1
    ```

3.  Shut down the HAWQ cluster: 

    ```shell
    $ hawq stop cluster -a -M fast
    ```

4.  Copy the master data directory to a backup location:

    ```shell
    $ cp -r ${MDATA_DIR} /catalog/backup/location
    ```
	The master data directory contains the catalog. Fatal errors can occur due to hardware failure or if you fail to kill a HAWQ process before attempting a filespace location change. Make sure you back this directory up.

### <a id="movingthefilespacelocation"></a>Step 4: Move the Filespace Location 

**Note:** Ambari users must perform this manual step.

HAWQ provides the command line tool, `hawq filespace`, to move the location of the filespace.

1. If you defined a custom port for HAWQ master, export the `PGPORT` environment variable. For example:

	```shell
	export PGPORT=9000
	```
1. Run the following command to move a filespace location:

	```shell
	$ hawq filespace --movefilespace default --location=hdfs://hdfs-cluster/hawq_new_filespace
	```
	Specify `default` as the value of the `--movefilespace` option. Replace `hdfs://hdfs-cluster/hawq_new_filespace` with the new filespace location.

#### **Important:** Potential Errors During Filespace Move

Non-fatal error can occur if you provide invalid input or if you have not stopped HAWQ before attempting a filespace location change. Check that you have followed the instructions from the beginning, or correct the input error before you re-run `hawq filespace`.

Fatal errors can occur due to hardware failure or if you fail to kill a HAWQ process before attempting a filespace location change. When a fatal error occurs, you will see the message, "PLEASE RESTORE MASTER DATA DIRECTORY" in the output. If this occurs, shut down the database and restore the `${MDATA_DIR}` that you backed up in Step 4.

### <a id="configuregphomeetchdfsclientxml"></a>Step 5: Update HAWQ to Use NameNode HA by Reconfiguring hdfs-client.xml and hawq-site.xml 

If you install and manage your cluster using command-line utilities, follow these steps to modify your HAWQ configuration to use the NameNode HA service.

**Note:** These steps are not required if you use Ambari to manage HDFS and HAWQ, because Ambari makes these changes automatically after you enable NameNode HA.

For command-line administrators:

1. Edit the ` ${GPHOME}/etc/hdfs-client.xml` file on each segment and add the following NameNode properties:

    ```xml
    <property>
     <name>dfs.ha.namenodes.hdpcluster</name>
     <value>nn1,nn2</value>
    </property>

    <property>
     <name>dfs.namenode.http-address.hdpcluster.nn1</name>
     <value>ip-address-1.mycompany.com:50070</value>
    </property>

    <property>
     <name>dfs.namenode.http-address.hdpcluster.nn2</name>
     <value>ip-address-2.mycompany.com:50070</value>
    </property>

    <property>
     <name>dfs.namenode.rpc-address.hdpcluster.nn1</name>
     <value>ip-address-1.mycompany.com:8020</value>
    </property>

    <property>
     <name>dfs.namenode.rpc-address.hdpcluster.nn2</name>
     <value>ip-address-2.mycompany.com:8020</value>
    </property>

    <property>
     <name>dfs.nameservices</name>
     <value>hdpcluster</value>
    </property>
     ```

    In the listing above:
    * Replace `hdpcluster` with the actual service ID that is configured in HDFS.
    * Replace `ip-address-2.mycompany.com:50070` with the actual NameNode RPC host and port number that is configured in HDFS.
    * Replace `ip-address-1.mycompany.com:8020` with the actual NameNode HTTP host and port number that is configured in HDFS.
    * The order of the NameNodes listed in `dfs.ha.namenodes.hdpcluster` is important for performance, especially when running secure HDFS. The first entry (`nn1` in the example above) should correspond to the active NameNode.

2.  Change the following parameter in the `$GPHOME/etc/hawq-site.xml` file:

    ```xml
    <property>
        <name>hawq_dfs_url</name>
        <value>hdpcluster/hawq_default</value>
        <description>URL for accessing HDFS.</description>
    </property>
    ```

    In the listing above:
    * Replace `hdpcluster` with the actual service ID that is configured in HDFS.
    * Replace `/hawq_default` with the directory you want to use for storing data on HDFS. Make sure this directory exists and is writable.

3. Copy the updated configuration files to all nodes in the cluster (as listed in `hawq_hosts`).

	```shell
	$ hawq scp -f hawq_hosts hdfs-client.xml hawq-site.xml =:$GPHOME/etc/
	```

### <a id="reinitializethestandbymaster"></a>Step 6: Restart the HAWQ Cluster and Resynchronize the Standby Master 

1. Restart the HAWQ cluster:

	```shell
	$ hawq start cluster -a
	```

1. Moving the filespace to a new location renders the standby master catalog invalid. To update the standby, resync the standby master.  On the active master, run the following command to ensure that the standby master's catalog is resynced with the active master.

	```shell
	$ hawq init standby -n -M fast

	```

## <a id="pxfnhdfsnamenode"></a>Using PXF with HDFS NameNode HA

If HDFS NameNode High Availability is enabled, use the HDFS Nameservice ID in the `LOCATION` clause \<host\> field when invoking any PXF `CREATE EXTERNAL TABLE` command. If the \<port\> is omitted from the `LOCATION` URI, PXF connects to the port number designated by the `pxf_service_port` server configuration parameter value (default is 51200).