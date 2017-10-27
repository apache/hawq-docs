---
title: Configuring HAWQ/PXF for Secure HDFS
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

When Kerberos is enabled for your HDFS filesystem, HAWQ, as an HDFS client, requires a principal and keytab file to authenticate access to HDFS (filesystem) and YARN (resource management). If you have enabled Kerberos at the HDFS filesystem level, you will create and deploy principals for your HDFS cluster, and ensure that Kerberos authentication is enabled and functioning for all HDFS client services, including HAWQ and PXF.

You will perform different procedures depending upon whether you use Ambari to manage your HAWQ cluster or you manage your cluster from the command line.

## <a id="task_kerbhdfs_ambarimgd"></a>Procedure for Ambari-Managed Clusters

If you manage your cluster with Ambari, you will enable Kerberos authentication for your cluster as described in the [Enabling Kerberos Authentication Using Ambari](https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.5.3/bk_security/content/configuring_amb_hdp_for_kerberos.html) Hortonworks documentation. The Ambari **Kerberos Security Wizard** guides you through the kerberization process, including installing Kerberos client packages on cluster nodes, syncing Kerberos configuration files, updating cluster configuration, and creating and distributing the Kerberos principals and keytab files for your Hadoop cluster services, including HAWQ and PXF. 

## <a id="task_kerbhdfs_cmdlinemgd"></a>Procedure for Command-Line-Managed Clusters

**Note**: HAWQ does not support command-line-managed clusters employing an Active Directory KDC.

If you manage your cluster from the command line, before you configure HAWQ and PXF for access to a secure HDFS filesystem ensure that you have:

- Enabled Kerberos for your Hadoop cluster per the instructions for your specific distribution and verified the configuration.

- Verified that the HDFS configuration parameter `dfs.block.access.token.enable` is set to `true`. You can find this setting in the `hdfs-site.xml` configuration file.

- Noted the host name or IP address of your HAWQ \<master\> and Kerberos Key Distribution Center \(KDC\) \<kdc-server\> nodes.

- Noted the name of the Kerberos \<realm\> in which your cluster resides.

- Distributed the `/etc/krb5.conf` Kerberos configuration file on the KDC server node to **each** HAWQ and PXF cluster node if not already present. For example:

    ``` shell
    $ ssh root@<hawq-node>
    root@hawq-node$ cp /etc/krb5.conf /save/krb5.conf.save
    root@hawq-node$ scp <kdc-server>:/etc/krb5.conf /etc/krb5.conf
    ```

- Verified that the Kerberos client packages are installed on **each** HAWQ and PXF node.

    ``` shell
    root@hawq-node$ rpm -qa | grep krb
    root@hawq-node$ yum install krb5-libs krb5-workstation
    ```

#### <a id="task_kerbhdfs_cmdlinemgd_steps"></a>Procedure

Perform the following steps to configure HAWQ and PXF for a secure HDFS. You will perform operations on both the HAWQ \<master\> and the \<kdc-server\> nodes.

1.  Log in to the Kerberos KDC server as the `root` user.

    ``` shell
    $ ssh root@<kdc-server>
    root@kdc-server$ 
    ```

2.  Use the `kadmin.local` command to create a Kerberos principal for the `postgres` user. Substitute your \<realm\>. For example:

    ``` shell
    root@kdc-server$ kadmin.local -q "addprinc -randkey postgres@REALM.DOMAIN"
    ```

3.  Use `kadmin.local` to create a Kerberos service principal for **each** host on which a PXF agent is configured and running. The service principal should be of the form `pxf/<host>@<realm>` where \<host\> is the DNS resolvable, fully-qualified hostname of the PXF host system \(output of `hostname -f` command\).

    For example, these commands add service principals for three PXF nodes on the hosts host1.example.com, host2.example.com, and host3.example.com:

    ``` shell
    root@kdc-server$ kadmin.local -q "addprinc -randkey pxf/host1.example.com@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "addprinc -randkey pxf/host2.example.com@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "addprinc -randkey pxf/host3.example.com@REALM.DOMAIN"
    ```

    **Note:** As an alternative, if you have a hosts file that lists the fully-qualified domain name of each PXF host \(one host per line\), then you can generate principals using the command:

    ``` shell
    root@kdc-server$ for HOST in $(cat hosts) ; do sudo kadmin.local -q "addprinc -randkey pxf/$HOST@REALM.DOMAIN" ; done
    ```

