---
title: Backing Up and Restoring HAWQ
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

This chapter provides information on backing up and restoring databases in HAWQ system.

As an administrator, you will need to back up and restore your database. HAWQ provides three utilities to help you back up your data:

-   `gpfdist`
-   PXF
-   `pg_dump`

`gpfdist` and PXF are parallel loading and unloading tools that provide the best performance.  You can use `pg_dump`, a non-parallel utility inherited from PostgreSQL.

In addition, in some situations you should back up your raw data from ETL processes.

This section describes these three utilities, as well as raw data backup, to help you decide what fits your needs.

## <a id="usinggpfdistorpxf"></a>About gpfdist and PXF 

You can perform a parallel backup in HAWQ using `gpfdist` or PXF to unload all data to external tables. Backup files can reside on a local file system or HDFS. To recover tables, you can load data back from external tables to the database. 

### <a id="performingaparallelbackup"></a>Performing a Parallel Backup 

1.  Check the database size to ensure that the file system has enough space to save the backed up files.
2.  Use the `pg_dump` utility to dump the schema of the target database.
3.  Create a writable external table for each table to back up to that database.
4.  Load table data into the newly created external tables.

>    **Note:** Put the insert statements in a single transaction to prevent problems if you perform any update operations during the backup.


### <a id="restoringfromabackup"></a>Restoring from a Backup 

1.  Create a database to recover to.
2.  Recreate the schema from the schema file \(created during the `pg_dump` process\).
3.  Create a readable external table for each table in the database.
4.  Load data from the external table to the actual table.
5.  Run the `ANALYZE` command once loading is complete. This ensures that the query planner generates optimal plan based on up-to-date table statistics.

### <a id="differencesbetweengpfdistandpxf"></a>Differences between gpfdist and PXF 

`gpfdist` and PXF differ in the following ways:

-   `gpfdist` stores backup files on local file system, while PXF stores files on HDFS.
-   `gpfdist` only supports plain text format, while PXF also supports binary format like AVRO and customized format.
-   `gpfdist` doesn’t support generating compressed files, while PXF supports compression \(you can specify a compression codec used in Hadoop such as `org.apache.hadoop.io.compress.GzipCodec`\).
-   Both `gpfdist` and PXF have fast loading performance, but `gpfdist` is much faster than PXF.

## <a id="usingpg_dumpandpg_restore"></a>About pg\_dump and pg\_restore 

HAWQ supports the PostgreSQL backup and restore utilities, `pg_dump` and `pg_restore`. The `pg_dump` utility creates a single, large dump file in the master host containing the data from all active segments. The `pg_restore` utility restores a HAWQ database from the archive created by `pg_dump`. In most cases, this is probably not practical, as there is most likely not enough disk space in the master host for creating a single backup file of an entire distributed database. HAWQ supports these utilities in case you are migrating data from PostgreSQL to HAWQ.

To create a backup archive for database `mydb`:

```shell
$ pg_dump -Ft -f mydb.tar mydb
```

To create a compressed backup using custom format and compression level 3:

```shell
$ pg_dump -Fc -Z3 -f mydb.dump mydb
```

To restore from an archive using `pg_restore`:

```shell
$ pg_restore -d new_db mydb.dump
```

## <a id="aboutbackinguprawdata"></a>About Backing Up Raw Data 

Parallel backup using `gpfdist` or PXF works fine in most cases. There are a couple of situations where you cannot perform parallel backup and restore operations:

-   Performing periodically incremental backups.
-   Dumping a large data volume to external tables - this process takes a long time.

In such situations, you can back up raw data generated during ETL processes and reload it into HAWQ. This provides the flexibility to choose where you store backup files.

## <a id="estimatingthebestpractice"></a>Selecting a Backup Strategy/Utility 

The table below summaries the differences between the four approaches we discussed above. 

<table>
  <tr>
    <th></th>
    <th><code>gpfdist</code></th>
    <th>PXF</th>
    <th><code>pg_dump</code></th>
    <th>Raw Data Backup</th>
  </tr>
  <tr>
    <td><b>Parallel</b></td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>No</td>
  </tr>
  <tr>
    <td><b>Incremental Backup</b></td>
    <td>No</td>
    <td>No</td>
    <td>No</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><b>Backup Location</b></td>
    <td>Local FS</td>
    <td>HDFS</td>
    <td>Local FS</td>
    <td>Local FS, HDFS</td>
  </tr>
  <tr>
    <td><b>Format</b></td>
    <td>Text, CSV</td>
    <td>Text, CSV, Custom</td>
    <td>Text, Tar, Custom</td>
    <td>Depends on format of row data</td>
  </tr>
  <tr>
