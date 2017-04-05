---
title: Configuring HAWQ to use Ranger Policy Management
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

Your HAWQ installation includes the following HAWQ-related Ranger components:

- Ranger Administrative UI
- HAWQ Ranger Plug-in Service

The Ranger Administrative UI is installed when you install HDP. You configure the Ranger service itself through Ambari. You configure HAWQ-Ranger authorization policies through the Ranger Administrative UI, which you can access at `http://<ranger-admin-node>:6080`. 

Installing or upgrading to HAWQ installs the HAWQ Ranger Plug-in Service, but neither configures nor registers the plug-in.  

To use Ranger for managing HAWQ authentication events, you must first install and register several HAWQ JAR files on the Ranger Administration host. This one-time configuration establishes connectivity to your HAWQ cluster from the Ranger Administration host. 

After registering the JAR files, you enable or disable Ranger integration in HAWQ by setting the `hawq_acl_type` configuration parameter. When Ranger is enabled, all access to HAWQ resources is controlled through Ranger security policies. The HAWQ Ranger Plug-in pre-populates Ranger with HAWQ policies to allow `gpadmin` superuser access to all resources. See [Creating HAWQ Authorization Policies in Ranger](ranger-policy-creation.html) for information about creating policies in Ranger.

Use the following procedures to register the HAWQ Ranger Plug-in Service and enable Ranger authorization for HAWQ.

## <a id="prereq"></a>Prerequisites
To use HAWQ Ranger integration, install a compatible Hadoop distribution and Apache Ranger 0.6. You must also have `admin` access to the **Ranger Admin UI**.

## <a id="jar"></a>Step 1: Install Ranger Connectivity to HAWQ
1. `ssh` into the Ranger Administration host as a user with root privileges:

    ``` bash
    $ ssh root@<ranger-admin-node>
    root@ranger-admin-node$ 
    ```
2. Create the directory for the HAWQ JAR files:

    ``` bash
    root@ranger-admin-node$ cd /usr/hdp/current/ranger-admin/ews/webapp/WEB-INF/classes/ranger-plugins
    root@ranger-admin-node$ mkdir hawq
    ```
3. Copy the necessary HAWQ JAR files (`postgresql-9.1-901-1.jdbc4.jar` and `ranger-plugin-admin-<version>.jar`) from the HAWQ master node to the new directory:

    ``` bash
    root@ranger-admin-node$ scp <hawq-master>:/usr/local/hawq/ranger/lib/*.jar ./hawq
    ```
4. Change the ownership of the new folder and JAR files to the `ranger` user:

    ``` bash
    root@ranger-admin-node$ chown -R ranger:ranger hawq
    ```
5. The `enable-ranger-plugin.sh` script configures Ranger connectivity to your HAWQ cluster. The command has the syntax:

    ``` pre
    enable-ranger-plugin.sh -r <ranger_admin_node>:<ranger_port> -u <ranger_user> -p <ranger_password> -h <hawq_master>:<hawq_port> -w <hawq_user> -q <hawq_password>
    ```

    Log in to the HAWQ master node as the `gpadmin` user and execute the `enable-ranger-plugin.sh` script. Ensure that \<hawq_master\> identifies the fully qualified domain name of the HAWQ master node. For example:

    ``` bash
    gpadmin@master$ cd /usr/local/hawq/ranger/bin
    gpadmin@master$ ./enable-ranger-plugin.sh -r ranger_host:6080 -u admin -p admin -h hawq_master:5432 -w gpadmin -q gpadmin

    RANGER URL  = ranger_host:6080
    RANGER User = admin
    RANGER Password = [*****]
    HAWQ HOST = hawq_master
    HAWQ PORT = 5432
    HAWQ User = gpadmin
    HAWQ Password = [*******]
    HAWQ service definition was not found in Ranger Admin, creating it by uploading /usr/local/hawq_<version>/ranger/etc/ranger-servicedef-hawq.json
    HAWQ service instance was not found in Ranger Admin, creating it.
    Updated POLICY_MGR_URL to http://ranger_host:6080 in /usr/local/hawq_<version>/ranger/etc/rps.properties
    Updated default value of JAVA_HOME to /usr/jdk64/jdk1.8.0_77 in /usr/local/hawq_<version>/ranger/etc/rps.properties
    ```
    
    **Note**: You can also enter the short form of the command: `./enable-ranger-plugin.sh -r` and the script will prompt you for entries.
    
    When the script completes, the default HAWQ service definition is registered in the Ranger Admin UI. This service definition is named `hawq`.