4.  Generate a keytab file for each principal that you created in the previous steps \(i.e. `postgres` and each `pxf/<host>`\). Save the keytab files in any convenient location \(this example uses the directory `/etc/security/keytabs`\). You will deploy the service principal keytab files to their respective HAWQ and PXF host machines in a later step. For example:

    ``` shell
    root@kdc-server$ kadmin.local -q "xst -k /etc/security/keytabs/hawq.service.keytab postgres@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "xst -k /etc/security/keytabs/pxf-host1.service.keytab pxf/host1.example.com@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "xst -k /etc/security/keytabs/pxf-host2.service.keytab pxf/host2.example.com@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "xst -k /etc/security/keytabs/pxf-host3.service.keytab pxf/host3.example.com@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "listprincs"
    ```

    Repeat the `xst` command as necessary to generate a keytab for each HAWQ and PXF service principal that you created in the previous steps.

5.  The HAWQ master server requires a `/etc/security/keytabs/hdfs.headless.keytab` keytab file for the HDFS principal. If this file does not already exist on the HAWQ master node, create the principal and generate the keytab. For example:

    ``` shell
    root@kdc-server$ kadmin.local -q "addprinc -randkey hdfs@REALM.DOMAIN"
    root@kdc-server$ kadmin.local -q "xst -k /etc/security/keytabs/hdfs.headless.keytab hdfs@REALM.DOMAIN"
    ```

6.  Copy the HAWQ service keytab file \(and the HDFS headless keytab file if you created one) to the HAWQ master segment host. For example:

    ``` shell
    root@kdc-server$ scp /etc/security/keytabs/hawq.service.keytab <master>:/etc/security/keytabs/hawq.service.keytab
    root@kdc-server$ scp /etc/security/keytabs/hdfs.headless.keytab <master>:/etc/security/keytabs/hdfs.headless.keytab
    ```

7.  Change the ownership and permissions on `hawq.service.keytab` (and `hdfs.headless.keytab`) as follows:

    ``` shell
    root@kdc-server$ ssh <master> chown gpadmin:gpadmin /etc/security/keytabs/hawq.service.keytab
    root@kdc-server$ ssh <master> chmod 400 /etc/security/keytabs/hawq.service.keytab
    root@kdc-server$ ssh <master> chown hdfs:hdfs /etc/security/keytabs/hdfs.headless.keytab
    root@kdc-server$ ssh <master> chmod 400 /etc/security/keytabs/hdfs.headless.keytab
    ```

8.  Copy the keytab file for each PXF service principal to its respective host. For example:

    ``` shell
    root@kdc-server$ scp /etc/security/keytabs/pxf-host1.service.keytab host1.example.com:/etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ scp /etc/security/keytabs/pxf-host2.service.keytab host2.example.com:/etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ scp /etc/security/keytabs/pxf-host3.service.keytab host3.example.com:/etc/security/keytabs/pxf.service.keytab
    ```

    Note the keytab file location on each PXF host; you will need this  information for a later configuration step.

9. Change the ownership and permissions on the `pxf.service.keytab` files. For example:

    ``` shell
    root@kdc-server$ ssh host1.example.com chown pxf:pxf /etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ ssh host1.example.com chmod 400 /etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ ssh host2.example.com chown pxf:pxf /etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ ssh host2.example.com chmod 400 /etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ ssh host3.example.com chown pxf:pxf /etc/security/keytabs/pxf.service.keytab
    root@kdc-server$ ssh host3.example.com chmod 400 /etc/security/keytabs/pxf.service.keytab
    ```

