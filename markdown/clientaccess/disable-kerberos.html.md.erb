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

Follow these steps to disable Kerberos security for HAWQ and PXF for manual installations.

**Note:** If you install or manage your cluster using Ambari, then the HAWQ Ambari plug-in automatically disables security for HAWQ and PXF when you disable security for Hadoop. The following instructions are only necessary for manual installations, or when Hadoop security is disabled outside of Ambari.

1.  Disable Kerberos on the Hadoop cluster on which you use HAWQ.
2.  Disable security for HAWQ:
    1.  Login to the HAWQ database master server as the `gpadmin` user:

        ``` bash
        $ ssh hawq_master_fqdn
        ```

    2.  Run the following command to set up HAWQ environment variables:

        ``` bash
        $ source /usr/local/hawq/greenplum_path.sh
        ```

    3.  Start HAWQ if necessary:

        ``` bash
        $ hawq start -a
        ```

    4.  Run the following command to disable security:

        ``` bash
        $ hawq config --masteronly -c enable_secure_filesystem -v “off”
        ```

    5.  Change the permission of the HAWQ HDFS data directory:

        ``` bash
        $ sudo -u hdfs hdfs dfs -chown -R gpadmin:gpadmin /hawq_data
        ```

    6.  On the HAWQ master node and on all segment server nodes, edit the `/usr/local/hawq/etc/hdfs-client.xml` file to disable kerberos security. Comment or remove the following properties in each file:

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

    7.  Restart HAWQ:

        ``` bash
        $ hawq restart -a -M fast
        ```

3.  Disable security for PXF:
    1.  On each PXF node, edit the `/etc/gphd/pxf/conf/pxf-site.xml` to comment or remove the properties:

        ``` xml
        <!--
        <property>
            <name>pxf.service.kerberos.keytab</name>
            <value>/etc/security/phd/keytabs/pxf.service.keytab</value>
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
