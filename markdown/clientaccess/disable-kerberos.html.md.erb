---
title: Disabling Kerberos Security
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

HAWQ supports Kerberos at both the HDFS and/or user authentication levels. You will perform different disable procedures for each.


## <a id="disable_kerb_hdfs"></a>Disable Kerberized HDFS for HAWQ/PXF

You will perform different procedures to disable HAWQ/PXF access to a previously-kerberized HDFS depending upon whether you manage your cluster from the command line or use Ambari to manage your cluster.

### <a id="disable_kerb_hdfs_ambari"></a>Procedure for Ambari-Managed Clusters

If you manage your cluster using Ambari, you will disable Kerberos authentication for your cluster as described in the [How To Disable Kerberos](https://docs.hortonworks.com/HDPDocuments/Ambari-2.4.2.0/bk_ambari-user-guide/content/how_to_disable_kerberos.html) Hortonworks documentation. Ambari will guide you through the de-kerberization process, including removing/updating any authentication-related configuration in your cluster.

### <a id="disable_kerb_hdfs_ambari"></a>Procedure for Command-Line-Managed Clusters

If you manage your cluster from the command line, follow these instructions to disable HDFS Kerberos security for HAWQ and PXF.

1.  Disable Kerberos on the Hadoop cluster on which you use HAWQ.
2.  Disable security for HAWQ:
    1.  Login to the HAWQ database master server as the `gpadmin` user and set up your HAWQ environment:

        ``` bash
        $ ssh gpadmin@<master>
        gpadmin@master$ . /usr/local/hawq/greenplum_path.sh
        ```

    2.  Start HAWQ if necessary:

        ``` bash
        gpadmin@master$ hawq start cluster
        ```

    3.  Update HAWQ configuration to disable security:

        ``` bash
        gpadmin@master$ hawq config -c enable_secure_filesystem -v “off”
        ```

    4.  Change the permission of the HAWQ HDFS data directory:

        ``` bash
        gpadmin@master$ sudo -u hdfs hdfs dfs -chown -R gpadmin:gpadmin /<hawq_data_hdfs_path>
        ```

    5.  On the HAWQ master node and on all segment server nodes, edit the `/usr/local/hawq/etc/hdfs-client.xml` file to disable kerberos security. Comment or remove the following properties in each file:

        ``` xml
        <!--
        <property>
          <name>hadoop.security.authentication</name>
          <value>kerberos</value>
        </property>

        <property>
          <name>dfs.namenode.kerberos.principal</name>
          <value>nn/_HOST@LOCAL.DOMAIN</value>
        </property>
        -->
        ```

    6.  Restart HAWQ:

        ``` bash
        gpadmin@master$ hawq restart cluster -a -M fast
        ```

3.  Disable security for PXF. Perform these steps on *each* PXF node:
    1.  Edit the `/etc/pxf/conf/pxf-site.xml` to comment out or remove the following properties:

        ``` xml
        <!--
        <property>
            <name>pxf.service.kerberos.keytab</name>
            <value>/etc/security/keytab/pxf.service.keytab</value>
            <description>path to keytab file owned by pxf service
            with permissions 0400</description>
        </property>

        <property>
            <name>pxf.service.kerberos.principal</name>
            <value>pxf/_HOST@HDB.LOCAL</value>
            <description>Kerberos principal pxf service should use.
            _HOST is replaced automatically with hostnames
            FQDN</description>
        </property>
        -->
        ```

    2.  Restart the PXF service.

        ``` bash
        root@pxf-node$ service pxf-service restart
        ```

## <a id="disable_kerb_hawq"></a>Disable Kerberos User Authentication for HAWQ

Perform the following procedure to disable Kerberos user authentication for HAWQ.

1. Comment out or remove the `pg_hba.conf` entry that mandates Kerberos authentication for HAWQ. The `pg_hba.conf` file resides in the directory specified by the `hawq_master_directory` server configuration parameter value. For example, comment out:

    ``` pre
    #host all all 0.0.0.0/0 gss include_realm=0 krb_realm=REALM.DOMAIN
    ```

2. Update the `pg_hba.conf` file to configure non-Kerberos access restrictions for all your HAWQ users. 

3. Reload HAWQ configuration:

    
    ``` bash
    gpadmin@master$ hawq stop master --reload
    ```

4. Notify your HAWQ users that `kinit` ticket requests are no longer required to authenticate to HAWQ.