10. On **each** PXF node, edit the `/etc/pxf/conf/pxf-site.xml` configuration file to identify the local keytab file and security principal name. Add or uncomment the properties, substituting your \<realm\>. For example:

    ``` xml
    <property>
        <name>pxf.service.kerberos.keytab</name>
        <value>/etc/security/keytabs/pxf.service.keytab</value>
        <description>path to keytab file owned by pxf service
        with permissions 0400</description>
    </property>

    <property>
        <name>pxf.service.kerberos.principal</name>
        <value>pxf/_HOST@REALM.DOMAIN</value>
        <description>Kerberos principal pxf service should use.
        _HOST is replaced automatically with hostnames
        FQDN</description>
    </property>
    ```

11. Perform the remaining steps on the HAWQ master node as the `gpadmin` user:
    1.  Log in to the HAWQ master node and set up the HAWQ runtime environment:

        ``` shell
        $ ssh gpadmin@<master>
        gpadmin@master$ . /usr/local/hawq/greenplum_path.sh
        ```

    2.  Run the following commands to configure Kerberos HDFS security for HAWQ and identify the keytab file:

        ``` shell
        gpadmin@master$ hawq config -c enable_secure_filesystem -v ON
        gpadmin@master$ hawq config -c krb_server_keyfile -v /etc/security/keytabs/hawq.service.keytab
        ```

    3.  Start the HAWQ service:

        ``` shell
        gpadmin@master$ hawq start cluster -a
        ```

    4.  Obtain a HDFS Kerberos ticket and change the ownership and permissions of the HAWQ HDFS data directory, substituting the HDFS data directory path for your HAWQ cluster. For example:

        ``` shell
        gpadmin@master$ sudo -u hdfs kinit -kt /etc/security/keytabs/hdfs.headless.keytab hdfs
        gpadmin@master$ sudo -u hdfs hdfs dfs -chown -R postgres:gpadmin /<hawq_data_hdfs_path>
        ```

    5.  On the **HAWQ master node and each segment node**, edit the `/usr/local/hawq/etc/hdfs-client.xml` file to enable kerberos security and assign the HDFS NameNode principal. Add or uncomment the following properties in each file:

        ``` xml
        <property>
          <name>hadoop.security.authentication</name>
          <value>kerberos</value>
        </property>
        ```

    6.  If you are using YARN for resource management, edit the `yarn-client.xml` file to enable kerberos security. Add or uncomment the following property in the `yarn-client.xml` file on the **HAWQ master and each HAWQ segment node**:

        ``` xml
        <property>
          <name>hadoop.security.authentication</name>
          <value>kerberos</value>
        </property>
        ```

    7.  Restart your HAWQ cluster:

        ``` shell
        gpadmin@master$ hawq restart cluster -a -M fast
        ```

## <a id="server_ticket_renew"></a>Setting the HAWQ Kerberos Ticket Renewal Interval

The HAWQ [`server_ticket_renew_interval`](../reference/guc/parameter_definitions.html#server_ticket_renew_interval) server configuration parameter governs the HAWQ HDFS client Kerberos ticket renewal interval. The default ticket renewal interval is 12 hours.

You configure the lifetime of a Kerberos ticket when you set up your KDC. To avoid ticket expiration, set the `server_ticket_renew_interval` to a value that is less than the lifetime of the ticket. 

#### <a id="task_kerbhdfs_ticket_renew"></a>Procedure

You will perform different procedures to set the ticket renewal interval if you manage your cluster from the command line or use Ambari to manage your cluster.

1. If you manage your cluster using Ambari:
    
    1.  Login in to the Ambari UI from a supported web browser.

    2. Navigate to the **HAWQ** service, **Configs > Advanced** tab and expand the **Custom hawq-site** drop down.

    3. Set the `server_ticket_renew_interval` value to the desired ticket renewal interval in milliseconds.

    4. **Save** this configuration change and then select the now orange **Restart > Restart All Affected** menu button to restart your HAWQ cluster.

    5. Exit the Ambari UI.  
    
2. If you manage your cluster from the command line:
    
    1.  Use the `hawq config` command to update the `server_ticket_renew_interval` configuration parameter. For example:

        ``` shell
        gpadmin@master$ hawq config -c server_ticket_renew_interval -v 86400000
        ```

    2.  Restart your HAWQ cluster:

        ``` shell
        gpadmin@master$ hawq restart cluster
        ```