<td><b>Compression</b></td><td>No</td><td>Yes</td><td>Only support custom format</td><td>Optional</td></tr>
<tr><td><b>Scalability</b></td><td>Good</td><td>Good</td><td>---</td><td>Good</td></tr>
<tr><td><b>Performance</b></td><td>Fast loading, Fast unloading</td><td>Fast loading, Normal unloading</td><td>---</td><td>Fast (Just file copy)</td><tr>
</table>

## <a id="estimatingspacerequirements"></a>Estimating Space Requirements 

Before you back up your database, ensure that you have enough space to store backup files. This section describes how to get the database size and estimate space requirements.

-   Use `hawq_toolkit` to query size of the database you want to backup. 

    ```
    mydb=# SELECT sodddatsize FROM hawq_toolkit.hawq_size_of_database WHERE sodddatname=’mydb’;
    ```

    If tables in your database are compressed, this query shows the compressed size of the database.

-   Estimate the total size of the backup files.
    -   If your database tables and backup files are both compressed, you can use the value `sodddatsize` as an estimate value.
    -   If your database tables are compressed  and backup files are not, you need to multiply `sodddatsize` by the compression ratio. Although this depends on the compression algorithms, you can use an empirical value such as 300%.
    -   If your back files are compressed and database tables are not, you need to divide `sodddatsize` by the compression ratio.
-   Get space requirement.
    -   If you use HDFS with PXF, the space requirement is `size_of_backup_files * replication_factor`.

    -   If you use gpfdist, the space requirement for each gpfdist instance is `size_of_backup_files / num_gpfdist_instances` since table data will be evenly distributed to all `gpfdist` instances.


## <a id="usinggpfdist"></a>Using gpfdist 

This section discusses `gpfdist` and shows an example of how to backup and restore HAWQ database.

`gpfdist` is HAWQ’s parallel file distribution program. It is used by readable external tables and `hawq load` to serve external table files to all HAWQ segments in parallel. It is used by writable external tables to accept output streams from HAWQ segments in parallel and write them out to a file.

To use `gpfdist`, start the `gpfdist` server program on the host where you want to store backup files. You can start multiple `gpfdist` instances on the same host or on different hosts. For each `gpfdist` instance, you specify a directory from which `gpfdist` will serve files for readable external tables or create output files for writable external tables. For example, if you have a dedicated machine for backup with two disks, you can start two `gpfdist` instances, each using one disk:

![](../images/gpfdist_instances_backup.png "Deploying multiple gpfdist instances on a backup host")

You can also run `gpfdist` instances on each segment host. During backup, table data will be evenly distributed to all `gpfdist` instances specified in the `LOCATION` clause in the `CREATE EXTERNAL TABLE` definition.

![](../images/gpfdist_instances.png "Deploying gpfdist instances on each segment host")

### <a id="example"></a>Example 

This example of using `gpfdist` backs up and restores a 1TB `tpch` database. To do so, start two `gpfdist` instances on the backup host `sdw1` with two 1TB disks \(One disk mounts at `/data1`, another disk mounts at `/data2`\).

#### <a id="usinggpfdisttobackupthetpchdatabase"></a>Using gpfdist to Back Up the tpch Database 

1.  Create backup locations and start the `gpfdist` instances.

    In this example, issuing the first command creates two folders on two different disks with the same postfix `backup/tpch_20140627`. These folders are labeled as backups of the `tpch` database on 2014-06-27. In the next two commands, the example shows two `gpfdist` instances, one using port 8080, and another using port 8081:

    ```shell
    sdw1$ mkdir -p /data1/gpadmin/backup/tpch_20140627 /data2/gpadmin/backup/tpch_20140627
    sdw1$ gpfdist -d /data1/gpadmin/backup/tpch_20140627 -p 8080 &
    sdw1$ gpfdist -d /data2/gpadmin/backup/tpch_20140627 -p 8081 &
    ```