6. Locate the `pg_hba.conf` file in the master directory of the HAWQ master node. To display the HAWQ master directory:
 
    ``` bash
    gpadmin@master$ hawq config --show hawq_master_directory
    GUC		: hawq_master_directory
    Value	: /data/hawq/master
    ```

    Edit the `pg_hba.conf` file on the HAWQ master node to configure HAWQ access for \<hawq_user\> on the \<ranger-admin-node\>. For example, you would add an entry similar to the following for the example `enable-ranger-plugin.sh` call above:

    ``` bash
    host  all     gpadmin    ranger_host/32       trust
    ```

    And reload HAWQ configuration:

    ``` bash
    gpadmin@master$ hawq stop cluster --reload
    ```

7.  After HAWQ reloads the configuration, use the fully-qualified domain name to log into the Ambari server. Click the **Ranger** link to display the Ranger Summary page, then select **Quick Links > Ranger Admin UI**. 

8.  Log in to the Ranger Access Manager. Click the **Edit** button for the **HAWQ** service. Ensure that the Active Status is set to Enabled, and click **Test Connection**. You should receive a message that Ranger connected successfully.  If the connection fails, verify the `hawq` service Config Properties, as well as your `pg_hba.conf` entries, and re-test the connection.

## <a id="enable"></a>Step 2: Configure HAWQ to Use Ranger Policy Management

The default Ranger service definition for HAWQ assigns the HAWQ administrator (typically `gpadmin`) all privileges to all objects. 

Once the connection between HAWQ and Ranger is configured, you may choose to set up policies for the HAWQ users according to the procedures in [Creating HAWQ Authorization Policies in Ranger](ranger-policy-creation.html) or enable Ranger with only the default policies. 

**Note**: Any authorization defined using `GRANT` commands will no longer apply after enabling HAWQ Ranger. Enabling Ranger authorization for HAWQ with only the default policies defined provides access only to the `gpadmin` user.

1. Log in to the Ambari UI, select the **HAWQ** Service, and then select the **Configs** tab.
2. Select the **Advanced** tab, and then expand **Custom hawq-site**.
4. Click **Add Property...** and add the new property, `hawq_acl_type=ranger` property. (If the property already exists, change its value from `standalone` (the default) to `ranger`.)
5. Click **Save** to save your changes.
6. Select **Service Actions > Restart All** and confirm that you want to restart the HAWQ cluster.


## <a id="rpsadminstate"></a>Displaying the Status of HAWQ/Ranger Integration

Determine the status of HAWQ/Ranger integration in your cluster by:

- Identifying the access control method currently in place in your HAWQ cluster. If the `hawq_acl_type` server configuration parameter value is  set to `ranger`, you have enabled Ranger authorization for HAWQ.

    ``` shell
    gpadmin@master$ hawq config -s hawq_acl_type
    GUC       : hawq_acl_type
    Value     : ranger
    ```

- Querying the state of your HAWQ cluster. If `hawq state` or Ambari **HAWQ Service Check** output identifies that the HAWQ Ranger Plug-in Service status is Active, the plug-in is up and running:

    ``` shell
    gpadmin@master$ hawq state
    ...
    20170327:16:35:06:508426 hawq_state:master:gpadmin-[INFO]:--   Current HAWQ acl type                          = ranger
    20170327:16:35:06:508426 hawq_state:master:gpadmin-[INFO]:--   HAWQ Ranger plugin service state               = Active
    ...
    ```

## <a id="customconfig"></a> Custom Configuration

Configuration files for the HAWQ Ranger Plug-in Service are located in the `$GPHOME/ranger/etc` directory. These files include:

| File     |  Description     |
|-------------|---------------------------|
| ranger-hawq-audit.xml |  HAWQ Ranger audit-related configuration, including the audit provider (log4j, Solr, HDFS) and provider-specific configuration |
| ranger-hawq-security.xml |  HAWQ Ranger service configuration, including the policy change polling interval |
| rps.properties |  HAWQ Ranger deployment-related configuration, including the HAWQ Ranger Plug-in Service port definition and JVM parameters|

Any configuration changes you make after you have registered the HAWQ Ranger Plug-in require a restart of the service. You can either restart the HAWQ cluster or restart just the HAWQ Ranger Plug-in Service:

``` shell
gpadmin@master$ /usr/local/hawq/ranger/bin/rps.sh stop
gpadmin@master$ /usr/local/hawq/ranger/bin/rps.sh start
```

## <a id="troubleshoot"></a> Troubleshooting Ranger Configuration

If resource name lookup is not working in the Ranger Admin UI:

1. Verify that the HAWQ Ranger plug-in JARs and JDBC driver have been copied to \<ranger-admin-node\>.
2. Test the connection between the Ranger Admin UI and the HAWQ master node by clicking the edit icon associated with the active HAWQ service definition, then clicking the **Config Properties: > Test Connection** button.
3. Verify that the HAWQ master node `pg_hba.conf` file includes a `host` entry for \<ranger-admin-node\>, HAWQ user (typically `gpadmin`).

