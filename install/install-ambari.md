---
title: Install Apache HAWQ using Ambari
---

## Prerequisites <a id="section_mqs_f3j_5r"></a>

-   Install a compatible version of HDP and Ambari, and ensure that your HDP system is fully functional. See the [Release Notes](/hdb/releasenotes/HAWQ20ReleaseNotes.html#topic_dhh_2jx_yt) for more information about HDFS compatibility.
-   Select and prepare all host machines that will run the HAWQ and PXF services. See [Select HAWQ Host Machines](select-hosts.html).

## Procedure <a id="section_kwy_f3j_5r"></a>

1.  Login to the Ambari server host machine as the `root` user.
2.  Create a staging directory where you will download and extract the tarballs for HAWQ and the HAWQ Ambari plug-in. The staging directory and all the directories above it must be readable and executable by the system user that runs the httpd process \(typically `apache`\). Make the directory readable and executable by all users. For example:

    ```
    $ mkdir /staging
    $ chmod a+rx /staging
    ```

    **Note:** Do not use the /tmp directory as a staging directory because files under /tmp can be removed at any time.

3.  Download the required Pivotal software tarball files from [Pivotal Network](https://network.pivotal.io/products/pivotal-hdb), saving them into the staging directory that you just created. The required tarball files are:

    |**Stack Name**|**Filename**|**Description**|
    |--------------|------------|---------------|
    |HDB-2.0.0.0|hdb-2.0.0.0-\<build\>.tar.gz|Pivotal HDB is a parallel SQL query engine that includes features from Apache HAWQ \(Incubating\) such as PXF.|
    |HDB-AMBARI-PLUGIN-2.0.0|hdb-ambari-plugin-2.0.0-hdp-\<build\>.tar.gz|The HAWQ plug-in provides Ambari installation and monitoring functionality for Apache HAWQ \(Incubating\).|

4.  Extract each tarball file into the staging directory:

    ```
    $ tar -xvzf /staging/hdb-2.0.0.0-*.tar.gz -C /staging/
    $ tar -xvzf /staging/hdb-ambari-plugin-2.0.0-hdp-*.tar.gz -C /staging/
    ```

4.  Install and/or run the HTTP service if it is not already running:

    ```
    $ yum install httpd
    $ service httpd start
    ```

5.  Each tarball is an archived yum repository and has a setup\_repo.sh script. The script creates a symlink from the document root of the httpd server \(/var/www/html\) to the directory where the tarball was extracted. On the host that will be used as a YUM repo, execute the setup\_repo.sh script that is shipped as a part of each tarball file:

    ```
    $ cd /staging/hdb*
    $ ./setup_repo.sh
    $ cd /staging/hdb-ambari-plugin*
    $ ./setup_repo.sh
    ```

6.  Update the Yum repo to install the HAWQ Ambari plug-in:

    ```
    $ yum install hdb-ambari-plugin
    ```

6.  Restart the Ambari server:

    ```
    $ ambari-server restart
    ```

    **Note:** You must restart the Ambari server before proceeding. The above command restarts only the Ambari server, but leaves other Hadoop services running.

7.  If you have already installed a HDP cluster and are adding HDB to the existing cluster, execute the following script to add the HDB repository to the Ambari server. (This step is not required if you are installing a new HDP cluster and HDB together at the same time.):

    ```
    $ cd /var/lib/hawq
    $ ./add_hdb_repo.py -u admin -p admin
    ```

    **Note:** Substitute the correct Ambari administrator password for your system.

8.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\) Verify that the HDB component is now available.
11. Select **HDFS**, then click the **Configs** tab.
12. Customize the HDFS configuration by following these steps:
    1.  On the **Settings** tab, change the DataNode setting **DataNode max data transfer threads** \(dfs.datanode.max.transfer.threads parameter \) to *40960*.
    1.  Select the **Advanced** tab and expand **DataNode**. Ensure that the **DataNode directories permission** \(dfs.datanode.data.dir.perm parameter\) is set to *750*.
    1.  Expand the **General** tab and change the **Access time precision** \(dfs.namenode.accesstime.precision parameter\) to *0*.
    1.  Expand **Advanced hdfs-site**. Set the following properties to their indicated values.

        **Note:** If a property described below does not appear in the Ambari UI, select **Custom hdfs-site** and click **Add property...** to add the property definition and set it to the indicated value.

        |Property|Setting|
        |--------|-------|
        |**dfs.allow.truncate**|true|
        |**dfs.block.access.token.enable**|*false* for an unsecured HDFS cluster, or *true* for a secure cluster|
        |**dfs.block.local-path-access.user**|gpadmin|
        |**HDFS Short-circuit read** \(**dfs.client.read.shortcircuit**\)|true|
        |**dfs.client.socket-timeout**|300000000|
        |**dfs.client.use.legacy.blockreader.local**|false|
        |**dfs.datanode.handler.count**|60|
        |**dfs.datanode.socket.write.timeout**|7200000|
        |**dfs.namenode.handler.count**|600|
        |**dfs.support.append**|true|

        **Note:** HAWQ requires that you enable `dfs.allow.truncate`. The HAWQ service will fail to start if `dfs.allow.truncate` is not set to "true."

    2.  Expand **Advanced core-site**, then set the following properties to their indicated values:

        **Note:** If a property described below does not appear in the Ambari UI, select **Custom core-site** and click **Add property...** to add the property definition and set it to the indicated value.

        |Property|Setting|
        |--------|-------|
        |**ipc.client.connection.maxidletime**|3600000|
        |**ipc.client.connect.timeout**|300000|
        |**ipc.server.listen.queue.size**|3300|

13. Click **Save** and enter a name for the configuration change (for example, *HAWQ prerequisites*). Click **Save** again, then **OK**.
13. If Ambari indicates that a service must be restarted, click **Restart** and allow the service to restart before you continue.
13. Select **Actions \> Add Service** on the home page.
14. Select both **HAWQ** and **PXF** from the list of services, then click **Next** to display the Assign Masters page.
15. Select the hosts that should run the HAWQ Master and HAWQ Standby Master, or accept the defaults. The HAWQ Master and HAWQ Standby Master must reside on separate hosts. Click **Next** to display the Assign Slaves and Clients page.
>

    **Note:** Only the **HAWQ Master** and **HAWQ Standby Master** entries are configurable on this page. NameNode, SNameNode, ZooKeeper and others may be displayed for reference, but they are not configurable when adding the HAWQ and PXF services.
>

    **Note:** The HAWQ Master component must not reside on the same host that is used for Hive Metastore if the Hive Metastore uses the new PostgreSQL database. This is because both services attempt to use port 5432. If it is required to co-locate these components on the same host, provision a PostgreSQL database beforehand on a port other than 5432 and choose the “Existing PostgreSQL Database” option for the Hive Metastore configuration. The same restriction applies to the admin host, because neither the HAWQ Master nor the Hive Metastore can run on the admin host where the Ambari Server is installed.

16. On the Assign Slaves and Clients page, choose the hosts that will run HAWQ segments and PXF, or accept the defaults. The Add Service Wizard automatically selects hosts for the HAWQ and PXF services based on available Hadoop services.
>

    **Note:** PXF must be installed on the HDFS NameNode, the Standby NameNode \(if configured\), *and* on each HDFS DataNode. A HAWQ segment must be installed on each HDFS DataNode.
>

    Click **Next** to continue.

17.  On the Customize Services page, the **Settings** tab configures basic properties of the HAWQ cluster. In most cases you can accept the default values provided on this page. Several configuration options may require attention depending on your deployment:
    *  **HAWQ Master Directory**, **HAWQ Segment Directory**: This specifies the base path for the HAWQ master or segment data directory.
    *  **HAWQ Master Temp Directories**, **HAWQ Segment Temp Directories**: HAWQ temporary directories are used for spill files. Enter one or more directories in which the HAWQ Master or a HAWQ segment stores these temporary files. Separate multiple directories with a comma. Any directories that you specify must already be available on all host machines. If you do not specify master or segment temporary directories, temporary files are stored in `/tmp/hawq/[master|segment]`.<br/><br/>As a best practice, use multiple master and segment temporary directories on separate, large disks (2TB or greater) to load balance writes to temporary files \(for example, `/disk1/tmp,/disk2/tmp`\). For a given query, HAWQ will use a separate temp directory (if available) for each virtual segment to store spill files. Multiple HAWQ sessions will also use separate temp directories where available to avoid disk contention. If you configure too few temp directories, or you place multiple temp directories on the same disk, you increase the risk of disk contention or running out of disk space when multiple virtual segments target the same disk. Each HAWQ segment node can have 6 virtual segments.
    *  **Resource Manager**: Select the resource manager to use for allocating resources in your HAWQ cluster. If you choose **Standalone**, HAWQ exclusively uses resources from the whole cluster. If you choose **YARN**, HAWQ contacts the YARN resource manager to negotiate resources. You can change the resource manager type after the initial installation. You will also have to configure some YARN-related properties in step 22. For more information on using YARN to manage resources, see [Managing Resources](/20/resourcemgmt/HAWQResourceManagement.html).

		**Caution:** If you are installing HAWQ in secure mode (Kerberos-enabled), then set **Resource Manager** to **Standalone** to avoid encountering a known installation issue. You can enable YARN mode post-installation if YARN resource management is desired in HAWQ.  
    *  **VM Overcommit**: Set this value according to the instructions in the [System Requirements](/20/requirements/system-requirements.html) document.

17.  Click the **Advanced** tab and enter a **HAWQ System User Password**. Retype the password where indicated.

17. \(Optional.\) On the **Advanced** tab, you can change numerous configuration properties for the HAWQ cluster. Hover your mouse cursor over the entry field to display help for the associated property.  Default values are generally acceptable for a new installation. The following properties are sometimes customized during installation:

    |Property|Action|
    |--------|------|
    |**General > HAWQ DFS URL**|The URL that HAWQ uses to access HDFS|
    |**General > HAWQ Master Port**|Enter the port to use for the HAWQ master host or accept the default, 5432. **CAUTION:** If you are installing HAWQ in a single-node environment \(or when the Ambari server and HAWQ are installed the same node\) then *you cannot accept the default port*. Enter a unique port for the HAWQ master|
    |**General > HAWQ Segment Port**|The base port to use for HAWQ segment hosts|

1.  If you selected YARN as the **Resource Manager**, then you must configure several YARN properties for HAWQ. On the **Advanced** tab of HAWQ configuration, enter values for the following parameters:

	|Property|Action|
    |--------|------|
    |**Advanced hawq-site > hawq\_rm\_yarn\_address**|Specify the address and port number of the YARN resource manager server \(the value of `yarn.resourcemanager.address`\). For example: rm1.example.com:8050|
    |**Advanced hawq-site > hawq\_rm\_yarn\_queue\_name**|Specify the YARN queue name to use for registering the HAWQ resource manager. For example: `default` **Note:** If you specify a custom queue name other than `default`, you must configure the YARN scheduler and custom queue capacity, either through Ambari or directly in YARN's configuration files. See [Integrating YARN with HAWQ](/20/resourcemgmt/YARNIntegration.html) for more details. |
    |**Advanced hawq-site > hawq\_rm\_yarn\_scheduler\_address**|Specify the address and port number of the YARN scheduler server \(the value of `yarn.resourcemanager.scheduler.address`\). For example: rm1.example.com:8030|

	If you have enabled high availability for YARN, then verify that the following values have been populated correctly in HAWQ:

	|Property|Action|
    |--------|------|
	|**Custom yarn-client > yarn.resourcemanager.ha**|Comma-delimited list of the fully qualified hostnames of the resource managers. When high availability is enabled, YARN ignores the value in hawq\_rm\_yarn\_address and uses this property’s value instead. For example, `rm1.example.com:8050,rm2.example.com:8050` |
	|**Custom yarn-client > yarn.resourcemanager.scheduler.ha**|Comma-delimited list of fully qualified hostnames of the resource manager schedulers. When high availability is enabled, YARN ignores the value in hawq\_rm\_yarn\_scheduler\_address and uses this property’s value instead. For example,`rm1.example.com:8030,rm2.example.com:8030` |

18.  Click **Next** to continue the installation. (Depending on your cluster configuration, Ambari may recommend that you change other properties before proceeding.)
18. Review your configuration choices, then click **Deploy** to begin the installation. Ambari now begins to install, start, and test the HAWQ and PXF configuration. During this procedure, you can click on the **Message** links to view the console output of individual tasks.

18.  Click **Next** after all tasks have completed. Review the summary of the install process, then click **Complete**.  Ambari may indicate that components on cluster need to be restarted. Choose **Restart > Restart All Affected** if necessary.
19. To verify that HAWQ is installed, login to the HAWQ master as `gpadmin` and perform some basic commands:

    1.  Source the `greenplum_path.sh` file to set your environment for HAWQ:

        ```
        $ source /usr/local/hawq/greenplum_path.sh
        ```

    1.  If you use a custom HAWQ master port number, set it in your environment. For example:

        ```
        $ export PGPORT=5432
        ```

    1.  Start the `psql` interactive utility, connecting to the postgres database:

        ```
        $ psql -d postgres
        psql (8.2.15)
        Type "help" for help.
        postgres=#
        ```

    3.  Create a new database and connect to it:

        ```
        postgres=# create database mytest;
        CREATE DATABASE
        postgres=# \c mytest
        You are now connected to database "mytest" as user "*username*".
        ```

    4.  Create a new table and insert sample data:

        ```
        mytest=# create table t (i int);
        CREATE TABLE
        mytest=# insert into t select generate_series(1,100);
        ```

    5.  Activate timing and perform a simple query:

        ```
        mytest=# \timing
        Timing is on.
        mytest=# select count(*) from t;
        count
        -------
        100
        (1 row)
        Time: 7.266 ms
        ```

## Post-Install Procedure for Hive and HBase<a id="post-install-pxf"></a>

In order to use the installed PXF service with HBase on a HDP cluster, you must manually add the path to the `pxf-hbase.jar` file to the `HBASE_CLASSPATH` environment variable and restart HBase.

If you are using Kerberos to secure Hive and HBase, you must configure proxy users, enable user impersonation, and configure PXF access to tables.

Follow this procedure to make the required changes:

1.  Use either a text editor or the Ambari Web interface to edit the `hbase-env.sh` file, and add the line:

    ```
    export HBASE_CLASSPATH=${HBASE_CLASSPATH}:/usr/lib/pxf/pxf-hbase.jar
    ```

    **Note:** Restart HBase after adding the PXF service in order to load the newly-installed PXF JAR file.

2.  (Optional.) For secure Hive installations, use either a text editor or the Ambari Web interface to edit the `hive-site.xml` file, and add the property:

    ```
    <property>
      <name>hive.server2.enable.impersonation</name>
      <description>Enable user impersonation for HiveServer2</description>
      <value>true</value>
    </property>
    ```

3.  (Optional.) For secure Hive and HBase installations, use either a text editor or the Ambari Web interface to edit the core-site.xml file, and add the properties:

    ```
    <property>
      <name>hadoop.proxyuser.hive.hosts</name>
      <value>*</value>
    </property>

    <property>
      <name>hadoop.proxyuser.hive.groups</name>
      <value>*</value>
    </property>

    <property>
      <name>hadoop.proxyuser.hbase.hosts</name>
      <value>*</value>
    </property>

    <property>
      <name>hadoop.proxyuser.hbase.groups</name>
      <value>*</value>
    </property>
    ```

4.  Restart both Hive and HBase to use the updated classpath and new properties.
5.  In order to use PXF with HBase or Hive tables, you must grant the `pxf` user read permission on those tables:
    * For HBase, use the `GRANT` command for each table that you want to access with PXF. For example:

        ```
        hbase(main):001:0> grant 'pxf', 'R', 'my_table'
        ```
    * Because Hive uses the HDFS ACLs for access control, ensure that the pxf has read permission on all of the HDFS directories that map to your database, tables, and partitions.