2.  Save the schema for the database:

    ```shell
    master_host$ pg_dump --schema-only -f tpch.schema tpch
    master_host$ scp tpch.schema sdw1:/data1/gpadmin/backup/tpch_20140627
    ```

    On the HAWQ master host, use the `pg_dump` utility to save the schema of the tpch database to the file tpch.schema. Copy the schema file to the backup location to restore the database schema.

3.  Create a writable external table for each table in the database:

    ```shell
    master_host$ psql tpch
    ```
    ```sql
    tpch=# CREATE WRITABLE EXTERNAL TABLE wext_orders (LIKE orders)
    tpch-# LOCATION('gpfdist://sdw1:8080/orders1.csv', 'gpfdist://sdw1:8081/orders2.csv') FORMAT 'CSV';
    tpch=# CREATE WRITABLE EXTERNAL TABLE wext_lineitem (LIKE lineitem)
    tpch-# LOCATION('gpfdist://sdw1:8080/lineitem1.csv', 'gpfdist://sdw1:8081/lineitem2.csv') FORMAT 'CSV';
    ```

    The sample shows two tables in the `tpch` database: `orders` and `line item`. The sample shows that two corresponding external tables are created. Specify a location or each `gpfdist` instance in the `LOCATION` clause. This sample uses the CSV text format here, but you can also choose other delimited text formats. For more information, see the `CREATE EXTERNAL TABLE` SQL command.

4.  Unload data to the external tables:

    ```sql
    tpch=# BEGIN;
    tpch=# INSERT INTO wext_orders SELECT * FROM orders;
    tpch=# INSERT INTO wext_lineitem SELECT * FROM lineitem;
    tpch=# COMMIT;
    ```

5.  **\(Optional\)** Stop `gpfdist` servers to free ports for other processes:

    Find the progress ID and kill the process:

    ```shell
    sdw1$ ps -ef | grep gpfdist
    sdw1$ kill 612368; kill 612369
    ```


#### <a id="torecoverusinggpfdist"></a>Recovering Using gpfdist 

1.  Restart `gpfdist` instances if they aren’t running:

    ```shell
    sdw1$ gpfdist -d /data1/gpadmin/backup/tpch_20140627 -p 8080 &
    sdw1$ gpfdist -d /data2/gpadmin/backup/tpch_20140627 -p 8081 &
    ```

2.  Create a new database and restore the schema:

    ```shell
    master_host$ createdb tpch2
    master_host$ scp sdw1:/data1/gpadmin/backup/tpch_20140627/tpch.schema .
    master_host$ psql -f tpch.schema -d tpch2
    ```

3.  Create a readable external table for each table:

    ```shell
    master_host$ psql tpch2
    ```
    
    ```sql
    tpch2=# CREATE EXTERNAL TABLE rext_orders (LIKE orders) LOCATION('gpfdist://sdw1:8080/orders1.csv', 'gpfdist://sdw1:8081/orders2.csv') FORMAT 'CSV';
    tpch2=# CREATE EXTERNAL TABLE rext_lineitem (LIKE lineitem) LOCATION('gpfdist://sdw1:8080/lineitem1.csv', 'gpfdist://sdw1:8081/lineitem2.csv') FORMAT 'CSV';
    ```

    **Note:** The location clause is the same as the writable external table above.

4.  Load data back from external tables:

    ```sql
    tpch2=# INSERT INTO orders SELECT * FROM rext_orders;
    tpch2=# INSERT INTO lineitem SELECT * FROM rext_lineitem;
    ```

5.  Run the `ANALYZE` command after data loading:

    ```sql
    tpch2=# analyze;
    ```


### <a id="troubleshootinggpfdist"></a>Troubleshooting gpfdist 

Keep in mind that `gpfdist` is accessed at runtime by the segment instances. Therefore, you must ensure that the HAWQ segment hosts have network access to gpfdist. Since the `gpfdist` program is a  web server, to test connectivity you can run the following command from each host in your HAWQ array \(segments and master\):

```shell
$ wget http://gpfdist_hostname:port/filename
```

Also, make sure that your `CREATE EXTERNAL TABLE` definition has the correct host name, port, and file names for `gpfdist`. The file names and paths specified should be relative to the directory where gpfdist is serving files \(the directory path used when you started the `gpfdist` program\). See “Defining External Tables - Examples”.

