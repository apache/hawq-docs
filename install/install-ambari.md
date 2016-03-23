---
title: Install Apache HAWQ using Ambari
---

Follow this procedure to install HAWQ using Ambari 2.2.1.

-   [Prerequisites](#section_mqs_f3j_5r)
-   [Procedure](#section_kwy_f3j_5r)

## Prerequisites <a name="section_mqs_f3j_5r"></a>

-   Install a compatible version of HDP and Ambari, and ensure that your HDP system is fully functional.
-   Select and prepare all host machines that will run the HAWQ and PXF services. See [Select HAWQ Host Machines](select-hosts.html).

## Procedure <a name="section_kwy_f3j_5r"></a>

1.  Login to the Ambari server host machine as the `root` user.
2.  Create a staging directory where you will download and extract the tarballs for HAWQ and the HAWQ Ambari plug-in. The staging directory and all the directories above it must be readable and executable by the system user that runs the httpd process \(typically `apache`\). Make the directory readable and executable by all users. For example:

    ```
    $ mkdir /staging
    $ chmod a+rx /staging
    ```

    **Note:** Do not use the /tmp directory as a staging directory because files under /tmp can be removed at any time.

3.  Download the required Pivotal software tarball files from [Pivotal Network](https://network.pivotal.io/products/pivotal-hd), saving them into the staging directory that you just created. The required tarball files are:

    |**Stack Name**|**Filename**|**Description**|
    |--------------|------------|---------------|
    |HDB-2.0.0.0 Beta|pivotal-hdb-2.0.0.0\_beta-20068.tar.gz|Pivotal HDB is a parallel SQL query engine that includes features from Apache HAWQ \(Incubating\) such as PXF.|
    |HAWQ-PLUGIN-2.0.0|hawq-plugin-2.0.0-hdp-429.tar.gz|The HAWQ plug-in provides Ambari installation and monitoring functionality for Apache HAWQ \(Incubating\).|

4.  Extract each tarball file into the staging directory:

    ```
    $ tar -xvzf /staging/pivotal-hdb-2.0.0.0_beta-20068.tar.gz -C /staging/
    $ tar -xvzf /staging/hawq-plugin-2.0.0-hdp-429.tar.gz -C /staging/
    ```

5.  Each tarball is an archived yum repository and has a setup\_repo.sh script. The script creates a symlink from the document root of the httpd server \(/var/www/html\) to the directory where the tarball was extracted. On the host that will be used as a YUM repo, execute the setup\_repo.sh script that is shipped as a part of each tarball file:

    ```
    $ cd /staging/pivotal-hdb*
    $ ./setup_repo.sh
    $ cd /staging/hawq-plugin*
    $ ./setup_repo.sh
    ```

6.  Update the Yum repo to install the HAWQ Ambari plug-in:

    ```
    $ yum install hawq-plugin
    ```

7.  Execute the following script to add the HDB repository to the Ambari server:

    ```
    $ cd /var/lib/hawq
    $ ./add_hdb_repo.py -u admin -p admin
    ```

    **Note:** Substitute the correct Ambari administrator password for your system.

8.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\) Verify that the HDB component is now available.
9.  Restart the Ambari server:

    ```
    $ ambari-server restart
    ```

    **Note:** You must restart the Ambari server before proceeding. The above command restarts only the Ambari server, but leaves other Hadoop services running.

10. Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user.
11. Select **HDFS**, then click the **Configs** tab.
12. Customize the HDFS configuration by following these steps:
    1.  On the **Settings** tab, change the DataNode setting **DataNode max data transfer threads** \(dfs.datanode.max.transfer.threads parameter \) to *40960*.
    1.  Select the **Advanced** tab and expand **DataNode**. Ensure that the **DataNode directories permission** \(dfs.datanode.data.dir.perm parameter\) is set to *750*.
    1.  Expand the **General** tab and change the **Access time precision** \(dfs.namenode.accesstime.precision parameter\) to *-1*.
    1.  Expand **Advanced hdfs-site**. Set the following properties to their indicated values.

        **Note:** If a property described below does not appear in the Ambari UI, select **Custom hdfs-site** and click **Add property...** to add the property definition and set it to the indicated value.

        |Property|Setting|
        |--------|-------|
        |**dfs.block.access.token.enable**|*false* for an unsecured HDFS cluster, or *true* for a secure cluster|
        |**dfs.allow.truncate**|true|
        |**dfs.support.append**|true|
        |**HDFS Short-circuit read** \(**dfs.client.read.shortcircuit**\)|true|
        |**dfs.block.local-path-access.user**|gpadmin|
        |**dfs.datanode.handler.count**|60|

        **Note:** HAWQ requires that you enable `dfs.allow.truncate`. The HAWQ service will fail to start if `dfs.allow.truncate` is not set to "true."

    2.  Expand **Advanced core-site**, then set the following properties to their indicated values:

        **Note:** If a property described below does not appear in the Ambari UI, select **Custom core-site** and click **Add property...** to add the property definition and set it to the indicated value.

        |Property|Setting|
        |--------|-------|
        |**ipc.client.connection.maxidletime**|3600000|
        |**ipc.client.connect.timeout**|300000|
        |**ipc.server.listen.queue.size**|3300|

13. Click **Save** and enter a name for the configuration change (for example, *HAWQ prerequisites*). Click **Save** again, then **OK**.
13. If Ambari indicates that hosts must be restarted, click **Restart** and allow the cluster to restart before you continue.
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
    *  **HAWQ Master Temp Directories**, **HAWQ Segment Temp Directories**: Enter one or more directories in which the HAWQ Master or a HAWQ segment stores temporary files. Separate multiple directories with a space. Any directories that you specify must already be available on all host machines. As a best practice, use multiple temporary directories on separate disks to load balance writes to temporary files \(for example, ``/disk1/tmp /disk2/tmp`\). If you do not specify a temporary directory, the HAWQ data directory is used to store temporary files.
    *  **Resource Manager**: Select the resource manager to use for allocating resources in your HAWQ cluster. If you choose **Standalone**, HAWQ exclusively uses resources from the whole cluster. If you choose **YARN**, HAWQ contacts the YARN resource manager to negotiate resources. You can change the resource manager type after the initial installation. See [Managing Resources](/200/hawq/resourcemgmt/HAWQResourceManagement.html).
    *  **VM Overcommit**: Set this value according to the instructions in the [System Requirements](/20/requirements/system-requirements.html) document.

17.  Click the **Advanced** tab and enter a **HAWQ System User Password**. Retype the password where indicated.

17. \(Optional.\) On the **Advanced** tab, you can change numerous configuration properties for the HAWQ cluster. Hover your mouse cursor over the entry field to display help for the associated property.  Default values are generally acceptable for a new installation. The following properties are sometimes customized during installation:

    |Property|Action|
    |--------|------|
    |**General > HAWQ DFS URL**|The URL that HAWQ uses to access HDFS.|
    |**General > HAWQ Master Port**|Enter the port to use for the HAWQ master host or accept the default, 5432. **CAUTION:** If you are installing HAWQ in a single-node environment \(or when the Ambari server and HAWQ are installed the same node\) then *you cannot accept the default port*. Enter a unique port for the HAWQ master.|
    |**General > HAWQ Segment Port**|The base port to use for HAWQ segment hosts.|
    |**Advanced hawq-site > hawq\_rm\_yarn\_address**|If you are using YARN for resource management, specify the address and port number of the YARN resource manager server \(the value of `yarn.resourcemanager.address`\). For example: localhost:8032.|
    |**Advanced hawq-site > hawq\_rm\_yarn\_queue\_name**|If you are using YARN for resource management, specify the YARN queue name to use for registering the HAWQ resource manager. For example: default.|
    |**Advanced hawq-site > hawq\_rm\_yarn\_scheduler\_address**|If you are using YARN for resource management, specify the address and port number of the YARN scheduler server \(the value of `yarn.resourcemanager.scheduler.address`\). For example: localhost:8030.|

18.  Click **Next** to continue the installation. (Depending on your cluster configuration, Ambari may recommend that you change other properties before proceeding.)
18. Review your configuration choices, then click **Deploy** to begin the installation. Ambari now begins to install, start, and test the HAWQ and PXF configuration. During this procedure, you can click on the **Message** links to view the console output of individual tasks.

18.  Click **Next** after all tasks have completed. Review the summary of the install process, then click **Complete**.  Ambari may indicate that components on cluster need to be restarted. Choose **Restart > Restart All Affected** if necessary.
19. To verify that HAWQ is installed, login to the HAWQ master as `gpadmin`:

    ```
    $ su - gpadmin
    $ source /usr/local/hawq/greenplum\_path.sh
    $ psql
    ```

    **Note:** HAWQ queries timeout after a period of 600 seconds. If a query on a newly-installed system appears to hang, wait for the timeout period to expire so that you can view the associated error message.

20. If you want to access data in external systems such as HDFS files, Hive or HBase, you must install the appropriate PXF plugin RPM for the external system on all the individual nodes of your cluster. See [Installing PXF Plugins](/200/hawq/pxf/InstallPXFPlugins.html) in the Apache HAWQ \(Incubating\) documentation for instructions.