## <a id="usingpxf"></a>Using PXF 

HAWQ Extension Framework \(PXF\) is an extensible framework that allows HAWQ to query external system data. The details of how to install and use PXF can be found in [Using PXF with Unmanaged Data](../pxf/HawqExtensionFrameworkPXF.html).

### <a id="usingpxftobackupthetpchdatabase"></a>Using PXF to Back Up the tpch Database 

1.  Create a folder on HDFS for this backup:

    ```shell
    master_host$ hdfs dfs -mkdir -p /backup/tpch-2014-06-27
    ```

2.  Dump the database schema using `pg_dump` and store the schema file in a backup folder:

    ```shell
    master_host$ pg_dump --schema-only -f tpch.schema tpch
    master_host$ hdfs dfs -copyFromLocal tpch.schema /backup/tpch-2014-06-27
    ```

3.  Create a writable external table for each table in the database:

    ```shell
    master_host$ psql tpch
    ```
    
    ```sql
    tpch=# CREATE WRITABLE EXTERNAL TABLE wext_orders (LIKE orders)
    tpch-# LOCATION('pxf://namenode_host:51200/backup/tpch-2014-06-27/orders'
    tpch-#           '?Profile=HdfsTextSimple'
    tpch-#           '&COMPRESSION_CODEC=org.apache.hadoop.io.compress.SnappyCodec'
    tpch-#          )
    tpch-# FORMAT 'TEXT';

    tpch=# CREATE WRITABLE EXTERNAL TABLE wext_lineitem (LIKE lineitem)
    tpch-# LOCATION('pxf://namenode_host:51200/backup/tpch-2014-06-27/lineitem'
    tpch-#           '?Profile=HdfsTextSimple'
    tpch-#           '&COMPRESSION_CODEC=org.apache.hadoop.io.compress.SnappyCodec')
    tpch-# FORMAT 'TEXT';
    ```

    Here, all backup files for the `orders` table go in the /backup/tpch-2014-06-27/orders folder, all backup files for the `lineitem` table go in /backup/tpch-2014-06-27/lineitem folder. We use snappy compression to save disk space.

4.  Unload the data to external tables:

    ```sql
    tpch=# BEGIN;
    tpch=# INSERT INTO wext_orders SELECT * FROM orders;
    tpch=# INSERT INTO wext_lineitem SELECT * FROM lineitem;
    tpch=# COMMIT;
    ```

5.  **\(Optional\)** Change the HDFS file replication factor for the backup folder. HDFS replicates each block into three blocks by default for reliability. You can decrease this number for your backup files if you need to:

    ```shell
    master_host$ hdfs dfs -setrep 2 /backup/tpch-2014-06-27
    ```

    **Note:** This only changes the replication factor for existing files; new files will still use the default replication factor.


### <a id="torecoverfromapxfbackup"></a>Recovering a PXF Backup 

1.  Create a new database and restore the schema:

    ```shell
    master_host$ createdb tpch2
    master_host$ hdfs dfs -copyToLocal /backup/tpch-2014-06-27/tpch.schema .
    master_host$ psql -f tpch.schema -d tpch2
    ```

2.  Create a readable external table for each table to restore:

    ```shell
    master_host$ psql tpch2
    ```
    
    ```sql
    tpch2=# CREATE EXTERNAL TABLE rext_orders (LIKE orders)
    tpch2-# LOCATION('pxf://namenode_host:51200/backup/tpch-2014-06-27/orders?Profile=HdfsTextSimple')
    tpch2-# FORMAT 'TEXT';
    tpch2=# CREATE EXTERNAL TABLE rext_lineitem (LIKE lineitem)
    tpch2-# LOCATION('pxf://namenode_host:51200/backup/tpch-2014-06-27/lineitem?Profile=HdfsTextSimple')
    tpch2-# FORMAT 'TEXT';
    ```

    The location clause is almost the same as above, except you don’t have to specify the `COMPRESSION_CODEC` because PXF will automatically detect it.

3.  Load data back from external tables:

    ```sql
    tpch2=# INSERT INTO ORDERS SELECT * FROM rext_orders;
    tpch2=# INSERT INTO LINEITEM SELECT * FROM rext_lineitem;
    ```

4.  Run `ANALYZE` after data loading:

    ```sql
    tpch2=# ANALYZE;
    ```
